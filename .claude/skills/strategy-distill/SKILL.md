---
name: strategy-distill
description: Internal output schema for distilled Root strategy files. Defines the frontmatter spec, section structure (one file per source, faction-named subsections inside), accuracy/rating fields, and editorial discipline for files written under docs/strategy/sources/.
user-invocable: false
allowed-tools:
  - "Read"
  - "Write"
  - "Edit"
---

# Strategy Distillation — Output Schema

This skill is the canonical schema for files written under
`docs/strategy/sources/`. It is preloaded into the `root-strategy-curator`
agent. It is not user-invocable — it has no standalone use outside the
curation workflow.

## File path

```
docs/strategy/sources/<domain>--<title-slug>.md
```

- **One file per source.** A single source covering multiple factions writes
  one file with multiple faction subsections — never split into per-faction
  files.
- `<domain>` is the source domain without TLD or `www`: `makecraftgame`,
  `boardgamegeek`, `reddit`, `spritesanddice`. For Reddit, prefix the
  subreddit: `reddit-rootgame`.
- `<title-slug>` is a kebab-case slug from the source title, max ~60 chars.

Examples:
- `makecraftgame--keepers-in-iron-guide.md`
- `spritesanddice--strategy-of-root.md`
- `reddit-rootgame--lord-of-hundreds-opening.md`
- `boardgamegeek--root-strategy-guide.md`

## Frontmatter (required)

```yaml
---
url: <full source URL>
source: <human-readable source name, e.g., "Make Craft Game">
author: <author name if known, else "unknown">
title: <source's actual title, verbatim>
date_published: <YYYY-MM-DD if visible on the source, else "unknown">
date_curated: <YYYY-MM-DD when this file was written>
factions:                       # slugs of every faction with its own body subsection
  - <slug>                      # e.g. eyrie, marquise, keepers-iron, warlord
expansions:                     # which expansions are addressed
  - base                        # always include if base game is in scope
  - riverfolk                   # Riverfolk expansion
  - underworld                  # Underworld expansion (Duchy + Corvids)
  - marauder                    # Marauder expansion (Warlord + Keepers)
  - homeland                    # Homeland expansion (Diaspora + Council + Knaves)
  - vagabond_pack               # Vagabond Pack
  - hirelings                   # Hirelings
  - landmarks                   # Landmark Pack
quality_tier: <1|2|3|4>         # from the source roster; never 5 (Tier 5 is skip)
summary: |
  <1–2 sentences capturing the source's main thesis or scope. Read like
  a librarian's catalog entry — what the file is about, not a teaser>.

# Accuracy/rating fields — managed by EXTERNAL review pipelines, NOT by
# the curator. The curator writes these as null. A separate agent reviews
# the file's claims against the Law and faction profiles, then sets these.
accuracy_rating: null           # 0–10 integer, or null if unreviewed
accuracy_notes: null            # short string summarizing review verdict, or null
last_reviewed: null             # YYYY-MM-DD of most recent review, or null
reviewed_by: null               # agent or process id (e.g. "root-pragmatist@2026-04-29"), or null
---
```

Optional frontmatter fields when relevant:
- `printing_basis: <p4|p6|p16|unknown>` — which Law printing the source
  references (or unknown if not stated).
- `tags: [opening, mid-game, endgame, matchup, scoring, item-economy, ...]`
- `relates_to: [<relative paths to other curated sources>]` — markdown-style
  paths like `./spritesanddice--strategy-of-root.md` for sibling sources.
- `fetch_status: <complete|partial|failed>` — defaults to `complete` when
  absent. Use `partial` when only some of the source's content was extractable
  (e.g., long thread truncated, a sub-page failed). Use `failed` for stub
  files written when the fetch could not complete. **Stubs MUST set this
  field** so downstream agents can filter incomplete content.

### Stub files (when fetch fails)

If a fetch fails but the source is known and rostered, write a stub file
rather than skipping. Stubs document the failure and the path to completion:

```yaml
fetch_status: failed
```

The body should contain only:

```markdown
# Distilled

*Fetch failed. <one-sentence reason>. To complete: <one-sentence retry path>.*

# Key Takeaways

*Unavailable — fetch failed.*

# Citations from Source

*Unavailable — fetch failed.*

# Source Notes

<editorial: tier, why this source matters, why the fetch failed, and what
needs to happen to complete the curation>
```

When a stub has `fetch_status: failed`, the validation-checklist requirement
that `factions[]` matches body H2 sections is **deferred**, since the body
is empty by design. Populate `factions[]` from the source roster as a
best-guess index that downstream filters can use.

