# Knaves of the Deepwood

---

## At a Glance

**Identity.** You are three wandering Captains who harass armies, scatter acclaim tokens across the map, and score points from both — a split scoring engine that demands you attack boldly and spread widely.

**Reach.** 4 (`rule:5.2.2`)

**Complexity.** High

**Setup constraints.** No corner placement. Each Captain starts in a separate forest with one Skunk (`faction:knaves$18.3.3`).

**Color.** Black (`#372F2C`)

**Faction icon.** faction-knaves

**Citation key.** `faction:knaves` (faction-specific rules cite as `faction:knaves$18.X.Y.Z`)

**Primary rule section.** `rule:18.`

**Exclusive constraint.** The Knaves cannot share a game with any Vagabond (`faction:knaves$18.2.1`).

---

## Win Condition

### Standard 30 VP Route

Your scoring engine has two channels. Each Evening, you score 1 VP for every 2 Prisoners in forests and 1 VP for every 2 acclaim on the map (`faction:knaves$18.6.1`). Run both in parallel. With 8 acclaim and a full cache of Prisoners, you can approach 7–8 VP per Evening cycle — but this requires both channels to be healthy simultaneously, and neither accumulates quickly on its own.

Acclaim spreads from battle (Have at Thee places acclaim after a successful attack, `faction:knaves$18.2.6`) and from item actions like Revel (`faction:knaves$18.5.1.4.5`) and Gift (`faction:knaves$18.5.1.4.6`). Prisoners come from Have at Thee and from the Assault item action (`faction:knaves$18.5.1.4.2`). Serve (`faction:knaves$18.5.1.4.7`) can also generate crafting VP as a secondary source.

**Scoring tempo classification: steady, punctuated by item action cycles.** Each round of Captain rotations tends to generate 3–6 VP if played well, but tempo dips sharply during the take-it-easy cycle when all Captains must Retire before refreshing.

### Dominance Path

Dominance is playable but requires ruling three clearings of one suit (or two corner clearings for bird). Because you have no buildings, you rule clearings only by placing Skunks and Captains — a fluid presence that enemies can dislodge. The path demands sustained military pressure to maintain rule against active opposition. Most players at intermediate experience prefer the VP route.

---

## Setup

### Step-by-Step Placement

1. **Gather pieces.** Form a supply of 10 Skunk warriors (`faction:knaves$18.3.1`).
2. **Choose three Captain cards.** You select from the 12 available Captains. Collect the three corresponding Captain warrior tokens (`faction:knaves$18.3.2`).
3. **Place Captains and Skunks.** Place 1 Captain warrior and 1 Skunk warrior each in three *different* forests (`faction:knaves$18.3.3`). No two Captains begin in the same forest.
4. **Set up player board.** Place the 6 items face up in your Stash that are shown on your 3 chosen Captain cards. Fill each Acclaim slot with 2 acclaim tokens (`faction:knaves$18.3.4`).

You start with exactly 6 items — two per Captain — and 8 acclaim tokens held off-board.

### Setup Theory

**Captain choice is character selection and build order combined.** Your three Captains fix your starting item suite entirely. The 12 Captains (see `rule:18.` appendix K) each bring two items and a passive or triggered ability. Think of the selection less like picking favorites and more like assembling a kit: do you want mobility (Dash boots from Thief or Harrier), sustained aggression (Assault swords and Skirmish crossbows from Ranger), or economic acceleration (Serve hammers from Tinker)?

**Balanced general recommendation for new players.** Choose one Captain with mobility items (`item:boot`), one with combat items (`item:sword` or `item:crossbow`), and one with economy items (`item:hammer` or `item:coin`). This avoids pigeonholing your entire early game into one mode. The Tinker, Ranger, and Vagrant together cover economy, aggression, and support respectively — a starting combination that community discussion (not authoritative source) suggests is forgiving.

