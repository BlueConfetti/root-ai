# Lord of the Hundreds

## At a Glance

**Identity:** A close-combat warlord who scores by holding clean, oppressed clearings while looting items to fuel a growing action economy — and periodically unleashing mob tokens that destroy enemy buildings.

- **Reach:** 9 (`rule:5.2.2`)
- **Complexity:** High
- **Color / Icon:** Red (`#e11b3f`) / faction-warlord
- **Faction citation key:** `faction:warlord` (faction-specific rules cite as `faction:warlord$14.X.Y`)
- **Primary rule section:** `rule:14.`

**Setup constraints:** Start in any corner clearing not already taken by another player; prefer the corner diagonally opposite to another player's start if one exists (`faction:warlord$14.3.2`).

**Scoring tempo:** Burst-capable with a steady baseline. Oppression scores 1–4 VP per turn depending on how many clean clearings you control; a strong mid-game with 5+ oppressed clearings yields 3 VP/turn. Early turns often generate only 1–2 VP while you build presence.

---

## Win Condition

### Standard Route (30 VP)

Your primary engine is **Oppress**: at the end of your Evening, you score points equal to the number of clearings you rule that have a Hundreds piece and no enemy pieces (`faction:warlord$14.6.2`). The scale is nonlinear — reaching 6+ oppressed clearings (4 VP/turn) is game-deciding speed.

Supplementary VP comes from:
- Removing enemy buildings and tokens in battle or via mobs (`rule:3.2.1`)
- Looting items from defenders and adding them to the Hoard, which can trigger a 1 VP overflow bonus (`faction:warlord$14.2.4.1`)
- Razing ruins to collect items during Birdsong (`faction:warlord$14.4.1`)

You are not a crafting-for-points faction. Contempt for Trade (`faction:warlord$14.2.3`) forces you to choose between hoarding an item (no points) or destroying it for its printed VP. The Hoard path is almost always correct — items convert to Command and Prowess, which unlock the actions and recruits that let you oppress more clearings.

### Dominance Path

Dominance is a legitimate endgame option. Because Oppress scales with the number of clean clearings you rule, you already need broad territorial control — which lines up well with mouse, rabbit, or fox Dominance requiring rule of three matching clearings at Birdsong (`rule:3.3.1.1`). Activate once you hit 10 VP and hold three target clearings free of enemy pieces. Bird Dominance is harder to execute (two opposite corners) but not impossible if you have Prowess and mobility.

---

## Setup

### Step-by-Step

1. **Gather pieces.** Form supplies of 20 warriors, 1 warlord, and 6 strongholds (`faction:warlord$14.3.1`).
2. **Garrison.** Place your warlord, four warriors, and one stronghold in a corner clearing that is not another player's starting corner. If possible, pick the corner diagonally opposite from another player's start (`faction:warlord$14.3.2`).
3. **Place items.** Place the four "R" items randomly under the ruins unless already done (`faction:warlord$14.3.3`).
4. **Get Stubborn.** Place your Stubborn mood card on your Mood Card slot (`faction:warlord$14.3.4`). Stubborn lets you ignore the first hit you take in warlord battles — a reasonable default for an early-game aggressor.

### Corner Choice

The diagonally-opposite corner preference is a hard setup constraint, not optional advice. If you get to pick your corner (e.g., you set up after a faction that started in an adjacent corner), prioritize the corner with the best ruin access and the most connected paths out of it. You want your early mobs to spread naturally toward ruins before opponents can contest them.

### Neighbor Considerations

- **Woodland Alliance adjacent:** Challenging. Their sympathy tokens block oppression (any enemy piece in the clearing breaks oppression), and every time you remove sympathy you trigger Outrage, feeding the Alliance supporters. Mobs will remove sympathy tokens via Raze since sympathy is an enemy token, but that still triggers Outrage. A nearby Alliance means you are paying ongoing costs — in Outrage cards and combat — just to keep clearings clean enough to oppress.
- **Eyrie adjacent:** Less threatening to you specifically. Your mobs can deny them building slots and force awkward Decree routing. Eyrie's forced-movement Decree can feed your Wrathful/Relentless warlord engagements.
- **Marquise adjacent:** They fill slots quickly with buildings. This compresses your ruin access and makes oppression harder early. However, mobs are very effective against Cat infrastructure once seeded.

### Opening Hand Priorities

