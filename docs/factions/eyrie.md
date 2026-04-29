# Eyrie Dynasties

## At a Glance

The Eyrie Dynasties are a **burst-then-snowball** faction: you build a programmed engine of actions called the Decree each turn, score points passively from your roosts each Evening, and threaten a runaway lead if left unchecked — but one unfulfillable Decree card sends you into turmoil, cutting your points and resetting your momentum.

| Attribute | Value |
|---|---|
| Faction citation key | `faction:eyrie` |
| Primary rule section | `rule:7.` |
| Reach | 7 (`rule:5.2.2`) |
| Complexity | Low (official rating; the Decree demands more forward-planning than the label implies) |
| Scoring tempo | Burst / steady (slow start, accelerating once roosts compound) |
| Color | Blue |

**Setup constraints.** You place 1 roost and 6 warriors in a corner clearing that is not occupied by another faction's starting clearing and, if possible, is diagonally opposite from another faction's starting clearing. (`faction:eyrie$7.3.2`)

---

## Win Condition

### Standard Route (30 VP)

Your primary path is passive. Every Evening you score VP based on how many roosts are currently on the map — the more roosts, the higher the per-turn yield (`faction:eyrie$7.6.1`). Building roosts requires ruling clearings and fulfilling your Build Decree cards, so your scoring engine and your board presence are the same thing. The Despot leader adds a secondary VP stream from destroying enemy buildings and tokens in battle (`faction:eyrie$7.8.4`).

Because each roost is worth incrementally more than the last, the Eyrie reward aggressive expansion. Getting to four or five roosts quickly generates compounding returns each turn. A well-managed Decree can carry you from 10 VP to 30 VP faster than most factions can respond.

### Dominance Path

Bird Dominance (`card:ROOT-67 (Base Game)`) requires ruling two opposite corner clearings at the start of your Birdsong. Ruling corners demands a military presence that the Eyrie can develop naturally through the Decree, but activating Dominance requires at least 10 VP first (`rule:3.3.1`). Community consensus holds that Eyrie are the faction best suited to a Bird Dominance attempt, given their structural pressure toward corner control — but opponents who understand this will contest corners directly.

Suit Dominance (Bunny/Fox/Mouse) is playable but uncommon; you would need to concentrate Decree cards of one suit in the Battle and Build columns without locking yourself into clearings you cannot reliably control.

### Scoring Tempo

The Eyrie start slow. With one roost, your Evening yields roughly zero to one VP (depending on the track position). As you build roosts, the track advances and your per-turn output climbs. The danger window is turns two through four: your Decree is still small, you have limited roosts on the board, and turmoil at this stage is costly. Once you have three or four roosts and a healthy Decree, the per-turn VP output becomes difficult for opponents to race.

---

## Setup

### Step-by-Step

1. **Gather Warriors.** Take your supply of 20 warriors. (`faction:eyrie$7.3.1`)
2. **Place Roost and Starting Warriors.** Choose a corner clearing not already claimed by another faction, preferably diagonally opposite from an existing starting corner. Place 1 roost and 6 warriors there. This becomes your starting clearing. (`faction:eyrie$7.3.2`)
3. **Choose Leader.** Select one of the four Eyrie leader cards and place it in your Leader Card slot. Leave the remaining three face up nearby. (`faction:eyrie$7.3.3`)
4. **Tuck Viziers.** Tuck your 2 Loyal Vizier cards into the Decree columns listed on your chosen leader. (`faction:eyrie$7.3.4`)
5. **Fill Roosts Track.** Place your 6 remaining roosts on your Roosts track from right to left. (`faction:eyrie$7.3.5`)

### Setup Theory

**Corner choice.** Prioritize a corner with good connectivity — multiple adjacent clearings and ideally two or three different suits accessible in one or two moves. A well-connected corner lets you fulfill Move and Battle Decree cards without backtracking. Avoid a corner that shares a single clearing with a faction that moves aggressively (Marquise, Hundreds), because you will begin with only 6 warriors.

**Neighbor considerations.** You want a corner that gives you room to build your first two or three roosts without immediate threat. If the Woodland Alliance starts nearby, their sympathy tokens can blockade the suit clearings you need for Decree actions — either clear sympathy early or avoid tucking single-suit Battle cards for that suit. Marquise is particularly dangerous at an adjacent corner because their density can prevent you from ruling clearings for Build actions.

