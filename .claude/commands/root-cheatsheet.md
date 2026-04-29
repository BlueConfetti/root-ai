---
description: Audit and extend the Root help/hurt cheatsheet for one or more factions. Runs in the main session so it can dispatch root-strategist, root-referee, and root-pragmatist workers in parallel waves of 3 factions. Pipeline per category is generate -> rules-verify -> pragmatic-vet -> synthesize, with sequential dependencies inside a category and full parallelism across categories and factions.
model: opus
allowed-tools:
  - Agent
  - Read
  - Write
  - Edit
  - Bash
  - Grep
  - Glob
argument-hint: [<faction-slug>...] [--audit-only] [--additions-only] [--dry-run]
---

# /root-cheatsheet

You orchestrate revision of `docs/root-faction-help-hurt-cheatsheet.md`.
You run in the main session (slash commands are not subagents), which is
the **only place where the Agent tool can actually dispatch new
subagents** — nested subagent dispatch is forbidden by Claude Code's
design.

For each in-scope faction, you run a four-phase pipeline that audits
existing entries and proposes net-new candidates across three
categories (Helping, Hurting, Awareness). Sequential dependencies live
inside a single claim's lifecycle (`generate -> rules-verify ->
pragmatic-vet -> author`); everything else parallelizes — across
categories, across claims, and across factions in waves of 3.

## Critical constraints

- **Multiple Agent calls in a single assistant message run concurrently.**
  This is the parallelization mechanism. Dispatch each phase's full
  fan-out in one message.
- **Your dispatch allowlist is fixed**: `root-strategist`,
  `root-referee`, `root-pragmatist`. No other agents.
- **Wave size is 3 factions**, matching `/root-3p-review`. Each wave
  fires up to 9 strategists in phase 1, up to 9 referees in phase 2,
  and up to 6 pragmatists in phase 3 (Awareness skips the pragmatist
  gate).
- **No category caps.** Strategists propose freely. The referee and
  pragmatist gates do the filtering; whatever survives lands in the
  cheatsheet.
- **Audience is intermediate.** Awareness items survive even if
  veterans already know them, as long as they're non-obvious from
  the player board / plain rule text and change a tactical decision.
- **Backup before any write.** Copy the cheatsheet to
  `docs/_runs/cheatsheet.<run-id>.bak.md` before any wave writes.

## Argument parsing

Parse `$ARGUMENTS`:

| Argument | Effect |
|---|---|
| (no args) or `all` | All 13 factions in waves of 3 |
| One or more `<faction-slug>` tokens | Process only those factions (one wave if <=3, else multiple) |
| `--audit-only` | Verdict on existing entries; do not propose new candidates |
| `--additions-only` | Skip audit; only propose net-new candidates that don't duplicate existing |
| `--dry-run` | Print proposed sections + verdict tables; do not modify the file |

If `$ARGUMENTS` is unparseable or contains an unknown slug, ask the
user once for clarification and proceed.

## Faction slug whitelist

Use these slugs only (no aliases). Mapping to display name and
citation prefix:

| Slug | Display name | Citation prefix |
|---|---|---|
| `marquise` | Marquise de Cat | `rule:6.X` |
| `eyrie` | Eyrie Dynasties | `faction:eyrie$7.X` |
| `woodland` | Woodland Alliance | `faction:woodland$8.X` |
| `vagabond` | Vagabond | `faction:vagabond$9.X` |
| `cult` | Lizard Cult | `faction:cult$10.X` |
| `riverfolk` | Riverfolk Company | `faction:riverfolk$11.X` |
| `duchy` | Underground Duchy | `faction:duchy$12.X` |
| `corvid` | Corvid Conspiracy | `faction:corvid$13.X` |
| `warlord` | Lord of the Hundreds | `faction:warlord$14.X` |
| `keepers-iron` | Keepers in Iron | `rule:15.X` |
| `diaspora` | Lilypad Diaspora | `faction:diaspora$16.X` |
| `council` | Twilight Council | `faction:council$17.X` |
| `knaves` | Knaves of the Deepwood | `faction:knaves$18.X` |

## Workflow

### 1. Initialize

- Generate a run_id:
  ```
  Bash: echo "cheatsheet-$(date -u +%Y-%m-%dT%H-%M-%SZ)"
  ```
- Ensure runs dir exists:
  ```
  Bash: mkdir -p docs/_runs
  ```
- Resolve in-scope factions from `$ARGUMENTS`. Build wave list (chunks
  of 3, in slug order).
- **Back up the cheatsheet** before any wave writes:
  ```
  Bash: cp docs/root-faction-help-hurt-cheatsheet.md docs/_runs/cheatsheet.<run-id>.bak.md
  ```
  Skip the backup only when `--dry-run` is set.
- Read the cheatsheet once into memory. For each in-scope faction,
  extract its section (between `### <Display name>` and the next `---`
  divider) so you can pass existing entries to the strategist.

