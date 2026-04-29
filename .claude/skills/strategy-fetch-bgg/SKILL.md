---
name: strategy-fetch-bgg
description: Fetch a BoardGameGeek thread (all pages, all articles, with author display names) via the api.geekdo.com private JSON endpoint using a small Python script in Bash. Use for any Root strategy content on BGG forums or threads. Bypasses BGG's WebFetch 403 and the anonymous XML API 401 — the SPA-backing JSON endpoint is reachable from the shell with browser-style headers.
user-invocable: true
argument-hint: <bgg-thread-url-or-id>
allowed-tools:
  - "Bash"
  - "Read"
---

# Strategy Fetch — BoardGameGeek (curl-based)

BGG returns 403 to `WebFetch` and 401 to anonymous `xmlapi2` calls.
However, the **`api.geekdo.com/api/article` endpoint** that backs the BGG
SPA is reachable from `curl` with `Origin` and `Referer` headers
identifying boardgamegeek.com. This skill uses a bundled Python script
that paginates through every article in a thread and resolves author
user IDs to display names.

This is the path going forward. It replaces the previous Chrome-based DOM
walker, which was significantly more complex and only ever saw page 1
(25 articles) of multi-page threads.

## Bundled assets

- `scripts/extract-thread.py` — single-file stdlib Python (urllib + json)
  that takes a BGG thread URL or numeric ID as argv[1], paginates every
  page, fetches author user records, and prints one structured JSON
  object to stdout.

## Why this works

The BGG SPA hits `https://api.geekdo.com/api/article?threadid=<id>&pageid=<n>`
to hydrate threads. The endpoint is unauthenticated but rejects requests
without browser-style headers. We send the same `Origin` and `Referer`
the SPA sends, plus a Chrome User-Agent string. No login, no API key, no
rate-limit concerns at typical curation volume.

Author display names live behind a separate `https://api.geekdo.com/api/users/<id>`
endpoint, which the script also hits (with in-process caching to avoid
duplicate fetches per thread).

## Workflow

1. **Run the script via Bash.** No prep, no tool loading, no Chrome:
   ```
   Bash: python3 .claude/skills/strategy-fetch-bgg/scripts/extract-thread.py "<bgg-thread-url-or-id>"
   ```
   Accepts either form:
   - Full URL: `https://boardgamegeek.com/thread/2138017` (or with slug)
   - Bare numeric ID: `2138017`

2. **Capture stdout.** The script prints one JSON object. Stderr carries
   warnings (e.g., user-fetch fallbacks) and errors. Non-zero exit means
   something went wrong — read stderr and stop.

3. **Pass the parsed object to `strategy-distill`** for the structured
   write-out.

## Output shape

```json
{
  "url": "https://boardgamegeek.com/thread/2138017/article/31072969",
  "title": null,
  "articles": [
    {
      "index": 0,
      "id": "31072969",
      "author": "Tristan Stevens",
      "username": "AuroraeEagle",
      "user_id": 1529825,
      "date": "2019-01-24T23:06:17+00:00",
      "edit_date": "2019-03-22T04:18:50+00:00",
      "first_post": true,
      "body": "Root Guide: Chapter 1 — …"
    },
    { "index": 1, "...": "..." }
  ],
  "is_forum_index": false,
  "thread_links": [],
  "_articles_seen": 71,
  "_pages_fetched": 3,
  "_total_articles_reported": 71
}
```

The `title` field is `null` because the article API does not return
thread title. The caller (curator) supplies it from the source roster
or from another source-of-truth.

## Pagination

BGG returns 25 articles per page by default. The script pages through
every result automatically up to 50 pages (ample headroom — the longest
Root threads have <200 articles). If a thread exceeds 50 pages, the
script logs a warning and stops; that case is unrealistic for any
strategy thread we'd curate.

## Forum index pages (TODO)

The current script fetches **threads only**, not forum index pages
(`/forum/<id>/...`). Forum indexes use a different endpoint
(`/api/forum?forumid=<id>`) which can be added if needed — for now,
treat forum-index URLs as a list-of-threads source: the user (or curator
agent) picks specific thread URLs to fetch.

## Failure modes

- **HTTP 403/401.** The headers in the script are tuned to match a real
  Chrome browser. If BGG tightens its origin/referer policy, refresh the
  headers from a live `curl` copied out of Chrome DevTools.
- **Empty articles array.** Either the thread ID is wrong or the thread
  was deleted. Check the URL.
- **Slow user-fetch loop.** A thread with 71 articles by 30 unique
  authors triggers ~30 user lookups (cached). On a slow connection that
  can take 10–30 seconds. Acceptable for curation cadence.
- **Body field is empty.** Some posts contain only attachments or links
  with no text. The script falls back to a lightweight HTML-strip of
  `bodyXml`; if both are empty, the body is empty and the post is
  effectively unconsumable. Skip it during distillation.

## When to skip this skill

- If the URL is not a BGG thread, use `strategy-fetch-blog` (WebFetch).
- For BGG forum *index* pages (lists of threads), this skill returns
  nothing useful — use the `strategy-discover` skill or feed thread URLs
  manually.
- For BGG game pages, reviews, or other non-thread content, this skill
  does not apply.

## Citation conventions for downstream files

- `source: "BoardGameGeek — <thread title>"`
- `author: "<display name> (@<username> on BGG)"` for the OP. If the
  thread has multiple substantive contributors, treat them all as the
  same source (one curated file) but attribute high-signal claims by
  username in the body or Source Notes.
- `quality_tier: 1`
- `url:` use the canonical URL the script returns (it points to the
  first article, which BGG treats as the thread anchor).
- `date_published:` use the ISO date from `articles[0].date` truncated
  to `YYYY-MM-DD`.