**Forest placement matters more than it looks.** Each Captain begins adjacent to the clearings that touch its starting forest. Forests with adjacency to many clearings give you more reach on turn 1. On the standard map, central forests touch 3–4 clearings; corner-adjacent forests may touch only 2. If you have three Captains in low-adjacency forests, your opening actions will be spent just moving to civilization.

**Opening hand.** You want cards that let you Protect the Weak cheaply (matching suits for your early acclaim token locations) and cards useful for crafting in Serve. Keep bird cards as flexible wild suits.

---

## Faction Rules & Abilities

### Exclusive with Vagabond

`faction:knaves$18.2.1` The Knaves cannot be in the same game as any Vagabond. This is a hard exclusion — not a setup restriction, but a legal constraint.

### Stash

`faction:knaves$18.2.2` Instead of a standard Crafted Items box, you use the Stash. Items in the Stash may be face up (available) or face down (spent). When you craft or take an item, place it face up. You flip items face down to use Item Actions during Captain Acts (`faction:knaves$18.5.1.4`). All face-down items stay down until Take It Easy (`faction:knaves$18.6.3`) — you cannot selectively refresh individual items mid-cycle.

**Edge case.** Filch lets you take an item from an enemy's Crafted Items box (`faction:knaves$18.5.1.3`). That item goes face up in your Stash. You can then use it as an item action, flipping it face down — on the same turn, if you haven't exhausted your actions.

### Acclaim

`faction:knaves$18.2.3` You have 8 acclaim tokens. Each clearing can hold at most one acclaim. Forests cannot hold acclaim. Acclaim scores VP in Evening (`faction:knaves$18.6.1`) and enables Protect the Weak (`faction:knaves$18.6.2`) and the Serve crafting mode (`faction:knaves$18.5.1.4.7`).

**Spreading vs. stacking.** Because each clearing holds at most one acclaim, your maximum on-board coverage is 8 clearings. You can never double up to get more VP from a single clearing — eight clearings each with one acclaim earns you 4 VP per Evening, which is your ceiling from this channel alone.

**Run Away** (`faction:knaves$18.2.7`): When any enemy removes your acclaim, they must also place 1 Skunk from your supply into a forest of their choice adjacent to the acclaim's former clearing. This makes removing acclaim slightly costly for opponents — but it also scatters your Skunks in positions you don't control. An empty Skunk supply nullifies the trigger entirely.

### Deepwood Runners

`faction:knaves$18.2.4` Captains and Skunks may move in and out of forests without needing to rule either end of the path. Normally, `rule:4.2.1` requires a mover to rule the origin, destination, or both. The Deepwood Runners exception removes this requirement for all Knaves warriors — Captains and Skunks alike. Non-Knaves pieces are not affected.

**Practical implication.** You can reposition Captains through forests even from clearings you do not rule — which means getting pushed off a clearing does not trap a Captain there. Forests function as transit nodes, not dead ends.

### Follow Me

`faction:knaves$18.2.5` When you move a Captain, you may move Skunks from the same clearing with it. Skunks stack defensive value around a Captain: Captains can only be hit in battle if no Skunks remain in the battle clearing (`faction:knaves$18.2.5`). Effectively, Skunks act as a hit buffer — opponents must chew through them before the Captain is in danger.

**Captain replacement.** Captains cannot be placed except via setup or Ready in Birdsong (`rule:18.4`), and cannot be replaced if removed (`faction:knaves$18.2.5`). Losing a Captain is a genuine setback: you lose that Captain's item contributions and must Ready it in a forest to bring it back, costing an action tempo and limiting your move+battle count that turn to three actions instead of four (`rule:18.4`).

### Have at Thee

`faction:knaves$18.2.6` When your Acting Captain attacks in battle, for each defending warrior you hit: instead of removing it, you move it to an adjacent forest with no Prisoners (ignoring the forest-movement rule). If no such forest is available, the warrior is removed normally. After the battle resolves, if the Acting Captain is still in the battle clearing, you place one acclaim there.

