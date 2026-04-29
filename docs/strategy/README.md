---
title: Root Strategy — Curated Third-Party Content
last_updated: 2026-04-29
---

# Root Strategy — Curated Third-Party Content

This directory holds **distilled summaries of third-party Root strategy
content**: blog posts, BGG forum threads, Reddit discussions, podcast notes,
and YouTube channel analyses. Each file is a structured digest of one external
source, written so an agent can read it quickly and cite it back.

The curated content is **derivative** and **non-canonical**. The Law of Root
(`rules/content/rules/root/en-US/p16/`) is always the rules authority; faction
profiles in `docs/factions/` are the project's own derivative strategy layer.
This directory is one level further out — it is *what other people say about
Root*.

## How to read a distilled file

Every file follows the schema in `.claude/skills/strategy-distill/SKILL.md`:

- **Frontmatter** — `url`, `source`, `author`, `title`, `date_published`,
  `date_curated`, `factions[]`, `expansions[]`, `quality_tier`, `summary`,
  plus accuracy fields (`accuracy_rating`, `accuracy_notes`,
  `last_reviewed`, `reviewed_by`) that the curator leaves null and a
  separate review pipeline populates.
- **Distilled** — `# Distilled` wrapper, then `## General` for cross-faction
  content (optional) and one `## <Faction Display Name>` H2 per faction the
  source discusses substantively. H3 subsections within each faction
  (Win Condition / Opening / Threat Matchups / etc.).
- **Key Takeaways** — 3–10 bullets grouped by faction with bold labels.
- **Citations from Source** — any `rule:X.Y.Z` cites the source itself made.
- **Source Notes** — editorial: reliability, gaps, conflicts with the Law,
  and relative-path links to faction profiles or sibling curated sources.

## How content is added

Three paths:

1. **One-off curation:** run `/root-strategy-curate <source-or-topic>` to
   dispatch a single `root-strategy-curator` agent. Best for adding one
   specific URL or one specific source's faction guide.
2. **End-to-end pipeline:** run `/root-strategy-pipeline [scope] [--discover]`
   — fat slash command orchestrator that spawns parallel discovery
   workers, dedupes against already-curated sources, then runs parallel
   extraction in waves of 3. Manifests at
   `docs/strategy/_runs/<run-id>.json` (gitignored), resumable via
   `--resume <run-id>`.
3. **Manual:** create a file by hand following the schema. Useful when
   you read something offline (a podcast episode, a printed PDF) and
   want to capture takeaways.

## How content is reviewed

After curation, run `/root-3p-review [scope] [--last N] [--only-new]`
to fill in the accuracy frontmatter fields (`accuracy_rating`,
`accuracy_notes`, `last_reviewed`, `reviewed_by`) and append a
`# Review` section to each curated doc. The reviewer cross-checks every
claim against the Law of Root and the project's faction profiles.

The review section is appended after a trailing `---` separator and
contains: verified claims, conflicts with the Law, stale points,
strategic judgment notes, and verified-vs-flagged citations from the
source. Reviews are idempotent — re-running replaces the prior section.

Pipeline:
- **Curator** owns: frontmatter (except accuracy fields), `# Distilled`,
  `# Key Takeaways`, `# Citations from Source`, `# Source Notes`.
- **Reviewer** owns: the 4 accuracy frontmatter fields, and the
  `# Review` section after the trailing `---`.

The two never overwrite each other.

## Directory layout

```
docs/strategy/
  README.md                         (this file)
  sources/
    <domain>--<title-slug>.md       (one file per source, all flat)
  _runs/                            (gitignored — pipeline manifests)
    <run-id>.json
```

**One file per source, not per faction.** A source covering multiple
factions writes a single file with one body section per faction it
discusses. The frontmatter `factions[]` list is the authoritative index
into which factions a source covers.

Filenames use the source's domain (without TLD) plus a kebab-case slug of
the title:

- `makecraftgame--keepers-in-iron-guide.md`
- `spritesanddice--strategy-of-root.md`
- `boardgamegeek--root-strategy-guide.md`
- `reddit-rootgame--lord-of-hundreds-opening.md`
  (Reddit prefixes the subreddit since the domain is shared)

To find which sources cover a given faction:
```
grep -l "^- eyrie$" docs/strategy/sources/*.md
```
or read each frontmatter block and inspect `factions[]`.

## Source Roster

The agent dispatches sources to fetch skills based on the table below.

### Tier 1 — High-signal, broad, current