### 2. For each wave, run phases 1-4

A wave is up to 3 factions. Process waves sequentially; phases inside
a wave are sequential, but dispatches inside a phase are parallel.

#### Phase 1 — Generate (parallel ×3 categories ×N factions in wave)

Dispatch one `root-strategist` per (faction, category) — up to 9 in a
single assistant message for a 3-faction wave.

Pass each strategist the existing entries for its category (verbatim,
with citations) and ask for both an audit pass and net-new candidates.
Use the prompt template in [Phase 1 prompt](#phase-1-prompt-strategist).

If `--audit-only`, the strategist only audits and skips additions.
If `--additions-only`, the strategist only proposes new candidates and
treats existing entries as "do not duplicate."

Each strategist returns a structured list of items. Parse all results
into a working set of claims.

#### Phase 2 — Rules verify (parallel ×3 categories ×N factions)

Dispatch one `root-referee` per (faction, category). Pass the working
set of claims from phase 1 (both audited-and-revised and net-new).
Each referee returns per-claim verdicts: `RULES_OK`, `RULES_WRONG`,
`RULES_AMBIGUOUS`, with verified citations and (for non-OK)
corrections.

Drop `RULES_WRONG` claims silently. Treat `RULES_AMBIGUOUS` as `FLAG`
and surface them in the final summary for the user to rule on.

Use the [Phase 2 prompt](#phase-2-prompt-referee).

#### Phase 3 — Pragmatic gate (parallel ×2 categories ×N factions)

For Helping and Hurting only (Awareness skips). Dispatch one
`root-pragmatist` per (faction, category-in-{helping,hurting}).
Pragmatist returns per-claim verdicts: `KEEP`, `MOVE_TO_AWARENESS`,
`DROP`, `FLAG`.

When a claim is `MOVE_TO_AWARENESS`, route it into the Awareness
section without re-verifying with the referee — trust the original
referee verdict.

Use the [Phase 3 prompt](#phase-3-prompt-pragmatist).

#### Phase 4 — Synthesize and write (sequential, in main session)

For each faction in the wave:

1. Assemble surviving claims:
   - Helping section: `KEEP` claims from pragmatist
   - Hurting section: `KEEP` claims from pragmatist
   - Awareness section: all `RULES_OK` Awareness claims + any
     `MOVE_TO_AWARENESS` migrations from H/H
2. Format each claim as a bulleted entry with a **Why:** line and
   citations, matching the existing cheatsheet style:
   ```
   - <one-line claim>
     - **Why**: <rationale>. (`rule:X.Y.Z`)
   ```
3. Write the assembled section back into the cheatsheet, replacing
   the old `### <Display name>` block (between that header and the
   next `---` divider — keep the divider). Use `Edit` with
   sufficient surrounding context to make the replacement unique.
4. If `--dry-run` is set, do not write — print the proposed section
   to the conversation instead.

### 3. Surface the run summary

After all waves complete, print:

- A **verdict table per faction** showing the disposition of every
  claim (existing entries: `KEEP_AS_IS` / `REVISED` / `DROPPED`; new
  candidates: `KEPT` / `MOVED_TO_AWARENESS` / `DROPPED` / `FLAGGED`)
  with the gate that produced the verdict and a one-line reason.
- The **backup path** (`docs/_runs/cheatsheet.<run-id>.bak.md`) so the
  user can revert if needed.
- A **flagged-claims list** for any `RULES_AMBIGUOUS` or pragmatist
  `FLAG` items that need user adjudication.

If `--dry-run`, additionally print the full proposed section text
per faction.

---

## Phase 1 prompt (strategist)

Send each `root-strategist` a focused prompt of this shape:

```
You are auditing and extending the {DISPLAY_NAME} {CATEGORY} entries
in the Root help/hurt cheatsheet (audience: intermediate players).

Existing {CATEGORY} entries for {DISPLAY_NAME}:

{VERBATIM_EXISTING_ENTRIES_OR_"(none)"}

CATEGORY DEFINITIONS
- Helping: passive table behaviors that feed this faction's engine
  (the inverse — not doing the behavior — should provably hurt them)
- Hurting: actionable counterplay opponents can take to slow them
  (must pass actionability + counterfactual)
- Awareness: non-obvious neutral facts that change tactical decisions
  (no action required; survives if a veteran knows it, as long as it's
  non-obvious to an intermediate player from the player board / rule
  text and changes a real decision)

YOUR TASK
{If --audit-only}: Audit each existing entry. Do not propose new
  candidates.
{If --additions-only}: Propose net-new candidate entries. Do not
  audit existing; treat them only as "do not duplicate."
{Otherwise}: Both — audit each existing entry, then propose net-new
  candidates that don't duplicate existing claims.

For AUDIT items, return one of:
  - KEEP_AS_IS: entry is accurate and well-stated
  - REVISE: entry has issues; provide the proposed revision text
  - DROP: entry should be removed; provide reason

For ADDITION items, propose as many candidate entries as you can
defend. No cap. Sharp, intermediate-level insights only — do not pad.

OUTPUT FORMAT
Return a numbered list. For each item:

  [N] type=<AUDIT|ADDITION>
      audit_verdict=<KEEP_AS_IS|REVISE|DROP>   (AUDIT only)
      claim: <one-line claim text>
      rationale: <why it works / why it's true>
      proposed_citations: [<rule:X.Y.Z>, <faction:NAME$X.Y.Z>, ...]
      audit_note: <reason if REVISE/DROP>      (AUDIT only)

CITATION CONVENTIONS
{Paste relevant citation conventions from project CLAUDE.md, including
the faction citation prefix for {DISPLAY_NAME}.}
```

## Phase 2 prompt (referee)

```
Verify the rules-correctness of these {DISPLAY_NAME} {CATEGORY}
cheatsheet claims against the Law of Root (printing 16 by default).

CLAIMS TO VERIFY:

{NUMBERED_LIST_OF_CLAIMS_WITH_PROPOSED_CITATIONS}

For each claim, return:

  [N] verdict=<RULES_OK|RULES_WRONG|RULES_AMBIGUOUS>
      verified_citations: [...]   (final correct citations)
      correction: <only if WRONG/AMBIGUOUS — what's actually true>

Use rule:X.Y.Z for general rules and faction:NAME$X.Y.Z for
faction-specific rules. If a claim conflates two separate rules,
mark RULES_AMBIGUOUS and explain.
```

## Phase 3 prompt (pragmatist)

```
Apply the actionability + counterfactual gate to these
{DISPLAY_NAME} {CATEGORY} claims (already rules-verified).

CLAIMS:

{NUMBERED_LIST_OF_RULES_OK_CLAIMS}

GATE
- Actionability: is there a concrete move an opponent can make
  (proactive or responsive) that addresses this lever? "Be aware
  of X" / "remember Y" are observations, not moves — those are
  MOVE_TO_AWARENESS.
- Counterfactual: if this lever does NOT fire, what does
  {DISPLAY_NAME} do instead? If the alternative is better for the
  faction than this lever is, the claim is inverted — DROP.

For each claim, return:

  [N] verdict=<KEEP|MOVE_TO_AWARENESS|DROP|FLAG>
      reasoning: <one-line>
```

---

## Style notes for synthesized entries

- Match the existing cheatsheet voice: terse, declarative, one
  bulleted claim per entry with a nested `**Why**:` line.
- Citations live inside backticks at the end of the rationale.
- Two adjacent backtick groups with no space = two separate
  citations (this pattern appears in the Law itself).
- Use `card:ROOT-N (Deck Name)` for any card cite in the collision
  set (Ambush!, Dominance, Crossbow, Anvil, Arms Trader, A Visit
  To Friends, Bake Sale, Birdy Bindle).

---

User arguments: $ARGUMENTS

If `$ARGUMENTS` is empty, treat as `all` (process every faction in
waves of 3).
