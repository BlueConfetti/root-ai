#!/usr/bin/env python3
"""Fetch a Reddit thread (post + threaded comments) via the public JSON endpoint.

Usage:
    python3 extract-thread.py <reddit-thread-url>

Prints one JSON object to stdout. Exits non-zero on error with a message
on stderr.

Reddit's public JSON is reachable without auth as long as a User-Agent is
sent. No API key is required for read-only access.
"""

import json
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone

USER_AGENT = "root-strategy-curator/1.0 (contact: project owner)"


def to_json_url(url: str) -> str:
    """Normalize a Reddit thread URL to its `.json` form."""
    url = url.split("?", 1)[0].rstrip("/")
    if url.endswith(".json"):
        return url
    return url + ".json"


def fetch(url: str) -> object:
    """GET a JSON URL with a custom User-Agent. Returns the parsed JSON."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def walk_comments(children, depth=0, out=None):
    """Flatten Reddit's nested comment tree into a list of dicts with depth."""
    if out is None:
        out = []
    for c in children:
        if c.get("kind") != "t1":
            continue  # skip "more" placeholders
        d = c.get("data") or {}
        body = d.get("body", "")
        if body in ("[deleted]", "[removed]"):
            continue
        out.append(
            {
                "depth": depth,
                "author": d.get("author"),
                "score": d.get("score"),
                "text": body,
            }
        )
        replies = d.get("replies")
        if replies and isinstance(replies, dict):
            walk_comments(
                replies.get("data", {}).get("children", []), depth + 1, out
            )
    return out


def main(argv):
    if len(argv) < 2:
        print(
            "usage: extract-thread.py <reddit-thread-url>", file=sys.stderr
        )
        sys.exit(2)

    json_url = to_json_url(argv[1])
    try:
        data = fetch(json_url)
    except urllib.error.HTTPError as e:
        print(f"HTTP {e.code} fetching {json_url}: {e.reason}", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"network error fetching {json_url}: {e.reason}", file=sys.stderr)
        sys.exit(1)

    if not (
        isinstance(data, list)
        and len(data) >= 2
        and data[0].get("data", {}).get("children")
    ):
        print(f"unexpected JSON shape from {json_url}", file=sys.stderr)
        sys.exit(1)

    post = data[0]["data"]["children"][0].get("data") or {}
    comments_listing = data[1].get("data", {}).get("children", [])

    created_utc = post.get("created_utc")
    created_iso = (
        datetime.fromtimestamp(created_utc, tz=timezone.utc).strftime("%Y-%m-%d")
        if created_utc is not None
        else None
    )

    out = {
        "url": "https://www.reddit.com" + post.get("permalink", ""),
        "title": post.get("title", ""),
        "subreddit": post.get("subreddit", ""),
        "author": post.get("author"),
        "score": post.get("score"),
        "created_utc": created_utc,
        "created_iso": created_iso,  # YYYY-MM-DD UTC, ready to drop into date_published
        "body": post.get("selftext", ""),
        "comments": walk_comments(comments_listing),
    }

    json.dump(out, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main(sys.argv)