Your hand is primarily a resource for Incite (one card per mob placed) and Build (one card per stronghold). On turn 1, keep:
- Any card matching your starting corner's suit — enables an immediate stronghold build or first mob.
- A bird card — flexible: can serve as either suit.

Discard multi-suit-requirement craftables and anything you cannot use in the first two turns. Your hand size is capped at five cards (`faction:warlord$14.6.3`), so clutter has a hard cost.

---

## Faction Rules and Abilities

### The Warlord

The warlord is a special warrior piece that functions differently from your regular warriors in two key ways (`faction:warlord$14.2.2`):

- It **cannot be removed outside of battle** — effects that say "remove all enemy pieces" (such as Favor cards) do not remove the warlord. The FAQ confirms this explicitly (`faq:Do the Favor... cards really remove all enemy pieces`).
- It **cannot be moved outside the Hundreds' turn**, and it cannot be placed except during setup (`faction:warlord$14.3.2`) or via the Anoint action (`faction:warlord$14.4.3`).

In battle, when you take hits, you choose which of your own pieces are removed — the warlord or a regular warrior (`faq:In battle, who chooses whether a hit removes the warlord`). The warlord counts as a warrior for rule and for oppression purposes.

### Contempt for Trade

Whenever you craft an item, you choose one of two outcomes (`faction:warlord$14.2.3`):
- Take the item (add it to the Hoard), scoring none of the card's listed VP.
- Permanently remove the item, scoring the card's listed VP.

You can still score extra crafting VP from effects like Master Engravers (`card:ROOT-82 (Exiles & Partisans Deck)`) even when taking the item. The item-to-Hoard path is correct almost every time — the Command/Prowess bonuses the item unlocks are worth far more than the 1–3 VP you would score by discarding it.

### The Hoard

Instead of a Crafted Items box, you have the Hoard with two tracks (`faction:warlord$14.2.4`):

- **Command track** holds `item:boot`, `item:sack`, and `item:coin` (up to 3 slots).
- **Prowess track** holds `item:hammer`, `item:tea`, `item:sword`, and `item:crossbow` (up to 4 slots).

**Gaining items** (`faction:warlord$14.2.4.1`): Place a new item in the leftmost empty slot of its track. If there is no empty slot, you must permanently remove either the incoming item or any item already on that track, and score 1 VP. This means a full track forces a painful choice: you lose mood access or VP.

**Command and Prowess values** (`faction:warlord$14.2.4.2`): Items on each track convert to a numeric stat:

| Items on track | Stat value |
|---|---|
| 0 | 1 |
| 1–2 | 2 |
| 3 | 3 |
| 4 (Prowess only) | 4 |

**Command** determines how many times you may act during the Command the Hundreds step (moves, battles, and builds). **Prowess** determines both how many warriors you recruit to the warlord's clearing each Birdsong and how many times you may Advance the Warlord per Daylight.

### Looters

When you initiate a battle as the attacker, if the defender has an item in their Crafted Items box, you may declare you want to loot (`faction:warlord$14.2.5`). This declaration comes before the defender decides whether to ambush (`faq:Do I declare whether I'm using my Looters before or after the defender declares`). If you declare looting:

- You deal no rolled hits (though you can still deal extra hits, such as from Wrathful mood).
- The defender deals their rolled hits normally.
- At the end of battle, if you rule the clearing, you take one item from the defender's Crafted Items box.

You cannot loot the Vagabond. Looting is primarily useful against the Underground Duchy (who stack items via Minister abilities) and late-game Marquise or Eyrie players who have been crafting freely.

### Crafting

You craft during Daylight by activating strongholds (`faction:warlord$14.2.1`). Each stronghold can be activated once per turn. A stronghold's suit matches its clearing, so diversifying your strongholds across suits is necessary to craft the cards you need.

---

## Turn Structure

### Birdsong

Your Birdsong has four mandatory steps in order (`rule:14.4`):

#### Raze

For each clearing that has a mob token (`faction:warlord$14.4.1`):
- Remove all enemy buildings and tokens from that clearing.
- Take one item from the ruin in that clearing, if any; remove the ruin if it was its last item.

After resolving all clearings with mobs, roll the mob die once and place a mob token in a matching clearing that (a) has no mob token already, and (b) is adjacent to a clearing with a mob token. If no such clearing exists, do not place.

