---
name: root-strategy
description: Use when reasoning about Root strategy and the question benefits from external perspectives — community consensus, alternative takes, recent meta discussion, faction tier debates, base-baiting / Eyrie-leader / Cult-revealed-suit type questions where multiple voices matter. Wraps the curated third-party strategy corpus at docs/strategy/sources/. Read in concert with root-factions (the project's own derivative strategy view); the curated layer is one level further out — what other people say.
user-invocable: true
allowed-tools:
  - "Read"
  - "Grep"
  - "Glob"
---

# Root Strategy Corpus Lens

Reference recipe for the curated third-party Root strategy corpus at
`docs/strategy/sources/`. Use this skill when a question benefits from
external perspectives — community consensus, contrarian takes, recent
meta discussion, faction tier rankings, multi-voice synthesis.

The corpus is **layer 3** in the project's three-layer authority stack:

| Layer | Source | Authority |
|---|---|---|
| 1 | Law (`rules/.../p16/rules.yml`, `faq.yml`) | Canonical |
| 2 | Faction profiles (`docs/factions/`) | Project-derivative, vetted by hand |
| 3 | Curated 3rd-party (`docs/strategy/sources/`) | *What other people say*, rated 0–10 |

When layers conflict, **higher-numbered layers lose**: Law beats profiles
beats curated. The reviewer pipeline (`/root-3p-review`) annotates layer
3 docs with explicit conflict callouts in the `# Review` section — read
that section before quoting any mechanical claim.

## Files

- Per-source files: `docs/strategy/sources/<domain>--<title-slug>.md`
- One file per source. Multi-faction sources get one
  `## <Faction Display Name>` H2 per faction discussed plus an optional
  `## General` section. Frontmatter `factions[]` is the canonical index.
- Roster + schema reference: `docs/strategy/README.md`
- Pipeline manifests: `docs/strategy/_runs/` (gitignored)

## Schema (key fields)

**Frontmatter:**
- `url`, `source`, `author`, `title` — provenance
- `factions[]` — citation-key slugs covered (e.g., `eyrie`, `marquise`,
  `keepers-iron`, plus `general` for cross-faction content)
- `expansions[]` — `base`, `riverfolk`, `underworld`, `marauder`,
  `homeland`, `vagabond_pack`, `hirelings`, `landmarks`
- `accuracy_rating` — 0–10 integer or `null` (unreviewed)
- `accuracy_notes` — paragraph summary of the reviewer's verdict
- `last_reviewed`, `reviewed_by`
- `fetch_status` — `complete` (default), `partial`, or `failed`
- `quality_tier` — 1–4 (curator's source-roster tier; **orthogonal** to
  `accuracy_rating` — tier is provenance-class, rating is verification)

**Body sections (curator-owned — do not modify when reading):**
- `# Distilled` → `## General` + per-faction H2s with H3 subsections
  (Win Condition / Opening Priorities / Mid-game Pivots / Threat
  Matchups / Card Priorities / Common Pitfalls / Endgame Routes)
- `# Key Takeaways` — bullets grouped by faction with bold labels
- `# Citations from Source` — `rule:X.Y.Z` cites the source itself made
- `# Source Notes` — curator's editorial

**Body section after `---` separator (reviewer-owned):**
- `# Review` — `## Verified claims`, `## Conflicts with the Law`,
  `## Stale or outdated`, `## Strategic judgment notes`,
  `## Citations from Source — verified` / `## Citations from Source — flagged`

## Lookup recipes

**Find every source that covers a faction** (frontmatter `factions[]`):
```
grep -l "^- <faction-slug>$" docs/strategy/sources/*.md
```
Use the citation-key slug: `eyrie`, `marquise`, `keepers-iron`, etc.
See top-level `CLAUDE.md` for the display-name → slug map.

**Read a faction's section out of a multi-faction doc:**
```
grep -nA 200 "^## <Faction Display Name>" docs/strategy/sources/<file>.md
```
Then `Read` from that line offset.

**Read the reviewer's verdict on a doc:**
```
grep -nA 60 "^# Review" docs/strategy/sources/<file>.md
```

**Read just the reviewer's Law-conflict flags:**
```
grep -nA 20 "^## Conflicts with the Law" docs/strategy/sources/<file>.md
```

**Find unreviewed docs (treat with caution):**
```
grep -l "^accuracy_rating: null$" docs/strategy/sources/*.md
```

**Find high-rated docs covering a faction** (rating ≥ 7):
```
for f in docs/strategy/sources/*.md; do
  rating=$(awk '/^accuracy_rating:/ {print $2; exit}' "$f")
  [ "$rating" != "null" ] && [ -n "$rating" ] && [ "$rating" -ge 7 ] && \
    grep -l "^- <faction-slug>$" "$f"
done
```

**Read accuracy notes for a specific doc** (the reviewer's verdict
paragraph in frontmatter):
```
awk '/^accuracy_notes:/,/^[a-z_]+:/' docs/strategy/sources/<file>.md
```

**Search across the whole corpus for a keyword** (card name, term,
mechanic):
```
grep -rn "<keyword>" docs/strategy/sources/
```

## Quality filtering rubric

Use `accuracy_rating` to weight cited claims:

| Rating | How to use |
|---|---|
| 9–10 | Solid; cite freely. Source's claims verified against the Law. |
| 7–8 | Mostly accurate. **Read `# Review`'s "Conflicts with the Law" before quoting any mechanical claim.** |
| 5–6 | Mixed. Cite only with explicit caveat. Prefer the same claim from a higher-rated source if available. |
| 3–4 | Significantly outdated or wrong. Only cite if no better source exists, with strong caveat. |
| 0–2 | Largely wrong. Generally do not cite. |
| `null` | Unreviewed. Treat as a default 5–6 and flag the unreviewed status when citing. |

The `# Review` section is more informative than the rating alone. A doc
with rating 6 might have most of its claims verified — the rating dropped
because of one specific mechanical error flagged in `## Conflicts with
the Law`. Read the actual review subsections before forming your own
weighting.

## Output contract for callers

- **Cite curated sources by file path** in markdown link form when
  surfacing a claim: `[Make Craft Game Keepers guide](docs/strategy/sources/makecraftgame--keepers-in-iron-guide.md)`.
  Or cite by source name in prose: "Make Craft Game's Keepers guide
  argues...".
- **Pass through, don't promote.** A curated source's strategy claim is
  **not** a `rule:X.Y.Z` cite. Cite the file path. If the source itself
  cited a rule, you may quote that cite — but verify against
  `# Review`'s "Citations from Source — verified/flagged" subsections
  that it's confirmed-correct, not flagged-incorrect.
- **Preserve hedges.** If the source says "often," "in my experience,"
  "usually," keep the hedge. Don't strengthen a probabilistic claim
  into an absolute.
- **Surface disagreement explicitly.** When two curated sources disagree
  on a strategy point (e.g., one says "always revolt turn 2," another
  says "turn 3 is fine in 4-player"), present both with attribution and
  ratings. Do not silently pick a winner. When tiebreaking is forced,
  weight by `accuracy_rating`.
- **Flag layer conflicts.** If a curated source contradicts the Law,
  the Law wins — surface the conflict (the reviewer probably already
  flagged it in `## Conflicts with the Law`; pass that through). If a
  curated source contradicts a faction profile, the profile wins for
  project-internal purposes; you may still note the disagreement as a
  "community-level alternative view."
- **The corpus is supplementary, not authoritative.** Faction profiles
  (`root-factions` skill) are the right starting point for "what does
  this project think about Eyrie?". The corpus is the right addition
  for "what do other people say?", "what's the recent meta?", "are
  there contrarian takes?", "is there published data on this?".
- **Don't quote-dump.** Distilled content is already a digest of a
  longer source. Pull the load-bearing claim or two; cite the file for
  the full digest.
