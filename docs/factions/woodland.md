# Woodland Alliance

## At a Glance

The Woodland Alliance is a slow-building insurgency that wins by spreading sympathy tokens across the map and cashing in large VP totals from revolts, while turning every attack against it into more fuel.

- **Identity**: Sympathy-token scorer that punishes aggression, builds through Outrage, and gains military flexibility from bases and officers.
- **Reach**: Low (starts with no pieces on the map; depends on adjacency for early expansion).
- **Complexity**: Medium. The core loop is readable, but supporter management, timing revolts versus spreading sympathy, and officer optimization reward experience.
- **Setup**: No pieces on the map at game start. Starts with 3 supporters from an opening draw. `faction:woodland$8.3`
- **Color**: Green.
- **Faction icon**: `faction-woodland`.
- **Faction citation key**: `faction:woodland`.
- **Primary rule section**: `rule:8.`

---

## Win Condition

You win by reaching 30 VP. `rule:3.1`

Your primary VP engine is the Sympathy track on your faction board. Each time you place a sympathy token — whether via Spread Sympathy or Organize — you uncover and score the VP printed on that space. `faction:woodland$8.4.2.3``faction:woodland$8.6.1.4` The track is progressive: early tokens score 1 VP each, and later placements score increasingly more as you approach a map saturated with sympathy. Ten tokens in total, ten placements possible. `faction:woodland$8.2.5`

Your secondary engine is revolts. A revolt removes all enemy pieces from a clearing, scores 1 VP per enemy building or token removed, and places a base. `faction:woodland$8.4.1.3``rule:3.2.1` A well-timed revolt against a dense position can yield 3–5 VP in a single Birdsong action.

**Dominance path.** You can activate a dominance card once you have at least 10 VP, replacing the VP race with a board-control condition. `rule:3.3.1` Fox, Bunny, and Mouse dominance require you to rule three clearings of the matching suit; Bird dominance requires you to rule two opposite corner clearings. `rule:3.3.1.1``rule:3.3.1.2` Dominance is situational for the Alliance — you typically win via points faster than you can muscle the board — but it remains a live threat that can influence how opponents move against you.

**Scoring tempo: slow-burn into burst.** Your first few turns generate VP in small increments (1 VP per early sympathy placement). Once you have a base and a few sympathetic clearings, a single revolt plus several Organize actions in Evening can spike 8–10 VP in two or three rounds. The table must either interrupt you early or deal with a nearly unstoppable endgame.

---

## Setup

### Walkthrough

1. **Gather warriors.** Form a supply of 10 warriors. `faction:woodland$8.3.1`
2. **Place bases.** Place all 3 bases on their respective spaces in the Bases box on your faction board. No bases go on the map at game start. `faction:woodland$8.3.2`
3. **Fill sympathy track.** Place all 10 sympathy tokens on your Sympathy track. None go on the map at game start. `faction:woodland$8.3.3`
4. **Gain supporters.** Draw 3 cards and place them face down on your Supporters stack. `faction:woodland$8.3.4`

You begin the game with no pieces on the map. Your opening presence is entirely intangible: three supporters, a hand of cards drawn during Advanced Setup, and the threat of what you can do once sympathy tokens reach the map.

### Setup theory

**Corner choice.** Unlike the Marquise or Eyrie, you are not constrained to a corner by a keep or roost. You begin without map presence, so your "starting position" is whatever clearing you first place sympathy into during turn 1. Prioritize your starting Spread Sympathy target over worrying about corner assignments. Choose a clearing that lets you reach multiple suits quickly and that is not already locked behind three enemy warriors (Martial Law applies immediately `faction:woodland$8.4.2.2.1`).

**Neighbor considerations.** You want at least one major military faction — Marquise, Eyrie, or Lord of the Hundreds — in the game. Their expansion activity generates Outrage triggers, funneling cards to your Supporters stack without any action on your part. `faction:woodland$8.2.6` A table with only low-aggression factions starves your supporter income. You would rather sit next to an active Marquise than across the map from one.

