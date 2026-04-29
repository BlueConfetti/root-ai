---
name: BGG thread 2138017 stub needs completion
description: boardgamegeek--root-strategy-guide.md is a stub; needs Chrome MCP session to populate body content
type: project
---

`docs/strategy/sources/boardgamegeek--root-strategy-guide.md` was written as a
stub on 2026-04-29 because Chrome MCP was unavailable.

**Why:** BGG blocks WebFetch (403) and the chrome-in-chrome MCP extension was
not connected during the initial pipeline validation run.

**How to apply:** When the user next asks to curate BGG content or refresh this
file, confirm Chrome MCP is available first (see feedback_chrome_mcp_availability.md),
then re-run `strategy-fetch-bgg` for `https://boardgamegeek.com/thread/2138017`.
The bundled extractor at `.claude/skills/strategy-fetch-bgg/scripts/extract-thread.js`
has been validated against this thread and returns 25 articles. Write the
result with a date suffix (`boardgamegeek--root-strategy-guide--2026-XX-XX.md`)
and ask the user whether to replace the stub.