**Opening hand priorities.** Your Birdsong forces you to add one or two cards to the Decree. Keep bird cards — they act as wildcards for any column. Keep the suits you are already positioned to execute: a fox card is safe to tuck into Recruit if your starting corner is fox-suited or adjacent to fox clearings. Avoid immediately tucking non-bird Battle cards unless you are certain that clearing will have enemies to fight every turn from now on — a Battle card with no valid target triggers turmoil (`faq:turmoil-partial-column`). Consider holding ambush cards in hand rather than tucking them if your position is stable.

**Leader choice at setup.** Despot (Move and Build viziers) is recommended for newer players: Move is nearly impossible to fail, and Build gives you a roost vizier to execute without needing to draw a suit card. Charismatic (Recruit and Battle viziers) produces warriors fast but commits you to battling somewhere every turn, which can become awkward if opponents retreat. Builder (Recruit and Move) is safe early and powerful if you plan to craft, but Disdain for Trade normally limits crafting to 1 VP per item, so Builder's upside requires deliberate deck construction. Commander (Move and Battle) is the most situational starting choice.

---

## Faction Rules and Abilities

### Crafting

You craft before resolving the Decree during Daylight by activating roosts (`faction:eyrie$7.2.1`). Each roost, when activated, provides one crafting hammer matching the suit of the clearing it occupies. This timing matters: crafting happens before your Decree resolution, so you cannot use a newly built roost (placed during Decree execution) to craft in the same turn.

**Edge case.** Because crafting precedes the Decree, you cannot use a card you craft (for example, a persistent effect card) to satisfy Decree actions in the same turn.

### Lords of the Forest

The Eyrie rule a clearing when tied for most combined warriors and buildings there, provided you have at least one Eyrie piece in that clearing (`faction:eyrie$7.2.2`). Standard ruling requires the most pieces; Lords of the Forest requires only a tie.

This is a significant military advantage. You can rule a clearing with three warriors even if an opponent also has three, as long as you have at least one piece present. It makes the Eyrie difficult to dislodge from contested clearings through attrition alone.

**Interaction with the Lizard Cult.** The Cult's Pilgrims ability overrides Lords of the Forest: the Cult rules any clearing in which they have a garden, regardless of piece counts (`faction:cult$10.2.4`). If the Cult places a garden in a clearing you need to rule for a Build action, you lose that building site unless you remove the garden.

### Disdain for Trade

Whenever you craft an item, you ignore the listed VP and instead score only 1 VP (`faction:eyrie$7.2.3`). Most craftable items are worth 2–4 VP to other factions; for you they are worth 1 VP regardless.

Exceptions exist: cards that grant extra crafting points through effects such as Master Engravers or the Legendary Forge can still give you those bonus points on top of the 1 base VP. The Builder leader nullifies Disdain for Trade entirely while that leader is active (`faction:eyrie$7.8.1`), restoring full item VP.

The practical implication: the value of crafting for the Eyrie lies in the card's persistent effect, not its VP payout. Craft Armorers (`card:ROOT-51 (Base Game)`), Cobbler (`card:ROOT-60 (Base Game)`), or Royal Claim (`card:ROOT-92 (Base Game)`) for their abilities — not for the points. Do not burn through your hand crafting items purely for VP.

---

## Turn Structure

### Birdsong

Your Birdsong has three steps, resolved in order (`faction:eyrie$7.4.`).

**Emergency Orders.** If you have no cards in your hand, draw one card (`faction:eyrie$7.4.1`). This is a safety valve, not a strategy. If you are regularly triggering Emergency Orders, your hand management is starving your Decree.

**Add to the Decree.** You must add one or two cards from your hand to the Decree columns (`faction:eyrie$7.4.2`). Key constraints:
- You must add at least one card. You cannot skip this step.
- You may add two cards, but only one of the two may be a bird card.
- Each card goes into any column of your choice. A card placed in Recruit means you must Recruit in a clearing of that suit this turn; a card in Battle means you must Battle in a clearing of that suit.

This is the most consequential decision you make each turn. Think two to three turns ahead: where will you have roosts to Recruit from? Where will enemies be to Battle? Where will you be able to rule clearings to Build? Bird cards offer flexibility — they satisfy any column in any clearing. Non-bird cards commit you to a specific suit.

