---
name: strategy-source-roster
description: Use to look up the curated roster of third-party Root strategy sources — what each source covers, which fetch skill it requires (Chrome vs WebFetch), and quality tier. Mirrors the source roster in docs/strategy/README.md.
user-invocable: true
allowed-tools:
  - "Read"
  - "Grep"
---

# Strategy Source Roster Lens

Reference recipe for the curated roster of third-party Root strategy sources.
The canonical roster lives in `docs/strategy/README.md` — this skill is a
lookup lens, not a duplicate.

## Why this exists

When a curator agent needs to gather strategy on a topic ("Lord of the Hundreds
opening play," "Eyrie vs Marquise mid-game"), it consults this roster to
decide:

1. **Which sources to hit** — based on faction coverage, tier, and freshness.
2. **Which fetch skill to use** — Reddit/BGG need `strategy-fetch-reddit` /
   `strategy-fetch-bgg` (Chrome-based, since WebFetch is blocked); blogs use
   `strategy-fetch-blog` (WebFetch-based).
3. **Whether to skip a source** — Tier 5 sources are SEO/AI-generated and
   should not be cited.

## Files

- `docs/strategy/README.md` — the canonical roster + schema
- `docs/strategy/sources/<domain>--<title-slug>.md` — distilled
  per-source files (one file per source, faction subsections inside)

## Lookup recipes

**Read the full roster:**
```
Read docs/strategy/README.md
```

**Find sources that cover a specific faction:**
```
grep -nA 2 "<faction>" docs/strategy/README.md
```

**Find which fetch skill to use for a domain:**
```
grep -n "<domain>" docs/strategy/README.md
```
The "Fetch method" column names the skill.

**See what's already curated for a faction** (frontmatter `factions[]`
list is the index):
```
grep -l "^- <faction-slug>$" docs/strategy/sources/*.md
```

**See what's been curated across the whole repo:**
```
ls docs/strategy/sources/
```

**Find a faction's section across all curated sources:**
```
grep -A 50 "^## <Faction Display Name>" docs/strategy/sources/*.md
```

## Quality tier guidance

- **Tier 1** — broad community discussion (Reddit, BGG, Discord). Use for
  current meta, recent releases, and questions where consensus matters.
- **Tier 2** — long-form blog guides. Use for faction deep dives and
  structured strategy.
- **Tier 3** — podcasts/videos. Mostly out-of-band; use as pointer references.
- **Tier 4** — quantitative tier lists and tournament stats. Use to ground
  claims about "the strong factions" or "the weak matchups."
- **Tier 5** — skip. SEO/AI content; not a reliable source.

## Faction coverage rules of thumb

- Pre-2022 sources do not cover **Marauder** (Lord of the Hundreds, Keepers in
  Iron).
- Pre-2024 sources do not cover **Homeland** (Lilypad Diaspora, Twilight
  Council, Knaves of the Deepwood).
- For p4/p6 historical questions, no third-party source is a reliable witness
  — go to the older `rules.yml` directly.

## Output discipline (when callers cite curated content)

- Curated content is **derivative**. Cite it as "<source> claims..." rather
  than as fact.
- If a curated file's "Citations from Source" section names a `rule:X.Y.Z`,
  prefer citing the underlying rule directly — the Law is the authority.
- "Source Notes" sections may flag conflicts with the Law. Honor those
  flags; do not relay a contradicted claim without the caveat.
