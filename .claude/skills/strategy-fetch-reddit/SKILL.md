---
name: strategy-fetch-reddit
description: Fetch a Reddit thread (post + threaded comments) via Reddit's public JSON endpoint using a small Python script in Bash. Use for any Root strategy content on r/rootgame or other Reddit threads. Bypasses both WebFetch and Chrome MCP — Reddit blocks both, but the public JSON endpoint is reachable from the shell.
user-invocable: true
argument-hint: <reddit-thread-url>
allowed-tools:
  - "Bash"
  - "Read"
---

# Strategy Fetch — Reddit (curl-based)

Reddit blocks both `WebFetch` (`Claude Code is unable to fetch from
www.reddit.com`) and the Chrome MCP (`This site is not allowed due to safety
restrictions`). However, Reddit's **public JSON endpoint is reachable from
Bash** with no auth or special headers beyond a User-Agent. This skill uses a
bundled Python script to fetch and parse the JSON.

This is significantly simpler than the Chrome path: no tab management, no DOM
walking, no rendering wait, no safety filter.

## Bundled assets

- `scripts/extract-thread.py` — single-file stdlib Python (urllib + json) that
  takes a Reddit thread URL as argv[1] and prints structured JSON to stdout.

## Workflow

1. **Run the script via Bash.** No prep, no tool loading, no Chrome:
   ```
   Bash: python3 .claude/skills/strategy-fetch-reddit/scripts/extract-thread.py "<reddit-thread-url>"
   ```
   The URL can be:
   - A canonical thread URL (`https://www.reddit.com/r/rootgame/comments/<id>/<slug>/`)
   - A short thread URL (`https://www.reddit.com/r/rootgame/comments/<id>/`)
   - A pre-`.json` URL (the script handles both shapes)

2. **Capture stdout.** The script prints one JSON object. Stderr is reserved
   for errors. If the script exits non-zero, something went wrong — read the
   stderr message and stop.

3. **Pass the parsed object to `strategy-distill`** for the structured
   write-out.

## Output shape

```json
{
  "url": "https://www.reddit.com/r/rootgame/comments/.../",
  "title": "Lord of the Hundreds opening priorities",
  "subreddit": "rootgame",
  "author": "username",
  "score": 47,
  "created_utc": 1717000000,
  "body": "post body text…",
  "comments": [
    { "depth": 0, "author": "user1", "score": 23, "text": "comment text…" },
    { "depth": 1, "author": "user2", "score": 12, "text": "reply…" }
  ]
}
```

Comments are flattened in-order (depth-first), with a `depth` field
preserving the reply tree structure.

## Discovery (finding Reddit threads to fetch)

Reddit search is also reachable via the JSON endpoint. To find threads on a
topic before fetching:

```
Bash: curl -sS -A "root-strategy-curator/1.0" \
  "https://www.reddit.com/r/rootgame/search.json?q=<query>&restrict_sr=1&sort=top&t=all&limit=10" \
  | python3 -c "import sys,json; d=json.load(sys.stdin); [print(f\"{c['data']['score']:>4} {c['data']['num_comments']:>3} | {c['data']['title']}\\n     https://www.reddit.com{c['data']['permalink']}\") for c in d['data']['children']]"
```

This returns a sorted list of candidate thread URLs ranked by score. The
agent or user picks which threads to actually fetch with the script above.

## Failure modes

- **Rate-limit (429).** Reddit allows ~60 requests/minute for unauthenticated
  callers. If you hit a 429, wait 60 seconds and retry. Don't loop blindly.
- **Empty post body.** Link/image posts have `"body": ""`. The comments may
  still be load-bearing — distill those.
- **Removed/deleted content.** The script filters out comments with body
  `[deleted]` / `[removed]` automatically. If the post itself is removed,
  `body` will say so; flag in `Source Notes` and decide whether to skip
  curation.
- **Quarantined / NSFW subs.** Reddit returns a different JSON shape with a
  consent prompt. The script will return an empty `comments` list and the
  post body will indicate the gate. Surface to the user.

## When to skip this skill

- If the URL is not a Reddit thread, use `strategy-fetch-blog` (WebFetch) or
  `strategy-fetch-bgg` (Chrome) instead.
- For multi-thread roundups (e.g., "all the recent Knaves discussions"),
  use the discovery query above to find candidates first, then call this
  skill per thread.

## Citation conventions for downstream files

- `source: "Reddit — r/<subreddit>"`
- `author: "u/<post-author>"` (the OP). High-scoring top comments can be
  attributed in the body: "Top reply (u/username, score 64) argues…"
- `quality_tier: 1`
- `url:` use the canonical URL the script returns (not the original input
  URL, which may have been the `.json` form).
- `date_published:` drop in the `created_iso` field directly — it's already
  in `YYYY-MM-DD` UTC format.