Mob spread is not optional — you must roll and place if eligible. This means mobs can advance toward clearings you do not want to mob (e.g., where you plan to build). Think ahead.

#### Recruit

Place warriors equal to your Prowess into the clearing with your warlord (`faction:warlord$14.4.2`). Then place one warrior per stronghold in each clearing that has at least one stronghold.

This two-part recruit is what makes strongholds valuable as infrastructure: even a single stronghold in a clearing generates one warrior per turn, anchoring presence without burning your Command on moves.

#### Anoint

If the warlord is not currently on the map, you must place it (`faction:warlord$14.4.3`): replace any Hundreds warrior in a clearing with the warlord, or if you cannot, place the warlord in any clearing.

Anoint is automatic and has no cost — losing the warlord in battle is painful (it disrupts recruit and Advance the Warlord) but not permanent.

#### Choose Mood

You must replace the mood card in your Mood Card slot with a different mood card that does not show an item currently in your Hoard (`faction:warlord$14.4.4`). You cannot stay on the same mood unless you are Lavish and no other options exist (you remain Lavish in that edge case).

As you fill the Hoard, moods whose items are already there become unavailable. A full Prowess track (four items) locks out Bitter, Grandiose, Stubborn, and Wrathful — leaving only Command-track moods and Lavish available. Managing Hoard composition keeps mood flexibility alive.

### Daylight

Your Daylight has three steps in order (`rule:14.5`):

#### Craft

Activate strongholds to craft cards (`faction:warlord$14.5.1`). Do this before spending Command actions on moves and battles, as crafting doesn't cost Command.

#### Command the Hundreds

Take up to Command actions, in any order (`faction:warlord$14.5.2`). Each action is one of:
- **Move:** Take a move (`rule:4.2`).
- **Battle:** Initiate a battle (`rule:4.3`).
- **Build:** Spend a card to place a stronghold in a matching clearing you rule (`faction:warlord$14.5.2.3`).

At Command 1 (no hoard items), you get one action total. At Command 2, you get two — that jump from 1 to 2 is the most important early-game threshold. Builds here cost a card and require rule, so you need enough warriors in a clearing before you can plant a stronghold.

#### Advance the Warlord

Take this action up to Prowess times (`faction:warlord$14.5.3`). Each use: move the warlord with any Hundreds warriors, then battle in the warlord's clearing. Both the move and the battle are optional each time you take the action — you can move without battling, or battle without moving.

Advance the Warlord is separate from your Command actions. With Prowess 2 and Command 2, you can Advance twice and take two Command actions — that is four discrete operations per Daylight at a relatively modest hoard investment.

**Grandiose mood swap:** When Grandiose, you perform Advance the Warlord before Command the Hundreds (`faction:warlord$14.7.2`). This means the warlord can move into a clearing and fight before your normal Command actions clean up or consolidate — useful for aggressive warlord-led assaults.

### Evening

Your Evening has three steps in order (`rule:14.6`):

#### Incite

Any number of times, spend a card to place a mob token in a matching clearing that (a) has no mob token already and (b) has a Hundreds warrior (including your warlord) (`faction:warlord$14.6.1`). Cards spent here are consumed, so weigh mob-seeding against your need for future Command builds and hand cards.

Mobs placed in Evening fire on your next Birdsong — they are a delayed, spreading threat. Mobs are also an oppression suppressor against yourself: a mob token is a Hundreds piece, satisfying the "has a Hundreds piece" requirement for Oppress, but mobs don't remove enemy pieces until Raze fires. So seeding a mob in a contested clearing this Evening means it may raze enemy pieces next turn, then let you oppress.

**Jubilant mood bonus:** When Jubilant and you Incite in your warlord's clearing, you may roll the mob die up to four additional times to chain-spread mobs (`faction:warlord$14.7.3`). This is the primary mob-flooding tool.

#### Oppress

Score VP equal to the number of clearings you currently rule that have a Hundreds piece and no enemy pieces (`faction:warlord$14.6.2`):

| Oppressed clearings | VP scored |
|---|---|
| 0 | 0 |
| 1–2 | 1 |
| 3–4 | 2 |
| 5 | 3 |
| 6+ | 4 |

The FAQ clarifies the exact conditions: you need to rule, have a Hundreds piece there, and have no enemy pieces there (`faq:What exactly is required for the Hundreds to oppress a clearing`). A mob token is a Hundreds piece. A Riverfolk trade post in the clearing counts as an enemy piece and blocks oppression.