**Opening hand priorities.** After drawing your initial hand, look at what you drew for supporters and what remains in your hand. Cards that match your intended first sympathy target are worth mobilizing on turn 1. Ambush cards and high-value craftables are worth keeping in hand. Everything else is a candidate for mobilization. You do not need a large hand to start — your Supporters stack is your real resource, and hand cards above two or three are diminishing returns early.

---

## Faction Rules and Abilities

### Crafting

You craft during Daylight by activating sympathy tokens. `faction:woodland$8.2.1` A token's suit matches the clearing it occupies. `rule:4.1.1` Each sympathy token may be activated only once per turn. This means your crafting capacity scales directly with your board presence. Zero sympathy on the map means zero crafting. Ten tokens across three suits means meaningful multi-suit access.

Crafting does not move or remove the sympathy token. Activating is simply pointing at it. `faq:activating-crafting`

### Guerrilla War

As the defender in battle, you deal hits equal to the higher roll, and the attacker deals hits equal to the lower roll. `faction:woodland$8.2.2` Normal battle rules are reversed for you on defense: where other factions deal the higher roll when attacking, attackers against you are punished by taking the high number and giving you the low result.

This makes attacking your warriors statistically miserable for opponents. When an opponent attacks with two warriors and rolls a 2 and a 1, you score 2 hits and they score 1. When they roll two 0s, they still score 0 and you still score 0 — but with only two warriors in a clearing, this is the ceiling anyway. The practical result is that a three-warrior defended clearing requires multiple attacks to clear, each costing the attacker more than expected.

Guerrilla War does not affect battles you initiate — you are the attacker there, and normal rules apply. `rule:4.3.3`

### The Supporters Stack

The Supporters stack is a private pool of cards separate from your hand. `faction:woodland$8.2.3` Supporters are spent by suit to take various actions (Revolt, Spread Sympathy, Train). They do not count against your hand size limit. You may inspect them at any time, but they are face down to other players.

**Capacity.** If you have no bases on the map, the Supporters stack can hold at most five cards. If a card would overflow the stack, it is discarded. Once any base is on the map, the Supporters stack is unlimited. `faction:woodland$8.2.3.1`

This capacity rule is the principal reason getting a first base out quickly matters so much. Until you have a base, every supporter above five is wasted — and Outrage income can easily push you past five if you are not spending.

### Removing Bases

When a base is removed, you lose ground fast. `faction:woodland$8.2.4` You must:

1. Discard all supporters matching the clearing of that base (including birds).
2. Remove half your officers, rounded up.
3. If you now have no bases on the map and more than five supporters, discard down to five.

A single base removal can collapse your officer count from four to two, halving your Evening actions. Combined with the matching-suit supporter purge, a successfully destroyed base often sets you back two to three turns of progress. Opponents know this — expect base destruction to be a coordinated priority at the table once you have two or more officers.

### Sympathy Tokens

You have 10 sympathy tokens. A clearing can hold only one. `faction:woodland$8.2.5``faction:woodland$8.2.5.1`

A clearing with a sympathy token is a **sympathetic clearing**. A clearing without one is an **unsympathetic clearing**. `faction:woodland$8.2.5.2` These terms matter for Revolt (which requires a sympathetic clearing `faction:woodland$8.4.1.1`), Spread Sympathy (which targets unsympathetic clearings `faction:woodland$8.4.2.1`), and Organize (which places into an unsympathetic clearing `faction:woodland$8.6.1.4`).

### Outrage

Whenever another player removes a sympathy token or moves any warriors into a sympathetic clearing, that player must give you one card matching the affected clearing from their hand. `faction:woodland$8.2.6` If they have no matching card (and no bird), they show you their hand and you draw one card from the deck for your Supporters stack.

Key details:

- **Placement does not trigger Outrage.** Only moving warriors or removing the token triggers it. `faq:placing-sympathetic-clearing`
- **The Vagabond does not trigger Outrage by moving.** The Vagabond uses a pawn, not a warrior. Removing a token still triggers it. `faq:vagabond-outrage``faq:vagabond-outrage-move`
- **Allied Vagabond movement does not trigger Outrage.** When the Vagabond forces allied warriors to move, it uses the Force keyword, which changed as of the Marauder Expansion (8th Printing). `faq:vagabond-allied-outrage`
- **Hirelings trigger Outrage.** When a hireling under another player's control removes sympathy or moves warriors into a sympathetic clearing, the controlling player triggers Outrage. `faq:hireling-outrage``rule:8.2.6`