**Prisoners and forests.** Forests holding Prisoners cannot receive more Prisoners from Have at Thee. Plan your Prisoner logistics: if adjacent forests fill up, captives start getting removed outright rather than imprisoned.

**Acclaim timing.** The acclaim placement from Have at Thee is conditional — the Captain must still be in the clearing at battle end. Nab (`faction:knaves$18.5.1.4.4`) can relocate the Captain if not hit, so carefully read its timing: acclaim is placed after the Captain optionally moves. Assault (`faction:knaves$18.5.1.4.2`) places Prisoners in separate forests per captive and its text directly references `rule:18.2.6`.

### Run Away

`faction:knaves$18.2.7` Covered above under Acclaim. The Skunk placement is mandatory for the enemy if your supply is not empty. The forest chosen is the enemy's choice, not yours.

### Crafting

`faction:knaves$18.2.8` You craft by activating the Acting Captain (via Filch, `faction:knaves$18.5.1.3`) or activating acclaim tokens on the map (via Serve, `faction:knaves$18.5.1.4.7`). Each acclaim can only be activated once per turn to craft. Items crafted via Filch do not score the listed VP (`faction:knaves$18.5.1.3`); items crafted via Serve do score (`faction:knaves$18.5.1.4.7`).

---

## Turn Structure

### Birdsong — Ready

You place one face-up Captain card in the Acting Captain slot on your board (`rule:18.4`). You gain that Captain's listed ability until you Retire it. If the corresponding Captain warrior is not on the map — because it was previously removed — you place it in any forest, remove all Prisoners from that forest and adjacent forests, and take only three actions (not four) in Captain Acts this turn.

**Choosing which Captain to Ready.** You revealed this choice at the end of your previous turn (when you Retired the prior Acting Captain). That means opponents know which Captain is active at the start of your Birdsong. The secret is gone by the time you act.

### Daylight — Captain Acts, then Retire

**Captain Acts** (`faction:knaves$18.5.1`): In any order and combination, you may take up to four actions with the Acting Captain. (Three actions if you had to place the Captain in a forest this turn.) Available actions:

- **Move** (`faction:knaves$18.5.1.1`): Take a move with the Acting Captain. You may bring Skunks from the same clearing along.
- **Battle** (`faction:knaves$18.5.1.2`): Initiate a battle in the Captain's clearing. Normal battle rules apply (`rule:4.3`).
- **Filch** (`faction:knaves$18.5.1.3`): Once per turn. Either craft a card by activating the Acting Captain, or take 1 item from an enemy's Crafted Items box in the Acting Captain's clearing. Crafted items do not score VP.
- **Item Action** (`faction:knaves$18.5.1.4`): Flip one face-up item in your Stash face down to take its action. Each item action costs one of your four (or three) Captain Acts for the turn. Available item actions:
  - **Dash** (`item:boot`): Move the Acting Captain up to twice, ignoring rule (`faction:knaves$18.5.1.4.1`).
  - **Assault** (`item:sword`): Battle in the Captain's clearing. Take *all* warriors you hit as Prisoners, each to a separate forest with no Prisoners (`faction:knaves$18.5.1.4.2`).
  - **Skirmish** (`item:crossbow`): Move the Captain from a forest, then battle in its destination clearing, ignoring the first hit taken (`faction:knaves$18.5.1.4.3`).
  - **Nab** (`item:sack`): Battle in the Captain's clearing. If the Captain would be hit, move it to an adjacent forest instead of removing it (if possible). If the Captain was not hit, you may move it after the battle (`faction:knaves$18.5.1.4.4`).
  - **Revel** (`item:tea`): In a clearing, place 1 acclaim and 1 Skunk at the Captain's location. If acclaim is already there, place 2 Skunks instead. In a forest, place only the Skunk (`faction:knaves$18.5.1.4.5`).
  - **Gift** (`item:coin`): In a clearing, place 1 acclaim and draw 1 card. If acclaim is already there, draw 2 cards instead. In a forest, draw 1 card only (`faction:knaves$18.5.1.4.6`).
  - **Serve** (`item:hammer`): In a clearing, place 1 acclaim. If acclaim is already there, activate any number of acclaim in that clearing to craft cards (each acclaim once per turn). You do score the listed VP (`faction:knaves$18.5.1.4.7`).

