# Marquise de Cat

## At a Glance

**Identity**: You are an industrial war machine — you score by building buildings, and your buildings generate the wood that funds more buildings.

**Reach**: 10 (highest in the game; `rule:5.2.2`)

**Complexity**: Low. Your turn structure is straightforward, though optimizing your wood economy and action sequencing takes practice.

**Setup constraints**: You place your keep in any corner clearing of your choice, then garrison all clearings except the diagonally opposite corner (`rule:6.3.2`, `rule:6.3.3`). In standard setup factions are placed in setup order (`rule:5.1.7`); the Marquise is conventionally setup position A and places first.

**Color**: Orange.

**Faction icon**: Cat.

**Citation key**: No `faction:` key. All Marquise rules cite via `rule:6.X`.

**Primary rule section**: `rule:6.`

---

## Win Condition

### Standard Route (30 VP)

You score points by placing buildings — sawmills, workshops, and recruiters — on the map (`rule:6.5.4.3`). Each building type has its own track on your faction board; the VP value revealed when you pull a building off the track increases as you build more of that type. Early buildings score modestly; later buildings score significantly more. Getting all fifteen buildings on the map is not required for a win, but pushing each track as far as possible is how you close out the game.

Secondary scoring sources include:
- Removing enemy buildings and tokens in battle (`rule:3.2.1`)
- Crafting items (`rule:3.2.2`)

Your scoring tempo is **steady, with a mid-game acceleration**. Your first few buildings score 0 or 1 VP each; the back half of each track is where the game is won. You need to survive long enough to reach those high-value build slots.

### Dominance Path

You are not a strong dominance candidate in most games. Your strength lies in building density, and dominance requires ruling specific clearings at the start of your Birdsong (`rule:3.3.1.1`, `rule:3.3.1.2`). With 25 warriors available, you can theoretically hold territory, but the VP you sacrifice by removing your score marker is typically larger than the tactical gain. Dominance is an option worth evaluating only when you're far behind and an opponent is close to 30 VP.

---

## Setup

### Step-by-Step Placement

1. **Gather pieces** (`rule:6.3.1`). Take 25 warriors and 8 wood tokens to your supply.
2. **Place the keep** (`rule:6.3.2`). Choose any corner clearing and place your keep token there. This is your home base for the game.
3. **Garrison** (`rule:6.3.3`). Place one warrior in every clearing on the map except the corner diagonally opposite your keep. That far corner starts empty.
4. **Place starting buildings** (`rule:6.3.4`). Place 1 sawmill, 1 workshop, and 1 recruiter distributed among your keep clearing and any adjacent clearings, in any combination.
5. **Fill building tracks** (`rule:6.3.5`). Put your remaining 5 sawmills, 5 workshops, and 5 recruiters on their respective tracks from right to left, leaving the leftmost space of each track empty.

### Setup Theory

**Corner choice.** Prefer a corner with at least two adjacent clearings that have open building slots. More adjacent clearings means more flexibility for your starting buildings and easier first-turn builds. On the Fall map, a corner adjacent to a two-slot rabbit clearing is well regarded by experienced players because rabbit cards (good for crafting Command Warren and Cobbler) are common, and those two particular cards are among your best persistent effects.

**Starting building placement.** The most common configuration is: sawmill in your keep clearing (maximally protected; generates wood on turn 1), workshop on an adjacent clearing of a suit you want to craft from, recruiter wherever the remaining slot fits best. Placing your sawmill in the keep clearing means that clearing is protected from enemy placement by The Keep (`rule:6.2.2`) and from revolts, since the Woodland Alliance cannot place sympathy there (see `faq` entry on revolts at the keep).

**Neighbor considerations.** You set up first, so you can pick whichever corner suits the map and the faction lineup. Avoid choosing a corner that puts you directly adjacent to a Woodland Alliance or Eyrie player in their corner — both factions can threaten your clearings early before you've consolidated. The empty far corner is an invitation; leaving it truly empty for several turns is usually correct.

