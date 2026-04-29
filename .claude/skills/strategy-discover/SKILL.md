---
name: strategy-discover
description: Discover new third-party Root strategy sources via WebSearch. Use when the curated source roster (docs/strategy/README.md) lacks coverage for a topic, faction, or recent meta question. Returns a ranked candidate list for the user to approve before fetching.
user-invocable: true
argument-hint: <topic | faction | "recent meta">
allowed-tools:
  - "WebSearch"
  - "WebFetch"
  - "Read"
  - "Grep"
---

# Strategy Discover — Find New Sources

This skill is a **discovery** step, not a fetcher. It runs WebSearches,
filters candidates, and returns a ranked list of URLs the curator (or the
user) should consider adding to the corpus. Fetching and distilling is
done separately by `strategy-fetch-*` and `strategy-distill`.

## When to use

- The user asks for content on a faction or topic the existing roster
  does not cover well (e.g., "tournament meta 2025," "Knaves of the
  Deepwood opening").
- The user wants to add new sources beyond what's already in
  `docs/strategy/README.md`.
- A faction-scoped curation request comes in but the roster has no
  faction-specific sources for that faction.

When the request names a known source or a specific URL, **skip
discovery** — go straight to the matching fetch skill.

## Workflow

1. **Read `docs/strategy/README.md`** to know what's already known. Do
   not re-propose sources already in the roster unless the request
   explicitly asks to refresh them.

2. **Read existing curated files** at `docs/strategy/sources/` to know
   what's already curated. Do not re-propose URLs already represented
   there.

3. **Run multiple targeted WebSearches.** A single query is rarely
   enough — vary phrasing to surface different sources. Use 3–5
   queries, including:
   - Faction + "strategy guide" (e.g., `Lord of the Hundreds Root
     strategy guide`)
   - Faction + "tier list" (e.g., `Root factions tier list 2025`)
   - Faction + "opening" / "tournament" / "matchup"
   - Source-type queries: `Root board game blog faction`,
     `r/rootgame strategy <faction>`, `boardgamegeek Root strategy
     <faction>`
   - Year-bounded queries when freshness matters: `Root <faction>
     strategy 2025` or `2024`.
   - When asking about post-2024 expansions (Homeland: Diaspora,
     Council, Knaves), constrain by year — older sources cannot cover
     them.

4. **Filter the result set:**
   - **Drop Tier 5 patterns** — `playrootgame.com`, `thegamersguides.com`,
     `stemgeek.com`, `meeplescorner.co.uk`, and any URL with the
     hallmarks of SEO/AI generation (duplicate slugs across many pages,
     "Ultimate Guide" + year in title, generic navigation).
   - **Drop already-curated URLs** by checking
     `docs/strategy/sources/`.
   - **Drop already-rostered domains** unless the candidate is a
     specific page not yet captured (e.g., a new Make Craft Game post
     on a faction we haven't curated yet).
   - **Drop non-strategic content** — reviews, unboxing posts, "is Root
     fun?" articles. We want strategy, not opinion.

5. **Annotate each surviving candidate:**
   - Domain and likely tier (1 if BGG/Reddit/Discord, 2 if known
     long-form blog, 3 if podcast/video, 4 if quantitative).
   - Fetch method (`strategy-fetch-blog` for WebFetch-friendly,
     `strategy-fetch-reddit` for Reddit, `strategy-fetch-bgg` for BGG;
     `(manual)` for podcasts/videos).
   - Faction coverage signal — what factions the snippet/title implies
     are covered.
   - Freshness signal — date in URL/title where visible.
   - One-sentence relevance note.

6. **Return the ranked candidate list** as a markdown table to the
   caller. Recommend a top 3–5 by relevance.

7. **Wait for user approval.** Do not fetch any candidate without
   explicit user confirmation. (The curator agent handles this gating;
   the discover skill itself does not fetch.)

## Output shape

A markdown table with columns:

| # | URL | Tier | Fetch | Factions | Freshness | Why |
|---|---|---|---|---|---|---|
| 1 | … | 2 | blog | knaves | 2025 | Long-form Knaves opening guide |

Plus a short prose section flagging:
- Roster updates the user should make by hand for any sources promoted
  to "regularly used" status.
- Any candidates that look promising but raised quality concerns
  (e.g., recent post on an otherwise-Tier-5 domain).

## Failure modes

- **No useful candidates.** The roster may already cover the space.
  Surface this fact rather than padding the result. "WebSearch surfaced
  only sources already in the roster — no new candidates for Eyrie."
- **All candidates are Tier 5.** Same response. Better to return zero
  than to pollute the corpus.
- **Faction is too new for any source.** Common for Homeland factions
  (Diaspora, Council, Knaves) since the expansion is recent. Surface
  this and recommend the user check Reddit/Discord directly.

## Citation conventions for downstream files

The discover skill itself writes nothing under `docs/strategy/`. Once a
candidate is approved and fetched, the matching fetch skill + distill
skill write the file with normal frontmatter conventions.
