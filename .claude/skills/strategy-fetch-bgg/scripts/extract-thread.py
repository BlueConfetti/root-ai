#!/usr/bin/env python3
"""Fetch a BoardGameGeek thread (all pages, with author display names) via the
private api.geekdo.com JSON endpoint.

Usage:
    python3 extract-thread.py <bgg-thread-url-or-id>

Prints one JSON object to stdout. Exits non-zero on error with a message
on stderr.

The api.geekdo.com endpoint backs the BGG SPA. It is reachable without
auth as long as Origin and Referer headers identify boardgamegeek.com.
This bypasses Chrome scraping entirely.

Output shape matches the previous Chrome-based extractor so the distill
schema stays the same:
    {
      "url": canonical thread URL,
      "title": "(unknown — API does not return thread title; caller may inject)",
      "articles": [
        {"index", "id", "author", "username", "date", "edit_date", "body"}
      ],
      "is_forum_index": false,
      "thread_links": [],
      "_articles_seen": <int>,
      "_pages_fetched": <int>,
      "_total_articles_reported": <int>
    }
"""

import json
import re
import sys
import urllib.error
import urllib.request
from typing import Any

API_BASE = "https://api.geekdo.com/api"
HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "Origin": "https://boardgamegeek.com",
    "Referer": "https://boardgamegeek.com/",
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/147.0.0.0 Safari/537.36"
    ),
}


def parse_thread_id(url_or_id: str) -> str:
    """Accept a BGG thread URL or a bare numeric ID and return the ID."""
    s = url_or_id.strip()
    if s.isdigit():
        return s
    m = re.search(r"/thread/(\d+)", s)
    if m:
        return m.group(1)
    raise ValueError(f"could not extract thread id from {url_or_id!r}")


def fetch_json(url: str) -> Any:
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def fetch_all_pages(thread_id: str) -> tuple[list[dict], int]:
    """Fetch every page of articles in a thread. Returns (articles, total)."""
    all_articles: list[dict] = []
    page = 1
    total = None
    while True:
        url = f"{API_BASE}/article?threadid={thread_id}&pageid={page}"
        data = fetch_json(url)
        articles = data.get("articles", [])
        if not articles:
            break
        all_articles.extend(articles)
        total = data.get("total")
        if total is not None and len(all_articles) >= total:
            break
        page += 1
        # Safety stop: no thread should need more than 50 pages of 25.
        if page > 50:
            print(
                f"warning: stopped at page {page} — thread may be larger",
                file=sys.stderr,
            )
            break
    return all_articles, total or len(all_articles)


def fetch_user(user_id: int, cache: dict) -> dict:
    """Fetch a user record by ID, with in-process cache."""
    if user_id in cache:
        return cache[user_id]
    try:
        data = fetch_json(f"{API_BASE}/users/{user_id}")
    except urllib.error.HTTPError as e:
        print(f"warning: user {user_id} fetch returned {e.code}", file=sys.stderr)
        data = {"username": None, "firstname": None, "lastname": None}
    cache[user_id] = data
    return data


def display_name(user: dict) -> str:
    """Build a display name from the user record."""
    first = (user.get("firstname") or "").strip()
    last = (user.get("lastname") or "").strip()
    if first or last:
        return (first + " " + last).strip()
    return user.get("username") or "unknown"


def html_strip(html: str) -> str:
    """Very lightweight HTML-to-text fallback. The API already gives a plain
    `body` field, so this is rarely needed — kept as a backstop."""
    if not html:
        return ""
    out = re.sub(r"<br\s*/?>", "\n", html, flags=re.I)
    out = re.sub(r"<[^>]+>", "", out)
    return out.strip()


def main(argv: list[str]) -> None:
    if len(argv) < 2:
        print("usage: extract-thread.py <bgg-thread-url-or-id>", file=sys.stderr)
        sys.exit(2)

    thread_id = parse_thread_id(argv[1])

    try:
        articles_raw, total = fetch_all_pages(thread_id)
    except urllib.error.HTTPError as e:
        print(f"HTTP {e.code} fetching thread {thread_id}: {e.reason}", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"network error fetching thread {thread_id}: {e.reason}", file=sys.stderr)
        sys.exit(1)

    user_cache: dict[int, dict] = {}
    pages_fetched = max(1, (len(articles_raw) + 24) // 25)

    articles_out = []
    for idx, a in enumerate(articles_raw):
        author_id = a.get("author")
        user = fetch_user(author_id, user_cache) if author_id else {}
        body = a.get("body") or html_strip(a.get("bodyXml", ""))
        articles_out.append(
            {
                "index": idx,
                "id": a.get("id"),
                "author": display_name(user),
                "username": user.get("username"),
                "user_id": author_id,
                "date": a.get("postdate", ""),
                "edit_date": a.get("editdate"),
                "first_post": a.get("firstPost", False),
                "body": body,
            }
        )

    canonical_url = (
        f"https://boardgamegeek.com/thread/{thread_id}/article/"
        f"{articles_out[0]['id']}"
        if articles_out
        else f"https://boardgamegeek.com/thread/{thread_id}"
    )
    out = {
        "url": canonical_url,
        "title": None,  # API does not return thread title; caller injects
        "articles": articles_out,
        "is_forum_index": False,
        "thread_links": [],
        "_articles_seen": len(articles_out),
        "_pages_fetched": pages_fetched,
        "_total_articles_reported": total,
    }

    json.dump(out, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main(sys.argv)