#### Draw and Discard

Draw one card (`faction:warlord$14.6.3`). Discard down to five if over the limit.

**Rowdy mood bonus:** In Evening, draw one more card. If your warlord's clearing has three or more enemy pieces, draw two more cards instead (`faction:warlord$14.7.6`). Note that Rowdy applies only to your draw step — it does not apply to Charm Offensive or other "draw a card" effects (`faq:Does the Rowdy mood let the Hundreds draw more cards when they use the Charm Offensive card`).

---

## Scoring Engine

| VP Source | Amount | Trigger | Timing |
|---|---|---|---|
| Oppress | 1–4 VP | End of Evening | Evening (Oppress step) |
| Removing enemy buildings/tokens | 1 VP each | Any battle or Raze | As removed |
| Ruin items (overflow) | 1 VP | Hoard track full, item gained | Birdsong (Raze) or any gain |
| Contempt for Trade (VP path) | Printed card VP | Item permanently removed | Daylight (Craft step) |
| Crafting extras (e.g., Master Engravers) | 1 VP | Crafting any item | Daylight (Craft step) |

Oppress is your engine. Everything else is secondary. In a typical mid-game turn with 4–5 oppressed clearings, you score 2–3 VP from Oppress alone. Mob razings that flatten two or three enemy buildings in one Birdsong can generate a burst of 2–3 additional VP.

---

## Playbook

### Opening (Turns 1–2)

Your first priority is reaching **Command 2** (one item on the Command track) as fast as possible. The jump from Command 1 to Command 2 doubles your Daylight actions and is the single biggest tempo inflection you have.

**Turn 1 goals:**
- In Daylight, build a second stronghold in an adjacent clearing you rule. This costs one matching card but is achievable if you held the right suit in your opening hand.
- Advance the Warlord into a clearing with a ruin or toward a mob-seeded clearing.
- In Evening, spend one card to place a mob token in a matching clearing with a Hundreds warrior — preferably adjacent to a ruin.

**Turn 2 goals:**
- If the mob fires on a ruin, you gain an item. Slot it into the appropriate Hoard track to raise Command or Prowess.
- Recruit is now buffed by any stronghold you placed — use the bonus warriors to hold additional clearings.
- Aim to have 3 oppressed clearings by end of turn 2 to score 2 VP in Evening.

Community players commonly advise prioritizing boot (`item:boot`) and sack (`item:sack`) first as Command-track items, since they push Command to 2 early. (Source: BGG strategy threads, 2022–2023 — plausibly pre-dates any minor balance tweaks.) Prowess items matter enormously for mid-game scaling, but if you start with Stubborn (crossbow item) as default mood, that slot is locked — you may not want to place a second crossbow on the Prowess track early.

### Mid-Game Pivots

By turns 3–5, you should be scoring 2–3 VP per turn from Oppress and pushing the warlord aggressively. Watch for these triggers:

**Trigger: Mobs are stalling.** If opponents keep destroying your mob tokens before Raze fires, your item supply dries up and the mob network collapses. Pivot: spend more cards on Incite in Evening from warlord-adjacent clearings, or target more isolated corners where opponents cannot contest the mob adjacently.

**Trigger: Prowess still at 1.** If you have not gained a Prowess-track item by turn 3, your warlord recruit is anemic (1 warrior per Birdsong). Pivot: use looting to steal items from defenders or route the warlord specifically toward a ruin-adjacent mob.

**Trigger: Opponents clustering in your clearings.** If the Woodland Alliance is spreading sympathy through your territory or the Eyrie is nesting roosts, clean those clearings before Evening so Oppress fires. Even two cleanings worth the extra Advance action.

**Trigger: Hoard filling up.** When a track approaches full, think carefully about which item to overflow. Overflowing the wrong Prowess item locks out a key combat mood (Wrathful, Stubborn). Consider deliberately overflowing a duplicate item type to bank a VP while preserving mood access.

### Endgame Routes

**Route 1 — Oppress acceleration.** At 5–6 oppressed clearings per turn (3–4 VP/turn), you close 30 VP in roughly 6–8 turns from mid-game. This requires map control across at least half the clearings and strong mob coverage. Hold your best combat mood (Wrathful or Relentless) to defend the warlord's position.

