---
url: https://makecraftgame.com/2022/04/15/root-faction-scoring-models/
source: Make Craft Game
author: Lily Gould
title: "Root Faction Scoring Models"
date_published: 2022-04-15
date_curated: 2026-04-29
factions:
  - marquise
  - eyrie
  - woodland
  - vagabond
  - riverfolk
  - cult
  - duchy
  - corvid
  - warlord
  - keepers-iron
expansions:
  - base
  - riverfolk
  - underworld
  - marauder
quality_tier: 2
summary: |
  Quantitative analysis of Root faction scoring trajectories across two draft
  formats (AdSet and Plus One Pool Draft) using linear regression modeling on
  tournament data. Covers all ten factions available through the Marauder
  expansion, with slopes and R² values for all-plays and winning-plays models.
accuracy_rating: 8
accuracy_notes: "Empirical analysis based on tournament regression data through the Marauder expansion (April 2022). No rule citations are made — all claims are statistical observations from tournament play, not assertions about rule mechanics. Every faction characterization is consistent with the Law and the project's faction profiles: Eyrie VP loss via turmoil is mechanically correct (`rule:7.7.1`); Alliance consistency, Cult high variance, Duchy format sensitivity, and Warlord early-game correlation are statistical inferences that do not contradict any Law text. The Keepers winning slope (4.22 VP/round, n=3) is directional given the tiny sample but plausible given the Keepers' burst scoring engine. The source explicitly acknowledges small sample sizes for Warlord and Keepers, and the curator's `# Source Notes` correctly flags no Homeland content. No Homeland, Twilight Council, Knaves, Lilypad Diaspora, or Corvid mechanical claims are made. Minor deduction for the inherent fragility of small-n regression findings for the Marauder factions, but the source is transparent about this limitation."
last_reviewed: 2026-04-29
reviewed_by: root-3p-reviewer@2026-04-29
---

# Distilled

## General

### Methodology
Two draft formats compared: AdSet and Plus One Pool Draft. Linear regression applied to round-by-round VP accumulation; R² values quantify how consistently a faction scales with time. Win-game slopes vs. all-plays slopes reveal whether winning requires above-average acceleration or consistent baseline performance.

### Key Finding: Format Matters
AdSet draft generally increased scoring velocity for most factions versus Plus One Pool. AdSet brought greater faction balance. The two formats create meaningfully different competitive environments.

### Winning vs. All Plays
Win-game slopes uniformly exceed all-play slopes — winning games involve faster point accumulation. The gap between all-plays and winning slopes reveals how much a faction must exceed baseline performance to win.

---

## Marquise de Cat

Near-identical scoring models between draft formats (0.1183 VP/round difference). No statistically significant variation between dataset types. Consistent, predictable scoring engine regardless of draft style.

---

## Eyrie Dynasties

Unique among factions for losing VP (turmoil). AdSet format shows marked improvement (0.7 VP/round increase), suggesting the draft style benefits Eyrie flexibility in card access. Format sensitivity is the key variable for Eyrie performance.

---

## Woodland Alliance

Most dramatic shift between formats of any faction. Extremely consistent performance across all-plays and winning scenarios — explains sustained tournament success. Consistency, not peak performance, is the Alliance's defining statistical trait.

---

## Vagabond

Surprisingly minimal variation despite rules changes (infamy mechanic modifications). The researcher hypothesizes meta-game adjustments compensated for mechanical shifts. Scoring model stability despite rule changes suggests the faction's trajectory is more player-skill-driven than mechanic-driven.

---

## Riverfolk Company

Near-identical scoring trajectories across draft formats but winning strategies diverge sharply: Plus One Pool winning path prioritizes rapid ramping from low initial scores; AdSet maintains consistent high scoring throughout. Two distinct winning styles emerge depending on draft format.

---

## Lizard Cult

Produces "chaos" in scoring models — high variance. Only one AdSet winning game in dataset, limiting reliability. Shows decreased average slope in newer formats. Inconsistency is statistically confirmed — not just a player perception.

---

## Underground Duchy

Second-highest slope in AdSet but fifth-ranked in Plus One Pool — strong format-specific advantage in AdSet. Flexible victory conditions with a centered win-round distribution. The format gap is the largest of any faction, making Duchy particularly draft-sensitive.

---

## Corvid Conspiracy

"Random and utterly chaotic" — widest variance in scoring trajectories. Improved competitive viability in AdSet format, achieving more tournament wins. Format-specific performance swing is significant; AdSet suits Corvids better.

---

## Lord of the Hundreds (Warlord)

Parallel scoring between all-plays and winning-plays models — initial-round performance predicts victory likelihood. If the Warlord starts well, they finish well; if not, the trajectory does not recover. Strong early correlation between early rounds and final outcome.

---

## Keepers in Iron