### Faction slugs

Use the slugs from the project's CLAUDE.md table:

| Display name | Slug used in `factions[]` and headers |
|---|---|
| Marquise de Cat | `marquise` |
| Eyrie Dynasties | `eyrie` |
| Woodland Alliance | `woodland` |
| Vagabond | `vagabond` |
| Lizard Cult | `cult` |
| Riverfolk Company | `riverfolk` |
| Underground Duchy | `duchy` |
| Corvid Conspiracy | `corvid` |
| Lord of the Hundreds | `warlord` |
| Keepers in Iron | `keepers-iron` |
| Lilypad Diaspora | `diaspora` |
| Twilight Council | `council` |
| Knaves of the Deepwood | `knaves` |

## Body structure

The body is **one file per source, one H2 section per faction the source
discusses, plus an optional General section for cross-faction content**.
Omit any faction the source does not discuss substantively. The frontmatter
`factions[]` list must match the H2 sections present in the body.

### `# Distilled` — required wrapper heading

Wraps all the source's strategic content. Below it, use H2 sections in this
order:

1. **`## General`** — optional. Cross-faction concepts, meta theory,
   pacing/dominance/suit-economy ideas, tier-list rankings, multi-faction
   matchup matrices. Include only if the source has substantive
   cross-faction content. Skip the section entirely if the source is
   purely faction-by-faction.

2. **`## <Faction Display Name>`** — one per faction substantively
   discussed. Display name verbatim (e.g., `## Eyrie Dynasties`,
   `## Lord of the Hundreds`). For machine parsing, the frontmatter
   `factions[]` list is authoritative.

   Within each faction section, use H3 subsections from this standard set,
   keeping only those the source addresses:

   - `### Win Condition / Scoring Path`
   - `### Opening Priorities`
   - `### Mid-game Pivots`
   - `### Endgame Routes`
   - `### Threat Matchups`
   - `### Card / Item Priorities`
   - `### Common Pitfalls`

   If the source has its own structure that doesn't map to these, mirror
   the source's structure as H3s.

Each subsection is **distillation**, not transcription:
- Paraphrase rather than quote-dump.
- Compress 1000-word source paragraphs into 100-word digests.
- Preserve the source's actual claims; do not insert your own analysis here.
- If the source makes a claim with no supporting reasoning, keep that
  claim but flag it as such ("Source asserts X without justification.").

### `# Key Takeaways` — required

3–10 bullets capturing the source's main load-bearing claims **across all
factions**. Group bullets by faction with bold labels for scanability:

```markdown
# Key Takeaways

- **General:** Crafting tempo dominates the first three rounds — every
  faction wants a craft turn 1.
- **Eyrie Dynasties:** Charismatic leader is the safest first choice;
  Despot punishes the Marquise harder but risks faster turmoil.
- **Marquise de Cat:** Sawmill placement in the keep clearing on turn 1
  is non-negotiable.
- **Lord of the Hundreds:** Bag and Boots are the priority crafts;
  reaching Command 2 by end of turn 1 unlocks the snowball.
```

Order by importance within each faction; order factions by the source's own
emphasis (most-discussed first).

### `# Citations from Source` — required (may be empty)

Any `rule:X.Y.Z`, `card:ROOT-N`, `item:NAME`, `faction:KEY$X.Y.Z`,
`hireling:TAG`, or `faq:<stub>` cites the **source itself** made (not
citations the curator added). Format as a bulleted list with the source's
surrounding sentence:

```markdown
- `rule:7.2.1` — "Eyrie's Decree forces actions in suit-order, even if
  illegal moves trigger turmoil."
```

If the source has no rule citations, write `*None.*` and move on.

### `# Source Notes` — required

Editorial section. The curator's view of the source's reliability, gaps,
and relationship to other content. Cover any of these that apply:

- **Reliability:** what tier it is, how careful the author is.
- **Coverage gaps:** what factions, expansions, or scenarios the source
  omits.
- **Staleness:** how old the source is and which expansions/errata may
  invalidate parts of it.
- **Conflicts with the Law:** any place the source's claim contradicts
  the Law. Use a backtick rule cite like `rule:7.2.1`.
- **Cross-references** to faction profiles or other curated sources, using
  native markdown relative links so they resolve on GitHub:
  - Faction profile: `[Eyrie profile](../../factions/eyrie.md)`
  - Sibling curated source: `[BGG canonical thread](./boardgamegeek--root-strategy-guide.md)`
  - Specific section: `[Eyrie scoring](../../factions/eyrie.md#scoring-engine)`