**Action ordering matters.** Because item actions cost one of your four actions each, plan the sequence. Moving into position (Move or Dash) should precede Battle or item-battle actions. Revel or Gift are often best last — you have already committed the Captain's location.

**Retire** (`faction:knaves$18.5.2`): Flip the Captain card face down and return it to your supply. This ends your Daylight. The Captain is now unavailable until its turn in the cycle comes around again — all three Captain cards must be face down before Take It Easy can trigger (`faction:knaves$18.6.3`).

### Evening

In order:

1. **Mock the Powerful** (`faction:knaves$18.6.1`): Score 1 VP per 2 Prisoners and 1 VP per 2 acclaim on the map. Round down for each separately — 3 Prisoners scores 1, not 1.5.

2. **Protect the Weak** (`faction:knaves$18.6.2`): For each acclaim on the map, you may spend one matching card to place 1 Skunk at that acclaim's clearing. This is your primary Skunk resupply mechanism outside of Revel. It also functions as a card sink for surplus hand cards.

3. **Take It Easy** (`faction:knaves$18.6.3`): If — and only if — all three Captain cards are face down in your supply: flip all three face up, flip all items in your Stash face up, and the enemy with the most Prisoners may remove all of their faction's Prisoners from adjacent forests and place them into a clearing of their choice. On a tie, you choose which tied enemy benefits.

   Take It Easy is both your refresh and your opponent's escape valve. Time it carefully: rushing all Captains through their actions to force a reset means a weaker scoring cycle on any individual turn. But holding Captains out lets enemies accumulate Prisoners and eventually earn a mass release.

4. **Draw and Discard** (`faction:knaves$18.6.4`): Draw one card. Discard down to five if needed.

---

## Scoring Engine

| VP Source | Amount | Trigger | Timing |
|---|---|---|---|
| Prisoners | 1 per 2 Prisoners in forests | Counted at Mock the Powerful | Evening, step 1 |
| Acclaim | 1 per 2 acclaim on map | Counted at Mock the Powerful | Evening, step 1 |
| Crafted items via Serve | Listed VP on card | Craft resolves | Daylight |
| Enemy buildings/tokens removed in battle | 1 VP each | Standard removal rule (`rule:3.2.1`) | Whenever removed |

**Maximum theoretical Evening scoring.** 8 acclaim = 4 VP from that channel. Prisoner count has no hard cap — the only limit is how many forests are adjacent to your active clearings, and each forest holds one Prisoner group (though multiple Assault hits per battle go to separate forests). In practice, 6–10 Prisoners is a realistic sustained position, yielding 3–5 VP per Evening alongside the acclaim channel.

---

## Playbook

### Opening (Turns 1–2)

Your first priority is getting Captains out of their starting forests and into clearings. Until a Captain is in a clearing, it cannot place acclaim or generate Prisoners.

On turn 1 with most Captain loadouts, your four actions will be spent approximately: Move into a clearing (1 action), then either Battle to start a Prisoner and earn acclaim from Have at Thee (1 action), or use an item action to place acclaim and a Skunk via Revel (1 action), then either move again or Filch if there is something worth taking. The goal is to have at least 2 acclaim on the map and 1–2 Prisoners by the end of turn 1.

Keep Captains separated across different parts of the map. Clustering them wastes the faction's distributed pressure model: you have three independent action generators, and they are most useful when each is threatening different enemies in different areas.

