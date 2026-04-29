---
url: https://makecraftgame.com/2022/03/25/keepers-in-iron-guide/
source: Make Craft Game
author: Luke Bridwell
title: Keepers in Iron Guide
date_published: 2022-03-25
date_curated: 2026-04-29
factions:
  - keepers-iron
expansions:
  - marauder
quality_tier: 2
summary: Comprehensive faction guide for the Keepers in Iron (Badgers) by Luke
  Bridwell, covering all three phases, the retinue/waystation/relic engine in
  detail, map-specific advice, and setup/draft considerations.
accuracy_rating: 5
accuracy_notes: The source offers solid structural coverage of the Keepers in Iron — the core retinue/waystation/relic engine, the hit-and-run loop, discard-check risk, and map-specific notes are all directionally sound. However it contains several factual errors that meaningfully undercut trust in the numbers. Most critically, the source repeatedly says "both waystations" (implying two) when the Keepers have three waystations per `rule:15.2.2`. Related to this, the column-bonus arithmetic is wrong (source claims 8 VP; actual is 3 columns × 2 VP = 6), and the "minimum of 24 points from three full columns" is wrong (all 12 relics recover exactly 27 VP since values are fixed at 1+2+3+3 per type, plus 6 column bonuses = 33). Additionally, the Gather Retinue section implies a player can both add cards and shift a card in the same Evening, contradicting the Law's either/or language (`rule:15.6.2`). The Live Off the Land pitfall bullet misattributes the mechanic: leaving stragglers prevents loss of Encamp access, not Live Off the Land triggers (which only fires on 4+ warrior stacks). The strategic framework and phased advice are otherwise reasonable; errors cluster around the math and two specific rule descriptions.
last_reviewed: 2026-04-29
reviewed_by: root-3p-reviewer@2026-04-29
---

# Distilled

## Keepers in Iron

### Win Condition / Scoring Path

The Keepers win through relics (up to 27 points) plus relic column bonuses (8 points). Three full retinue columns yield a minimum of 24 points. Supplementary income comes from craftable items and destroying enemy pieces. The faction board's three-column Retinue (move / battle-then-delve / move-or-recover) is the action engine; cards placed there enable actions without discarding unless specific discard triggers fire (delving without ruling sufficient surrounding clearings, or recovering without ruling adequate matching-suit clearings).

Waystations are the building layer: each grants one extra card draw per evening (up to four total), and each holds two relic types. Placing both waystations on turn one is essentially mandatory.

### Opening Priorities

- Deploy both waystations on turn one.
- Prioritize bird cards in hand selection; one bird minimum for consistency.
- Fill retinue to 10 cards before investing in recruiting or crafting.
- Avoid three red-suit factions in the pool; Badgers strengthen with fewer opposing reds.
- Prefer earlier turn order within the round.

### Mid-game Pivots

**Hit and Run** is the core tactical loop: move from map edges into delve clearings, battle and delve for relics (one relic per clearing maximum on the board at any time), then move back to recovery clearings. Never keep more than one relic per clearing. Leave straggler warriors behind when moving to prevent "Live off the Land" triggers and enable future Encamp actions.

Card allocation shifts during daylight:
- Move action: use birds or suited cards matching recovery clearings (never loses retinue cards).
- Battle then Delve: discard suited cards first; aim for 2+ relics per turn.
- Move or Recover: rule 2–3 matching-suit clearings to recover without discarding; repeat if conditions allow.

Crafting priority order: card draw items first, points second, movement improvement third.

### Common Pitfalls

- Discarding retinue cards in rounds 1–3 collapses the action engine.
- Keeping more than one relic per clearing exposes them to Prized Trophies (opponents score when relics are destroyed, and opponents choose where the relic lands).
- Moving all warriors out of a clearing without leaving stragglers triggers Live off the Land losses and forecloses future Encamp.
- Over-investing in recruiting at low reach (low-reach games should prioritize retinue; high-reach games can recruit frequently for board presence).

### Threat Matchups

- Avoid drafting into a pool with three red-suit factions — they apply constant pressure on the retinue's suited-card supply.
- Devout Knights ability (ignore first hit in battle when holding at least one relic and one keeper warrior) provides meaningful combat resilience, but Prized Trophies create a persistent targeting incentive for all opponents.

### Card / Item Priorities

Retinue receives cards first (highest priority). Birds are maximally flexible. Recruiting uses suited cards matching waystation suits. Crafting is lowest priority. Preferred crafts in order: card draw items, point-generating items, movement items.

### Endgame Routes

Calculate needed victory points; three full retinue columns produce at minimum 24 points. Supplement with craftable items. The faction's "play from behind" design allows comeback potential via massive late scoring. Evening's Gather Retinue phase lets the player shift cards between columns and add battle cards mid-game as the engine matures.

### Map-Specific Notes

- **Autumn / Summer:** Excellent. Many connected clearings enable consistent three-clearing ruling.
- **Winter:** Challenging. Central clearings are heavily contested; start in the bottom-middle region.
- **Lake:** Difficult. Ferry dependency creates chokepoints; focus north/east regions.
- **Mountain:** Excellent. Central clearings become accessible after the opening; avoid the bottom clearing with paths.

# Key Takeaways