This section is the **only** place where the curator inserts their own
analysis. The Distilled and Key Takeaways sections must remain the source's
voice. Do **not** populate `accuracy_rating` here — that is set in
frontmatter by the external review pipeline.

## Linking conventions

Use native markdown relative links so they render on GitHub:

| Target | Path from `docs/strategy/sources/<file>.md` |
|---|---|
| Faction profile | `../../factions/<slug>.md` |
| Faction profile section | `../../factions/<slug>.md#<section-anchor>` |
| Sibling curated source | `./<other-file>.md` |
| Strategy README | `../README.md` |
| In-doc anchor | `#<heading-slug>` |

Rule and card citations stay as backtick tokens (e.g., `rule:7.2.1`,
`card:ROOT-12 (Exiles & Partisans)`) — those map to the YAML data trees, not
to renderable Markdown files.

## Editorial discipline

1. **Source's voice in body, curator's voice only in Source Notes.** Do not
   insert original strategy analysis into Distilled or Key Takeaways —
   those represent what the source said.
2. **Pass through, don't promote.** A source's strategy claim is the
   source's claim. Do not relabel it as a `rule:X.Y.Z` cite unless the
   source itself cites that rule.
3. **Preserve nuance.** If the source hedges ("often," "usually," "in my
   experience"), keep the hedge. Don't strengthen claims.
4. **Compress, don't dilute.** A 5,000-word source might distill to 800
   words. Aim for 200–2,000 words of body text per file; longer if the
   source is exceptionally rich and covers many factions.
5. **Citations from the source are gold.** When a source already does the
   work of citing rules, capture every citation — those are reusable and
   verifiable.
6. **Accuracy fields are null at curation time.** The curator never sets
   `accuracy_rating`, `accuracy_notes`, `last_reviewed`, or `reviewed_by`.
   Those are populated by a separate review pipeline.

## Frontmatter validation checklist

Before writing the file:

- [ ] `url` resolves and is the canonical source URL (not a redirect).
- [ ] `factions[]` uses slugs from the table above and matches the H2
  faction sections in the body exactly.
- [ ] `expansions[]` uses the lowercase tags above.
- [ ] `quality_tier` matches the tier in `docs/strategy/README.md`.
- [ ] `date_curated` is today's date in `YYYY-MM-DD`.
- [ ] `summary` is 1–2 sentences and reads like a catalog entry.
- [ ] `accuracy_rating`, `accuracy_notes`, `last_reviewed`, `reviewed_by`
  are all `null`.
- [ ] If the fetch failed or was partial, `fetch_status` is set
  accordingly. Successful fetches may omit the field (`complete` is the
  default).

## Example skeleton

```markdown
---
url: https://spritesanddice.com/posts/strategy-root/
source: Sprites and Dice
author: <author>
title: The Strategy Of Root
date_published: 2020-08-12
date_curated: 2026-04-29
factions:
  - marquise
  - eyrie
  - woodland
  - vagabond
  - cult
  - riverfolk
expansions:
  - base
  - riverfolk
quality_tier: 2
summary: Faction-by-faction strategic overview covering the four base
  factions plus Lizard Cult and Riverfolk Company, with emphasis on
  scoring tempo and faction-specific levers.
accuracy_rating: null
accuracy_notes: null
last_reviewed: null
reviewed_by: null
---

# Distilled

## General

Crafting tempo dominates the first three rounds. Every faction wants a
craft on turn 1; failing to craft creates compounding tempo loss…

## Marquise de Cat

### Win Condition / Scoring Path
…
### Opening Priorities
…
### Threat Matchups
…

## Eyrie Dynasties

### Win Condition / Scoring Path
…
### Opening Priorities
…

## Lizard Cult

### Win Condition / Scoring Path
…
### Common Pitfalls
…

# Key Takeaways

- **General:** Turn-1 craft is non-negotiable for every faction.
- **Marquise de Cat:** Sawmill in the keep clearing first; recruiter second.
- **Eyrie Dynasties:** Charismatic leader is the safest first choice.
- **Lizard Cult:** Garden tempo wins; aggression usually loses.

# Citations from Source

*None.*

# Source Notes

Tier 2 source. Single overview post covering the four base factions plus
Riverfolk-era Cult and Otters. Pre-Marauder, so no Lord of the Hundreds
or Keepers in Iron content. Author hedges most strategic claims with "in
my experience"-style language; treat as one experienced player's view
rather than aggregated wisdom. See [Make Craft Game's Keepers guide](./makecraftgame--keepers-in-iron-guide.md)
for the Marauder gap.
```