**A New Roost.** If you have no roosts at all on the map (all were destroyed or lost), place a roost and three warriors in a clearing with the fewest warriors where all pieces can fit (`faction:eyrie$7.4.3`). This emergency recovery fires only when you have zero roosts — it does not trigger because you have few roosts. After recovery, you still go through the remainder of your turn normally.

### Daylight

Your Daylight has two steps, in order (`faction:eyrie$7.5.`).

**Craft.** You may activate roosts to craft cards from your hand (`faction:eyrie$7.5.1`). This step precedes Decree resolution. Crafting is optional; you are not required to craft each turn.

**Resolve the Decree.** You must execute all cards in your Decree, column by column from left to right (`faction:eyrie$7.5.2`). Within a column, resolve cards in any order. The four columns and their actions:

- **Recruit.** Place a warrior in any clearing that has one of your roosts and whose suit matches the card suit (`faction:eyrie$7.5.2.1`). You cannot Recruit in a clearing without a roost, even if you have warriors there.
- **Move.** Move at least one warrior from any clearing whose suit matches the card suit (`faction:eyrie$7.5.2.2`). The FAQ confirms you may move one warrior at a time and fulfill multiple Move cards from the same clearing, or even move warriors back and forth, as long as you follow movement rules (`faq:move-same-clearing`).
- **Battle.** Initiate a battle in any clearing whose suit matches the card suit (`faction:eyrie$7.5.2.3`). You must be present in the clearing and there must be an enemy present to battle.
- **Build.** Place a roost in any clearing you rule whose suit matches the card suit that does not already have a roost (`faction:eyrie$7.5.2.4`). You must rule the clearing — Lords of the Forest applies — and the clearing must have an empty building slot.

**If you cannot fully take any action in your Decree, you immediately fall into turmoil** (`rule:7.7`). Partial completion is not allowed: if your Battle card requires a fox clearing but no fox clearing has enemies, you go into turmoil the moment you reach that card (`faq:turmoil-partial-column`).

The columns resolve left to right, but within a column you can choose the order of individual cards. This matters: if you have multiple Battle cards and one clearing has enemies, you may be able to satisfy both by using the same clearing for each card (a separate battle for each).

### Evening

Your Evening has two steps, in order (`faction:eyrie$7.6.`).

**Score Points.** Score the VP shown on the rightmost empty space of your Roosts track (`faction:eyrie$7.6.1`). As you place roosts on the map, your Roosts track empties from left to right, advancing through higher-value spaces. Community sources consistently report the track progression as approximately 0, 1, 2, 3, 4, 4, 5 VP for one through seven roosts respectively. Once you have scored the evening, note that roosts removed from the map return to the track — your score regresses if roosts are destroyed.

**Draw and Discard.** Draw one card plus one card per uncovered draw bonus on your Roosts track (`faction:eyrie$7.6.2`). Then discard down to five cards if needed. Draw bonuses are revealed as roosts leave the track (i.e., as you build more roosts onto the map). A larger roost presence thus accelerates hand replenishment as well as VP output.

---

## Scoring Engine

| VP Source | Amount | Trigger | Timing |
|---|---|---|---|
| Evening roost scoring | Varies by roost count (0–5 VP per turn) | Each Evening phase | Evening, Score Points step |
| Removing enemy buildings / tokens | 1 VP per piece | When you remove an enemy building or token in any context | Immediate, during the action |
| Despot leader bonus | 1 extra VP (2 total) per battle | When you remove at least one enemy building or token in battle, while Despot is active | Immediate, during Battle |
| Crafting items | 1 VP per item (Disdain for Trade) | When you craft an item | Daylight, Craft step |
| Crafting items (Builder leader) | Full listed VP | When Builder is active and you craft | Daylight, Craft step |
| Royal Claim (`card:ROOT-92 (Base Game)`) | 1 VP per clearing you rule | Discarded during Birdsong | Birdsong |

The evening roost scoring is your primary engine. Every other source is incidental acceleration. The key insight: each additional roost increases your per-turn yield, so the slope of your VP curve steepens as you expand. Opponents who destroy a roost during a critical turn can drop you from 4 VP/turn to 2 VP/turn overnight.

---

## Playbook

### Opening (Turns 1–2)