Outrage is the reason you are not entirely passive in the early game. Every opponent who expands into sympathetic clearings feeds your engine.

---

## Turn Structure

### Birdsong

Your Birdsong has two steps in this order: first Revolt, then Spread Sympathy. `faction:woodland$8.4`

**Revolt.** You may take this any number of times. `faction:woodland$8.4.1` For each revolt:

1. Choose a sympathetic clearing that has no base and that matches a base type still on your faction board. `faction:woodland$8.4.1.1` (You cannot revolt a suit whose base you have already placed. `faq:revolt-existing-base`)
2. Spend two supporters matching the clearing's suit. `faction:woodland$8.4.1.2`
3. Remove all enemy pieces from the clearing. Place the matching base there. Place warriors equal to the number of sympathetic clearings matching the base's suit. Add one warrior to the Officers box — it is now an officer. Score 1 VP per enemy building or token removed during this step. `faction:woodland$8.4.1.3``rule:3.2.1`

Revolt happens at the start of your turn, before most opponents can react. A revolt in a clearing with three enemy buildings scores 3 extra VP before you have even placed sympathy.

Note: You cannot revolt in a clearing with the Marquise's keep token, because you cannot place a sympathy token there in the first place. `faq:revolt-keep``rule:6.2.2`

**Spread Sympathy.** You may take this any number of times. `faction:woodland$8.4.2` For each:

1. Choose an unsympathetic clearing adjacent to a sympathetic clearing. If no sympathetic clearings exist anywhere, you may choose any clearing. `faction:woodland$8.4.2.1`
2. Spend supporters matching the suit of the chosen clearing. The number required is printed above the sympathy track space being uncovered. `faction:woodland$8.4.2.2` If the target clearing contains at least 3 warriors belonging to another player (including warriors they treat as their own — Mercenaries, hirelings, etc.), pay one additional supporter of the same suit. This is Martial Law. `faction:woodland$8.4.2.2.1`
3. Place the sympathy token and score the VP printed on the uncovered space. `faction:woodland$8.4.2.3`

Early placements cost 1 supporter; later placements cost more as the track fills. Martial Law adds one card to those costs. A clearing with 3+ enemy warriors is not impassable, but you pay extra for it.

### Daylight

You may take these actions in any order and number. `faction:woodland$8.5`

**Craft.** Activate sympathy tokens to craft a card from your hand. `faction:woodland$8.5.1` Each token may be activated once per turn. `rule:4.1.1`

**Mobilize.** Add a card from your hand to the Supporters stack. `faction:woodland$8.5.2` This is how you voluntarily build supporter reserves. There is no limit to how often you do this per turn and no cost beyond the card itself.

**Train.** Spend a card whose suit matches the clearing of a base you have on the map to place one warrior in the Officers box as an officer. `faction:woodland$8.5.3` You may do this multiple times per turn, limited only by your hand size and how many matching cards you have.

Daylight is where you convert your hand into future action capacity. A Mobilize turn feeds revolts and sympathy spreading; a Train turn buys Evening actions. Both compete for the same hand cards.

### Evening

Your Evening has two steps in order: Military Operations, then Draw and Discard. `faction:woodland$8.6`

**Military Operations.** You may take up to your total number of officers worth of actions, in any order and number. `faction:woodland$8.6.1` Your officers count is the number of warriors in your Officers box.

Available actions per officer token spent:

- **Move.** Take one move. You must rule the origin, destination, or both. `faction:woodland$8.6.1.1``rule:4.2.1`
- **Battle.** Initiate a battle. `faction:woodland$8.6.1.2`
- **Recruit.** Place one warrior in any clearing that has one of your bases. `faction:woodland$8.6.1.3`
- **Organize.** Remove one of your warriors from an unsympathetic clearing. Place a sympathy token there, then score the VP on the uncovered track space. `faction:woodland$8.6.1.4`

