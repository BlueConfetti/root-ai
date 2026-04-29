---
description: Review curated third-party Root strategy files against the Law of Root and faction profiles. Fills accuracy frontmatter fields and appends/replaces a # Review section. Runs in main session so it can dispatch root-3p-reviewer workers in parallel waves of 3.
model: sonnet
allowed-tools:
  - Agent
  - Read
  - Write
  - Edit
  - Bash
  - Grep
  - Glob
argument-hint: [scope] [--last <n>] [--only-new]
---

# /root-3p-review

You orchestrate the third-party content review pipeline. You run in the
main session (slash commands are not subagents), which is the **only
place where the Agent tool can actually dispatch new subagents** —
nested subagent dispatch is forbidden by Claude Code's design.

You enumerate candidates from `docs/strategy/sources/`, apply filters,
and dispatch parallel `root-3p-reviewer` workers in waves of 3. Each
worker reviews one file end-to-end (frontmatter accuracy fields + a
`# Review` section at the bottom). You collect results into a manifest
and emit a final summary.

## Critical constraints

- **Multiple Agent calls in a single assistant message run concurrently.**
  This is the parallelization mechanism. Dispatch waves of 3 in single
  messages.
- **Your dispatch allowlist is fixed**: `subagent_type: root-3p-reviewer`
  only.
- **Wave size is 3.** Each worker loads the Law, faction profiles, and
  the candidate doc — keep parallelism modest to bound peak token use.
- **You own the manifest.** Workers return JSON in their result text;
  you parse and write the manifest. Workers never touch the manifest.
- **Manifest path: `docs/strategy/_runs/review-<run-id>.json`.** Same
  gitignored `_runs/` directory as the curation pipeline, with a
  `review-` prefix to distinguish run kind.
- **Workers handle file edits themselves.** They update frontmatter
  and append/replace the `# Review` section. You do not edit curated
  files directly.

## Argument parsing

Parse `$ARGUMENTS` into a structured request:

| Argument | Effect |
|---|---|
| (no args) | `scope=all`, no filters — review every doc, replace existing reviews if any |
| `all` | Same as no-args |
| `<faction-slug>` (e.g. `eyrie`, `marquise`, `keepers-iron`) | Filter to docs whose frontmatter `factions[]` contains this slug |
| `<file-path>` (path containing `/` or ending in `.md`) | Review only that one file |
| `--last <n>` | Filter to docs whose `date_curated` is within the last N days |
| `--only-new` | Filter to docs whose `last_reviewed` is `null` (i.e., never reviewed) |

Filters compose. Example: `eyrie --only-new` reviews unreviewed Eyrie
docs only. Example: `--last 7 --only-new` reviews unreviewed docs
curated in the last week.

If `$ARGUMENTS` is unparseable, ask the user once for clarification,
then proceed.

## Workflow

### 1. Initialize

- Generate a run_id with the `review-` prefix:
  ```
  Bash: echo "review-$(date -u +%Y-%m-%dT%H-%M-%SZ)"
  ```
- Create the runs dir if missing:
  ```
  Bash: mkdir -p docs/strategy/_runs
  ```
- Write the initial manifest skeleton (see schema below) to
  `docs/strategy/_runs/<run-id>.json` using `Write`. Tell the user
  the run_id.

### 2. Enumerate candidates

- List all curated source files:
  ```
  Bash: ls docs/strategy/sources/*.md
  ```
- For each file, read the frontmatter (just the top YAML block):
  ```
  Bash: awk '/^---$/{c++; next} c==1{print}' <file> | head -30
  ```
  Or use `Read` with a small line range. You need: `factions`, `date_curated`, `last_reviewed`.
- Apply filters:
  - **Scope**: if scope is a faction slug, keep files where
    `factions[]` contains that slug. If scope is a file path, keep only
    that file. Otherwise (`all`), keep all.
  - **`--last N`**: keep files where `date_curated >= today - N days`.
    Use Bash to compute the cutoff date:
    ```
    Bash: date -u -v -7d +%Y-%m-%d   # macOS
    Bash: date -u -d "7 days ago" +%Y-%m-%d   # Linux
    ```
    Detect platform if needed.
  - **`--only-new`**: keep files where `last_reviewed: null` (look for
    the literal string `last_reviewed: null` or `last_reviewed:` with
    nothing after it).

  Mark files that pass all filters as `status="pending"` in the
  manifest. Mark files that match scope but fail filters as
  `status="skipped"` with `skip_reason` populated.

  Files outside scope are not added to the manifest at all.

- Write the populated candidate list to the manifest.

### 3. Dispatch reviewers (waves of 3)

Filter to `status="pending"`. If none, jump to step 5.

Process in **waves of 3**:

- Pick the next 3 pending candidates.
- **Dispatch all 3 in a single assistant message** — three concurrent
  `Agent(subagent_type="root-3p-reviewer", ...)` calls, one per
  candidate. Each worker gets the **reviewer prompt** below with the
  candidate's `file_path` filled in.
- When all three return, parse each worker's response. Each returns a
  JSON code block with `status`, `accuracy_rating`, `verdict`, etc.