**Opening hand priorities.** Keep any card of the suit matching your keep clearing — you may need it for Field Hospitals (`rule:6.2.3`) in turn 1 if you get hit. Beyond that, keep bird cards for extra actions. Discard low-value single-suit cards whose suit you have no buildings near.

---

## Faction Rules and Abilities

### Crafting

The Marquise crafts during Daylight by activating workshops (`rule:6.2.1`). Each workshop activates as a single crafting piece whose suit matches the clearing it occupies (`rule:4.1.1`). You can activate multiple workshops in one crafting step.

**Edge cases.** A workshop destroyed before Daylight cannot be activated that turn. Workshops in different clearings of the same suit count as separate activations, but together they can satisfy multi-symbol costs — though in practice the shared deck contains no card with multiple symbols of the same suit.

### The Keep

You can place pieces in the clearing with your keep token; other players cannot (`rule:6.2.2`). This is an absolute restriction: the word "cannot" is not overridable unless explicitly stated (`rule:1.1.2`).

**Edge cases and clarifications.**
- Other players *can* move pieces into the keep clearing via the Move action (`faq` on moving to the keep: "Yes! 'Place' is a different keyword from 'move.'"). The restriction is on *placing*, not moving.
- If the keep is removed from the map, it cannot be placed again (`rule:6.2.2`). Losing the keep is a severe setback; it removes the placement restriction that keeps your home base secure and eliminates the destination for Field Hospital recoveries.
- The Woodland Alliance cannot place sympathy tokens in the keep clearing (`rule:6.2.2` via the FAQ on revolts at the keep), which prevents revolts there.
- The Swap glossary entry explicitly notes that swapping ignores the keep restriction (`item:Replace` in glossary: "swap ignores... the Marquise's keep").

### Field Hospitals

Whenever any number of your warriors are removed from a clearing, you may spend a card matching that clearing's suit to place those warriors in your keep clearing instead of returning them to supply (`rule:6.2.3`).

This is the core resilience mechanism of the faction. Instead of losing warriors permanently (until recruited), you recycle them directly back to your home base at the cost of a card.

**Edge cases and clarifications.**
- Field Hospitals triggers whenever your warriors are removed from *any* clearing, including when you are the attacker suffering hits.
- The card you spend must match the clearing from which the warriors were removed, not the keep clearing.
- You may choose not to use Field Hospitals even when able — returning warriors to supply is sometimes correct (e.g., supply is your preferred source for a later Recruit action).
- Bird cards are wild and can satisfy Field Hospitals for any clearing suit (`rule:2.1.1`).
- Field Hospitals does not apply to hirelings or Riverfolk mercenaries — those are not Marquise warriors (`rule:1.5.3`).
- In the timing interaction with ambush: if an ambush removes your last attacker(s), you can immediately spend a matching card to return them to the keep, potentially avoiding the "no remaining warriors" check that ends the battle. The FAQ confirms this: "Immediately, as long as you spend a card. This means you can avoid the check for 'no remaining warriors' prompted by the ambush."

---

## Turn Structure

### Birdsong

Place one wood token in each clearing that contains one or more of your sawmills — one token per sawmill present (`rule:6.4`). A clearing with two sawmills generates two wood; a clearing with one generates one.

**Ordering note.** Wood generation happens at the start of your turn, before any actions. This means wood generated this Birdsong is available for Build actions in your Daylight.

### Daylight

You proceed in two stages (`rule:6.5`):

**Stage 1 — Crafting.** You may activate workshops to craft cards. This step happens before your actions and does not count as an action.

**Stage 2 — Actions.** Take up to three actions in any order and number. You may take the same action multiple times (e.g., Battle twice). Additionally, for each bird card you spend (not as part of an action), you gain one extra action.

Available actions:

**Battle** (`rule:6.5.1`). Initiate a battle per the standard battle rules (`rule:4.3`). You are the attacker; you choose the clearing and the defender.

**March** (`rule:6.5.2`). Take up to two moves. A single March action gives you two moves, making it very efficient — two consecutive groups of warriors can relocate for one action slot. You must follow normal movement rules for each individual move (rule or adjacency requirements, `rule:4.2.1`).