**Captain prioritization.** On your first cycle you will use each Captain once before Take It Easy triggers. Decide in advance which Captain will be most aggressive (combat loadout, goes earlier), which will spread acclaim (economy loadout, goes second), and which will do utility work (mobility loadout, can go last with a weaker action count if needed).

### Mid-Game Pivots

**When your Prisoner count exceeds 4 and your acclaim coverage is thin:** enemies are getting 2+ VP per Evening from Mock the Powerful, but you have nothing to show from acclaim. Pivot to actively spreading acclaim — use Revel and Gift with whatever Captain acts next, and prioritize Have at Thee battles in currently unacclaimed clearings.

**When a dominant faction is pulling ahead:** target their warriors specifically with Assault. Assault takes all hit warriors as Prisoners, not just one (`faction:knaves$18.5.1.4.2`). Hitting a clearing with 3 warriors in one Assault battle can gut a faction's presence in an area while simultaneously loading you with 3 Prisoners and potentially 1.5 VP per Evening from them alone.

**When Take It Easy is imminent:** evaluate whether it is worth triggering this turn or postponing. Postpone if the leader has many Prisoners and would get a large free release — wait until they have been reduced or their Prisoner count drops. Trigger if your items are depleted and you need Captains or items back badly enough that the enemy release is an acceptable cost.

**When your Skunks are nearly exhausted:** Protect the Weak (`faction:knaves$18.6.2`) and Revel (`faction:knaves$18.5.1.4.5`) rebuild them, but only if you have matching cards or in-position acclaim. If Skunk supply is empty, Run Away no longer triggers (`faction:knaves$18.2.7`), and your Captains have no buffer in combat — a Captain can be hit directly. Refresh Skunks before this becomes a problem.

### Endgame Routes

**Acclaim-rush close.** If you have 6–8 acclaim on the map and 4–6 Prisoners, you are scoring 5–7 VP per Evening. At this rate, 30 VP is reachable within two to three more cycles. Opponents who begin removing acclaim aggressively are a signal that they fear this close: respond by maintaining at least four clearings covered even if others are stripped, since four acclaim still earns 2 VP per Evening and the Skunks generated by Run Away give you board presence to reclaim cleared spots.

**Battle-burst close.** Assault with a full Stash and combat-loaded Captain against a high-warrior clearing can spike your Prisoner count by 3–5 in a single action. Combine with an existing acclaim spread to generate a 6–8 VP Evening immediately. This is harder to set up but more resistant to disruption because it happens in one turn.

**Serve crafting contribution.** Serve is a secondary VP channel, not a primary win route. It contributes most when you are sitting on 2+ acclaim in a single suit clearing and have matching cards to spend. Tinker (`card:ROOT-298 (Homeland)`) draws a card after each Serve, which can chain into additional crafts or Protect the Weak spending in the same Evening — a small but real engine if you lean into it.

---

## Threat Factions

### Marquise de Cat

The Marquise's buildings fill clearing slots and establish control across many clearings early (`rule:6.`). This threatens you in two ways. First, cleared-slot clearings are where you want to spread acclaim, and a Marquise-controlled board tends to have many warriors there — you can raid them and earn Prisoners, but entering those clearings is costly. Second, if the Marquise's Keep is active (`rule:6.2.2`), placing sympathy or other tokens in the Keep clearing is blocked, though acclaim is neither sympathy nor a building — acclaim placement itself is not blocked by the Keep's restriction (which prevents enemies placing pieces via "place," and acclaim placement counts as piece placement; verify at table). Prioritize Assaulting Marquise warrior clusters to swing both Prisoner count and board control simultaneously.

### Eyrie Dynasties