Your opening goal is to build your second roost as quickly as possible without triggering turmoil. One roost yields minimal VP; two roosts shows the engine starting.

Turn 1: Add one or two cards to the Decree. If you took Despot, your viziers are on Move and Build. Add a Recruit card (ideally the suit of your starting corner, or a bird card) to begin building a warrior pool. Execute Move and Build: move warriors into an adjacent clearing and build a roost there if you rule it. Keep your added cards simple — suits you already control, or birds.

Turn 2: You now have at least two Decree cards beyond your viziers. The Move vizier lets you keep repositioning; the Build vizier pressures you to keep ruling clearings. Add another Recruit card or a bird card to Move. Avoid adding Battle cards unless you are confident in having targets every turn forward.

If you chose Charismatic: your Recruit vizier double-produces warriors, so lean into Recruit heavily in the opening. Build your warrior density before expanding territory; you will have the numbers to rule contested clearings.

If you chose Commander: your Move and Battle viziers push you toward aggressive expansion. Pick your battles carefully — you want to destroy enemy buildings (scoring points and weakening opponents) rather than battling in cleared-out forest. Commander's extra attack hit makes him effective at removing Marquise buildings or Woodland Alliance sympathy tokens.

### Mid-Game Pivots

By turns 3–5 your Decree has grown to five to eight cards. This is where management complexity escalates. Signs you need to pivot:

**If your Battle cards are becoming unfulfillable:** opponents are retreating from your clearings, or the relevant suit clearings are empty. Either add bird Battle cards (which can fire in any clearing) or accept that turmoil is coming and plan it for a turn when the VP penalty is smallest (few bird cards in the Decree).

**If your Build cards are stacking without roosts to place:** you may have ruled clearings but lack available building slots, or you cannot rule the required suit clearing. Add a bird Build card for flexibility, or shift to expanding to new suits.

**If you are being chased for the lead:** opponents will begin attacking your roosts. Prioritize clearings you can defend: those you can Recruit into repeatedly and where Lords of the Forest helps you maintain the rule. Pull warriors from clearings you cannot hold rather than leaving a skeleton force that concedes the clearing anyway.

**Strategic turmoil.** Some players argue that a planned turmoil — accepted deliberately when the Decree has few bird cards and the point penalty is low — can be a useful reset. You choose your new leader based on what the board needs next, and you re-enter with lean viziers. Community consensus acknowledges this as a legitimate tactical tool in experienced hands, though it carries risk if opponents capitalize on your weakened Evening scoring turn. Flag: this advice may reflect a pre-p16 balance state; evaluate against your current game.

### Endgame Routes

From 20 VP onward, you are either closing through roost scoring or pivoting to Dominance.

**Closing through roosts:** your Evening yield at five to seven roosts is high enough that simply defending your position wins the race in two to four turns. Identify which roosts opponents can reach and reinforce those clearings. Do not add aggressive new Decree cards at this stage — simplify the Decree to cards you know you can fulfill. One failed turn at 25 VP from turmoil can cost the game.

**Switching to Bird Dominance:** if opponents are close to 30 VP and your roost scoring cannot outpace them, activating Bird Dominance (`card:ROOT-67 (Base Game)`) pivots you to a different win condition. You need to rule both opposite corners at the start of your Birdsong. Holding corners with the Eyrie is natural given your Decree-driven expansion, but activating Dominance requires 10 VP first (`rule:3.3.1`). The Decree must continue firing — you still cannot afford turmoil.

If you are at 26–28 VP and opponents are at 27–29 VP, racing to 30 is usually correct over switching to Dominance.

---

## Threat Factions

### Woodland Alliance

The Woodland Alliance is your most persistent structural problem. Their sympathy tokens (`faction:woodland$8.2.5`) can appear in the very suit clearings your Decree depends on. If you have a fox Battle card tucked and the Alliance has sympathy in every fox clearing, you cannot battle there without triggering Outrage (`faction:woodland$8.2.6`) — they gain supporters, and you still have not satisfied the Decree. More critically, when the Alliance revolts and places a base, they remove all non-Alliance pieces from that clearing (`faction:woodland$8.4.1`): your roost and warriors evaporate at once, collapsing your scoring track by one step and potentially triggering turmoil when you can no longer fulfill the Build or Recruit cards tied to that clearing's suit.