**Recruit** (`rule:6.5.3`). Place one warrior at each recruiter on the map. You may take the Recruit action only once per turn. This action scales directly with your recruiter count: one recruiter returns one warrior, three recruiters return three warriors.

**Build** (`rule:6.5.4`). Place one building (sawmill, workshop, or recruiter) in a clearing you rule. You pull the leftmost building of the chosen type from its track on your faction board. You must:
1. Choose a clearing you rule (`rule:6.5.4.1`).
2. Pay the building's wood cost from that clearing, any adjacent clearings you rule, or any clearings connected through clearings you rule (`rule:6.5.4.2`). Wood travels through your ruled supply chain — a network of contiguous clearings you rule.
3. Place the building and score the VP printed on the space just uncovered on your faction board (`rule:6.5.4.3`).

**Overwork** (`rule:6.5.5`). Spend a card matching the clearing of a sawmill to place one wood token there. This action bypasses the Birdsong limit (one token per sawmill) and gives you a flexible way to top up wood in a specific clearing in preparation for a Build.

### Evening

Draw one card plus one additional card per uncovered draw bonus on your faction board (`rule:6.6`). Then discard down to five cards if you hold more than five.

**Draw bonuses.** There are draw bonus spaces on your faction board, each covered by a building. As you build recruiters, you uncover draw bonuses. More recruiters on the map means more cards per turn, which fuels Field Hospitals and extra actions.

---

## Scoring Engine

| VP Source | Amount | Trigger | Timing |
|---|---|---|---|
| Build sawmill | Per track position (increases with each build) | Place sawmill on map | Daylight: Build action |
| Build workshop | Per track position (increases with each build) | Place workshop on map | Daylight: Build action |
| Build recruiter | Per track position (increases with each build) | Place recruiter on map | Daylight: Build action |
| Remove enemy building | 1 per building | Remove an enemy building | Whenever it happens |
| Remove enemy token | 1 per token | Remove an enemy token | Whenever it happens |
| Craft item | Listed on card | Craft any item card | Daylight: crafting step |

**On the building tracks.** The VP amounts per build are printed on the faction board, not in the Law text. The Law confirms you "score the victory points listed on the space uncovered" (`rule:6.5.4.3`). Early buildings on each track score 0 or 1 VP; later buildings score more. Spreading builds evenly across all three types (rather than rushing one to completion) is typically suboptimal — the back of each track is where the points concentrate, so focused building sequences pay off more.

**Crafting.** Items scored through crafting are among your faster-scoring opportunities. Boots and coins in particular are easy to craft if you have workshops in the right clearings, and each crafted item scores immediately.

---

## Playbook

### Opening (Turns 1–2)

Your garrison starts spread across nearly the entire map, which looks strong but is tactically fragile: isolated single warriors are easy targets for the Eyrie or any aggressive faction. The standard first move is to consolidate: take a March action to pull distant warriors toward your keep cluster, then build a sawmill.

A common turn-1 sequence: **March → March → Build (sawmill)**. This pulls warriors from the outer clearings back toward your core, placing the sawmill somewhere in your network to start wood generation immediately.

An alternative if your opening hand is strong: **Build (sawmill) → Overwork → Build (recruiter)** — front-loading construction when you have the cards to support it.

By the end of turn 1, you want:
- Warriors consolidated into defensible clusters of 3–4.
- A sawmill generating wood.
- At least one building slot protected from easy takeover.

Turn 2 priorities: get the Recruit action in. With even two recruiters on the map, Recruit refills multiple positions. Build your second recruiter early to uncover draw bonuses; more cards per turn directly enables more Field Hospital recoveries.

Community consensus (from BGG and Reddit primers, predominantly from 2019–2022 discussions that may predate minor rules revisions) is that early recruiter density is undervalued by new Marquise players, who often rush sawmills for wood but neglect the card draw that sustains the whole engine.

### Mid-Game Pivots