The Eyrie's Decree demands they battle (`rule:7.5.2`), which means their warriors move aggressively and they will frequently contest clearings you have acclaim in. Turmoil wipes their Decree (`rule:7.7`), so applying pressure that forces them to expand their Decree beyond what they can sustain is an indirect counter. More directly: the Eyrie accumulates warriors quickly via Recruit. Large Eyrie stacks are excellent Assault targets — harvesting 3–4 Eyrie warriors from a single Assault battle can disrupt their board position while filling your Prisoner forests.

### Woodland Alliance

The Alliance's Sympathy tokens spread across the board (`rule:8.5.1`) and their Outrage ability (`rule:8.2.6`) punishes factions that move warriors into sympathetic clearings. You move Captains and Skunks frequently — Outrage will fire. Budget for the card cost. Worse, Alliance Revolt actions build Bases (`rule:8.4.1`) and convert clearings into strongpoints you struggle to hold. You have no buildings to contest rule with, so the Alliance can earn board dominance in areas you rely on for acclaim spreading. Attack Alliance sympathy clearings to limit their spread, and use Have at Thee to trap Woodland warriors in forests rather than letting them reinforce.

### Lord of the Hundreds

The Hundred's Warlord (`rule:14.2.2`) and strong battlefield presence make them dangerous to engage carelessly. The Warlord cannot be taken as a Prisoner via Have at Thee — the FAQ confirms Favor cards do not remove the Warlord (`faq:favorvswarlord`), and by analogy the Warlord's own protection (`rule:14.2.2`) means hits to the Hundreds in battle let the Hundreds player choose whether the Warlord absorbs a hit. Assault battles against the Hundreds can inadvertently waste actions on a protected piece. Prefer targeting Hundreds warriors outside the Warlord's clearing, and use Nab to stay mobile when forced to engage near the Warlord.

---

## Card Priorities

### Craftable Card Tiers

**Top priorities:**

- **Cobbler** (`card:ROOT-60 (Base Game)`): An extra move at start of Evening is powerful for repositioning a Captain after scoring without spending a Daylight action.
- **Command Warren** (`card:ROOT-63 (Base Game)`): A free battle at start of Daylight, before Captain Acts. This effectively gives you a fifth action when the battle is worth taking.
- **Stand and Deliver!** (`card:ROOT-102 (Base Game)`): Once per Birdsong, take a random card from an enemy. You operate with a thin hand (max five, draw one per turn, spend on Protect the Weak). Card advantage is scarce — this persistent engine is valuable.
- **Better Burrow Bank** (`card:ROOT-55 (Base Game)`): Once per Birdsong, draw a card and give one to an enemy. Net neutral on cards, but timing control is useful. Less critical than Stand and Deliver but worth holding.
- **Scouting Party** (`card:ROOT-95 (Base Game)`): Immunity to ambushes as attacker. Because you battle frequently, this removes a real risk. Your Captains are hard to remove (Skunks buffer them) but ambush hits can still remove supporting Skunks.

**Situational:**

- **Armorers** (`card:ROOT-51 (Base Game)`): Ignore all rolled hits taken as defender. Useful in reactive positions. Less impactful when you are the attacker, which you should be most of the time.
- **Brutal Tactics** (`card:ROOT-58 (Base Game)`): Extra hit as attacker but scores a point for the defender. Acceptable when the extra hit decisively clears a blocking Skunk or captures a critical warrior.
- **Tax Collector** (`card:ROOT-105 (Base Game)`): Remove one of your own warriors to draw a card. Skunks are a resource, but if you have surplus in a low-priority clearing this is workable card draw.
- **Royal Claim** (`card:ROOT-92 (Base Game)`): Score VP equal to clearings you rule at Birdsong. Situational: you have no buildings, so ruling requires warrior density. Hard to execute reliably but occasionally strong if you have Skunks spread across contested clearings.

**Generally skip:**

- **Favor of the Foxes / Mice / Rabbits** (`card:ROOT-73`, `ROOT-74`, `ROOT-75`, all Base Game): These clear all enemy pieces from their suit's clearings. They also remove your own acclaim if it is in those clearings — a serious self-inflicted wound if you are trying to maintain the acclaim channel. Use only in desperation or when you have no acclaim in the targeted suit.

