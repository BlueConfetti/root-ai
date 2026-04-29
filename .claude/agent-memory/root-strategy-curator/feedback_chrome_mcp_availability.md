---
name: Chrome MCP availability check
description: Chrome MCP tools (mcp__claude-in-chrome__*) are not always present in the deferred tool set — check before dispatching strategy-fetch-bgg
type: feedback
---

Before running `strategy-fetch-bgg`, verify Chrome MCP availability with
`ToolSearch(query="select:mcp__claude-in-chrome__tabs_context_mcp")`. If the
tool is not returned, the Claude-in-Chrome extension is not connected and the
BGG fetch will fail.

**Why:** During the first real pipeline run (2026-04-29), ToolSearch returned
no results for all chrome MCP tool names. WebFetch also returns 403 on BGG.
The result was a stub file rather than real content.

**How to apply:** At the start of any curation session that includes a BGG
source, run the ToolSearch check first. If it fails, write a stub file with
the fetch-failed note and tell the user to retry in a session where Chrome
MCP is active. Do not attempt WebFetch on BGG as a fallback — it always 403s.
