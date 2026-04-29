---
url: https://sudo-nano.github.io/posts/Root-Counterplay-Guide/
source: Flash of Stupid (sudo-nano.github.io)
author: TheMagicalC
title: "Root Counterplay Guide"
date_published: 2024-08-12
date_curated: 2026-04-29
factions:
  - duchy
  - woodland
  - corvid
  - warlord
  - cult
expansions:
  - base
  - riverfolk
  - underworld
  - marauder
quality_tier: 2
summary: |
  Living document covering how to counter specific Root factions. Targets
  intermediate players. Published August 2024 with a November 2025 update.
  Covers Underground Duchy, Woodland Alliance, Corvid Conspiracy, Lord of
  the Hundreds, and Lizard Cult (incomplete). Author notes it accepts pull
  request contributions.
accuracy_rating: 7
accuracy_notes: Mechanically sound on most faction descriptions. Core claims about Duchy ramp, Alliance base destruction, Corvid Exposure, Warlord Oppress conditions, and Cult Revenge are all accurate against p16. Two imprecisions worth noting: (1) markets are described as providing "card cycling and procurement," but markets are crafting activators that score via Baron of Dirt — they have no inherent card-cycling function; (2) the Warlord section describes mobs destroying "enemy non-warrior pieces" which is correct but leaves out that Raze removes both buildings and tokens specifically, not a general non-warrior category. The Cult section is flagged as incomplete in the source and the anti-strategy advice ("minimize meeple casualties") is imprecise — any battle vs. Cult as defender feeds their acolyte pool, and there is no clean way to selectively reduce Cult warrior kills during combat. The Nov 2025 Outrage correction is current and matches p16. No rule citations present to verify. No outright Law contradictions.
last_reviewed: 2026-04-29
reviewed_by: root-3p-reviewer@2026-04-29
fetch_status: partial
---

# Distilled

## Underground Duchy

### What They Do
Deploy massive warrior numbers with slow initial recruitment that rapidly escalates. Strengthen through swaying nobles, building citadels (rapid recruitment), and markets (card cycling and procurement).

### How to Counter
Attack aggressively within the first three rounds before ramping completes. Early mole players often fortify defensible clearings — disruption is harder once fortified. Window is narrow; passive play against Duchy concedes the mid-game.

---

## Woodland Alliance

### What They Do
Maintain minimal board presence while accumulating followers and sympathy tokens. Destroying sympathy requires sacrificing matching suit cards or losing cards to their supporters. Revolts convert sympathy into bases, warriors, and action-economy increases. VP scales with sympathy token quantity.

### How to Counter
Target bases — destroying them forces discarding matching supporters and removes half the officers. Corvid Snare plots create effective base blockades: Alliance cannot deploy through snares or revolt in blocked suits.

*2025-11-29 correction*: When sympathy tokens are destroyed, if a player lacks matching suit cards, the Alliance player views their hand and draws from the deck (not takes from hand).

---

## Corvid Conspiracy

### What They Do
Deploy face-down plots with four functions: Bombs (remove enemy pieces), Snares (prevent placement/movement), Extortion (steal random cards + draw bonus), and Raids (spawn warriors in adjacent clearings). Face-down tokens provide combat advantages; face-up tokens require crow presence to flip.

### How to Counter
Expose plots by revealing matching suit cards and guessing plot type. Strategically guess Raids (removing them safely) or the worst-case scenario. Balance exposure cost against combat risk.

---

## Lord of the Hundreds (Warlord)

### What They Do
Control clearings exclusively and score only from unoccupied controlled territory. Mob tokens destroy enemy non-warrior pieces during turns, enforcing control through intimidation.

### How to Counter

**Preventing VP**: Station minimal warriors in their clearings to deny scoring — effective for heavy factions that can absorb losses.

**Preventing Recruiting**: Kill the Warlord piece before recruitment actions; this blocks recruiting for one turn since recruitment precedes Warlord replacement.

**Preventing Mobs**: Coordinate multi-faction perimeters around Hundreds territory. Corvid Snare plots prevent mob placement in affected clearings.