Officers are not spent or removed when you take actions — the count is the ceiling on how many actions you can take this Evening. A faction board with four officers means four Evening actions.

Organize is the key late-game action. It converts warriors you have moved into position into sympathy tokens, independently of the supporter cost you would pay in Birdsong. A warrior sitting in a heavily contested clearing costs you one officer action to convert into a sympathy — no supporters required, and it still scores VP.

**Draw and Discard.** Draw one card, plus one per uncovered draw bonus. If you hold more than five cards after drawing, discard down to five. `faction:woodland$8.6.2`

---

## Scoring Engine

| VP Source | Amount | Trigger | Timing |
|---|---|---|---|
| Spread Sympathy | Printed on faction board track (scales up with each token placed) | Each sympathy placement | Birdsong (Spread Sympathy step 3) |
| Organize | Printed on faction board track | Each sympathy placement via Organize | Evening (Military Operations) |
| Revolt — enemy buildings/tokens removed | 1 VP per building or token | Removing enemy pieces during revolt | Birdsong (Revolt step 3) |
| Revolt — general removal scoring | 1 VP per enemy building or token | Any removal you cause, including during revolt | Instantaneous on removal `rule:3.2.1` |
| Crafting items | Listed on card | Crafting a card with an item | Daylight (Craft) |

The Sympathy track VP values escalate: early tokens (positions 1–3) score 1 VP each; mid-track tokens score 2 VP each; the final placements score 3 or 4 VP each. The exact values are printed on the faction board. Total possible VP from the full track is 22 points.

Reaching 30 VP typically requires combining full or near-full sympathy track completion with several VP-generating revolts. Crafting items provides supplementary points rather than the backbone.

---

## Playbook

### Opening

Your turn-1 goal is a sympathy token on the map. Without one, you cannot spread adjacently, cannot revolt, and cannot craft.

With three supporters from setup and a starting hand, assess what suits you have access to. Mobilize any card you do not plan to craft or use as an ambush, then Spread Sympathy into the cheapest available clearing (1 supporter for the first token). Score 1 VP.

Choose your first target in a clearing that:
1. You can afford (you have the matching suit in supporters).
2. Is in or adjacent to a high-traffic area, to maximize future Outrage income.
3. Is not under Martial Law — 3 enemy warriors means you pay an extra supporter before you even have income.

Turn 1 is about getting on the board. Turn 2 is about whether you can set up a revolt. To revolt, you need two matching supporters and a sympathetic clearing of the matching suit. If your second turn sees enough Outrage from the previous player's movement, you may have supporters enough to place a second sympathy token and position for a revolt in Birdsong of turn 3.

Some players aim to have a first base by turn 3 or 4, unlocking the unlimited supporter cap and adding an officer. Community consensus around online play (based on sources from 2018–2023, which may not reflect the most current meta) suggests that early revolt pressure discourages opponents from massing in your sympathy clearings.

### Mid-game pivots

The mid-game inflection point is reaching two bases. With two bases you have:
- Two suits' worth of unlimited supporter capacity.
- Two or more officers from revolt plus any training.
- Enough VP momentum that opponents must respond.

If a base comes under threat, shift your supporters to protect it. Losing a base costs you half your officers (rounded up) and purges an entire suit of supporters. That can reverse a turn of progress.

Watch for two signals to shift strategy:

1. **Opponents cluster near your bases.** If 4+ enemy warriors ring a base clearing, direct defense becomes costly. Consider whether your Evening actions are better spent Organizing sympathy into the surrounding clearings than trying to hold the base clearing itself. Force opponents to choose between attacking your base (expensive, due to Guerrilla War) and chasing sympathy tokens elsewhere.

2. **You have 3+ officers.** At this level, every Evening you can Move, Organize, Recruit, and still have an action left over. This is when the Organize engine starts running faster than opponents can suppress sympathy tokens. Some players argue that reaching four officers is the point of no return for the Alliance — opponents who wait until this stage to suppress usually lose the race.

### Endgame routes

From 20 VP, you need 10 more. Common finishing patterns:

