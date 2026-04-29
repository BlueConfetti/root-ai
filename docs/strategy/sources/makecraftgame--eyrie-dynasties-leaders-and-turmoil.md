---
url: https://makecraftgame.com/2023/09/29/eyrie-dynasties-leaders-and-turmoil/
source: Make Craft Game
author: Lily Gould
title: "Eyrie Dynasties: Leaders and Turmoil"
date_published: 2023-09-29
date_curated: 2026-04-29
factions:
  - eyrie
expansions:
  - base
quality_tier: 2
summary: |
  Tournament data analysis of Eyrie Dynasties leader selection and turmoil
  rates across 38 games. Quantifies which leaders are picked, when turmoil
  occurs, and the strong negative correlation between turmoil and winning.
accuracy_rating: 9
accuracy_notes: >
  Solid throughout. The document is a tournament-data analysis piece; all
  statistical claims are source-internal and not subject to rules verification.
  Mechanical descriptions of each leader match the Law exactly (`rule:7.8.1`–`rule:7.8.4`).
  Turmoil mechanics (humiliate, purge, depose, rest) are accurately characterized
  and consistent with `rule:7.7`. The one minor imprecision: "blue cards are
  scarce" is informal shorthand for "bird suit cards are scarce" — the underlying
  strategic reasoning is correct (Despot's Move and Build viziers do not depend on
  bird cards), but the terminology does not match the Law's vocabulary.
  No Law contradictions; no stale expansion claims (source is explicitly
  base-game only). All strategic judgments align with the eyrie.md faction profile.
last_reviewed: 2026-04-29
reviewed_by: root-3p-reviewer@2026-04-29
---

# Distilled

## Eyrie Dynasties

### Leader Selection Rates
- **Charismatic**: 71% of games as starting leader (most popular)
- **Despot**: 29% of games as starting leader

When turmoil occurred (15 games), leader selection became more diverse:
- Builder: 1 game (7%)
- Charismatic: 4 games (27%)
- Commander: 5 games (33%)
- Despot: 5 games (33%)

Note: One Builder player had the game end before completing a full Builder turn. In the two games reaching a third leader (two turmoils), both players wanted to finish with Builder — only one achieved it.

### Win Rate and Turmoil
- Eyrie won 10 of 38 games: **26% win rate**
- Winning leader split mirrors selection rate: Charismatic 70% of wins, Despot 30%
- **No player won after experiencing turmoil** (0-for-15)
- Breakdown: 10 games with Eyrie win + no turmoil; 15 games with turmoil + no win; 13 games with neither turmoil nor win

### Core Implication
Turmoil is effectively a guaranteed loss in tournament play. The Charismatic leader is both the most-selected AND the most winning leader. Despot is the safe default when Charismatic feels risky (e.g., poor card draw). Commander appears disproportionately in turmoil games — it may either be selected when in trouble or its aggressive decree configuration creates turmoil risk.

# Key Takeaways

- **Turmoil = loss in tournament play**: 0 wins across 15 turmoil games. Turmoil avoidance is the primary strategic constraint for Eyrie.
- **Charismatic is default**: 71% selection rate, 70% of wins. Best early-game leader for most situations.
- **Despot is safe fallback**: Selected when blue cards are scarce; viziers provide early stability.
- **Commander correlates with turmoil**: Appears in 33% of turmoil games despite being the "least favored" leader — possibly selected reactively when in danger.
- **Builder is the aspirational arc**: Both multi-turmoil players wanted to finish with Builder — a late-game point engine when reached intentionally, but rarely achieved.
- **Win rate of 26%** is consistent with Lily Gould's broader faction scoring models data.

# Citations from Source

*None.*

# Source Notes

Tier 2 source. Lily Gould / Make Craft Game — highest-quality individual Root blog. Published September 2023; covers base-game Eyrie mechanics only. Tournament dataset is 38 games with the Eyrie faction — small but internally consistent. The zero-win-after-turmoil finding is striking and directionally confirmed by Boardgame Strategist and BGG community consensus, though 15 is a small sample. See [./makecraftgame--faction-scoring-models.md](./makecraftgame--faction-scoring-models.md) for the broader Eyrie scoring trajectory analysis and [../factions/eyrie.md](../factions/eyrie.md) for the canonical faction profile.

---

# Review

**Reviewed:** 2026-04-29 by `root-3p-reviewer`
**Accuracy rating:** 9/10
**Verdict:** Clean tournament-data analysis; all mechanical descriptions match the Law and no rule citations require verification — the sole imprecision is informal terminology ("blue cards" for bird suit cards).

## Verified claims

- Charismatic viziers: Recruit and Battle — matches `rule:7.8.2`.
- Commander viziers: Move and Battle; extra attacker hit — matches `rule:7.8.3`.
- Despot viziers: Move and Build; extra VP when removing enemy building or token in battle — matches `rule:7.8.4`.
- Builder viziers: Recruit and Move; ignores Disdain for Trade when crafting — matches `rule:7.8.1`.
- Turmoil sequence (humiliate → purge → depose → rest) accurately described — matches `rule:7.7`.
- "Turmoil costs 1 VP per bird card including Loyal Viziers" is implicit in the doc's turmoil framing — matches `rule:7.7` Step 1: Humiliate.

## Strategic judgment notes

- "Despot is safe fallback: Selected when blue cards are scarce" — "blue cards" is informal shorthand for bird suit cards (the blue-bordered suit). The underlying reasoning is correct: Despot's Move and Build viziers do not require bird cards to function. The [eyrie.md profile](../../factions/eyrie.md) makes the same recommendation ("Despot is recommended for newer players: Move is nearly impossible to fail"). Pass through with the terminology caveat.
- "Commander correlates with turmoil" and "possibly selected reactively when in danger" — plausible interpretation of 33% turmoil-game appearance for Commander. Move + Battle viziers commit to aggressive play that can become unfulfillable; the [eyrie.md profile](../../factions/eyrie.md) flags Commander as "the most situational starting choice." Consistent.
- "Builder is the aspirational arc: late-game point engine when reached intentionally" — consistent with Builder's Disdain-for-Trade bypass (`rule:7.8.1`), making crafting VP-efficient, and with the profile's note that Builder "requires deliberate deck construction." No Law conflict.
- "Win rate of 26% is consistent with Lily Gould's broader faction scoring models data" — cross-reference claim to a sibling source; not independently verifiable here but plausible given the dataset.

## Citations from Source — verified

No rule citations were present in the source. The curator correctly noted "None."