**Read your build track.** By turns 3–5 you should be pushing each building type meaningfully. Watch for the moment your sawmill count outpaces your construction needs — at that point, shift build actions toward workshops (for crafting) or recruiters (for card draw and Recruit scaling).

**Recognize the "Great Wall" line.** If you are taking pressure from multiple directions, consolidate to a defensible region rather than trying to hold the entire map. Control roughly half the clearings with strong warrior density; cede the periphery temporarily. Some experienced players describe drawing a line across the map and deliberately withdrawing from the far side — maintaining rule over your core clearings at 3–4 warriors each makes attacks prohibitively expensive.

**Watch sympathy spread.** If the Woodland Alliance is establishing sympathy in your core clearings, spend actions and cards to remove it before it becomes a revolt base. Sympathy in a clearing with one of your buildings threatens both the building (revolt removes your pieces) and your wood supply chain. Two warriors defending a sympathy-adjacent clearing is the minimum; three is safer.

**Card hand management.** You rarely want to sit at zero cards. Field Hospitals require cards matching specific suits, and unexpected attacks can drain your hand quickly. If a Recruit action would uncover a draw bonus, prioritize that build.

### Endgame Routes

With 10 or more buildings on the map, your per-build VP values are climbing. An endgame turn where you build two high-value buildings — say, your fifth sawmill and fourth recruiter — can yield 7+ VP in a single turn.

**Closing burst.** The most common Marquise closing pattern is: build up to 3–5 actions through bird card expenditure, chain Build actions using wood stored across multiple clearings. At this point you are not fighting for territory — you are converting stored wood and saved bird cards into VP as fast as possible.

**Crafting finish.** Royal Claim (`card:ROOT-92 (Base Game)`) is a legitimate closing play if you rule many clearings: score one point per clearing you rule, then discard it. In the final turns, if you rule eight clearings, Royal Claim alone can provide a decisive push.

---

## Threat Factions

### Woodland Alliance

The Alliance is your primary existential threat. Their Outrage mechanic (`faction:woodland$8.2.6`) rewards them for every warrior you move into a sympathetic clearing, and Revolt (`faction:woodland$8.4.1`) removes all of your pieces from a clearing and places an Alliance base there — destroying your buildings and eliminating you from that clearing in a single action.

The specific danger: the Alliance grows faster than your building track can score if you let sympathy spread unchecked. A revolt in a core clearing with two of your buildings can erase 3–5 VP of infrastructure you spent multiple turns constructing. The counter-plays are proactive rather than reactive:

- Keep 2–3 warriors in any clearing adjacent to known sympathy to deter revolt (revolts require ruling the clearing).
- Spend an action to remove sympathy tokens before they multiply. The cost (Battle or the VP loss from hitting tokens) is almost always worth it compared to a revolt.
- The Alliance cannot place sympathy in your keep clearing (`rule:6.2.2`), which makes your keep cluster permanently safe from revolt. Anchor important buildings there.
- When the Alliance tries to establish a third base: treat this as a crisis. Three bases enable their scoring engine to accelerate dramatically.

### Eyrie Dynasties

The Eyrie's Decree forces them to take escalating actions each turn or face Turmoil (`faction:eyrie$7.5`, `faction:eyrie$7.7`). As they add cards to the Decree, they become committed to repeated battles and moves in specific suit clearings. Their Roosts generate points passively each turn, making them a high-scoring faction if left unchecked.

The danger for you: Eyrie warriors can accumulate fast, and a large Eyrie force supported by a Commander leader (`card:ROOT-2 (Base Game)`) deals extra hits. Eyrie's commitment to the Decree also means they will battle in your clearings even when it costs them warriors — they have no choice.

Counter-plays:
- Maintain warrior density high enough that Eyrie battles are expensive. A clearing with four of your warriors requires the Eyrie to take multiple battles (or roll very well) to clear it.
- Target Roosts when the Eyrie score drops — even one destroyed Roost creates a tempo setback and can trigger Turmoil if they have a Recruit card in the Decree they cannot fulfill.
- Don't let them score freely. If the Eyrie is approaching 20 VP, force them into costly battles rather than ceding territory.

### Vagabond