- **Full sympathy coverage.** With seven or eight tokens already placed, the remaining two or three track positions each score 3–4 VP. A two-action Evening (Move + Organize) plus a Spread Sympathy in Birdsong can add 6–8 VP in a single turn.
- **Revolt spike.** A revolt into a clearing holding two or three buildings scores the removal points plus the base warriors and officer. Against Marquise or Eyrie, a single revolt into a dense clearing can score 4–6 VP and erase a major opponent's presence simultaneously.
- **Combine both.** Revolt in Birdsong for VP, then Organize in Evening for VP. With enough officers and supporters, a single turn can push from 20 to 29+.

If you are being suppressed — sympathy removed faster than you can replace it — shift to training officers and positioning warriors for concentrated Organize plays. The Organize action bypasses the supporter cost entirely, so even supporter-dry turns can still advance your VP track.

---

## Threat Factions

### Eyrie Dynasties

The Eyrie is your most dangerous recurring threat. With the Commander leader, the Eyrie attacks as both a strong attacker (extra hit `card:ROOT-2 (Base Game)`) and can accumulate enough Decree cards to systematically clear clearings each turn. The Eyrie benefits from Lords of the Forest, meaning they frequently rule clearings and can move freely; they will push through sympathetic clearings as a matter of routine expansion, feeding you Outrage income — but they can also be fast enough to pull a base down before you can reinforce.

More critically, the Eyrie can execute an Eyrie Emigre-style build-up that reaches your base clearing in just two or three turns of Decree movement. A committed anti-Alliance Eyrie bird can rotate a Commander into their Decree early and attack your base before you have more than two officers.

Counter-play: Make attacking your bases expensive. Three warriors in a base clearing means Guerrilla War costs the Eyrie two or three Decree recruits per assault. Craft Armorers (`card:ROOT-51 (Base Game)`) if you can — requiring an extra battle to break through a defended base is often enough to redirect the Eyrie toward other objectives.

### Marquise de Cat

The Marquise occupies the board densely, meaning Outrage triggers often. This is double-edged: you gain supporters, but the Marquise also has the most buildings to lose to revolts, which means they have strong incentive to suppress your sympathy early.

The Marquise's Field Hospitals (`rule:6.2.3`) let them return warriors removed by revolt back to their keep clearing rather than supply, which blunts your VP gain from revolt. You still score per building and token removed, but the Marquise recovers faster than other factions from a revolt.

The Marquise can also impose a near-permanent Martial Law condition on key clearings by stationing three warriors there. This costs you an extra supporter per spread, slowing your track.

Counter-play: Do not spread sympathy into Marquise-dense clearings until you have surplus supporters. Target their clearings for revolt rather than trying to hold sympathy there. The Marquise's buildings score you VP on revolt removal and deny them the economic recovery of a full building track.

### Lizard Cult

The Lizard Cult's Lost Souls mechanism collects cards from the discard pile by suit. The Cult can also remove sympathy tokens through Sanctify and Convert actions (replacing your token with a garden). Because the Cult spends Acolytes for actions but does not move warriors into clearings in the conventional sense, Outrage triggers are infrequent — you get less supporter income from the Cult than from Marquise or Eyrie.

Community sources from approximately 2023 characterize the Lizard Cult matchup as a net negative for the Alliance: the Cult can convert your sympathy tokens cheaply (triggering Outrage for supporters, but replacing the token with a Cult garden), and the Cult's passive income from Outcast suits can inadvertently benefit from your spreading into contested clearings.

Counter-play: Limit how much you place sympathy in clearings of a suit the Cult has marked as Outcast. Revolt into Cult clearings with gardens when possible — the garden removal scores you VP and damages their economy. Keep one base suit away from high-Cult-density areas if you can manage the board geometry.

### Lord of the Hundreds

The Warlord spreads mob tokens widely and benefits from scoring VP by oppressing clearings. Oppression scoring is passive and does not require attacking you — but the Warlord's Mob actions spread warriors broadly, triggering frequent Outrage and feeding your supporters substantially.

The Warlord's Looters ability (`rule:14.2.5`) means they can take cards from your hand on battle, not your Supporters stack. This still stings if they battle you, but does not directly drain supporters.

