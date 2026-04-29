# Vagabond

## At a Glance

**Identity**: A lone pawn who scores through relationship management, quests, and opportunistic combat while immune to removal and unconstrained by ruling.

| Attribute | Value |
|---|---|
| Reach | 2 |
| Complexity | High |
| Scoring tempo | Steady with burst potential |
| Color | Gray (#6d6e70) |
| Icon | faction-vagabond |
| Faction citation key | `faction:vagabond` |
| Primary rule section | `rule:9.` |

**Setup constraints**: Place your pawn in any forest at the start of the game — no corner requirement, no adjacency rules, no building placement `faction:vagabond$9.3.2`. Your setup choices are almost entirely about which character you choose and which ruins you start near.

---

## Win Condition

### Standard 30 VP Route

Your points come from three streams that you control and can weight by character and situation:

1. **Relationship improvements** — each time you advance a faction's marker on the Allied track, you score the VP printed on the new space `faction:vagabond$9.2.9.1.2`. Getting four factions to Allied can net double digits from this source alone.
2. **Quests** — choose to score one VP per matching completed quest (including the one you just finished) or draw two cards `faction:vagabond$9.5.5`. The scoring option snowballs: your second matching quest scores 2, your third scores 3. Chaining same-suit quests is a core engine.
3. **Hostile combat** — Infamy adds one VP per piece of a Hostile faction you remove in battle on your turn (beyond the first warrior that triggered Hostility) `faction:vagabond$9.2.9.3.1`, plus the standard VP for removing buildings and tokens `rule:3.2.1`. A Hostile faction that fields buildings turns into a reliable point engine.
4. **Exploration** — score one VP each time you take an item from a ruin `faction:vagabond$9.5.3`.

There is no single dominant path. What you optimize depends on your character, the factions present, and who is running away with the board.

### Coalition Path (4+ Players Only)

If the table has four or more players, you can activate a dominance card during your Daylight — provided you have at least 10 VP at the time `rule:3.3.1` — and instead of claiming the dominance victory condition yourself, use the Vagabond-specific coalition rule `faction:vagabond$9.2.8`.

When you activate a dominance card as a coalition, you choose one other player (not already in a coalition, not currently on a dominance win path) who has fewer VP than every other player except you `faction:vagabond$9.2.8`. Place your score marker on their faction board. You no longer score points. If that player wins the game, you win too.

A coalition with a Hostile faction is permitted; doing so moves their relationship marker to Indifferent `faction:vagabond$9.2.9.3.4`. You also cannot form a coalition with a player who has already activated a dominance card, because they have no VP marker on the track `faq:coalition-dominance-player`.

The coalition path is situational. It requires reading the table well: you need a coalition partner who can plausibly win and who has a strong late-game trajectory. Community consensus from various online discussions treats it as a rarely-pursued backup rather than a primary plan, given that the Vagabond can often reach 30 VP faster by continuing solo play. That said, if you are behind and a strong player is being suppressed by others, forming a coalition buys you a legitimate path to win without exposing yourself to further attack.

### Scoring Tempo

Steady throughout — exploration and quests provide VP from turn 1 — with burst potential when you chain same-suit quests or go on a sustained Hostile rampage. You are not a slow-burn faction; you can spike unexpectedly when your quest pool aligns.

---

## Setup

### Step-by-Step Walkthrough

1. **Choose a character card** and place it in your Character Card slot `faction:vagabond$9.3.1`. Your character determines your starting items and Special Action. This is the most important decision you make in setup.
2. **Place your pawn in any forest** `faction:vagabond$9.3.2`. You start in a forest, which means you begin Slip-adjacent to several clearings simultaneously.
3. **Shuffle your quest deck**, draw 3 quest cards, and place them face up near you `faction:vagabond$9.3.3`.
4. **Populate the ruins**: take the 4 ruins from the map, collect the R-marked `item:sack`, `item:boot`, `item:hammer`, and `item:sword`. Place one beneath each ruin (shuffle each stack), then return each stack to an empty ruin slot on the map `faction:vagabond$9.3.4`.
5. **Take your starting items** as listed on your character card `faction:vagabond$9.3.5`. Tea, coin, and sack items go to their tracks; everything else goes face up in your Satchel. Return unused S-items to the box.
6. **Set all non-Vagabond faction markers to Indifferent** on your Relationships chart `faction:vagabond$9.3.6`.

### Forest Placement

Starting in a forest means you immediately have access to Slip (`faction:vagabond$9.4.2`) on your first Birdsong, reaching any adjacent clearing without spending a `item:boot`. Choose a forest that touches clearings with ruins — you want to explore early — and that sits near the center of anticipated conflict so Aid opportunities exist from turn 1.

If the board has a central forest, that is usually correct. Edge forests save movement costs when navigating Hostile territory later but cost you in early exploration range.

### Character Selection

This deserves extended treatment because your character is your build:

- **Tinker** (base game) starts with `item:boot`, `item:torch`, `item:sack`, `item:hammer`. Day Labor recovers any matching or bird card from the discard. Extra `item:hammer` access makes crafting Favor cards realistic. Community consensus marks this as the strongest base-game character, with some players arguing it approaches overpowered in open tables — note that this judgment reflects pre-p16 play and may be partially addressed by experienced player expectations rather than rule changes.
- **Thief** (base game) starts with `item:boot`, `item:torch`, `item:tea`, `item:sword`. Steal takes a random card from any player with pieces in your clearing. Card pressure against hand-intensive factions (Woodland Alliance, Lizard Cult) is real. The `item:tea` gives strong early Refresh, and starting with a `item:sword` means you can battle from turn 1.
- **Ranger** (base game) starts with `item:boot`, `item:torch`, `item:crossbow`, `item:sword`. Hideout repairs three items and then immediately ends Daylight — a panic button that also lets you recover mid-battle. Combat-oriented and forgiving of aggressive play.
- **Adventurer** (Vagabond Pack) starts with `item:boot`, `item:torch`, `item:hammer`. Improvise lets you treat any item as another once per turn while questing, at the cost of damaging it. Highly flexible; good for completing awkward quests.
- **Harrier** (Vagabond Pack) starts with `item:coin`, `item:torch`, `item:sword`, `item:crossbow`. Glide moves you to any clearing on the map, ignoring adjacency and Hostile penalties, by exhausting one `item:torch`. Exceptional mobility; coin provides extra draw.
- **Ronin** (Vagabond Pack) starts with `item:boot`, `item:boot`, `item:torch`, `item:sword`. Swift Strike exhausts a `item:sword` to deal an extra hit after rolling. The most straightforwardly combat-focused character.

### Opening Hand

Your opening hand should support whichever suit concentrations give you quest matches earliest. You want to avoid holding cards you cannot give away during Aid (because Aid requires giving a card matching your clearing). Broad-suit hands are easier to Aid from; bird-heavy hands can be difficult to spend. If you are playing Tinker, keeping one copy of a Favor card suits that are common on the board is worthwhile.

---

## Faction Rules and Abilities

### Lone Wanderer

Your pawn is not a warrior `faction:vagabond$9.2.2`. This means you cannot rule a clearing and cannot stop another player from ruling one. No faction ever gains a combat advantage from your presence the way they do from an opposing warrior stack. Your pawn also cannot be removed from the map under any circumstances.

**Full Removal edge case**: if an effect removes all enemy pieces from your clearing — such as a Favor of the Foxes card `card:ROOT-73 (Base Game)`, an Alliance revolt, or a Corvid bomb — you cannot be removed. Instead, you damage three items `faction:vagabond$9.2.2.1`. This is painful but survivable if your item pool is healthy.

### Nimble

You can move regardless of who rules your origin or destination clearing `faction:vagabond$9.2.3`. The standard requirement that you must rule one end of a move `rule:4.2.1` does not apply to you.

### Defenseless

As defender in battle, you are defenseless if you have no undamaged `item:sword` `faction:vagabond$9.2.4`. Defenseless means the attacker deals an extra hit `rule:4.3.5.2`. Keeping at least one undamaged sword in your Satchel prevents this bonus hit — do not let attrition strip you to zero swords before you can Repair.

### Items and the Satchel

Your capabilities run on items. Items can be face up (ready) or face down (exhausted). You exhaust face-up undamaged items to take actions, flipping them face down `faction:vagabond$9.2.5`.

Track items (`item:tea`, `item:coin`, `item:sack`) auto-move to their respective tracks when placed face up; each track holds a maximum of three `faction:vagabond$9.2.5.1`. Satchel items (`item:boot`, `item:sword`, `item:crossbow`, `item:torch`, `item:hammer`) stay in the Satchel.

**Item capacity**: your limit is six items plus two per `item:sack` on track `faction:vagabond$9.6.4`. Exceeding the limit at Evening forces you to remove the surplus permanently. Plan acquisition so you have room before you Explore or take items through Aid.

### Maximum Rolled Hits

In battle, your maximum rolled hits equals your total undamaged `item:sword` — face up or face down — in your Satchel `faction:vagabond$9.2.6`. You have no warriors, so the standard "warriors in the clearing" cap does not apply directly to you. Protecting your swords protects your offensive ceiling.

### Taking Hits

Every hit you take damages one undamaged item `faction:vagabond$9.2.7`. If no undamaged items remain, you ignore further hits. This means a heavily depleted item pool paradoxically immunizes you from further damage — but you will also be nearly non-functional until you Repair.

### Crafting

You exhaust `item:hammer` to activate your pawn as a crafting piece, ignoring the once-per-turn limit on crafting piece activation `faction:vagabond$9.2.1`. Multiple hammers let you craft multi-icon cards. When you craft an item card, you take the item immediately, face up `faction:vagabond$9.2.1`. Note that you cannot craft cards requiring multiple suits in the same action, because all your hammers match your current clearing's suit `faq:vagabond-multi-suit-craft`.

### Relationships

Every non-Vagabond faction starts Indifferent. Your Relationships chart has an Allied track with four spaces and one Hostile box `faction:vagabond$9.2.9`.

**Improving**: Aid a non-Hostile faction the number of times printed between their current space and the next during the same turn `faction:vagabond$9.2.9.1.1`. Each Aid costs one item plus a matching card. After meeting the threshold, advance the marker one space right and score the printed VP `faction:vagabond$9.2.9.1.2`.

**Allied**: once at the final Allied space, that faction is Allied. Aiding them scores 2 VP each time `faction:vagabond$9.2.9.2.1`. You can also force their warriors to move with you `faction:vagabond$9.2.9.2.2` and treat their warriors as yours in battle (up to your sword cap) `faction:vagabond$9.2.9.2.3`. Using Allied warriors to absorb hits comes with a risk: if you take more hits via Allied warrior removal than via item damage in the same battle, that faction becomes Hostile at the end of battle `faction:vagabond$9.2.9.2.4`.

**Hostile**: removing any warrior of a non-Hostile faction makes that faction Hostile immediately `faction:vagabond$9.2.9.3`. Every subsequent piece you remove from a Hostile faction in battle on your turn (after the warrior that triggered Hostility) scores one Infamy VP `faction:vagabond$9.2.9.3.1`. Moving into a Hostile faction's clearings costs an extra `item:boot` `faction:vagabond$9.2.9.3.2`. You cannot Aid a Hostile faction back toward Indifferent, but you can still Aid them to take items from their Crafted Items box `faction:vagabond$9.2.9.3.3`.

One critical clarification: you do not go Hostile when you remove buildings or tokens — only when you remove warriors `faq:vagabond-hostile-building`. You also do not go Hostile when removing hireling warriors controlled by another faction; hirelings are not faction pieces `faq:vagabond-hireling-hostile`.

### Forest Movement and Slip

Normal Move actions cannot take you into a forest, only out of one `faction:vagabond$9.2.10`. Slip (Birdsong) lets you move into an adjacent clearing or forest without spending a `item:boot`, and it bypasses effects that prevent movement such as Corvid snares `faction:vagabond$9.4.2`. Slip is free and cannot be blocked by Hostile penalties.

---

## Turn Structure

### Birdsong

Two ordered steps:

1. **Refresh** `faction:vagabond$9.4.1`: flip two exhausted items face up per `item:tea` on the Refresh track (not counting tea you flip up in this step), then flip three more. Base refresh without any tea is three items. Two teas on track = seven items refreshed before your turn begins. Refresh is what makes tea the single most powerful scaling item.

2. **Slip** `faction:vagabond$9.4.2`: optional free move to any adjacent clearing or forest, ignoring Hostile movement penalties and movement-prevention effects. Use this to reposition cheaply before spending actions, to reach a quest clearing, or to enter a forest for a free Rest.

### Daylight

All Daylight actions can be taken in any order, any number of times, by exhausting the listed items `faction:vagabond$9.5`. You are constrained only by item availability.

- **Move** `faction:vagabond$9.5.1`: exhaust one `item:boot` to move (plus one more `item:boot` if the destination has Hostile warriors). You cannot move into a forest; from a forest you may only move to an adjacent clearing.
- **Battle** `faction:vagabond$9.5.2`: exhaust one `item:sword` to initiate battle. Check your relationship with the defender before committing.
- **Explore** `faction:vagabond$9.5.3`: exhaust one `item:torch` to take one item from under a ruin in your clearing. Score 1 VP if you take an item. Reveal it and place it in your Satchel or on track. Removing the last item removes the ruin.
- **Aid** `faction:vagabond$9.5.4`: exhaust any one item and give a card matching your clearing to a player with faction pieces in your clearing (even Hostile). Then optionally take one item from their Crafted Items box. Check relationship after.
- **Quest** `faction:vagabond$9.5.5`: choose a quest matching your clearing's suit, exhaust the two listed items. Score VP equal to your matching completed quests (including this one), or draw two cards. Draw a replacement quest.
- **Strike** `faction:vagabond$9.5.6`: exhaust one `item:crossbow` to remove one enemy warrior in your clearing. If no warriors remain, remove another of their faction pieces instead. Check relationship. Note: Strike does not count as battle and does not trigger Infamy VP `faq:vagabond-strike-infamy`.
- **Repair** `faction:vagabond$9.5.7`: exhaust one `item:hammer` to move one damaged item to your Satchel in its current orientation. Track items auto-move to track.
- **Craft** `faction:vagabond$9.5.8`: exhaust one `item:hammer` per crafting icon on the card; your clearing must match all icons.
- **Special Action** `faction:vagabond$9.5.9`: exhaust items listed on your character card to trigger the character-specific ability.

### Evening

Four ordered steps `faction:vagabond$9.6`:

1. **Rest** `faction:vagabond$9.6.1`: if you are in a forest, all damaged items move to your Satchel face up (free full repair). This is the most efficient repair method but requires a `item:boot` or Slip to reach a forest.
2. **Draw Cards** `faction:vagabond$9.6.2`: draw one card, plus one per `item:coin` on track. Two coins means three cards per turn — among the highest draw rates in the game.
3. **Discard Cards** `faction:vagabond$9.6.3`: discard down to five cards if over the limit.
4. **Check Item Capacity** `faction:vagabond$9.6.4`: discard items permanently if over your limit (six base, plus two per `item:sack` on track). Items removed this way leave the game.

---

## Scoring Engine

| VP Source | Amount | Trigger | Timing |
|---|---|---|---|
| Relationship improvement | Printed on Allied track space | Aid threshold met | Daylight (Aid action) |
| Aiding an Allied faction | 2 VP | Each Aid action | Daylight (Aid action) |
| Quest completion (score option) | 1 VP × matching completed quests | Quest resolved | Daylight (Quest action) |
| Exploration | 1 VP | Item taken from ruin | Daylight (Explore action) |
| Enemy building/token removal | 1 VP per piece | Removed in battle or Strike | Daylight |
| Infamy | 1 VP per enemy piece removed (Hostile only, after triggering warrior) | Battle on your turn | Daylight (Battle action) |
| Crafting an item card | Printed on card | Item crafted | Daylight (Craft action) |

**Key observations**: Quest scoring accelerates as your quest pile grows. A third same-suit quest scores 3 VP at once; a fourth scores 4. Pairing this with two `item:coin` on track (3 cards/turn) means you can sustain the quest cycle without running dry. Infamy is efficient when multiple Hostile clearings are in play but is fundamentally a secondary income stream — building a faction toward Allied then farming 2 VP per Aid is often more reliable.

---

## Playbook

### Opening (Turns 1–2)

Your first priority is expanding your item pool. Start in a forest touching ruin clearings. Slip (Birdsong 1) to reach a ruin clearing. Explore twice in Daylight if your `item:torch` supply allows. Each ruin yields 1 VP and an item.

Simultaneously begin Aid. Any faction with pieces in your clearing is an Aid target. Give them a matching card, take an item from their Crafted Items box if available. You are burning cards for items: this is a favorable exchange early because your hand is full and your item pool is sparse.

Prioritize completing your first quest on turn 1 or 2 if the quest is in your starting clearing's suit and the items are manageable. Take the VP option on your first quest completion regardless of suit — one VP is always fine, and the exponential benefit of same-suit repetition only materializes once you have two or more matching completed quests.

Turn 2, reassess: do you have enough items to sustain Daylight actions comfortably? If not, continue exploring. If yes, begin choosing Aid targets deliberately with an eye toward which faction you want Allied first.

### Mid-Game Pivots

**Pivot: Quest chain discovered** — if you have two or more completed quests in the same suit and the face-up quest pool shows more matching suits, commit. Route your Slip and Movement toward those clearings and draw cards through the quest channel rather than scoring. You are building up for a larger scoring burst.

**Pivot: Table turns on you** — if two or more factions begin attacking you, assess your sword count. If you can repair and fight back, go Hostile deliberately with the weakest attacker and farm Infamy while staying Indifferent or Allied with factions who cannot easily attack you. If your items are in crisis, spend a turn in a forest (Evening Rest) and buy time.

**Pivot: Coalition opportunity** — if one player is being suppressed hard by everyone else and you have 10 VP, consider activating a dominance card for a coalition. You want a partner whose win condition is plausible and whose faction is currently underestimated. The coalition eliminates you as a VP scoring threat, which can reduce player attention on you.

**Pivot: Hostile farming transition** — once a faction goes Hostile and has buildings on the board, their buildings become your points. Each building is 2 VP (1 standard + 1 Infamy) if you remove it in battle on your turn. If they are Hostile and weak, escalate: Strike warriors to enable your battle attack, then clean up buildings.

### Endgame Routes

**Quest burst**: if you have four or five completed quests in the same suit and are sitting at 22–25 VP, completing one more quest of that suit can close the gap in one action. Route everything toward that clearing.

**Hostile annihilation**: if multiple factions are Hostile and have structures, you can sprint through 6–10 VP by chain-attacking. You need sufficient swords and boots for this; plan Refresh to ensure your items are live.

**Allied Aid farming**: if you have two or three factions Allied and the game is approaching a close, sustained Aid spends generate 2 VP per action. This is slow but reliable. In a tight race, this may be your steadiest finishing route if combat would cost more items than it returns.

---

## Threat Factions

### Woodland Alliance

The Alliance uses Outrage to punish players who move warriors into sympathetic clearings `faction:woodland$8.2.6`. Your pawn is not a warrior, so moving into a sympathetic clearing does not trigger Outrage `faq:vagabond-outrage`. This actually makes you uniquely comfortable navigating the Alliance's territorial web.

The threat runs the other way: if the Alliance's sympathy and revolt cycle is running fast, they can build clearings of concentrated warriors that are difficult for anyone to contest, which limits your Aid targets and can lock you out of clearings you need for quests. More practically, Alliance revolts include a "remove all enemy pieces" step — your pawn survives but you take three item damage `faction:vagabond$9.2.2.1`. A well-timed revolt in your clearing is one of the few ways to genuinely hurt your item economy without combat.

Counter-play: you can remove sympathy tokens without going Hostile (no warriors involved `faq:vagabond-hostile-building`). Removing a token is 1 VP and removes the Alliance's revolt setup. Strike lets you remove tokens in clearings even if no Alliance warriors are present.

### Eyrie Dynasties

The Eyrie's Lords of the Forest ability rules any clearing where they are tied `faction:eyrie$7.2.1`. Their Decree forces them to expand, often creating large warrior stacks that are hard to contest. If they are unchecked, the Eyrie can reach 30 VP through building placements before you can accumulate enough quests or Aid VPs.

You face a tempo problem more than a direct conflict problem: the Eyrie's scoring is fast and steady. If they are Allied with you, you benefit from moving their warriors and borrowing their combat strength. If they go Hostile against each other (common in high-player-count games), you can harvest Infamy from their weakened state. Timing your Hostile transition against a declining Eyrie is often efficient.

### Corvid Conspiracy

The Corvids' plot tokens and Snare deserve attention. Snare prevents movement out of a clearing until the token is removed `faction:corvid$13.4.1` — with one exception: Slip ignores all effects that prevent movement `faction:vagabond$9.4.2`. You can Slip out of a Snare. This makes Corvids less dangerous to you than to most factions, but they can still place Snares in clearings you need to reach, and their bomb plots can trigger Full Removal (damaging three items) `faction:vagabond$9.2.2.1`.

Counter-play: Strike (`item:crossbow`) removes Corvid plot tokens without triggering Hostility (no warriors involved), and Slip lets you escape Snares on the subsequent Birdsong.

### Lord of the Hundreds

The Hundreds' Oppress ability (`faction:warlord$14.6`) scores VP when they rule a clearing with no enemy pieces — and you can occupy clearings without being an enemy piece that prevents Oppress (your pawn does not rule, does not count as a warrior). More relevant: the Hundreds' Raze ability can destroy ruins `faction:warlord$14.4.1`, eliminating the items you need for exploration. If ruins disappear early, your VP-per-exploration score is cut short and your item expansion is stunted.

Counter-play: prioritize exploring ruins before the Hundreds can raze them. If the Hundreds are razing ruins frequently, shift your scoring emphasis toward quests and Allied Aid farming rather than exploration.

---

## Card Priorities

### Top Priority Crafted Items

**`item:tea` (Root Tea cards)** — every tea on the Refresh track adds two extra Refresh flips per Birdsong `faction:vagabond$9.4.1`. One tea: 5 refreshes per turn. Two teas: 7. Three teas: 9. Three teas effectively makes item depletion nearly irrelevant. The Root Tea cards (`card:ROOT-89 (Base Game)`, `card:ROOT-90 (Base Game)`, `card:ROOT-91 (Base Game)`) each yield a `item:tea` when crafted. These are the single highest-priority craftable items for almost every character.

**`item:sack` (Gently Used Knapsack, Mouse-in-a-sack, etc.)** — each `item:sack` on track raises your item capacity by two `faction:vagabond$9.6.4` and has other minor uses. Capacity matters once your item pool exceeds six, which happens naturally through Aid and exploration. Craft sacks early to avoid forced item discards.

**`item:coin` (Investments, Foxfolk Steel, etc.)** — each `item:coin` on track is +1 card per Evening draw `faction:vagabond$9.6.2`. Two coins gives you three cards per turn. Three coins gives four. Card draw fuels Aid, which fuels item acquisition and relationship advancement.

### Situational

**Armorers** `card:ROOT-51 (Base Game)` — discard to ignore all rolled hits taken in one battle. This is a get-out-of-jail card for an overextended attack or a defensive ambush that would otherwise destroy your item pool. Useful for the Ranger and Ronin who fight frequently.

**Better Burrow Bank** `card:ROOT-55 (Base Game)` — draw one card per Birdsong if you share one with an enemy. Steady extra draw but requires ongoing enemy presence in adjacent clearings. Solid for any character with a strong card-draw-to-Aid pipeline.

**Cobbler** `card:ROOT-60 (Base Game)` — extra Move at start of Evening. Movement is often your most constrained resource; an extra move after your Daylight actions can set you up for the next turn's quest or Aid at low cost.

**Woodland Runners** `card:ROOT-109 (Base Game)` — passive extra move in Birdsong. Stacks well with Slip for aggressive repositioning.

**Favor of the Foxes/Mice/Rabbits** `card:ROOT-73 (Base Game)`, `card:ROOT-74 (Base Game)`, `card:ROOT-75 (Base Game)` — these remove all enemy pieces in the named suit's clearings. They do not remove the Vagabond pawn (only your own pawn is immune; these do damage items if your pawn is in an affected clearing `faction:vagabond$9.2.2.1`). You can craft these via Tinker or multiple hammers and hold them as a board-wipe threat. However, you do not control where other factions build, so their value is highly situation-dependent.

### Ambush Cards

Hold at least one Ambush for defense. Your item pool is your health bar; two unblocked hits from an Ambush card against you damage two items. More importantly, being defenseless (no undamaged `item:sword`) lets attackers deal an extra hit, so an Ambush held when you are at one sword may save a critical item.

Playing Ambush as the defender deals two immediate hits and can end the battle if no attacking warriors remain after the ambush resolution `rule:4.3.1.2`. As a pawn, you count for the "no remaining warriors or pawns" check.

### Dominance Cards

You cannot use dominance cards for their standard victory condition `faction:vagabond$9.2.8`. Their only special use is as a coalition trigger. If you are not pursuing a coalition, treat dominance cards purely as suits for spending (each is a bird card `rule:3.3.3`). Do not discard them arbitrarily — they go near the map as available rather than to the discard `rule:3.3.3`.

---

## Common Pitfalls

- **Spreading hostility too early.** Going Hostile with two or three factions at once doubles and triples your movement cost (`item:boot` per Hostile faction's clearings). You can end up unable to reach quests or Aid targets without exhausting most of your boots. Go Hostile deliberately and manage which factions you antagonize.

- **Ignoring item capacity.** Acquiring items freely through Aid and exploration and then discarding them permanently at Evening Check is a serious tempo loss. Know your current item limit (six plus two per `item:sack` on track) before each Explore and Aid, and craft `item:sack` items proactively.

- **Taking VP on every quest instead of cards.** Early quests should almost always score VP. But once you have multiple completed quests in the same suit, drawing two cards is sometimes better — it fuels Aid, which fuels items and relationships, which multiplies later VP. This is a judgment call that depends on your current VP and the game's pace, but reflexively scoring VP from every quest is a common suboptimal habit.

- **Neglecting Repair.** Each `item:hammer` Repair action recovers one damaged item. Your Ranger's Hideout repairs three items but ends Daylight. If you are not Ranger, the slower manual Repair is easy to deprioritize. Going into battle with a damaged item pool narrows your combat ceiling and leaves you Defenseless against smart attackers.

- **Undervaluing Slip.** Slip is free every Birdsong and ignores all movement restrictions including Hostile penalties and Corvid Snares `faction:vagabond$9.4.2`. Treating it as irrelevant and always spending boots to move is wasteful. Every turn, ask whether Slip can replace the first boot of your route.

- **Overcommitting to Allied relationships.** Building toward Allied is VP-efficient if you follow through — but mid-track relationships that never reach Allied pay you once and then sit idle. If a faction's playscape is collapsing (they are losing buildings fast), do not sink Aid into advancing their relationship. Pivot to a faction that will survive to the endgame.

- **Fighting factions at full strength.** Vagabond combat is most efficient against factions that already have their warrior presence reduced. Attacking a large Marquise stack when you have two swords is a bad trade. Attack when the target is weak; use Strike to soften first if needed.

- **Forgetting the Forest Rest.** A free full item repair is available at Evening if you are in a forest `faction:vagabond$9.6.1`. One boot and a Slip can get you to a forest; spend an Evening there when item damage is high. Players who never use forests miss a major recovery mechanism.

---

## Mechanic Clarifications

### Does moving into a sympathetic clearing trigger Woodland Outrage?

No. Outrage triggers when a player moves warriors into or removes sympathy from a clearing `faction:woodland$8.2.6`. Your pawn is not a warrior, so entering a sympathetic clearing does not trigger Outrage `faq:vagabond-outrage`. Removing a sympathy token does trigger Outrage, however, because that is an item removal, not a warrior movement.

### Does Strike trigger Infamy?

No. Infamy specifies you must remove the piece in battle during your turn `faction:vagabond$9.2.9.3.1`. Strike is not a battle. You do not score Infamy VP for Strike kills `faq:vagabond-strike-infamy`.

### Does removing a building make the owner Hostile?

No. Hostility triggers only when you remove a warrior `faction:vagabond$9.2.9.3`. Buildings, tokens, and sympathy tokens are removed without Hostility consequences — unless you were already Hostile with that faction, in which case they were already Hostile and Infamy applies to warrior removal only `faq:vagabond-hostile-building`.

### What happens when a "remove all enemy pieces" effect hits your clearing?

You cannot be removed, but you damage three items `faction:vagabond$9.2.2.1`. This applies to Favor cards, Alliance revolts, and Corvid bombs, among others. The Hundreds' warlord also cannot be removed by these effects `faq:favor-warlord-vagabond`.

### Can you consent to coalition formation?

No. Coalition does not require the partner's consent `faq:no-consent-required`. The Vagabond places their score marker on the chosen player's faction board; the chosen player cannot refuse.

### Can you form a coalition with a player already on a dominance win?

No. A player who has activated a dominance card has no score marker on the VP track. The coalition rule requires choosing a player with fewer VP than others `faction:vagabond$9.2.8`; a dominance player has no VP to compare `faq:coalition-dominance-player`. However, a player you have already coalition-partnered with can activate a dominance card afterward `faq:coalition-dominance-player`.

### Can the coalitioned partner and the Vagabond battle each other?

No. Once you form a coalition, you are no longer enemies with that player. The Battle rule requires battling an enemy `rule:4.3`; coalition partners cannot battle each other `faq:coalition-battle`.

### Does the Vagabond cause Outrage when moving Allied warriors into sympathetic clearings?

No. The Vagabond's Allied movement uses the Force keyword, and forced movement of Allied warriors does not trigger Outrage `faq:vagabond-allied-outrage`. This was changed as of the Marauder Expansion (8th Printing, now incorporated in p16).

### Does forcing Allied warriors into a clearing with Hostile faction warriors cost extra boots?

No. The extra `item:boot` cost for Hostile clearings applies to the Vagabond's own movement `faction:vagabond$9.2.9.3.2`. Forcing Allied warriors to move is part of your Move action and does not independently cost you an extra boot.

---

## Reference Index

**Faction citation key**: `faction:vagabond`

**Primary rule section**: `rule:9.`

**Related glossary entries**:
- `item:boot` — movement, Hostile penalty cost
- `item:sword` — battle max hits, Defenseless condition
- `item:torch` — Explore, Aid, character Special Actions
- `item:hammer` — Repair, Craft activation
- `item:crossbow` — Strike action
- `item:tea` — Refresh track
- `item:coin` — Evening draw track
- `item:sack` — item capacity track
- Glossary: Enemy `item:enemy` — coalition partner is not an enemy (affects battle eligibility)
- Glossary: Warrior — pawn is not a warrior (affects rule, Outrage, Defenseless)

**Hireling form**: There is no dedicated Vagabond hireling in the base hireling pool. However, several Vagabond characters appear in expansion content and the Homeland map.

**Cross-faction interactions**:
- Woodland Alliance: pawn does not trigger Outrage on movement; removing sympathy does trigger Outrage.
- Riverfolk Company: if you hire Riverfolk Mercenaries, you can start a battle without your own pieces in the clearing `faq:vagabond-riverfolk-mercenaries`; the hiring rules are in `rule:11.2.7`.
- Ferry landmark: you can force Allied warriors using the Ferry `faq:vagabond-ferry-allied`.
- Lord of the Hundreds: Favor cards do not remove the Hundreds' warlord, same as your pawn `faq:favor-warlord-vagabond`.
- Twilight Council: Vagabond Allies clause may appear in Council rules `faction:council$17.`; consult `rule:17.` for specifics.
- Coalition interactions: see Win Condition section above; key FAQ entries are `faq:coalition-dominance-player` and `faq:coalition-battle`.