| Source | URL | Fetch method | Faction coverage | Notes |
|---|---|---|---|---|
| r/rootgame | https://www.reddit.com/r/rootgame/ | `strategy-fetch-reddit` (Bash + Python) | All | Reddit blocks WebFetch *and* Chrome MCP, but the public JSON endpoint is reachable from the shell — no auth, no rendering |
| BGG Root strategy forum | https://boardgamegeek.com/forum/2344731/root/strategy | (forum index — not yet supported by `strategy-fetch-bgg`; pick specific thread URLs) | All | BGG returns 403 to WebFetch and 401 to anonymous XML API |
| BGG canonical strategy thread | https://boardgamegeek.com/thread/2138017 | `strategy-fetch-bgg` (Bash + Python) | Base game + early expansions | The de-facto community FAQ; `api.geekdo.com/api/article` JSON endpoint reachable from shell with browser-style headers |
| Woodland Warriors Discord | https://discord.gg/rbFWvDP | (manual only) | All | Not scrapeable; pointer reference only |
| The Root Database | https://therootdatabase.com/ | `strategy-fetch-blog` | Fan factions + components | Tracks current Law of Root |

### Tier 2 — Long-form written guides, evergreen

| Source | URL | Fetch method | Faction coverage | Notes |
|---|---|---|---|---|
| Make Craft Game (Lily Gould) | https://makecraftgame.com/ | `strategy-fetch-blog` | Through Marauder Expansion | Highest-quality individual blog |
| Sprites and Dice — "Strategy Of Root" | https://spritesanddice.com/posts/strategy-root/ | `strategy-fetch-blog` | Base + Riverfolk + UD | Per-faction overview |
| Boardgame Strategist | https://boardgamestrategist.wordpress.com/category/root/ | `strategy-fetch-blog` | Base + Riverfolk only | **Stale (last post Sept 2019)** |
| Elusive Meeple | https://elusivemeeple.com/2019/05/19/root-strategy-tips/ | `strategy-fetch-blog` | Base game only | Single short post |
| Steam guide "ROOT: Factions Unveiled" | https://steamcommunity.com/sharedfiles/filedetails/?id=3288028859 | `strategy-fetch-blog` | Multiple expansions | Faction-by-faction |

### Tier 3 — Podcasts & video (archive-only or manual transcription)

| Source | URL | Fetch method | Notes |
|---|---|---|---|
| Woodland War Machine | https://woodlandwarmachine.podbean.com/ | (manual transcription) | 72 episodes, ended June 2023; podbean RSS may be parseable for episode metadata |
| Romp (Leder podcast) | (search) | (manual) | Audio-only |
| NitroRev's Root | https://www.youtube.com/channel/UCPSMvb6Tz_cQb9SD1FlxI3Q | (manual + YouTube transcripts) | Video-only |
| Lord of the Board | https://www.youtube.com/c/LordoftheBoard | (manual + YouTube transcripts) | Video-only |
| WeiRd Root | https://www.youtube.com/c/WeiRdRoot | (manual + YouTube transcripts) | Fan content focus |

### Tier 4 — Quantitative / meta

| Source | URL | Fetch method | Notes |
|---|---|---|---|
| TierMaker community tier lists | https://tiermaker.com/categories/board-games/root-digital-board-game-1114062 | `strategy-fetch-blog` | Latest update Oct 2025 |
| Make Craft Game tournament stats | https://makecraftgame.com/2021/05/22/root-tournament-overall-statistics/ | `strategy-fetch-blog` | Aggregate win rates |

### Tier 5 — Skip or use with caution

- **playrootgame.com** — duplicate URL patterns, SEO/AI-generated style. Spot-check against the Law before citing.
- **thegamersguides.com / stemgeek.com / meeplescorner.co.uk** — beginner-level, generic.

## Coverage caveats by source age

- Pre-2022 sources miss **Marauder** (Lord of the Hundreds, Keepers in Iron).
- Pre-2024 sources miss **Homeland** (Lilypad Diaspora, Twilight Council, Knaves of the Deepwood).
- Tag `expansions[]` in frontmatter so a future agent can filter accordingly.

## Output discipline

- **Pass through, don't promote.** A source's strategy claim is *that source's
  claim*. Do not promote it to a `rule:X.Y.Z` cite without verifying against
  the Law.
- **Preserve cites the source already made.** If a blog post cites
  `rule:7.2.1`, capture it under "Citations from Source."
- **Flag conflicts with the Law.** If a source says something the Law
  contradicts, note it in "Source Notes."
