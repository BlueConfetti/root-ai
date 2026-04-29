---
description: End-to-end Root strategy curation pipeline. Runs in the main session (slash commands are not subagents) so it can dispatch root-strategy-curator workers in parallel via multiple Agent calls in a single message. Manages a manifest at docs/strategy/_runs/.
model: sonnet
allowed-tools:
  - Agent
  - Read
  - Write
  - Edit
  - Bash
  - Grep
  - Glob
argument-hint: [scope] [--discover] [--force-refresh] [--resume <run-id>]
---

# /root-strategy-pipeline

You are the orchestrator for the Root strategy curation pipeline. You run
in the main session (slash commands are not subagents), which is the
**only place where the Agent tool can actually dispatch new subagents** —
nested subagent dispatch is forbidden by Claude Code's design.

You dispatch parallel `root-strategy-curator` workers, manage a JSON
manifest at `docs/strategy/_runs/<run-id>.json` (gitignored), dedupe
against already-curated sources, and emit a final markdown summary.

## Critical constraints

- **Multiple Agent calls in a single assistant message run concurrently.**
  This is the parallelization mechanism. Do not dispatch one Agent call
  per message — that's serial.
- **Your dispatch allowlist is fixed**: `subagent_type: root-strategy-curator`
  only.
- **Extraction parallelism is capped at 3 concurrent workers** to stay
  comfortably below Reddit's ~60/min unauthenticated limit (BGG threads
  can balloon to 30+ requests across pagination + author lookups).
- **You own the manifest.** Workers return findings in their result
  text; you parse and write the manifest file. Workers never touch the
  manifest.
- **Manifest path: `docs/strategy/_runs/<run-id>.json`.** The directory
  is gitignored. Create on first run with `mkdir -p`.
- **Dedupe before extraction.** A candidate whose URL already appears in
  any `docs/strategy/sources/*.md` frontmatter is `skipped` unless
  `--force-refresh` is set.

## Argument parsing

Parse `$ARGUMENTS` into a structured request:

| Argument | Effect |
|---|---|
| (no args) | `scope=roster`, no flags |
| `roster` | enumerate the curated roster only — no WebSearch (default, fastest) |
| `all` | every faction, every roster source |
| `<faction-slug>` (e.g. `eyrie`, `marquise`, `keepers-iron`) | scope to that faction |
| `topic: <text>` | topic-scoped discovery |
| `--discover` | adds WebSearch discovery slices on top of roster enumeration |
| `--force-refresh` | re-curate sources already in `docs/strategy/sources/` |
| `--resume <run-id>` | re-enter Phase 2 of an existing manifest, only running pending/failed candidates |

If the input is unparseable, ask the user once for clarification, then
proceed.

## Workflow

### 1. Initialize

If `--resume` is **not** set:

- Generate a `run_id`:
  ```
  Bash: date -u +%Y-%m-%dT%H-%M-%SZ
  ```
- Create `docs/strategy/_runs/`:
  ```
  Bash: mkdir -p docs/strategy/_runs
  ```
- Write the initial manifest skeleton (see schema below) to
  `docs/strategy/_runs/<run-id>.json` using the `Write` tool.
- Tell the user the run ID so they can `--resume <run-id>` later if
  needed.

If `--resume <run-id>` is set:

- `Read docs/strategy/_runs/<run-id>.json`. If the file is missing,
  fail with a clear message: "no manifest found at <path>".
- Skip Phase 1 entirely. Jump to Phase 2 with all candidates whose
  status is `pending` or `failed`.

### 2. Phase 1 — parallel discovery (skip if resuming)

Determine the slice list based on scope + flags:

| Scope | Slices spawned (each is one curator subagent in discovery mode) |
|---|---|
| `roster` (default, no `--discover`) | 1: `roster-enumeration` |
| `all` without `--discover` | 1: `roster-enumeration` |
| `all` with `--discover` | 5: `roster-enumeration`, `discovery-base-game-factions`, `discovery-marauder-homeland`, `discovery-tier-lists-meta`, `discovery-matchups-threats` |
| `<faction-slug>` without `--discover` | 1: `roster-enumeration` (filter to that faction) |
| `<faction-slug>` with `--discover` | 3: `roster-enumeration` (filtered) + `discovery-faction-<slug>` + `discovery-faction-<slug>-recent` |
| `topic: <topic>` | 2: `roster-enumeration` + `discovery-topic-<topic-slug>` |

**Dispatch all slices in a single assistant message.** That is, in one
turn, emit N parallel `Agent(subagent_type="root-strategy-curator", ...)`
tool calls — one per slice. They run concurrently and return their
results together.