The Vagabond operates outside normal faction dynamics: the pawn cannot be removed, items restore warrior-like capabilities, and the Hostile scoring rule (`faction:vagabond$9.2.9.3`) means a Vagabond hostile to you scores VP every time they remove your warriors.

The danger: a Vagabond sitting in your core clearings with the Crossbow item can chip away at your warriors for free, scoring VP while you pay cards to Field Hospital the survivors back. Because you cannot remove the pawn, normal battle suppression doesn't work.

Counter-plays:
- Make the Vagabond's life difficult early. A large warrior presence in clearings the Vagabond frequents raises their damage costs.
- Avoid being the Vagabond's sole hostile opponent. If another faction is also hostile, the Vagabond's VP gains are split.
- Some players advocate never crafting tea for the Vagabond (`card:ROOT-89 (Base Game)`, `card:ROOT-90 (Base Game)`, `card:ROOT-91 (Base Game)`) — items repaired by tea extend their ability to attack you. This is a reasonable heuristic though occasionally the tempo from your own crafting outweighs the concern.

### Corvid Conspiracy

The Corvids place Plot tokens across the map, scoring VP each time they flip one (`faction:corvid$13.4.2`). Each plot type creates a different problem: a Bomb removes all enemy pieces when flipped (`faction:corvid$13.7.1`), a Snare prevents enemy pieces from being placed in or moved from its clearing (`faction:corvid$13.7.2`), and Extortion takes a random card from each enemy with pieces in the clearing when flipped (`faction:corvid$13.7.3`).

The danger for you specifically: a Bomb detonated in a high-density clearing can remove multiple warriors and a building in a single flip, and Extortion taxes a hand-card-hungry faction like you. A Snare in a core clearing blocks your movement through it and can freeze wood in a clearing you can no longer access freely. Because your scoring depends on building density, losing buildings to Corvid plots disrupts your track progression directly.

Counter-plays:
- Use the Exposure ability (every faction can use it): if you have pieces in a clearing with a face-down plot, show the Corvids a matching card to guess the plot type (`faction:corvid$13.2.4`). A correct guess removes the plot and scores you a VP.
- Keep the hand large enough to absorb an Extortion if you cannot remove it.
- Field Hospitals can recover warriors lost to a Bomb if you hold a matching card.

---

## Card Priorities

### Top-Tier Crafted Effects

**Command Warren** (`card:ROOT-63 (Base Game)`). Costs one rabbit. Gives you a free battle at the start of Daylight, before your action phase. This is worth crafting as soon as possible: the extra battle essentially extends your action economy by one each turn, and it lets you clear sympathy or threaten opponents before they can react. Placing your opening workshop in a rabbit clearing is often motivated specifically by wanting to reach Command Warren.

**Cobbler** (`card:ROOT-60 (Base Game)`). Costs one rabbit. A free move at the start of Evening. Persistent extra movement is highly valuable for a faction that relies on repositioning warriors to protect buildings and supply chains. Cobbler's timing (Evening) means you can reposition after seeing the full board state of your turn.

**Armorers** (`card:ROOT-51 (Base Game)`). Costs one bird. Discard in battle to ignore all rolled hits taken. This card dramatically raises the cost of attacking you. Opponents who know you hold Armorers must commit to higher warrior counts before attacking, which is a strong deterrent. Once crafted, hold it until a battle where you're defending something valuable.

**Sappers** (`card:ROOT-94 (Base Game)`). Costs one bird. Discard as defender to deal an extra hit. Complements Armorers — together they give you both damage mitigation and extra damage dealt as a defender.

**Tax Collector** (`card:ROOT-105 (Base Game)`). Costs one fox. Once per Daylight, remove one of your warriors from the map to draw a card. This trades a warrior for card advantage, which is excellent if you have warrior surplus (post-Recruit). Using Tax Collector to thin overstacked clearings while drawing is efficient.

**Better Burrow Bank** (`card:ROOT-55 (Base Game)`). Costs one rabbit. At start of Birdsong, you may draw a card; if you do, an enemy also draws one. In a hand-intensive game, the extra draw is usually worth the benefit you give an opponent, especially early when your hand is small.

