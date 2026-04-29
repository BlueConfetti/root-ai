---
name: strategy-fetch-blog
description: Fetch a third-party blog post or article via WebFetch. Use for any Root strategy source that responds to WebFetch (Make Craft Game, Sprites and Dice, Boardgame Strategist, Elusive Meeple, The Root Database, Steam guides, tier list pages). The simplest fetch path — try this before reaching for Chrome.
user-invocable: true
argument-hint: <blog-or-article-url>
allowed-tools:
  - "WebFetch"
  - "Read"
---

# Strategy Fetch — Blog / Article (WebFetch)

This is the **default** fetcher. Use it for any source that responds to
WebFetch. The Reddit and BGG fetch skills exist only because those two
domains block WebFetch.

## When to use this skill

- The URL is on a domain not listed under "Fetch method: Chrome" in
  `docs/strategy/README.md`.
- A first-pass `WebFetch` confirms the page returns content (status 200,
  body present).

## When to NOT use this skill

- Reddit: `strategy-fetch-reddit`
- BGG forums/threads: `strategy-fetch-bgg`
- YouTube videos / Discord / podcast audio: no automated fetch path —
  pointer reference only, distill from your own notes.

## Workflow

1. **WebFetch the URL** with a focused extraction prompt:

   ```
   WebFetch(
     url=<source-url>,
     prompt="Extract the title, author, publish date if visible, and the
     full article body as plain text. Preserve any rule citations
     (rule:X.Y.Z), card names, and headings. List the H2/H3 headings
     verbatim. If the page is a multi-part guide with links to sub-pages,
     list those links."
   )
   ```

2. **Inspect the response.**
   - If the body is short or marketing-only, the page is likely a category
     index or landing page rather than an article. Look for the actual
     article URL and re-fetch.
   - If the page redirects, WebFetch reports the redirect. Re-fetch the
     redirect target.
   - If the page is paywalled or login-walled, the response will note this.
     Stop and ask the user.

3. **If the source spans multiple pages** (e.g., a faction guide series on
   one blog), call WebFetch per URL. Distill them as **separate files**
   under the appropriate faction directory.

4. **Hand the extracted content** to `strategy-distill` for the structured
   write-out. WebFetch returns markdown-ish text; do not write it raw to
   `docs/strategy/`.

## Common quirks by source

| Domain | Quirk |
|---|---|
| `makecraftgame.com` | Multi-faction guides are linked from category pages; fetch each guide URL separately. |
| `spritesanddice.com` | "Strategy of Root" is one long post covering all factions — write a single distilled file with one `## <Faction>` H2 per covered faction. |
| `boardgamestrategist.wordpress.com` | Stale (last post Sept 2019); flag in `Source Notes`. |
| `steamcommunity.com/sharedfiles/filedetails/?id=...` | Some Steam guides have multi-page navigation; check for `Page 1/2/3` controls. |
| `therootdatabase.com` | Mostly fan-faction content; flag clearly in `Source Notes` since it's not canonical strategy. |
| `tiermaker.com` | Tier list pages are mostly images + voting widgets; the extractable content is the tier labels and faction placements only. |

## Citation conventions for downstream files

- `source: <human-readable site name>` — e.g. "Make Craft Game", not the bare domain.
- `author: <author byline if visible>`
- `date_published: <YYYY-MM-DD if visible, else "unknown">`
- `quality_tier:` look it up in `docs/strategy/README.md`.