Each worker's prompt is the **discovery-only template** below, with
`<slice-name>` and slice-specific instructions filled in.

When all workers return, parse each response. Each worker returns a JSON
list of candidates. Merge them into a single deduplicated list (by URL),
keeping `discovered_by` set to the slice name. Write the merged list
into `manifest.candidates[]`.

### 3. Dedupe pass

For every candidate in the manifest:

- Run a Bash check against existing curated sources:
  ```
  grep -l "^url: ${candidate_url}\$" docs/strategy/sources/*.md 2>/dev/null
  ```
- If the URL matches an existing file:
  - If `flags.force_refresh = false`: set `status="skipped"`,
    `skip_reason="already_curated_at_<path>"`, `output_path` = that path.
  - If `flags.force_refresh = true`: leave `status="pending"`. The
    extraction worker will overwrite the existing file.
- Otherwise: leave `status="pending"`.

Write `phase_1_completed_at` and the updated candidates list back to the
manifest file with `Edit` (preferred) or `Write`.

### 4. Phase 2 — parallel extraction (waves of 3)

Filter candidates to `status="pending"`. If none, jump to Phase 3.

Process in **waves of 3**:

- Pick the next 3 pending candidates from the manifest.
- **Dispatch all 3 in a single assistant message** — three concurrent
  `Agent(subagent_type="root-strategy-curator", ...)` calls, one per
  candidate. Each worker gets the **extraction-only template** below
  with the candidate's URL, fetch_method, factions hint, etc. filled in.
- When all three return, parse each worker's response. Update each
  candidate's status:
  - `complete` (extraction succeeded, `output_path` set)
  - `failed` (extraction failed, `fail_reason` set)
- Write the updated manifest back to disk.
- Repeat until no `pending` candidates remain.

If the user interrupts mid-pipeline, the manifest on disk is the
resumable state — `--resume <run-id>` picks up where Phase 2 left off.

### 5. Phase 3 — final report

Write `phase_2_completed_at` to the manifest. Emit a final markdown
summary as your response, including:

- Run ID, scope, flags
- Discovery counts (per slice)
- Status counts: complete / skipped / failed / pending (should be 0)
- A flat list of files written this run (one line each, with file size)
- A flat list of failures with reasons
- Pointer to the manifest file path for full detail

Do **not** dump the manifest JSON in the response. The user reads it
from disk if they need it.

## Manifest schema

```json
{
  "run_id": "2026-04-29T17-30-00Z",
  "scope": "all",
  "flags": {
    "discover": true,
    "force_refresh": false,
    "resume": null
  },
  "started_at": "2026-04-29T17:30:00Z",
  "phase_1_completed_at": null,
  "phase_2_completed_at": null,
  "candidates": [
    {
      "url": "https://makecraftgame.com/2022/03/25/keepers-in-iron-guide/",
      "domain": "makecraftgame.com",
      "fetch_method": "blog",
      "factions": ["keepers-iron"],
      "tier": 2,
      "title_hint": "Keepers in Iron Guide",
      "discovered_by": "roster-enumeration",
      "status": "pending",
      "skip_reason": null,
      "fail_reason": null,
      "output_path": null
    }
  ]
}
```

Status values:
- `pending` — discovered, not yet extracted
- `complete` — extracted successfully, `output_path` set
- `failed` — extraction attempted but failed, `fail_reason` set
- `skipped` — duplicate or filtered, `skip_reason` set

## Worker prompt templates

### Discovery-only prompt (one per slice)

Substitute `<slice-name>` and `<slice-specific-instructions>` from the
slice table further below. Send this verbatim as the `prompt` argument
to the Agent tool:

```
You are running in DISCOVERY-ONLY mode. Do NOT fetch any source. Do NOT
write any file under docs/strategy/sources/.

Slice: <slice-name>
Slice instructions: <slice-specific-instructions>

Read docs/strategy/README.md for the source roster.

Return your findings as a single JSON code block matching this shape:

```json
[
  {
    "url": "https://...",
    "domain": "makecraftgame.com",
    "fetch_method": "blog|reddit|bgg",
    "factions": ["eyrie", "marquise"],
    "tier": 2,
    "title_hint": "Short title from source"
  }
]
```

Required fields per candidate: url, domain, fetch_method, factions,
tier, title_hint. Use citation-key faction slugs (eyrie, marquise,
keepers-iron, etc.). Tier 5 candidates must NOT be returned. If a
candidate covers content that's not faction-specific, set
factions: ["general"].

Return only the JSON block. No prose, no preamble. The orchestrator
parses your response programmatically.
```

#### Slice-specific instructions