### Situationally Valuable

**Royal Claim** (`card:ROOT-92 (Base Game)`). Score one VP per clearing you rule, then discard. This is a one-time scoring burst rather than a persistent effect. Powerful at endgame when you rule many clearings; weak in the early game when ruling fewer than five.

**Scouting Party** (`card:ROOT-95 (Base Game)`). Costs one mouse. Persistent: you ignore ambush cards as attacker. Strong if you're running repeated aggressive battles; less impactful in games where you're mostly defending.

**Woodland Runners** (`card:ROOT-109 (Base Game)`). Costs one bird. Persistent effect (check card for specifics). Situationally useful for expanding your movement options.

**Brutal Tactics** (`card:ROOT-58 (Base Game)`). Costs one bird. As attacker, deal an extra hit but the defender scores 1 VP. Useful for punching through large defensive stacks but the VP gift is a meaningful cost. Craft only when you need to crack fortified positions.

### Ambush Guidance

Hold ambush cards until you're defending a high-value clearing — specifically one containing multiple buildings or your keep. The threat of an ambush deters attacks; playing it removes the threat but recovers two hits.

You can also use ambush cards to foil the opponent's ambush (`rule:4.3.1.1`): if your opponent tries to ambush you as defender, you can play a matching ambush as attacker to cancel it.

Bird ambush cards are the most flexible since they match any clearing.

### Dominance Considerations

Activating a dominance card costs you your VP track, which is your primary win engine. The tradeoff is almost never favorable unless you are in last place with no realistic path to 30 VP through building. If you do consider dominance, the bird dominance (`card:ROOT-67 (Base Game)`) may suit your territorial strengths best — you start the game with warriors in many clearings and can often control opposite corners — but you would need 10 VP first (`rule:3.3.1`).

### Overwork Targets

Overwork (`rule:6.5.5`) — spending a card to place a wood token on a sawmill — is most valuable when you are one wood short of a build this turn and do not want to wait. The card must match the sawmill's clearing, so hold fox, rabbit, and mouse cards of the suits matching your sawmill locations.

---

## Common Pitfalls

- **Starting too spread out.** Your garrison covers almost every clearing at turn 1, and new players try to hold all of them. Isolated single warriors die for free to the Eyrie and the Woodland Alliance. Consolidate aggressively in turns 1–2.

- **Neglecting recruiter construction.** Sawmills generate wood, workshops enable crafting, but recruiters are what sustain your warrior count and draw bonuses. Skipping recruiters means a depleted hand and a stalling Recruit action.

- **Letting wood sit in isolated clearings.** Wood on a clearing you no longer rule cannot be spent for a Build (`rule:6.5.4.2`). If opponents push you back, you lose both the clearing and the wood stored there. Move your builds to follow your wood, or accept you'll lose it.

- **Over-relying on Field Hospitals.** Field Hospitals is powerful, but it costs cards. If you burn your hand hospitalizing warriors every turn, you lose crafting, extra actions, and the ability to overwork. Treat it as a safety valve, not a default.

- **Not removing sympathy.** Every turn you delay addressing Woodland Alliance sympathy is another opportunity for them to revolt. A revolt in a building-heavy clearing is a setback you will spend two or three turns recovering from.

- **Building in clearings you do not rule.** The Build action requires you to rule the target clearing (`rule:6.5.4.1`). Building behind your own lines — in clearings you strongly hold — is far safer than pushing buildings into contested territory.

- **Misjudging wood connectivity.** You can only spend wood from clearings you rule along a contiguous chain you rule (`rule:6.5.4.2`). If opponents break your chain, you may have wood you cannot access. Verify connectivity before choosing a build target.

- **Spending bird cards recklessly.** Bird cards as extra actions are excellent, but they are also wild for Field Hospitals and ambush foils. Burning them all for actions early can leave you exposed to an ambush you cannot foil.

---

## Mechanic Clarifications

**Can other players move warriors into my keep clearing?**