The primary risk: the Warlord's Seize action lets them move rapidly and place mobs, reaching your base clearing and mustering for an attack before your officer count catches up. A fast Warlord who stabilizes on five or six clearings can also run away in VP from oppression before you revolt into enough of their clearings.

Counter-play: Aim revolts at mob-heavy clearings. The Warlord's mobs are tokens, scoring you VP on revolt removal. With Guerrilla War, you are also an effective defender against Warlord attacks — do not yield a base clearing without a fight.

---

## Card Priorities

### Crafting priorities

**Top priorities:**

- **Armorers** (`card:ROOT-51 (Base Game)`) — Bird card, persistent. In battle, discard to ignore all rolled hits. Makes your defended bases nearly impervious for one fight: an opponent must deal two hits through an ambush before Armorers even enters play. Arguably the strongest single defensive crafting card for the Alliance.
- **Sappers** (`card:ROOT-94 (Base Game)`) — Bird card, persistent. As defender, discard for an extra hit. Combines with Guerrilla War for punishing returns: you roll the high die, deal an extra hit from Sappers, and the attacker still takes the low roll.
- **Command Warren** (`card:ROOT-63 (Base Game)`) — Bunny card, persistent. At start of Daylight, may initiate a battle. Gives you an attack action without spending an officer. Lets you use Evening entirely for Organize/Move/Recruit while still contesting clearings.
- **Better Burrow Bank** (`card:ROOT-55 (Base Game)`) — Bunny card, persistent. At start of Birdsong, may draw one card; if you do, choose an enemy to draw one card. Card economy is critical: more hand cards means more mobilization, more training, more options. The symmetric draw is an acceptable cost because you typically need cards more than your opponents do.

**Situational:**

- **Stand and Deliver!** (`card:ROOT-102 (Base Game)`) — Fox card, persistent. Once in Birdsong, take a random card from an enemy; they score 1 VP. Generates supporter income from any opponent's hand. Situationally strong when you are supporter-starved and need a specific suit.
- **Tax Collector** (`card:ROOT-105 (Base Game)`) — Fox card, persistent. Once in Daylight, remove one of your warriors from the map to draw a card. Useful to convert warriors you cannot otherwise deploy (no bases in their area) into card draw. Does not help your VP engine but keeps your hand healthy.
- **Cobbler** (`card:ROOT-60 (Base Game)`) — Bunny card, persistent. At start of Evening, take a move. Free movement independent of your officer count. Excellent if your officer count is low (one or two) and you need to reposition warriors for Organize plays.
- **Favor of the Foxes/Mice/Rabbits** (`card:ROOT-73 (Base Game)`, `card:ROOT-74 (Base Game)`, `card:ROOT-75 (Base Game)`) — Immediate effects. Remove all enemy pieces in clearings of the named suit. Does not score you VP directly, but clears a path for sympathy placement or revolt and often scores indirect VP via removed buildings and tokens. `rule:3.2.1`

**Lower priority:**

- **Brutal Tactics** (`card:ROOT-58 (Base Game)`) — Bird card, persistent. As attacker, deal an extra hit but defender scores 1 VP. You rarely want to be the attacker; Guerrilla War makes defending preferable. Brutal Tactics is counterproductive to your defensive posture.
- **Scouting Party** (`card:ROOT-95 (Base Game)`) — Mouse card, persistent. Ignore ambush cards as attacker. Same issue as Brutal Tactics: your power is on defense, not offense.

### Ambush hold/play guidance

Ambush cards serve you exceptionally well on defense due to Guerrilla War. When defending, you already take the high roll; an ambush deals two immediate hits before dice are even rolled (`rule:4.3.1.2`), which can end battles outright if the attacker has only one or two warriors. Hold ambush cards unless your hand is too large to fit into Evening discard limits.

As attacker you have no inherent ambush bonus — but using an ambush to foil a defender's ambush (`rule:4.3.1.1`) protects your assault in key revolts. If you are revolting into a clearing where an opponent might hold a matching ambush (especially Fox or Mouse — common suits in most hands), consider holding a matching foil.

### Dominance card considerations