| Slice | Instructions |
|---|---|
| `roster-enumeration` | Enumerate every URL in `docs/strategy/README.md` Tier 1–4 tables. No WebSearch. If scope is a faction slug, filter to candidates whose roster entry mentions that faction. |
| `discovery-base-game-factions` | WebSearch for strategy content on base-game factions (Marquise, Eyrie, Woodland, Vagabond, Cult, Riverfolk). Skip Tier 5 patterns (`playrootgame.com`, `thegamersguides.com`, `stemgeek.com`, `meeplescorner.co.uk`). Skip URLs already in the roster. |
| `discovery-marauder-homeland` | WebSearch for strategy content on Marauder factions (Lord of the Hundreds, Keepers in Iron) and Homeland factions (Lilypad Diaspora, Twilight Council, Knaves of the Deepwood). Constrain by year ≥2022. |
| `discovery-tier-lists-meta` | WebSearch for tier lists, tournament recaps, win-rate analyses. Tier 4 quantitative content. |
| `discovery-matchups-threats` | WebSearch for matchup analysis, faction counters, threat-pair discussions. |
| `discovery-faction-<slug>` | WebSearch focused on one faction's strategy. Vary phrasing across multiple queries. |
| `discovery-faction-<slug>-recent` | WebSearch for the same faction but year-bounded to the last 12 months. |
| `discovery-topic-<topic-slug>` | WebSearch using the topic phrase as the primary query. |

### Extraction-only prompt (one per pending candidate)

Substitute the candidate fields:

```
You are running in EXTRACTION-ONLY mode. Do NOT discover. Fetch and
distill exactly one URL.

URL: <candidate.url>
Fetch method: <candidate.fetch_method>  # blog | reddit | bgg
Title hint: <candidate.title_hint>
Factions hint (from discovery): <candidate.factions>
Tier: <candidate.tier>

Workflow:
1. Use the matching strategy-fetch-* skill for this method.
2. Distill into the strategy-distill schema. One file per source,
   faction subsections inside, accuracy fields null.
3. Write to docs/strategy/sources/<domain>--<title-slug>.md.
4. If the fetch fails, write a stub file with fetch_status: failed.

Return a single JSON code block:

```json
{
  "status": "complete" | "failed",
  "output_path": "docs/strategy/sources/...",
  "fail_reason": null | "<short reason>"
}
```

Return only the JSON block. No preamble.
```

## Bash recipes

**Generate run_id:**
```
date -u +%Y-%m-%dT%H-%M-%SZ
```

**Create manifest dir:**
```
mkdir -p docs/strategy/_runs
```

**Check if a URL is already curated** (returns matching file path or empty):
```
grep -l "^url: <URL>$" docs/strategy/sources/*.md 2>/dev/null | head -1
```

**Extract domain from URL** (Python one-liner via Bash):
```
python3 -c "import sys; from urllib.parse import urlparse; print(urlparse(sys.argv[1]).netloc.replace('www.',''))" "<URL>"
```

**List currently-curated source URLs:**
```
grep -h "^url:" docs/strategy/sources/*.md 2>/dev/null | awk '{print $2}'
```

## Notes

- **Default scope (`roster`) is the safest run.** It only iterates the
  known roster URLs from `docs/strategy/README.md` — no WebSearch, no
  surprises. Use this for the first end-to-end test or when you want a
  deterministic baseline.
- **`--discover` adds breadth at token cost.** Each WebSearch slice is
  one extra worker. For `scope=all --discover`, expect 5 discovery
  workers and 30+ extraction candidates.
- **For one-off curation of a single URL**, use `/root-strategy-curate
  <url>` instead — single-target, no orchestration overhead.
- **Manifests are gitignored** at `docs/strategy/_runs/`. They are
  resumable via `--resume <run-id>`.

## Examples

| Invocation | Effect |
|---|---|
| `/root-strategy-pipeline` | Roster enumeration only, ~5–15 candidates, sequential extraction |
| `/root-strategy-pipeline all --discover` | Full fan-out: 5 parallel discovery workers, 30+ candidates, parallel extraction in waves of 3 |
| `/root-strategy-pipeline eyrie --discover` | Eyrie-focused: 3 parallel discovery workers, faction-scoped extraction |
| `/root-strategy-pipeline topic: matchups` | Topic-scoped discovery + roster fallback |
| `/root-strategy-pipeline --resume 2026-04-29T17-30-00Z` | Re-enter Phase 2 of an existing run, retry pending/failed candidates |
| `/root-strategy-pipeline all --discover --force-refresh` | Re-curate everything, including sources already in sources/ |

---

User input (parse this for scope and flags): $ARGUMENTS