Counter-plays: keep a Battle card or warrior presence in clearings where Alliance sympathy is likely to appear. Clear sympathy as soon as it appears in critical suit clearings — the Outrage cost is usually worth paying. Do not let the Alliance establish a base in your starting corner.

### Marquise de Cat

The Marquise's industrial capacity produces buildings fast and fills clearings with warriors, both of which can prevent you from ruling clearings for Build actions. Their Keep token blocks sympathy but also means a dense central clearing you may need to move through. Field Hospitals (`rule:6.2.3`) means your attacks on the Marquise are expensive: they recycle warriors you kill, so battles rarely produce the board-state change you paid for.

Counter-plays: target Marquise workshops and sawmills with Despot-boosted attacks rather than hunting her warriors. Destroying buildings produces VP for you (1 base + 1 Despot bonus) while weakening her crafting and production. Avoid prolonged attrition battles against Marquise in fortified clearings.

### Lord of the Hundreds

The Warlord's Oppress mechanic (`faction:warlord$14.6.2`) can score him points in clearings you vacate, and his Looters ability (`faction:warlord$14.2.5`) lets him steal cards when attacking you — cards you need for the Decree. His warrior density from Wraths can rival yours. Additionally, Befoul (`faction:warlord$14.5.2`) can destroy your roosts as tokens without requiring a battle.

Counter-plays: maintain warriors in clearings adjacent to his territory so he cannot Oppress easily. Do not leave clearings lightly held when the Warlord is active. Keep bird cards in hand when he threatens to Looter you.

### Corvid Conspiracy

The Corvids place plot tokens (`faction:corvid$13.2.1`) that can flip to remove your pieces. A Snare in your key building clearing triggers during movement and can strand warriors — potentially leaving you unable to fulfill a Move or Recruit action. Their Bomb plot, when flipped, removes all pieces in a clearing.

Counter-plays: Battle to remove plots from clearings where you have roosts. Plots must be battled with the Corvid present (or removed by specific card effects), so keep an eye on where the Corvid is placing.

---

## Card Priorities

### Top Priorities

**Armorers** (`card:ROOT-51 (Base Game)`) — Bird craft, Bird suit. Discard to ignore all rolled hits taken in one battle. Because the Decree forces you into battles you might not otherwise choose, you will occasionally face ambushes or heavily defended clearings. Armorers provides insurance. Craft this when you have a bird roost available. Worth 1 VP (Disdain for Trade), but the effect value vastly exceeds that.

**Scouting Party** (`card:ROOT-95 (Base Game)`) — Mouse craft. As attacker in battle, you are not affected by ambush cards. The Decree forces you to battle in specific clearings. Opponents who know your Decree can hold ambush cards and play them during your forced attacks, dealing 2 immediate hits and potentially triggering turmoil if you lose critical warriors. Scouting Party neutralizes this threat entirely. The 1 VP (Disdain for Trade) is irrelevant compared to protection from a forced-turmoil scenario.

**Royal Claim** (`card:ROOT-92 (Base Game)`) — Bird craft. In Birdsong, discard to score 1 VP per clearing you rule. When you have five or more roosts and rule several clearings, this can close games. Late-game, 6–8 VP from one card discard is exceptional.

**Tax Collector** (`card:ROOT-105 (Base Game)`) — Fox craft. Once per Daylight, remove one of your warriors from a clearing to draw a card. The Eyrie draw at most two cards per turn (base one plus one draw bonus), and your five-card hand limit creates tension with Decree feeding. Tax Collector converts excess warriors into cards, smoothing your hand. Particularly strong with Charismatic, who produces warriors rapidly.

### Situational

**Cobbler** (`card:ROOT-60 (Base Game)`) — Bunny craft. Take a move at the start of Evening. Useful when your Decree's Move cards leave a warrior pool out of position; an extra Evening move lets you reposition for next turn's Decree.

**Command Warren** (`card:ROOT-63 (Base Game)`) — Bunny craft. Initiate a battle at the start of Daylight. Normally your battles are Decree-driven and you choose their location during resolution. Command Warren adds a bonus pre-Decree battle, which can remove a blocking enemy before your Decree fires, or destroy a building for Despot points before Decree resolution.