Activating dominance requires 10 VP and removes you from the score track. `rule:3.3.1` The Alliance rarely needs to go this route because the sympathy track can push toward 30 VP faster than the board-control dominance condition can be secured. If three enemy factions are actively suppressing your sympathy and you cannot close the VP gap, Bird Dominance (rule two opposite corners) may offer a path out that does not depend on the track. Use it as a last resort or as a table-reads opportunity.

### Spending for activation vs. holding

Cards in hand above four are candidates for Mobilize unless you are holding them for a specific craft or ambush. A Supporters stack of two or three matching cards is a reasonable working reserve; more than five matching supporters in a single suit before you have a base is waste. After a base, you can hold deeper reserves — but only if you expect to need them (approaching a costly late-game revolt, or anticipating a major Outrage turn when opponents surge).

---

## Common Pitfalls

- **Spreading sympathy into Martial Law clearings before you can afford it.** Paying three supporters (two base plus one Martial Law) for a 1 VP token early game exhausts your hand and stalls revolts. Verify supporter counts before targeting enemy-dense clearings.

- **Not getting a base by turn 3–4.** With no base, your Supporters stack is capped at five cards. Outrage income during this window is wasted the moment it would push you to six. Prioritize your first revolt over perfect sympathy positioning.

- **Hoarding supporters without spending them.** Your hand cards count against your five-card limit at end of Evening; your Supporters stack (pre-base) also caps at five. Over-mobilizing without revolting or spreading wastes cards. Move cards through your system.

- **Ignoring officer count until the endgame.** Officers are turn actions. Two officers means two Evening actions; four means four. A single Train action in Daylight costs one card and adds one officer. Players who reach the endgame with two officers find themselves too slow to complete the sympathy track or execute final revolts before another faction wins.

- **Leaving bases undefended.** A base with zero warriors is defenseless against any opponent who can battle. The attacker gets an extra hit automatically (`rule:4.3.5.2`), meaning even a single attacking warrior destroys your base and triggers the Base Removal penalty. Keep at least two or three warriors in each base clearing.

- **Revolting too early in a vulnerable clearing.** A revolt that triggers before you have two or three officers leaves you with one fresh officer and warriors equal only to the sympathetic clearings of that suit. If the base clearing has few same-suit adjacencies, you arrive with one warrior. That base is gone before your next turn.

- **Attacking with Guerrilla War-capped positions.** Guerrilla War only applies when you are the defender. When you attack, you deal the higher roll — but so does the defender you are attacking, unless they are the Woodland Alliance themselves. Offensive plays with three warriors versus a three-warrior Eyrie clearing is a coin-flip, not the favorable trade you have on defense.

- **Losing both bases within two turns.** With no bases, you return to a five-supporter cap, lose all officers beyond two (if you had four, you drop to two), and lose any progress that the supporters were fueling. Recovery from a full board wipe is slow. If one base is threatened, consider whether sacrificing it is worth protecting the second, rather than fighting two separate defensive actions simultaneously.

---

## Mechanic Clarifications

### Does placing a piece in a sympathetic clearing trigger Outrage?

No. Outrage requires either (a) removing the sympathy token or (b) moving warriors into the clearing. Placing a piece does not trigger it. `faction:woodland$8.2.6``faq:placing-sympathetic-clearing`

### Does the Vagabond trigger Outrage by moving?

No. The Vagabond uses a pawn, not warriors. Moving the pawn into a sympathetic clearing does not trigger Outrage. However, if the Vagabond removes a sympathy token, the controlling player does trigger Outrage. `faq:vagabond-outrage``faq:vagabond-outrage-move`

### Do Allied Vagabond warriors trigger Outrage when moved?

No, as of the Marauder Expansion (8th Printing). Allied movement by the Vagabond now uses the Force keyword, which removes this trigger. `faction:woodland$8.2.6``rule:9.2.9``faq:vagabond-allied-outrage`

### Does a hireling under another player's control trigger Outrage?

Yes. Outrage specifies "when a player removes…" — the controlling player triggers Outrage when their controlled hireling moves into a sympathetic clearing or removes the token. `faction:woodland$8.2.6``rule:16.4.3.7``faq:hireling-outrage`

### Can I revolt in a suit I've already built a base for?