**Design Note (author's opinion)**: Lords require opponent cooperation to balance. They easily win 1v1 but fall quickly to coordinated heavy faction opposition, particularly against flexible warrior-deployers.

---

## Lizard Cult

### What They Do
Unconventional engine and action economy mechanics. (Section incomplete in source.)

### How to Counter
Destroy gardens by minimizing meeple casualties in battles — combat defeats feed their acolyte pool and thus their action economy.

# Key Takeaways

- **Underground Duchy must be attacked in rounds 1–3**: The ramp is real; passive early play concedes the mid-game to Duchy.
- **Woodland Alliance bases are the primary target**: Destroying bases removes half the officers and forces supporter discards — more impactful than sympathy token removal alone.
- **Corvid plots: guess Raids or worst-case**: Strategic guessing minimizes exposure cost while neutralizing the most dangerous plots.
- **Kill the Warlord before his recruitment action**: One-turn recruiting block is achievable with precise timing.
- **Corvid Snares counter both Woodland Alliance and Lord of the Hundreds**: Most versatile anti-faction tool in the game for controlling territory access.
- **Lizard Cult anti-strategy**: Minimize warrior deaths in battle — every killed lizard warrior is an acolyte, which is an action.

# Citations from Source

*None.*

# Source Notes

Tier 2 source. Living document with last update November 2025 — more current than most sources. Covers Underground Duchy, Woodland Alliance, Corvid, Lord of the Hundreds, and Lizard Cult (partial). Marquise, Eyrie, Vagabond, Riverfolk, Keepers in Iron, and all Homeland factions are absent — document is explicitly incomplete. Author notes it accepts external contributions. The Woodland Alliance sympathy correction (Nov 2025) aligns with p16 rules. See [../factions/](../factions/) for full faction profiles covering all 13 factions.

---

# Review

**Reviewed:** 2026-04-29 by `root-3p-reviewer`
**Accuracy rating:** 7/10
**Verdict:** Mechanically accurate on the essentials with two imprecisions and one incomplete section; no Law contradictions.

## Verified claims

- "Revolts convert sympathy into bases, warriors, and action-economy increases" ✓ matches `faction:woodland$8.4.1.3`.
- "Destroying [bases] forces discarding matching supporters and removes half the officers" ✓ matches `faction:woodland$8.2.4`.
- "if a player lacks matching suit cards, the Alliance player views their hand and draws from the deck" ✓ matches `faction:woodland$8.2.6`.
- Corvid "face-down tokens provide combat advantages" (Embedded Agents extra hit) ✓ matches `faction:corvid$13.2.5`.
- "if this removes a Raid token, it does not place warriors" ✓ matches `faction:corvid$13.2.4`.
- "Kill the Warlord piece before recruitment actions; this blocks recruiting for one turn since recruitment precedes Warlord replacement" ✓ matches Birdsong sequence: Recruit is step 2, Anoint is step 3 (`faction:warlord$14.4.2`, `faction:warlord$14.4.3`).
- "Corvid Snare plots prevent mob placement in affected clearings" ✓ snare prevents enemy pieces from being placed in its clearing (`faction:corvid$13.7.2`); mob tokens are Hundreds pieces, and the Hundreds are enemies of the Corvids.
- "combat defeats feed their acolyte pool" (Cult / Revenge) ✓ matches `faction:cult$10.2.3`.

## Conflicts with the Law

None found.

## Stale or outdated

No stale content identified. The Nov 2025 Woodland Alliance correction is current and matches p16's Outrage rule (`faction:woodland$8.2.6`).

## Strategic judgment notes

- "markets (card cycling and procurement)" — markets are crafting activators that score via Baron of Dirt (`faction:duchy$12.5.2`). They have no inherent card-cycling function. This is an imprecise characterization; the [Duchy profile](../../factions/duchy.md) describes markets and citadels as "identical for crafting purposes." Acceptable as loose flavor but inaccurate as a mechanical description.

- "Mob tokens destroy enemy non-warrior pieces during turns" — Raze (`faction:warlord$14.4.1`) removes "all enemy buildings and tokens." Framing mobs as targeting "non-warrior pieces" is technically correct (buildings and tokens are not warriors) but imprecise; it could mislead readers into thinking the mechanism is defined by what it excludes rather than what it targets.

- "minimize meeple casualties in battles" (Cult anti-strategy) — imprecise advice. Revenge fires whenever Cult warriors are removed while defending (`faction:cult$10.2.3`), which happens in any battle the Cult defends. There is no clean way to fight Cult without triggering Revenge; the only practical avoidance is to use non-battle removal effects (Favor cards, etc.) which bypass Revenge entirely. The advice as stated implies the attacker can modulate Cult warrior kills during battle, which they cannot. The Cult section is noted as incomplete in the source.

- "Corvid Snares counter both Woodland Alliance and Lord of the Hundreds: Most versatile anti-faction tool in the game for controlling territory access" — defensible judgment. Not independently verifiable as universal; the [Corvid profile](../../factions/corvid.md) confirms snares lock clearings (`faction:corvid$13.7.2`) and the Duchy profile cross-references snares blocking Burrow movement (`docs/factions/duchy.md`). Pass through as strategy claim.

## Citations from Source — verified

*None present in source.*