- **Keepers in Iron:** Deploy both waystations on turn one — every other decision flows from the card draw they generate.
- **Keepers in Iron:** Fill the retinue to 10 cards before recruiting or crafting; discarding retinue cards in rounds 1–3 is the primary failure mode.
- **Keepers in Iron:** Hit and Run is the dominant tactical loop — delve at the front, recover at the rear, never hold more than one relic per clearing.
- **Keepers in Iron:** Prized Trophies make relic hoarding dangerous; opponents are mechanically incentivized to destroy undefended relic clusters.
- **Keepers in Iron:** Avoid three red factions in the pool; bird cards are the consistency backbone of the retinue.
- **Keepers in Iron:** Autumn and Mountain maps favor the faction strongly; Lake is the hardest map to navigate.
- **Keepers in Iron:** The comeback mechanic (Encamp from map edge when no warriors or waystations remain) is a designed safety valve — play from behind is a legitimate late-game strategy.

# Citations from Source

*None.*

# Source Notes

Tier 2 source. Luke Bridwell's Make Craft Game is the highest-quality individual Root strategy blog in the roster. This is a single-faction deep dive with thorough phase-by-phase coverage and map-specific guidance. No accuracy concerns flagged at curation time.

Coverage gap: predates any Homeland expansion content. Marauder-only scope.

See [Keepers in Iron faction profile](../../factions/keepers-iron.md) for the project's own derivative strategy layer. See [BGG canonical strategy thread](./boardgamegeek--root-strategy-guide.md) for community discussion of base-game factions.

---

# Review

**Reviewed:** 2026-04-29 by `root-3p-reviewer`
**Accuracy rating:** 5/10
**Verdict:** Solid structural coverage of the relic engine undermined by repeated errors on waystation count, column-bonus arithmetic, and two specific rule descriptions.

## Verified claims

- "each grants one extra card draw per evening (up to four total)" — correct; draw = 1 + waystations on map; three waystations = four cards per Evening per `rule:15.6.3`.
- "retinue cannot hold more than ten cards" — confirmed `rule:15.6.2`.
- "Move action... never loses retinue cards" — correct; the Move column has no discard check; only Battle-then-Delve and Move-or-Recover trigger checks per `rule:15.5.2.2.2` and `rule:15.5.2.3.3`.
- "Devout Knights ability (ignore first hit in battle when holding at least one relic and one keeper warrior)" — verified; condition is clearing has at least one relic and at least one Keeper warrior per `rule:15.2.4`.
- "opponents score when relics are destroyed, and opponents choose where the relic lands" — verified; Prized Trophies: enemy places relic in any forest face up and scores an extra VP per `rule:15.2.5`.
- "Encamp from map edge when no warriors or waystations remain" — verified; `rule:15.4.1` emergency clause triggers when "no warriors or waystations in any clearings."

## Conflicts with the Law

- "Placing **both** waystations on turn one" and "Deploy **both** waystations on turn one" — the Keepers have **three** waystations, not two. `rule:15.2.2` states "You have three waystations." This error appears in Win Condition and Key Takeaways.

- "relic column bonuses (8 points)" — incorrect arithmetic. There are three relic columns, each yielding 2 VP on completion (`rule:15.5.2.3.2`). Three columns = 6 VP, not 8.

- "three full retinue columns yield a minimum of 24 points" — incorrect. Each relic type has exactly four tokens with fixed values 1, 2, 3, 3 (`rule:15.2.1`): per-type total = 9 × 3 types = 27 raw VP. Three column completions add 6 VP = 33 total. The word "minimum" is a red flag too — there is no variance in relic totals, and 24 is simply the wrong number.

- "Evening's Gather Retinue phase lets the player shift cards between columns **and** add battle cards mid-game" — the Law says either add cards **or** shift one card, not both in the same Evening. `rule:15.6.2`: "You may add any number of cards from your hand to any Retinue slots, **or** you may shift one card in your Retinue to a different slot."

- "Moving all warriors out of a clearing without leaving stragglers triggers Live off the Land losses and forecloses future Encamp actions" — misattributes the mechanic. Live Off the Land (`rule:15.6.1`) removes one warrior from each clearing with **four or more** Keeper warriors at Evening; it has nothing to do with moving all warriors out of a clearing. The second consequence (forecloses Encamp) is correct reasoning, but it follows from `rule:15.4.1` (Encamp requires a warrior present), not from Live Off the Land.

## Strategic judgment notes

- "Hit and Run is the core tactical loop: move from map edges into delve clearings, battle and delve for relics, then move back to recovery clearings" — defensible mid-game pattern; the [Keepers in Iron profile](../../factions/keepers-iron.md) Playbook section describes the same sequence of Move → Battle-then-Delve → Move-or-Recover without naming it "Hit and Run." Consistent.
- "Avoid three red-suit factions in the pool" — draft-meta judgment; no Law-level constraint, but consistent with the profile's Bird-card flexibility notes.
- "Fill retinue to 10 cards before investing in recruiting or crafting" — judgment call; the profile's Opening section agrees that early Retinue loading is the priority, though it hedges on exact sequencing. Pass through with caveat: this can conflict with the mandatory-waystation-first priority also in the source.

## Citations from Source — verified

*The `# Citations from Source` block states "None." No curator-inserted rule citations to verify.*