**Route 2 — Raze burst + Oppress.** If you have a dense mob network in enemy-heavy territory, a single Birdsong can strip 3–5 enemy buildings, scoring 3–5 VP in addition to your Oppress total. This burst can close from 20–25 VP in one or two turns if set up correctly.

**Route 3 — Dominance.** With 10 VP and three clearings of the right suit cleanly held, activate a matching Dominance card. Your Hoard-driven action economy is well-suited to holding territory. Protect those three clearings through Birdsong.

---

## Threat Factions

### Woodland Alliance

The Alliance is one of your most important matchups to manage. Their sympathy tokens are circular tokens (`faq:Which pieces are buildings? Which are tokens`), and the Raze step removes all enemy buildings and tokens in mob clearings (`faction:warlord$14.4.1`) — so a mob token in a sympathetic clearing will remove the sympathy on your next Birdsong. This gives you a tool to clear sympathy without spending warriors in a costly battle.

The tension is that removing sympathy (whether by Raze or battle) triggers Outrage (`faction:woodland$8.2.6`), giving the Alliance a supporter card that fuels their revolt engine. Raze-triggered Outrage comes from you, so you pay the card cost. Weigh whether clearing a sympathetic clearing is worth feeding the Alliance supporters.

Counter-plays: Route your mob network through Alliance-sympathized clearings to raze both sympathy and buildings in one step. If you must remove sympathy in battle, do it alongside removing Alliance warriors so the hit is worth the Outrage cost. Pressure the Alliance's base clearings — Alliance bases are buildings, and mobs raze them once adjacent.

### Eyrie Dynasties

The Eyrie is a consistent mid-game threat because their Decree forces them to move into and recruit in many clearings — which directly blocks oppression. A roost in your clearing denies oppression for as long as it sits there. The Eyrie player knows this and may use your clearings as safe staging grounds if you do not fight back.

Counter-plays: Target roosts specifically in battle — each roost removed scores you 1 VP and clears a potential oppression site. Your warlord with Wrathful mood is a very effective anti-Eyrie weapon in the right clearing. If the Eyrie goes into Turmoil near you, capitalize: a chaotic Eyrie board creates clearing vacuums you can oppress.

### Riverfolk Company

Riverfolk trade posts are tokens, not buildings (`faq:Which pieces are buildings? Which are tokens`). They count as enemy pieces for Oppress purposes — a trade post in your clearing blocks oppression even if you rule it and have a mob there. Riverfolk also have few warriors and often can't defend well, but trade posts spread passively.

Counter-plays: Battle Riverfolk in their trade post clearings early — they are often undefended. Removing a trade post scores you 1 VP and clears oppression. Be aware that Riverfolk Mercenaries (hired by other factions) count as enemy pieces in your clearings too. Do not oppress a clearing that has any enemy piece, Hundreds or otherwise.

### Underground Duchy (Looter Consideration)

The Duchy builds up Ministers and collects items in their Crafted Items box at a high rate. They are a premium Looter target — entering battle and ruling the clearing lets you strip one item from their box per engagement. Time Looter declarations against Duchy defenders when you are confident you can win rule of that clearing.

---

## Card Priorities

### Top Priority: Items for the Hoard

Your highest-priority crafting targets are cards that give you items on their immediate effects. These directly grow Command and Prowess:

- **Root Tea** (`card:ROOT-89 (Base Game)` / `card:ROOT-90 (Base Game)` / `card:ROOT-91 (Base Game)`) — crafts `item:tea` onto the Prowess track. Tea unlocks Grandiose mood. Easy to craft (single suit), widely available.
- **Mouse-in-a-Sack** (`card:ROOT-83 (Base Game)`) — crafts `item:sack` onto the Command track. Single-mouse-suit cost. Gets you from Command 1 to Command 2 cheaply.
- **Gently Used Knapsack** (`card:ROOT-78 (Base Game)`) — crafts `item:sack`. Alternative sack source.
- **Smuggler's Trail** (`card:ROOT-96 (Base Game)`) — crafts `item:boot`. Puts you toward Command 2 or fills the boot slot if sack is already there.
- **Investments** (`card:ROOT-80 (Base Game)`) — crafts `item:coin`. Command-track item; opens Rowdy mood for better card draw.
- **Foxfolk Steel** (`card:ROOT-76 (Base Game)`) — crafts `item:sword`. Top Prowess item: unlocks Wrathful mood (extra hit as attacker in warlord's clearing) and boosts Prowess value.
- **Sword** (`card:ROOT-104 (Base Game)`) — single-mouse craft for `item:sword`. Same value.

### Situational

- **Brutal Tactics** (`card:ROOT-58 (Base Game)`) — as a craftable bird persistent effect, deals an extra hit as attacker but lets the defender score 1 VP. Use if you need raw combat power, accept the VP gift.
- **Armorers** (`card:ROOT-51 (Base Game)`) — discard to ignore all rolled hits in a single battle. High value if your warlord is in a dangerous position.
- **Sappers** (`card:ROOT-94 (Base Game)`) — extra hit as defender. Pairs with Stubborn for warlord defense.
- **Royal Claim** (`card:ROOT-92 (Base Game)`) — score 1 VP per clearing you rule at Birdsong. If you rule many clearings it can accelerate, but it competes for your limited card budget.
- **Coffin Makers** (`card:ROOT-62 (Exiles & Partisans Deck)`) — score per warriors removed to supply over the game. You remove many warriors via mobs and battles, making this a slow but real VP source.
- **Propaganda Bureau** (`card:ROOT-86 (Exiles & Partisans Deck)`) — replace an enemy warrior in a matching clearing with your own. Useful for seizing rule before building or oppressing.

### Low Priority / Skip

- **Better Burrow Bank** (`card:ROOT-55 (Base Game)`) — card-draw utility. You have a tight hand limit and minimal use for the enemy-draw clause.
- **Charm Offensive** (`card:ROOT-59 (Exiles & Partisans Deck)`) — draws a card and gifts an opponent 1 VP. The FAQ confirms Rowdy does not enhance this draw (`faq:Does the Rowdy mood let the Hundreds draw more cards when they use the Charm Offensive card`). Not worth the slot.
- **Cobbler** (`card:ROOT-60 (Base Game)`) — extra move at start of Evening. You already have good mobility from Advance the Warlord and Command. Low marginal value.

### Ambush Cards

Hold ambush cards for defense. Your warlord is a high-value target, and an ambush in the warlord's clearing buys time against an attacker trying to remove it. Using ambush offensively (to foil an incoming ambush) is correct if you are attacking into a clearing where the defender might ambush. Do not spend ambush cards for suit on non-critical builds if you lack other suit coverage — a one-card ambush defense is often worth keeping.

### Dominance Cards

Keep at least one matching Dominance card in mind for the Route 3 endgame (`rule:3.3`). Your natural board state (broad rule across 3+ clearings of a single suit) can set this up. Save a matching card to spend for an available Dominance card if you choose that path.

---

## Common Pitfalls

- **Leaving the warlord without warrior escort.** Without an escort, the warlord takes all hits in battle and can be removed on one lucky high roll. The Anoint step replaces it next Birdsong, but one turn without warlord-adjacent recruiting and Advance the Warlord is a serious tempo loss.

- **Filling the Hoard too quickly with duplicate-track items.** You want items across both tracks. Stuffing the Prowess track with four items locks out all four Prowess moods — you are stuck cycling only Command-track moods and Lavish. Build the Hoard deliberately.

- **Neglecting Prowess early.** Prowess at 1 means one warrior recruit per Birdsong and one Advance per Daylight. That is barely enough to maintain board presence. Getting to Prowess 2 is a higher priority than a second Command action in most early-game situations.

- **Seeding mobs with no adjacent mob.** The Raze step requires you to roll and spread a mob adjacent to an existing mob token. If all your mobs are isolated (no adjacent mob), the spread step cannot fire and the network stagnates. Keep at least one connected chain of mobs to propagate.

- **Over-spending cards on Incite.** Your card hand is thin (max five cards, draw one per turn plus mood bonuses). Spending three or four cards per Evening on mobs leaves nothing for builds, which strangles your stronghold expansion and Command growth.

- **Oppressing clearings with Riverfolk trade posts or any enemy token.** A single enemy token in a clearing — even one you rule — blocks oppression completely. Audit every clearing before Evening for stray tokens.

- **Forgetting Contempt for Trade.** When you craft an item, you must actively choose to hoard or score VP. Automatically taking the VP path when the Hoard would benefit more from the item is a common reflex error.

- **Using Lavish poorly.** Lavish lets you burn Hoard items for warriors (two per item) at the end of Birdsong. This is a situational desperation tool, not a routine play. Using it reduces your Command/Prowess, constricts future mood options, and trades long-term engine for short-term bodies.

---

## Mechanic Clarifications

### Does the warlord survive Favor cards?

**Q:** Can Favor of the Foxes / Rabbits / Mice remove the warlord?
**Resolution:** No. The warlord cannot be removed outside of battle (`faction:warlord$14.2.2`). Favor cards state they remove all enemy pieces in matching clearings, but the warlord's special rule overrides the general removal. (`faq:Do the Favor... cards really remove all enemy pieces from those clearings`)

### Who chooses which piece takes a hit — warlord or warrior?

**Q:** When the Hundreds player takes hits in battle and both the warlord and regular warriors are present, who decides removal order?
**Resolution:** The Hundreds player chooses. Warriors must be removed before buildings and tokens, but the warlord is a warrior — so if only warriors are in the clearing, the Hundreds player decides whether to remove the warlord or another warrior first. (`faq:In battle, who chooses whether a hit removes the warlord`) (`rule:4.3.6`)

### What exactly qualifies a clearing for Oppress?

**Q:** What conditions must all be true?
**Resolution:** You must (1) rule the clearing, (2) have at least one Hundreds piece there (a mob token counts), and (3) have no enemy pieces there. A Riverfolk Mercenary warrior you are using does not make the clearing "yours" for oppression purposes if it is still an enemy piece. A mob plus a hired Riverfolk Mercenary warrior in a clearing you rule does not oppress. (`faq:What exactly is required for the Hundreds to oppress a clearing`) (`faction:warlord$14.6.2`)

### Does Rowdy apply to Charm Offensive or other card-draw effects?

**Q:** If I have the Rowdy mood and craft Charm Offensive, do I draw the extra Rowdy card when Charm Offensive fires?
**Resolution:** No. Rowdy applies only to your Draw and Discard step in Evening, not to any other "draw a card" effect. (`faq:Does the Rowdy mood let the Hundreds draw more cards when they use the Charm Offensive card`) (`faction:warlord$14.7.6`)

### When do I declare Looters — before or after the defender declares ambush?

**Q:** Sequence of Looters vs. ambush declaration?
**Resolution:** The Hundreds player declares Looters first. Then the defender may or may not play an ambush card. (`faq:Do I declare whether I'm using my Looters before or after the defender declares that they are ambushing`) (`faction:warlord$14.2.5`)

### Can the Hundreds oppress with a mob token and no warrior?

**Q:** Does a lone mob token in a clearing satisfy "has a Hundreds piece" for Oppress?
**Resolution:** Yes. A mob token is a Hundreds piece (`faction:warlord$14.6.2`). As long as you rule the clearing and no enemy pieces are present, you score oppression with a mob alone.

---

## Reference Index

- **Faction citation key:** `faction:warlord`
- **Primary rule section:** `rule:14.`
- **Faction-specific rules:** `faction:warlord$14.2.1` through `faction:warlord$14.7.8`

**Relevant glossary entries:**
- `item:boot`, `item:sack`, `item:coin` — Command-track Hoard items
- `item:hammer`, `item:tea`, `item:sword`, `item:crossbow` — Prowess-track Hoard items
- `item:Rule` — how rule is determined (warriors + buildings; tokens and pawns do not count)

**Hireling forms (Marauder Expansion):**
- Flame Bearers (`card:ROOT-192 (Marauders)`) — the large Hundreds-flavored hireling
- Rat Smugglers (`card:ROOT-193 (Marauders)`) — the small Hundreds-flavored hireling

**Cross-faction interactions:**
- Favor cards do not remove the warlord (`faq:Do the Favor... cards really remove all enemy pieces from those clearings`)
- Riverfolk Mercenaries in your clearing count as enemy pieces and block Oppress
- Woodland Alliance sympathy tokens block Oppress (an enemy token in the clearing breaks oppression). Raze removes all enemy buildings and tokens in mob clearings (`faction:warlord$14.4.1`) — sympathy tokens are tokens, so a mob in a sympathetic clearing will raze the sympathy token on your next Birdsong. The Alliance counters this by spreading sympathy ahead of your mob chain.
- Vagabond cannot be looted (`faction:warlord$14.2.5`)
- The warlord cannot be removed by non-battle effects from any faction, including those that say "remove all enemy pieces" (`faction:warlord$14.2.2`)