### Ambush Guidance

Hold ambush cards defensively. You battle often as the attacker, meaning enemies will frequently have the opportunity to ambush you. An ambush in your hand lets you foil theirs (`rule:4.3.1.1`). Spending ambush cards proactively as suit-fillers for Protect the Weak is often wrong unless you have a surplus.

### Dominance Considerations

Dominance is viable once you have reached 10 VP (`rule:3.3.1`). Fox dominance is arguably the most achievable — you need three fox clearings, and Skunks can hold them if you concentrate. Bird dominance (two opposite corners) is harder without buildings. The key risk: you cannot score VP after activating a dominance card, so your Prisoner and acclaim VP channels go dark. Transition only if you can realistically achieve the win condition within 2–3 turns with your existing board position.

---

## Common Pitfalls

- **Keeping all three Captains bunched.** The faction's power lies in three independent vectors of pressure. Captains in adjacent areas trample on each other's Prisoner forests and compete for the same acclaim slots. Spread them.

- **Letting the Stash run dry before Take It Easy.** All six items face down means you have no item actions available until the refresh. Face-down items are powerful — Assault, Skirmish, Dash each add a full extra action equivalent. Burning them all in one rush for a single Captain leaves the other two Captains mechanically weaker for their turns.

- **Forgetting that Take It Easy is conditional on all three Captains being Retired.** Players occasionally try to trigger Take It Easy on an evening where one Captain has not yet been Used. The text is explicit: all three Captain cards must be face down (`faction:knaves$18.6.3`). If you miss using a Captain in a cycle, you are delaying your own refresh.

- **Scoring only one VP channel.** Running acclaim with zero Prisoners (or vice versa) makes Mock the Powerful weak. With only acclaim, your ceiling is 4 VP per Evening; with only Prisoners, your ceiling depends entirely on forest logistics. The scoring formula is designed to reward both channels simultaneously.

- **Placing acclaim in suits you cannot card-match for Protect the Weak.** Protect the Weak lets you place Skunks cheaply by spending matching cards (`faction:knaves$18.6.2`). If all your acclaim is in fox clearings and your hand is all mouse cards, you get no Skunks from Protect the Weak. Align your acclaim placements to your hand composition when possible, or use Gift (`faction:knaves$18.5.1.4.6`) to draw into matching suits.

- **Ignoring Captain loss risk.** Captains without Skunk cover can be hit directly (`faction:knaves$18.2.5`). A lost Captain returns with only three actions on its re-entry turn (`rule:18.4`), costing you one action for the whole cycle. Worse, re-entry removes Prisoners from the placement forest and adjacent forests — you may lose Prisoners you need for scoring.

- **Using Filch when Serve would score VP.** Filch lets you craft an item but gives you zero listed VP (`faction:knaves$18.5.1.3`). Serve crafting does score (`faction:knaves$18.5.1.4.7`). If you have acclaim already in the Acting Captain's clearing, Serve is usually superior. Reserve Filch for turns when you need a specific item from an enemy or there is no acclaim in position for Serve.

---

## Mechanic Clarifications

### Can a Captain move from a clearing it does not rule?

Yes. Deepwood Runners (`faction:knaves$18.2.4`) exempts Captains and Skunks from `rule:4.2.1`'s requirement that you rule the origin, destination, or both. They may move from any clearing they occupy regardless of rule.

### Can Skunks move independently, without a Captain?

Standard Knaves Daylight has no action that moves Skunks alone. Skunks move via Follow Me when accompanying a Captain (`faction:knaves$18.2.5`), or they are placed in clearings via Revel (`faction:knaves$18.5.1.4.5`) and Protect the Weak (`faction:knaves$18.6.2`). No explicit action grants a standalone Skunk move.