Yes. The restriction on the Keep is that other players cannot *place* pieces there (`rule:6.2.2`). Move is a distinct keyword from place (`faq` entry: "Yes! 'Place' is a different keyword from 'move.'"). Opponents can move warriors into your keep clearing freely.

**If the Woodland Alliance wants to revolt in my keep clearing, can they?**

No. A revolt requires placing a sympathy token first (`faction:woodland$8.4.1`), and sympathy cannot be placed in the keep clearing because placing is restricted to you only (`rule:6.2.2`). The FAQ confirms this interaction directly.

**Does Field Hospitals apply when I am the attacker and take hits?**

Yes. Field Hospitals activates "whenever any number of Marquise warriors are removed from a clearing" (`rule:6.2.3`) — it does not distinguish attacker from defender.

**Can I use Field Hospitals on Riverfolk mercenaries I've hired?**

No. Field Hospitals works on Marquise warriors specifically. Riverfolk mercenaries are Riverfolk faction pieces, not Marquise warriors (`rule:1.5.3`).

**After an ambush removes my attacking warriors, can I immediately use Field Hospitals to avoid ending the battle?**

Yes. The FAQ confirms: you can spend a matching card immediately, placing those warriors at the keep, and the check for "no remaining warriors" that ends the battle happens after this. If Field Hospitals returns warriors to the keep clearing before the check, the battle does not end automatically.

**What happens if my keep token is removed?**

It cannot be placed again (`rule:6.2.2`). The restriction preventing enemies from placing pieces at that clearing disappears, and Field Hospitals loses its destination. This is a catastrophic loss.

**Does building in a clearing require me to have warriors there?**

No. You must *rule* the clearing (`rule:6.5.4.1`), and ruling requires more total warriors and buildings than any other single player (`rule:2.5`). You could rule a clearing by having buildings there without warriors, though that clearing would be extremely vulnerable.

**Can I build the same building type multiple times in one turn?**

Yes. Each Build action places one building, and you have three action slots plus extra actions from bird cards. Nothing prevents you from taking Build twice in the same turn, placing two buildings of the same or different types.

---

## Reference Index

**Citation key**: No `faction:` key. All Marquise rules cite via `rule:6.X`.

**Primary rule section**: `rule:6.`

**Related glossary entries**:
- `item:boot` — common crafting target; easily crafted with one workshop active
- `item:sword` — scored when crafted; `item:crossbow` — scored when crafted
- Place (`rule:21.20`) — the precise definition that makes the keep restriction work
- Remove (`rule:21.24`) — how pieces leave the map; relevant to Field Hospitals timing

**Hireling form**: The Mechanical Marquise 2.0 clockwork bot exists but is out of scope for this profile (non-faction, bot content).

**Cross-faction interactions worth noting**:
- *Woodland Alliance*: Alliance cannot place sympathy at the keep (`rule:6.2.2`); revolts there are impossible. Outrage (`faction:woodland$8.2.6`) applies normally when you move into sympathetic clearings — you pay cards.
- *Vagabond*: Vagabond can move into your keep clearing freely. If hostile to you, Vagabond scores VP removing your warriors (`faction:vagabond$9.2.9.3`). Field Hospitals can recover warriors removed by the Vagabond.
- *Corvid Conspiracy*: A Bomb plot removes all enemy pieces in its clearing when flipped (`faction:corvid$13.7.1`). A Snare prevents enemy pieces from being placed in or moved from its clearing (`faction:corvid$13.7.2`). Field Hospitals can recover warriors lost to a Bomb if you hold a matching card.
- *Riverfolk Company*: Purchasing Riverfolk mercenaries gives you warriors you can use in battle, but Field Hospitals does not apply to them (`rule:1.5.3`). Riverfolk Mercenaries cannot battle the Riverfolk themselves (`faq` entry on mercenaries), though they can battle other factions including Riverfolk-controlled hirelings.
- *Lilypad Diaspora*: Diaspora can move using rivers (`faction:diaspora$16.2.4`); their mobility may let them reach your clearings faster than expected. Protect core clearings accordingly.