- Update each candidate's manifest entry:
  - `status`: `complete` or `failed`
  - `accuracy_rating`: from worker output
  - `verdict`: from worker output
  - `previously_reviewed`: from worker output
  - `fail_reason`: if failed
- Write the updated manifest back to disk.
- Repeat until no `pending` candidates remain.

### 4. Reviewer prompt template

Substitute `<file_path>`:

```
Review the curated third-party Root strategy file at: <file_path>

Read the file. Read the p16 Law of Root (rules.yml + faq.yml). Read the
faction profile(s) at docs/factions/<slug>.md for each faction in the
file's frontmatter. Read any cards the file references.

Cross-check every substantive claim in the # Distilled and
# Key Takeaways sections against the Law. Verify every rule citation
in the # Citations from Source section.

Update the file:
1. Frontmatter: set accuracy_rating (0-10), accuracy_notes (one
   paragraph), last_reviewed (today UTC), reviewed_by
   ("root-3p-reviewer@<today>").
2. Append (or replace if existing) a # Review section at the bottom of
   the file, after a "---" separator. Use the template in your agent
   instructions.

Do NOT modify the # Distilled, # Key Takeaways, # Citations from
Source, or # Source Notes sections — those belong to the curator.

Return one JSON code block:

{
  "status": "complete" | "failed",
  "file_path": "<repo-relative-path>",
  "accuracy_rating": <0-10 integer or null>,
  "verdict": "<one-sentence verdict>" or null,
  "previously_reviewed": <bool> or null,
  "fail_reason": null or "<short reason>"
}

No preamble. Only the JSON.
```

### 5. Final report

- Write `completed_at` to the manifest.
- Emit a final markdown summary as your response, including:
  - Run ID, scope, flags
  - Candidate counts: total in scope / pending / skipped (with reasons) /
    complete / failed
  - A table of completed reviews: `file | rating | verdict (truncated)`
  - A list of failures with `fail_reason`
  - Pointer to the manifest file path

Do **not** dump the manifest JSON in the response. The user reads it
from disk if they want full detail.

## Manifest schema

```json
{
  "run_id": "review-2026-04-29T18-00-00Z",
  "kind": "review",
  "scope": "all",
  "flags": {
    "last_days": null,
    "only_new": false
  },
  "started_at": "2026-04-29T18:00:00Z",
  "completed_at": null,
  "candidates": [
    {
      "file_path": "docs/strategy/sources/makecraftgame--keepers-in-iron-guide.md",
      "factions": ["keepers-iron"],
      "date_curated": "2026-04-29",
      "previously_reviewed": false,
      "status": "pending",
      "accuracy_rating": null,
      "verdict": null,
      "skip_reason": null,
      "fail_reason": null
    }
  ]
}
```

Status values:
- `pending` — in scope, not yet reviewed in this run
- `complete` — reviewed successfully, file updated
- `failed` — review attempted but worker returned an error
- `skipped` — in scope but filter excluded it (e.g., already reviewed when `--only-new` set; outside `--last N` window)

## Bash recipes

**Generate run_id:**
```
echo "review-$(date -u +%Y-%m-%dT%H-%M-%SZ)"
```

**List source files:**
```
ls docs/strategy/sources/*.md
```

**Read a file's frontmatter only:**
```
awk '/^---$/{c++; next} c==1{print} c==2{exit}' <file>
```

**Compute "N days ago" date (cross-platform):**
```
python3 -c "from datetime import datetime, timedelta, timezone; print((datetime.now(timezone.utc) - timedelta(days=$N)).strftime('%Y-%m-%d'))"
```

**Check if a file has been reviewed** (exit 0 if reviewed, non-zero if not):
```
awk '/^---$/{c++; next} c==1 && /^last_reviewed:/ && !/null/{found=1; exit} END{exit !found}' <file>
```

## Notes

- **Default scope (`all`) refreshes everything.** If you only want to
  fill in unreviewed docs, pass `--only-new`. If you want to spot-check
  recently-curated content only, pass `--last 7`.
- **Reviews are idempotent.** Re-running on a doc replaces its existing
  `# Review` section and frontmatter accuracy fields. There's no harm
  in re-reviewing.
- **The reviewer never edits curator-owned content.** It only owns the
  4 accuracy frontmatter fields and the `# Review` section after the
  trailing `---` separator.
- **For one-off review of a single file**, you can pass the file path
  as scope: `/root-3p-review docs/strategy/sources/<file>.md`.

## Examples

| Invocation | Effect |
|---|---|
| `/root-3p-review` | Review every curated source, refreshing existing reviews |
| `/root-3p-review --only-new` | Review only docs that have never been reviewed |
| `/root-3p-review eyrie` | Review every doc that mentions Eyrie |
| `/root-3p-review eyrie --only-new` | Review unreviewed Eyrie docs only |
| `/root-3p-review --last 7` | Review docs curated in the last 7 days |
| `/root-3p-review docs/strategy/sources/spritesanddice--strategy-of-root.md` | Review a single file |

---

User input (parse for scope and flags): $ARGUMENTS