### Does Have at Thee trigger on both Battle and item-battle actions?

Have at Thee (`faction:knaves$18.2.6`) specifies "When a Captain attacks a faction in battle." Battle is initiated by Battle (`faction:knaves$18.5.1.2`), Assault (`faction:knaves$18.5.1.4.2`), Skirmish (`faction:knaves$18.5.1.4.3`), and Nab (`faction:knaves$18.5.1.4.4`). Assault's own text references `rule:18.2.6` directly, confirming Assault uses the Have at Thee Prisoner-capture mechanic (though Assault takes *all* hit warriors, not just one). Skirmish and Nab initiate a battle, so Have at Thee's "takes 1 warrior as Prisoner" applies to those battles as well — except that Assault's text overrides Have at Thee's "1 warrior" limit with "all warriors you hit."

**Resolution:** On a plain Battle action, Have at Thee takes 1 defending warrior as Prisoner. On an Assault, all hit warriors become Prisoners. Skirmish and Nab use Have at Thee's standard 1-warrior capture. Cite `rule:1.1` (faction rules override general rules when both cannot be followed).

### When a Captain is placed via Ready into a forest, which Prisoners are removed?

The rule states: remove any Prisoners in that forest and adjacent forests (`rule:18.4`). "Adjacent" for a forest means the clearings that touch it without crossing a printed path, and forests separated by only one printed path (`rule:2.4.1`). This can clear a wide zone of Prisoners depending on the forest chosen. Be deliberate about where you place a returning Captain.

### Can I use Take It Easy mid-round (not in Evening)?

No. Take It Easy is the third step of Evening (`faction:knaves$18.6.3`). It does not trigger outside Evening even if all three Captain cards happen to be face down at some other point in the round (which is unusual since Captains are Retired in Daylight and readied in Birdsong, but clarifying anyway). The refresh only happens at Evening step 3.

### Can I activate acclaim in a clearing I am not in?

Only via Serve (`faction:knaves$18.5.1.4.7`), and only acclaim matching the Acting Captain's current clearing. You cannot activate acclaim tokens remotely. Filch activates only the Acting Captain's own clearing, not distant tokens.

---

## Reference Index

**Faction citation key.** `faction:knaves`

**Primary rule section.** `rule:18.`

**Glossary items referenced.**
- `item:boot` — Dash action
- `item:sword` — Assault action
- `item:crossbow` — Skirmish action
- `item:sack` — Nab action
- `item:tea` — Revel action
- `item:coin` — Gift action
- `item:hammer` — Serve action

**Captain cards.** Twelve Captains are listed in appendix K of `rule:18.`. Their faction card IDs are `card:ROOT-288 (Homeland)` through `card:ROOT-299 (Homeland)`.

**Hireling form.** No dedicated Knaves hireling exists in the p16 card data.

**Cross-faction interactions.**
- Vagabond: mutual exclusion (`faction:knaves$18.2.1`). No Knaves game includes any Vagabond.
- Woodland Alliance Outrage (`rule:8.2.6`): Moving Knaves warriors into sympathetic clearings triggers Outrage. Captains and Skunks are warriors; they trigger Outrage on entry.
- Hirelings general interaction (`rule:16.4.3`): Hireling warriors are not faction pieces. Have at Thee captures "defending warrior" — it captures enemy warriors, which includes hireling warriors controlled by other players (they are enemies to you). Confirm at table whether the Prisoner placement applies normally to hireling warriors.
- Lord of the Hundreds Warlord (`rule:14.2.2`): The Warlord can absorb hits at the Hundreds player's discretion. Assault battles against the Hundreds may result in the Warlord being taken as a Prisoner; the FAQ addresses who chooses hit assignment in battle (`faq:whoassignshits`) — the defending player does. So the Hundreds player can choose to have their Warlord absorb a hit rather than regular warriors if they prefer.
