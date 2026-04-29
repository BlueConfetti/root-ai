---
description: Gather third-party Root strategy content from community sources and distill it into structured per-source files under docs/strategy/.
model: sonnet
allowed-tools:
  - Agent
argument-hint: <faction | source | url | topic>
---

# /root-strategy-curate

Thin wrapper that hands a curation request off to the `root-strategy-curator`
agent.

## What this command does

The agent gathers strategy content from third-party Root sources (blogs, BGG
threads, Reddit, etc.) and writes one structured Markdown file per source
under `docs/strategy/<faction-slug>/`. It does not synthesize across sources
— each file is a faithful distillation of one source's view, separate from
the root-analyst pipeline.

## Workflow

1. Take the user's input as the curation target. Pass through verbatim.
   Common shapes:
   - **Faction**: "Lord of the Hundreds" / "Eyrie" / "all Marauder factions"
   - **Source**: "Make Craft Game" / "the BGG strategy thread"
   - **URL**: a direct link to a blog post, BGG thread, or Reddit thread
   - **Topic**: "opening play" / "endgame scoring" / "matchups against
     Vagabond"
   - **Empty**: prompt the user once for what to curate, then proceed.

2. Dispatch via the Agent tool:
   - `subagent_type: root-strategy-curator`
   - `description`: short summary (e.g. "Curate Make Craft Game Marauder")
   - `prompt`: the full user input plus any context the user supplied.
     Include explicit Chrome authorization phrasing if the user has already
     consented to Chrome use this session ("user has authorized Chrome MCP
     for this session").

3. Relay the curator's report verbatim. Do not summarize the file contents —
   the user can read the written files directly.

## Notes

- The agent will list its plan (URLs to hit, fetch method per URL) before
  executing if the work spans >3 sources or involves Chrome. Approve the
  plan if asked.
- For one-off curation of a single URL, the user can also invoke a fetch
  skill directly: `/strategy-fetch-blog <url>`,
  `/strategy-fetch-reddit <url>`, `/strategy-fetch-bgg <url>`. Those skills
  return raw extracted content; they do not write distilled files.
- The source roster lives at `docs/strategy/README.md` and is hand-edited.
  If the agent suggests a roster update at the end of its run, the user
  applies it manually.