**Brutal Tactics** (`card:ROOT-58 (Base Game)`) — Bird craft. As attacker in battle, deal an extra hit but the defender scores 1 VP. Useful for forcing through difficult engagements, especially when you need to clear a clearing for a Build action and the defender has ambush cards. Use sparingly — gifting VP is a real cost.

**Favor of the Foxes/Mice/Rabbits** (`card:ROOT-73 (Base Game)`, `card:ROOT-74 (Base Game)`, `card:ROOT-75 (Base Game)`) — Suit crafts. Remove all enemy pieces from all clearings of a suit. Powerful situational board-wipes. If you craft one, hold it until it removes multiple opponents' pieces. The Disdain for Trade restriction means the craft itself only costs a card but pays 1 VP; the value is the effect.

### Skip / Low Priority

**Better Burrow Bank** (`card:ROOT-55 (Base Game)`), **Birdy Bindle** (`card:ROOT-56 (Base Game)`), **Smuggler's Trail** (`card:ROOT-96 (Base Game)`), and similar hand-management permanents add marginal value when your real constraint is choosing which cards to tuck into the Decree, not drawing cards per se. Prioritize effect cards over draw-acceleration cards.

### Ambush Hold/Play Guidance

You spend cards adding to the Decree each Birdsong, so hand pressure is real. Hold ambush cards in hand unless you have a specific reason to tuck them. An ambush in your hand protects your roosts when others attack you; an ambush in the Decree is a Battle card that forces you to attack somewhere matching that suit. Bird ambush (`card:ROOT-46 (Base Game)`) is the strongest to hold because it defends against any attack.

### Dominance Card Considerations

Bird Dominance (`card:ROOT-67 (Base Game)`) is your most natural Dominance. If you are at 10+ VP, approaching a stall, and you can see a path to controlling both opposite corners within two turns, activating it is a viable pivot. Suit Dominances are harder to execute: three clearings of one suit is achievable but requires heavy Decree commitment to that suit at the expense of board flexibility.

In multi-player games, do not activate Dominance while multiple players can threaten both corners simultaneously. Wait until you can hold the required clearings for at least two consecutive Birdsong checks.

---

## Common Pitfalls

- **Tucking a non-bird Battle card too early.** A Battle card for a specific suit commits you to fighting in that suit every turn. If opponents learn your Decree, they evacuate that clearing. Prefer bird Battle cards or avoid Battle cards until you are confident about target availability.

- **Decree bloat without roosts to match.** Adding two cards every Birdsong means your Decree grows by ten to fourteen cards over five to seven turns. If you have not built roosts to support Recruit actions or clearings to support Build actions, the Decree outruns your board presence.

- **Neglecting warriors in starting corner.** The starting corner holds your first roost. If opponents seize it, you lose a roost, drop down the scoring track, and may trigger turmoil. Keep enough warriors there to maintain rule under Lords of the Forest.

- **Bird-heavy Decree entering turmoil.** Turmoil costs 1 VP per bird card on the Decree (`faction:eyrie$7.7.1`). A Decree loaded with bird cards (tucked for their flexibility) can cost four to six VP in a single turmoil. Track how many birds you have and consider purging a bird card via a different mechanism, or planning the turmoil for when the bird count is lowest.

- **Ignoring hand limit.** Your hand cap is five cards (`faction:eyrie$7.6.2`). Drafting two cards per Evening into a hand already near five means discarding useful cards. Tuck aggressively enough that your Evening draw actually lands in an empty hand slot, or use Tax Collector to burn warriors for cards on demand.

- **Attacking the Marquise into Field Hospitals.** Battling Marquise warriors in her own territory is often wasteful. Her warriors come back (`rule:6.2.3`); your Decree card is spent for the turn on a battle that accomplished little. If you must Battle the Marquise, target clearings with buildings and use Despot.

- **Starting with Commander.** Community consensus treats Commander as the weakest starting leader for new players. The extra attack hit is powerful but situational; the Move and Battle viziers commit you to aggressive play before you have the infrastructure to support it. Despot or Charismatic are safer opening choices.

- **Over-extending without Scouting Party.** Once other players identify you as the score leader, they will ambush your Decree-forced attacks. Without Scouting Party, a well-timed ambush can strip warriors from a critical clearing and cause the next Battle or Recruit card to fail.

---

## Mechanic Clarifications