No. Revolt requires choosing a sympathetic clearing "without a base that matches a base on your faction board" — meaning an unbuilt base on your board. If you have already placed all three bases, you cannot revolt at all. `faction:woodland$8.4.1.1``faq:revolt-existing-base`

### Can I revolt in a clearing with the Marquise's keep?

No. You would need to place a sympathy token in that clearing first, and the Marquise's Keep prevents any player except the Marquise from placing pieces there. Since sympathy tokens are your pieces, you cannot place them in the keep clearing, and therefore can never satisfy the sympathetic clearing requirement for a revolt there. `rule:6.2.2``faq:revolt-keep`

### What happens when a base is removed — in what order?

When a base is removed: (1) discard all supporters matching the clearing's suit, including birds; (2) remove half your officers rounded up; (3) if you now have no bases and more than five supporters, discard to five. `faction:woodland$8.2.4` Effects are resolved in that order.

### What does "officers" mean mechanically?

Officers are warriors placed in the Officers box on your faction board. They are not on the map — they are an abstraction of military command capacity. Each warrior in the Officers box grants one Evening action under Military Operations. `faction:woodland$8.6.1` Warriors are added to the Officers box via Revolt (one per revolt `faction:woodland$8.4.1.3`) and Train (`faction:woodland$8.5.3`). They are removed when a base is destroyed (half rounded up `faction:woodland$8.2.4`).

### Can I take more Military Operations actions than I have officers?

No. You may take actions "up to your number of officers." `faction:woodland$8.6.1` If you have two warriors in your Officers box, you take at most two Evening actions.

### Can I Organize into a clearing that already has a sympathy token?

No. Organize places a sympathy token into an unsympathetic clearing. `faction:woodland$8.6.1.4` A clearing with a sympathy token is sympathetic and therefore ineligible.

---

## Reference Index

- **Faction citation key**: `faction:woodland`
- **Primary rule section**: `rule:8.`
- **Faction rules and abilities**: `rule:8.2`
  - Crafting: `faction:woodland$8.2.1`
  - Guerrilla War: `faction:woodland$8.2.2`
  - Supporters Stack: `faction:woodland$8.2.3`
  - Capacity: `faction:woodland$8.2.3.1`
  - Removing Bases: `faction:woodland$8.2.4`
  - Sympathy Tokens: `faction:woodland$8.2.5`
  - Outrage: `faction:woodland$8.2.6`
- **Faction Setup**: `rule:8.3`
- **Birdsong — Revolt**: `faction:woodland$8.4.1`
- **Birdsong — Spread Sympathy**: `faction:woodland$8.4.2`
  - Martial Law: `faction:woodland$8.4.2.2.1`
- **Daylight**: `rule:8.5`
  - Craft: `faction:woodland$8.5.1`
  - Mobilize: `faction:woodland$8.5.2`
  - Train: `faction:woodland$8.5.3`
- **Evening — Military Operations**: `faction:woodland$8.6.1`
  - Organize: `faction:woodland$8.6.1.4`
- **Evening — Draw and Discard**: `faction:woodland$8.6.2`

**Glossary cross-references:**
- `item:sympathy` (sympathy token as piece type)
- `item:supporters` (supporters as faction resource)

**Hireling form**: The Woodland Alliance has no hireling version in the base Law.

**Cross-faction interactions:**
- Vagabond + Outrage: `faction:woodland$8.2.6``rule:9.2.9` — Vagabond pawn does not trigger Outrage on move; removing sympathy does.
- Vagabond Allied movement: `rule:9.2.9``faq:vagabond-allied-outrage` — Force keyword prevents Outrage from Allied warrior movement.
- Hireling control + Outrage: `rule:16.4.3.7``faq:hireling-outrage` — Controlling player triggers.
- Marquise Keep + Revolt: `rule:6.2.2``faq:revolt-keep` — Keep clearing is immune to sympathy placement.
- Lizard Cult + Convert/Sanctify: Cult can remove sympathy tokens (triggering Outrage but replacing with gardens) via `rule:10.` actions.
- Dominance activation: `rule:3.3.1` — Available to the Alliance on the same 10 VP threshold as other factions.