Highest winning-play slope of all factions at 4.22 VP/round. Limited win data (only three games) makes statistical reliability questionable. If the slope holds with more data, Keepers may have the highest ceiling scoring rate of any faction.

# Key Takeaways

- **Woodland Alliance wins through consistency, not peaks**: Most consistent faction in tournament data; this explains sustained high performance across formats.
- **Eyrie is format-sensitive**: AdSet gives Eyrie 0.7 VP/round advantage — draft format selection significantly impacts Eyrie viability.
- **Duchy is draft-sensitive**: Second-highest AdSet slope but fifth in Plus One Pool — biggest format swing of any faction.
- **Lizard Cult is statistically chaotic**: High variance confirmed quantitatively, not just by player perception.
- **Warlord's early game predicts outcome**: Parallel all-plays / winning-plays slope means early round performance is the best predictor of Warlord victory.
- **Keepers have the highest winning slope (4.22 VP/round)** but small sample (n=3) — treat as directional, not conclusive.
- **Corvids benefit from AdSet**: More tournament wins and better slopes in AdSet vs. Plus One Pool.

# Citations from Source

*None.*

# Source Notes

Tier 2 source. Lily Gould / Make Craft Game — highest-quality individual Root blog. Published April 2022, covers all factions through Marauder. Quantitative methodology is transparent and replicable. No Homeland expansion factions. Dataset sizes for newer factions (Keepers, Warlord) are small — treat those findings as directional. Compare with tournament-statistics companion article at [./makecraftgame--root-tournament-overall-statistics.md](./makecraftgame--root-tournament-overall-statistics.md).

---

# Review

**Reviewed:** 2026-04-29 by `root-3p-reviewer`
**Accuracy rating:** 8/10
**Verdict:** Solid empirical source — no rule contradictions anywhere; all faction characterizations align with the Law and project faction profiles, with the expected small-sample fragility for Marauder factions explicitly acknowledged.

## Verified claims

- "Unique among factions for losing VP (turmoil)" — Eyrie turmoil step 1 (Humiliate) confirms VP loss per bird card on the Decree, including Loyal Viziers. ✓ `rule:7.7.1`
- Lizard Cult produces "chaos" / high variance — consistent with the Cult's complexity rating and its dependence on Outcast alignment, acolyte availability, and opponent behavior. Profile and Law both support this characterization as a faction requiring many inputs to align. ✓
- Woodland Alliance "most consistent faction" / "consistency not peak performance" — the Alliance scoring profile (sympathy tokens score incrementally; revolts score on enemy density) produces a stable per-turn floor that does not depend on turmoil risk or opponent service purchases. Consistent with `rule:8.` and the Alliance faction profile's "slow-burn into burst" characterization.
- Duchy "second-highest slope in AdSet but fifth-ranked in Plus One Pool" — a statistical claim with no Law dependency. No conflict.
- Warlord "parallel scoring / early game predicts outcome" — the Warlord's Oppress engine (`rule:14.6.2`) scores 1–4 VP per turn based on clean clearings, and early clearings staked determine whether the trajectory compounds or stalls. Consistent with the Warlord profile's "burst-capable with a steady baseline."
- Keepers "4.22 VP/round winning slope" — the Keepers' burst recovery model (6–10 VP per round in mid-to-late game) makes a high winning-game slope plausible; n=3 caveat acknowledged by source and carried through by curator. No Law contradiction. ✓
- "Vagabond minimal variation despite infamy mechanic modifications" — the infamy mechanic (`rule:9.2.9.3.1`) exists in current p16 Law; this is a historical observation about pre-publication rule changes, not a current-state mechanical claim. Acceptable as contextual observation.

## Stale or outdated

- Source predates Homeland expansion (Lilypad Diaspora, Twilight Council, Knaves of the Deepwood) — no content on those three factions. Frontmatter `expansions[]` and `# Source Notes` correctly scope the coverage. No inaccuracy, just bounded scope.
- Data collected through approximately early 2022; the competitive meta and draft formats may have shifted since publication. Tournament format prevalence (AdSet vs Plus One Pool Draft) should be treated as a period snapshot.

## Strategic judgment notes

- "Eyrie is format-sensitive — AdSet gives 0.7 VP/round advantage" — the Eyrie profile notes that card access is the key variable for managing the Decree without turmoil. Better card availability in AdSet aligning with reduced turmoil risk is strategically defensible. Consistent with [Eyrie profile](../../factions/eyrie.md) observations on hand management and Decree risk.
- "Corvids benefit from AdSet — more tournament wins and better slopes" — the Corvid profile notes their burst-punctuated tempo; AdSet's improved card access plausibly smooths their plotting cadence. Judgment claim; no Law conflict.
- "Keepers may have the highest ceiling scoring rate" — the Keepers profile confirms 6–10 VP per round in burst windows. Directional claim acknowledged as such.

## Citations from Source — verified

*None. The source makes no rule citations; there is nothing to verify.*