### Does turmoil trigger if a Decree column is empty?

No. Turmoil triggers only when you have a card in your Decree that you cannot complete. An empty column generates no required action and thus cannot trigger turmoil (`faq:empty-column-turmoil`, citing `rule:7.7`).

### Does turmoil trigger if I complete some but not all cards in a column?

Yes. The moment any single card in the Decree cannot be fully taken, you fall into turmoil immediately (`faq:turmoil-partial-column`, citing `rule:7.7`). You do not finish the column first.

### Can I move one warrior at a time, or back and forth, to fulfill multiple Move cards?

Yes. The FAQ explicitly confirms that you can move one warrior at a time from the same clearing to fulfill multiple Move cards, and you may move the same warrior back and forth provided each movement follows the movement rules (`faq:move-same-clearing`, citing `rule:7.5.2`).

### What happens to the Loyal Viziers during turmoil?

During turmoil's Purge step, all Decree cards are discarded except your Loyal Viziers (`faction:eyrie$7.7.2`). The Loyal Viziers survive and are re-tucked into the new leader's designated columns during Depose (`faction:eyrie$7.7.3`).

### If I go into turmoil, do I still score in Evening?

Yes. Turmoil ends Daylight and begins Evening (`faction:eyrie$7.7.4`). You proceed through Evening normally — you score points from your Roosts track and draw cards. The turmoil only cancels remaining Daylight actions.

### Does the Charismatic leader require placing two warriors or allow placing two?

The Charismatic leader requires placing two warriors whenever you take a Recruit action — "you must place two warriors instead of one" (`faction:eyrie$7.8.2`). If you have only one warrior in supply, the FAQ clarifies you must place as many as possible, so you place one warrior and go into turmoil for failing to place the required two (`faq:charismatic-one-warrior-left`, citing `rule:7.7` and `rule:7.8.3`).

### Does Lords of the Forest interact with the Cult's Pilgrims?

Yes. The Cult's Pilgrims ability explicitly overrides Lords of the Forest: the Cult rules any clearing in which they have a garden, regardless of Eyrie piece counts (`faction:cult$10.2.4`). The Cult's faction rule takes precedence per the Golden Rule of Precedence (`rule:1.1.3`).

### What does the Despot leader's extra VP actually mean?

The Despot scores 1 extra VP when removing at least one enemy building or token in battle. The base rule awards 1 VP for removing any enemy building or token (`rule:3.2.1`). Despot brings the total to 2 VP for the act of removing at least one building or token in a single battle. You do not get additional VP for removing multiple buildings/tokens in the same battle — the bonus fires once per battle, not once per piece (`faq:despot-ability`, citing `rule:7.8.4`).

---

## Reference Index

- **Faction citation key:** `faction:eyrie`
- **Primary rule section:** `rule:7.`
- **Faction rule subsections:** `faction:eyrie$7.2.1` (Crafting), `faction:eyrie$7.2.2` (Lords of the Forest), `faction:eyrie$7.2.3` (Disdain for Trade), `faction:eyrie$7.3.` (Setup), `faction:eyrie$7.4.` (Birdsong), `faction:eyrie$7.5.2` (Decree resolution), `faction:eyrie$7.6.` (Evening), `faction:eyrie$7.7.` (Turmoil), `faction:eyrie$7.8.1`–`faction:eyrie$7.8.4` (Leaders)
- **Relevant glossary entries:** none specific to Eyrie in the Glossary appendix; see `item:boot`, `item:sword`, `item:hammer` for crafting item references
- **Hireling form:** The Eyrie have a hireling form (Eyrie-flavored hireling in the marauders-hirelings content). See `marauders-hirelings.yml` for the hireling card. Cross-link when the hireling profiles doc is written.
- **Cross-faction interactions:**
  - Cult Pilgrims overrides Lords of the Forest: `faction:cult$10.2.4`
  - Crafting VP general rule: `rule:3.2.2`; Eyrie exception: `faction:eyrie$7.2.3`
  - Despot and building-removal VP stacking: `rule:3.2.1`
  - Dominance card activation: `rule:3.3.1`
  - Vagabond coalition: if a Vagabond forms a coalition with you, they share your win condition; this interacts with the Decree system in that a coalition Vagabond benefits from your roost-driven scoring without being able to influence your Decree choices
