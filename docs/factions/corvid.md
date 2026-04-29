# Corvid Conspiracy

## At a Glance

**Identity:** You place hidden plot tokens across the map and score an escalating burst of points each time you flip one face-up — the more plots already revealed, the more a single flip is worth.

| Attribute | Value |
|---|---|
| Reach | 3 |
| Complexity | High |
| Scoring tempo | Burst / punctuated |
| Color | Purple (`#925da5`) |
| Faction icon | `faction-corvid` |
| Citation key | `corvid` |
| Primary rule section | `rule:13.` |

**Setup constraints:** You do not start in a corner. You scatter one warrior into any clearing of each suit — fox, rabbit, and mouse — for a total of three warriors spread across the map (`faction:corvid$13.3.2`).

---

## Win Condition

### Standard 30 VP Route

Your points come from flipping plots. When you flip a plot face-up in Birdsong, you score one victory point per face-up plot token currently on the map, counting the one you just flipped (`faction:corvid$13.4.2`). That means the first flip is worth 1 point, the second flip is worth 2, the third worth 3, and so on — as long as earlier tokens remain face-up. The math compounds steeply: flipping all eight plots in sequence, with each prior token still on the map, yields 1+2+3+4+5+6+7+8 = 36 points. In practice you will never achieve that theoretical ceiling, but it illustrates why your power grows with plot density. Your secondary scoring comes from crafting items and from removing enemy buildings and tokens in battle (`rule:3.2.1`, `rule:3.2.2`).

### Dominance Card Path

You can activate a dominance card during Daylight when you have at least 10 victory points (`rule:3.3.1`). The Corvids have no special interaction with dominance; you play one like any other faction. Because your scoring is burst-oriented and you start weak, dominance is a niche route — you need 10 VP on the track first, and reaching that mark slowly can leave you exposed. Community players note that dominance is rarely the right call unless an opponent is far ahead and a VP race is already lost.

### Scoring Tempo

Your tempo is **punctuated burst**. Early turns are slow: you spread warriors, plant plots, and build toward a critical mass. Once three or four plots are face-down on the map and you have a hand full of cards, a single Birdsong can swing 10 or more points. The faction can feel weak for many rounds and then rapidly surge to the front, which makes you simultaneously hard to read and hard to slow down once momentum is established.

---

## Setup

### Step-by-Step Placement

1. Gather 15 warriors and 8 plot tokens, all face-down (`faction:corvid$13.3.1`).
2. Place 1 warrior in any clearing of each suit — fox, rabbit, and mouse — for a total of three warriors (`faction:corvid$13.3.2`). You may choose any clearing of each suit; you are not restricted to a particular part of the map.

### Setup Theory

**Corner choice:** You have no corner; this is a significant structural fact. Unlike the Marquise, Eyrie, or Underground Duchy, you begin dispersed and without a home territory. This means you have no natural defensive anchor, no safe recruiter base, and no head start in any particular region. Treat your three starting warriors purely as plot-seed vectors: get them into clearings where you want your first plots, not clearings that feel "strategic" in the traditional sense.

**Suit distribution:** Since you recruit by suit, the clearings you start in determine which suits you can reinforce on turn one. A common approach is to begin in the three clearings closest to the center of the map across all three suits, giving you the flexibility to reach any quadrant quickly. If the map has a cluster of same-suit clearings in one area, seeding the edge of that cluster can let a single recruit action flood you with warriors cheaply.

**Neighbor considerations:** You want neighbors who are too busy fighting each other to spend actions guessing your plots. The Woodland Alliance and Eyrie Dynasties both have strong incentives to contest your clearings for their own reasons, and both have high action efficiency — they may find time to Expose you. Slower, more building-focused factions (Marquise, Underground Duchy) are less likely to dedicate actions to exposure attempts early. The Vagabond's Steal action does not interact with Exposure directly, but a Vagabond with many items and cards in hand can make multiple Exposure attempts cheaply.

**Opening hand priorities:** You want cards spread across multiple suits to enable flexible recruiting. A hand with two or three different suits lets you place warriors in multiple clearings on turn one. Bird cards are especially valuable for recruiting because spending a bird lets you choose one suit and flood an entire suit's clearings (`faction:corvid$13.4.3`). Discard duplicates of a suit you already cover heavily if they don't also craft something useful.

---

## Faction Rules & Abilities

### Plot Tokens

You have eight plot tokens, two of each type: bomb, snare, extortion, and raid (`faction:corvid$13.2.2`). While in your supply they are face-down (feather side up). Once placed on the map, a token can be face-down (still showing the feather) or face-up (showing its unique icon) (`faction:corvid$13.2.2.1`). You — and only you — can inspect any face-down plot token on the map at any time. Each clearing can hold at most one plot token (`faction:corvid$13.2.2.2`).

**Token types:**

- **Bomb** — when flipped, removes all enemy pieces from its clearing, then the bomb itself is removed (`faction:corvid$13.7.1`). This is a one-use area clear.
- **Snare** — while face-up, enemy pieces cannot be placed in or moved from its clearing (`faction:corvid$13.7.2`). This is an ongoing lockout effect that persists until the snare is removed.
- **Extortion** — when flipped, takes a random card from each enemy player with faction pieces in its clearing (`faction:corvid$13.7.3`). While face-up, you draw one additional card in Evening.
- **Raid** — when removed (face-up or face-down, by any means except Exposure), places one warrior in each clearing adjacent to the clearing from which the raid was removed (`faction:corvid$13.7.4`). If a raid token is removed by Exposure, this effect is suppressed (`faction:corvid$13.2.4`).

### Nimble

You can move regardless of who rules your origin or destination clearing (`faction:corvid$13.2.3`). The standard movement rule requires that you rule either the origin or destination (`rule:4.2.1`); Nimble removes that constraint entirely. You can move through or into heavily contested clearings without needing to fight your way to rule first. This is a permanent, unconditional ability.

### Exposure

Any number of times during their own turn, an enemy who has faction pieces in a clearing with one of your face-down plot tokens may attempt to guess its type. They show you a card matching the suit of that clearing and name a plot type. If wrong, they hand you the card — a net gain for you. If correct, they remove the plot token and score one victory point. If the removed token is a raid, the raid's warrior-placement effect does **not** trigger (`faction:corvid$13.2.4`).

Exposure is constrained to the enemy's own turn and cannot be used once the enemy begins the last step of their turn (`faction:corvid$13.2.4`, `rule:1.4.3`). It also cannot be used to interrupt another action (`rule:1.4.2`).

**Practical implication:** Exposure is the primary mechanic that disciplines your plot placement. Spread plots into clearings where opponents have few or no warriors, or into clearings where opponents cannot afford to spend cards on guessing (because they need those cards for their own faction mechanics). An opponent who guesses wrong gives you a free card — this is not always a bad outcome, and you can sometimes afford to let enemies try in order to fatten your hand.

### Embedded Agents

When you are the defender in battle and you have a face-down plot token in the clearing of battle, you deal an extra hit — even if you are defenseless (have no warriors there) (`faction:corvid$13.2.5`). This is an after-roll extra hit (`rule:4.3.5.1`). It interacts directly with the defenseless rule: normally, a defender with no warriors deals zero hits from rolling (`rule:4.3.3.1`), but Embedded Agents adds one extra hit on top of that (`rule:4.3.5.1`).

**Key edge case:** Embedded Agents requires a face-**down** token. If your only token in that clearing has been flipped face-up, the bonus does not apply.

### Crafting

You craft during Birdsong by activating plot tokens, whether face-up or face-down (`faction:corvid$13.2.1`). Each activated plot token contributes its clearing's suit toward crafting costs. A token can be activated for crafting without being flipped.

---

## Turn Structure

### Birdsong

Your Birdsong has three mandatory steps resolved in order (`rule:13.4.` pretext):

**1. Craft** (`faction:corvid$13.4.1`)

Activate any plot tokens (face-up or face-down) to craft cards from your hand. Plot tokens contribute the suit of their clearing. You do not flip them or score points by activating them for crafting.

**2. Flip Plots** (`faction:corvid$13.4.2`)

This is your primary scoring step. Any number of times, you may flip a face-down plot token face-up, provided you have at least one Corvid warrior in that clearing. Each time you flip:
1. Score one VP per face-up plot token currently on the map, including the one you just flipped.
2. If the token is a bomb or extortion, resolve its flip effect immediately.

You may flip multiple tokens in a single Birdsong. You choose the order. Because scoring scales with the current count of face-up tokens, flipping multiple in sequence means earlier flips score at a lower value than later flips.

**Ordering matters:** If you flip a bomb first, it removes enemy pieces in that clearing and then removes itself. That token is gone before subsequent flips, so the bomb does not count toward VP scoring for those later flips. Flip non-removing tokens first if you want them to count toward subsequent flip scores.

**3. Recruit** (`faction:corvid$13.4.3`)

Once per Birdsong, you may spend any one card to place one warrior in each clearing matching the card's suit. If you spend a bird card, choose one suit; bird cards do not give multi-suit placement. Recruiting is optional.

### Daylight

You may take up to three actions in any order and number (`rule:13.5.` pretext):

**Move** (`faction:corvid$13.5.1`): Take a standard move. Your Nimble ability means you need not rule either clearing.

**Plot** (`faction:corvid$13.5.2`): Place a face-down plot token in a clearing that currently has no plot token. Cost: remove one Corvid warrior from that clearing, plus one additional warrior for each plot you have already placed this turn. The first plot costs 1 warrior, the second costs 2 additional warriors (3 total removed), the third costs 3 additional warriors (6 total removed). Placing multiple plots in one Daylight is costly and requires forward planning with warrior reserves.

**Battle** (`faction:corvid$13.5.3`): Initiate a battle.

**Trick** (`faction:corvid$13.5.4`): Swap two plot tokens on the map. Both tokens must share the same facing — either both face-up or both face-down. You cannot use Trick to flip a token; it only swaps position.

### Evening

Your Evening has two steps, resolved in order (`rule:13.6.` pretext):

**Exert** (`faction:corvid$13.6.1`): You may take one of the Daylight actions listed above. If you do, you skip the Draw step entirely this Evening.

**Draw** (`faction:corvid$13.6.2`): Draw one card, plus one card per face-up extortion token currently on the map. Then discard down to five cards if you have more.

The choice between Exert and Draw is your most frequent tactical decision. Drawing cards fuels recruiting and hand size; Exerting gives an extra action when you need to plot, move, or battle at a critical moment.

---

## Scoring Engine

| VP Source | Amount | Trigger | Timing |
|---|---|---|---|
| Flip a plot token | 1 per face-up token on map (incl. flipped) | Flip step in Birdsong | Birdsong |
| Remove enemy building | 1 per building | Enemy piece removed in battle | Daylight (battle) |
| Remove enemy token | 1 per token | Enemy piece removed in battle | Daylight (battle) |
| Craft an item | Per card's VP listing | Crafting | Birdsong (crafting) |
| Expose attempt fails | 0 VP directly; gain a card | Enemy guesses wrong | Enemy turn |

The flip economy is the heart of your engine. Each face-up token on the map raises the value of every subsequent flip. Extortion tokens add a secondary benefit: each face-up extortion token increases your Evening draw by one, improving hand size and thus recruiting capacity. A face-up extortion token in a contested clearing that you never remove can provide a steady card-draw bonus for multiple turns.

Snare tokens contribute indirectly: locking a clearing prevents enemies from using it, which can protect adjacent clearings where you have warriors or unflipped plots. Raid tokens contribute through warrior economy: when removed (not via Exposure), they seed adjacent clearings with warriors, letting you spread without spending actions.

---

## Playbook

### Opening

**Turns 1–2 priorities:**

Your first Birdsong recruit is critical. You start with three warriors and three cards. Spend a card on turn one to put two or three warriors in a suit cluster where you intend to place your first plots. Avoid overcommitting to one region — your warriors are both plot currency and defenders.

Plot on turn one if you can do so at a reasonable warrior cost. The first plot costs one warrior (`faction:corvid$13.5.2`). Placing even one face-down token early gives you crafting suits, Embedded Agents protection in that clearing, and sets up a scoring spike. The longer you wait to place your first plot, the further behind on tempo you fall.

Target clearings where opponents have no warriors to begin with. A face-down token in an empty clearing is safe from Exposure and costs opponents an action and a card to check. Clearings near your starting warriors are the natural first targets.

**Opening hand reads:** If you have a bird card and warriors spread across multiple suits, leading with a recruit action before plotting lets you reinforce before spending the warrior. If you already have two warriors in a clearing and a matching card, plot on action one, then recruit on action two to reload the clearing.

### Mid-Game Pivots

The mid-game for the Corvids is about increasing plot density without bleeding warriors faster than you can recruit.

**Plot density threshold:** Three to four face-down plots on the map is the critical mass where a flip burst becomes threatening. Below three, single flips score too few points to be dangerous. Above four, opponents have strong incentives to start guessing actively, and you may lose tokens to Exposure before you can flip them.

**Signs to pivot toward flipping:** If two or more opponents have warriors in your plot clearings and are holding cards matching those suits, your plots are at risk. Flip them before they are exposed, even if the score is lower than you planned. A plot removed by Exposure returns to your supply and costs you time to replace; a flip on your own schedule always nets you points.

**Signs to hold plots:** If opponents are distracted — fighting each other, building in other regions, low on hand cards — hold. Wait until you can place a fourth or fifth plot to maximize the scoring spike.

**Extortion timing:** Flip extortion tokens when enemy players have large hands and faction pieces in the clearing. An extortion flip against three players with four cards each steals three cards and scores points. Timing this for after another faction's crafting phase (when their hand is full) is ideal.

**Bomb placement:** Place bombs under pressure. If an enemy is massing warriors in a clearing adjacent to your plots, plant a bomb in their path. Flip it in Birdsong to clear the clearing, scoring points and removing the threat simultaneously.

**Trick as misdirection:** Use Trick to swap face-down tokens into or out of contested clearings. If an opponent is about to correctly guess a snare in a high-value clearing, trick it with a cheap token you care less about. The opponent guesses a different type and potentially wastes the card. Note: both tokens must share the same facing (`faction:corvid$13.5.4`).

### Endgame Routes

When you have four or more face-up plots on the map, each new flip is worth at least 5 VP. The race to 30 at that point is often a single Birdsong.

**Finisher pattern:** Spend the turns before your winning Birdsong planting as many face-down tokens as your warrior economy allows. Use Exert for a fourth action if you need to. On your scoring turn, flip all available face-down tokens in order — non-removing types first, then bomb last if used — maximizing the running count for each flip.

**Protecting the spike:** Before your winning turn, use snares to lock contested clearings and prevent opponents from moving warriors in to attempt Exposure. If you have only one flip left before 30, opponents may try to race you by attacking your warriors or plotting clearings. Battle defensively and use Embedded Agents deterrence.

**Raiding as endgame fuel:** If you are short on warriors for the final plot push, look for raid tokens already on the map. Deliberately removing a raid token — by battling or any other means — seeds adjacent clearings with warriors (`faction:corvid$13.7.4`), which you can immediately use to plot. Chaining a raid removal into a new plot placement on the same turn is an efficient way to stretch a thin warrior supply.

---

## Threat Factions

### Woodland Alliance

The Alliance's Outrage mechanic punishes you for moving warriors into sympathetic clearings (`faction:woodland$8.2.6`). You do not trigger Outrage by placing plots — plots are tokens, not warriors — but your recruit and move actions frequently bring warriors into contested regions. Once the Alliance has spread sympathy, your ability to cheaply reinforce clearings narrows. More critically, the Alliance can build officers and take many actions, including battles that remove your plot tokens and score VP from building removal (`rule:3.2.1`). The Alliance also has strong card draw from Outrage itself, giving them resources to make Exposure attempts.

**Counter-plays:** Plant plots in sympathetic clearings to generate cards from failed Exposure (the Alliance's hand is usually large). Use snares to lock clearings before the Alliance can march or revolt. Target Alliance bases with bombs, since base removal scores points and disrupts their entire operation.

### Eyrie Dynasties

The Eyrie's Decree can force a large number of moves and battles in a single turn. A fully committed Eyrie player may battle through multiple clearings in one Daylight, removing warriors you need for plot placement. Their Lords of the Forest ability means they rule easily across the map, making it harder for you to find clearings where you can plot safely without facing eventual Eyrie pressure (`faction:eyrie$7.2.2`). The Eyrie also has solid card draw through the Decree, giving them resources for Exposure.

**Counter-plays:** The Eyrie must commit to every card in their Decree column or go into Turmoil. If you can disrupt one key clearing — perhaps with a bomb or snare — you can force Turmoil, which removes all their Decree cards, costs them VP, and sets them back substantially. Snare tokens in clearings the Eyrie needs to access for their Decree are particularly punishing. Picking off isolated Eyrie warriors in battles where you have Embedded Agents backup is also a strong defensive play.

### Vagabond

The Vagabond's ability to move freely into forests and take Steal actions (`faction:vagabond$9.5.6`) gives them flexible positioning. A Vagabond with a large item inventory, particularly many swords, can deal multiple hits in battle, which threatens your warriors without those battles scaling as favorably for you. The Vagabond can also hold multiple cards of various suits, making them one of the more capable Exposure threats: they can afford to spend a card on a guess because they replenish quickly. Additionally, if the Vagabond goes Hostile with you, they gain Infamy VP whenever they remove your warriors in battle (`faction:vagabond$9.2.9.3.1`), creating a feedback loop where attacking you benefits them directly.

**Counter-plays:** Community players recommend avoiding direct confrontation with a well-equipped Hostile Vagabond when possible — their item advantage in sustained battles usually exceeds yours. Use snares to restrict Vagabond movement (their pawn is subject to snare lockouts) and plant plots in forests or remote clearings the Vagabond is unlikely to visit. Staying on good terms with the Vagabond early — giving them no reason to go Hostile with you — is often the simplest mitigation.

### Marquise de Cat

The Marquise fills the map with buildings and warriors, and their widespread presence means almost every clearing eventually has an enemy warrior capable of Exposure attempts. More concretely, the Marquise's Field Hospitals (`rule:6.2.3`) mean warriors removed by your bombs return to the keep clearing rather than the supply, partially blunting bomb efficiency. A Marquise with many recruiters will outpace your warrior supply in a prolonged war of attrition.

**Counter-plays:** Bomb the Marquise's building clusters: the VP you score from building removal is real, and the board presence it erases is significant. Place plots in clearings without Marquise buildings, since those clearings have fewer warriors and less Marquise incentive to check. Snares can prevent the Marquise from marching to reinforce a threatened clearing, buying time before your flip turn.

---

## Card Priorities

### Top Priority: Craft These

**Stand and Deliver!** (`card:ROOT-102 (Base Game)`) — In Birdsong, take a random card from an enemy (they score 1 point). You already take cards from failed Exposure attempts and from extortion flips; this persistent effect adds a reliable hand-building mechanism every single turn. Your faction constantly needs cards for recruiting, and a robust hand is your biggest limitation. The opponent's 1 VP is usually worth it.

**Tax Collector** (`card:ROOT-105 (Base Game)`) — Once in Daylight, remove one of your own warriors from the map to draw a card. The Corvids frequently have warriors they need to convert into plots anyway; Tax Collector lets excess warriors double as card draws. Particularly valuable in clearings where you have more warriors than you need after plotting.

**Codebreakers** (`card:ROOT-61 (Base Game)`) — Once in Daylight, look at another player's hand. This turns Exposure from a guessing game into a knowledge game. When you know an opponent is holding a fox card and your fox-clearing plot is a snare, you know how to value that interaction. Codebreakers is expensive (a two-suit craft cost) but the information advantage is disproportionate to its price.

**Corvid Planners** (`card:ROOT-64 (Exiles & Partisans Deck)`) — While moving, ignore rule. This overlaps with your innate Nimble ability (`faction:corvid$13.2.3`) if playing the Exiles & Partisans deck. Nimble already covers your faction warriors' movement; Corvid Planners would be redundant if Nimble is fully operational. Note for table context: in games with the base deck only, this card is not available.

**Informants** (`card:ROOT-79 (Exiles & Partisans Deck)`) — In Evening, if you would draw cards, you may instead take one ambush card from the discard pile. Ambush cards double as hand manipulation and emergency defensive tools. Since you sometimes forgo draws via Exert, the option to take from discard is more flexible than it sounds.

### Situational

**Armorers** (`card:ROOT-51 (Base Game)`) — In battle, discard to ignore all rolled hits taken. Your defense is generally thin, and this card provides a one-time save in a pivotal battle. Worth crafting if you anticipate a specific large attack you cannot avoid.

**Sappers** (`card:ROOT-94 (Base Game)`) — As defender, deal an extra hit. Stacks with Embedded Agents if you have a face-down plot in the clearing. Together they can swing a defensive battle significantly, but Sappers is a discard effect and Embedded Agents is persistent — don't rely on the combo regularly.

**Better Burrow Bank** (`card:ROOT-55 (Base Game)`) — At start of Birdsong, draw one card; choose an enemy to also draw one card. Card-for-card exchange is usually even, but if your hand is small and you need fuel for recruiting, this can help. The opponent draw can also be useful if you want a specific enemy to have more cards in hand for an extortion timing.

**Coffin Makers** (`card:ROOT-62 (Exiles & Partisans Deck)`) — Score one point per five warriors removed from the map at start of each Birdsong. In a game with heavy fighting, this can add up. Less useful to you specifically since your warriors should be staying on the map as plot guards and recruiters, but in high-combat tables it occasionally contributes.

### Skip or Low Priority

**Royal Claim** (`card:ROOT-92 (Base Game)`) — Score one point per clearing you rule at the start of Birdsong. The Corvids typically do not rule many clearings; plot tokens are tokens and do not contribute to rule (`rule:2.6`). This card rewards factions that commit to building up ruling presence, which is not your game plan.

**Brutal Tactics** (`card:ROOT-58 (Base Game)`) — As attacker, deal an extra hit but defender scores one point. You rarely want to give opponents free VP; your scoring is tight enough that charity is costly.

### Ambush Hold vs. Play

Hold ambush cards as long as possible. Your Embedded Agents ability already gives you one extra defensive hit when you have a face-down token present; an ambush stacked on top of that can make attacking you extremely costly. The deterrence value of a held ambush is real — opponents who know you might have both Embedded Agents and an ambush may choose not to battle you at all.

Play an ambush reactively when you need to survive a critical attack that would otherwise remove the warriors guarding a key plot.

### Dominance Considerations

Activating a dominance card is rarely your primary plan. Your scoring engine, when it fires, can produce 10+ points in a single turn; a slow dominance march is usually inferior to a well-timed flip burst. Consider dominance only if you are being heavily Exposed (losing plots faster than you can replace them) and a VP race is no longer viable. Bird dominance — ruling two opposite corners — is particularly difficult for a faction without a corner anchor.

---

## Common Pitfalls

**Planting plots where enemies have warriors.** Your plots are vulnerable to Exposure from the moment you place them. A face-down token in a clearing full of enemy warriors is a guessing-game gift; opponents can afford to try repeatedly on their turns since a wrong guess costs a card (which they gain back over time), and they only need one correct guess to remove the token.

**Over-investing warriors into a single region.** The Plot action's escalating warrior cost means your second plot of the turn is expensive (`faction:corvid$13.5.2`). Spending all your warriors in one region to place two plots in one Daylight can leave you with no warriors for recruits or defense. Spread and pace your plotting.

**Neglecting recruiting.** Without warriors in matching clearings, you cannot plant plots, and without cards you cannot recruit. The faction is easy to starve: one bad stretch of low hand size → no recruiters → no warriors → no plots → stalling engine. Keep your hand replenished and prioritize recruiting before plotting when both are available.

**Flipping too early.** Flipping a single plot scores 1 VP. Flipping three in one Birdsong (with the others already face-up) scores 3+4+5 = 12 VP. Patience multiplies your scoring dramatically. The temptation to flip on the first available Birdsong is the most common beginner error.

**Flipping too late.** Holding all eight plots face-down is just as dangerous as flipping too early. Opponents who see your board state — warriors spread across many clearings, no face-up plots — know your burst is coming and will attempt Exposure aggressively as soon as they read your timing. Spread flips across a few turns rather than building to a single all-or-nothing turn.

**Ignoring the Exert/Draw tradeoff.** Reflexively drawing every Evening wastes the Exert action in situations where a fourth Daylight action would have been decisive. Conversely, Exerting every turn starves your hand and kills recruiting. Read each Evening on its merits.

**Misusing Trick.** Trick requires both tokens to share the same facing. You cannot use it to flip a face-down token into a cleared location by swapping with a face-up token. Forgetting this constraint mid-game leads to wasted actions.

---

## Mechanic Clarifications

**Can I inspect my own face-down tokens at any time?**
Yes. You can look at any face-down plot token on the map at any time (`faction:corvid$13.2.2.1`). You are never confused about what you have placed.

**Can an enemy attempt Exposure when I have no warriors in the clearing?**
Yes. Exposure requires only that the enemy has faction pieces in the clearing and that there is a face-down plot token there (`faction:corvid$13.2.4`). There is no requirement for Corvid warriors to be present.

**Does a removed Raid token place warriors when exposed by an enemy?**
No. The Raid's warrior-placement effect specifically does not trigger if the raid is removed by Exposure (`faction:corvid$13.2.4`). The suppression is explicit in the Exposure text: "if this removes a Raid token, it does not place warriors."

**Can I use Embedded Agents if my only piece in the clearing of battle is a face-down plot token and no warriors?**
Yes. Embedded Agents applies "even defenseless" (`faction:corvid$13.2.5`). A defenseless defender normally deals zero hits from rolling (`rule:4.3.3.1`); Embedded Agents adds one extra hit on top of zero. You still deal one hit total as long as a face-down token is present.

**Does Snare prevent the Corvids themselves from moving into or out of the clearing?**
No. Snare says "enemy pieces cannot be placed in or moved from its clearing" (`faction:corvid$13.7.2`). Corvid pieces are not enemies of the Corvids. Your own warriors are free to enter or leave a snarred clearing.

**Can I flip a plot token in a clearing where I have no warriors?**
No. Flipping requires "any Corvid warriors" in the clearing (`faction:corvid$13.4.2`). You must have at least one warrior present to flip.

**Does Bomb score points for the Corvids for the pieces it removes?**
No. The Bomb removes enemy pieces — it is not a battle — so the standard rule that you score for removing enemy buildings and tokens in battle (`rule:3.2.1`) does not apply. You score only the flip VP from the flip action itself.

**When a Bomb is flipped, does the Bomb itself count toward the VP scoring?**
The flip scores one VP per face-up plot on the map. The Bomb is flipped (becomes face-up), that flip is resolved, and then the Bomb is removed. The flip effect (remove enemies + remove bomb) resolves after scoring, so the Bomb does count toward the VP total of its own flip. It does not count toward future flips because it is immediately removed.

**Can I use Trick during Daylight and Exert during Evening to perform Trick twice in one turn?**
Yes. Trick is a Daylight action, and Exert lets you take one Daylight action during Evening. If you Trick in Daylight and then Exert Trick in Evening, you resolve Trick twice. Note that Exerting costs you the Evening draw (`faction:corvid$13.6.1`).

**Does Exposure require the guessing player to be in the clearing themselves, or just have faction pieces there?**
Any faction piece suffices — warriors, buildings, tokens, or pawns. The rule says "an enemy with faction pieces" (`faction:corvid$13.2.4`), not specifically warriors.

---

## Reference Index

**Faction citation key:** `corvid`

**Primary rule section:** `rule:13.`

**Subsection map:**

| Rule | Content |
|---|---|
| `faction:corvid$13.2.1` | Crafting |
| `faction:corvid$13.2.2` | Plot Tokens |
| `faction:corvid$13.2.2.1` | Token Facing |
| `faction:corvid$13.2.2.2` | Placement Limits |
| `faction:corvid$13.2.3` | Nimble |
| `faction:corvid$13.2.4` | Exposure |
| `faction:corvid$13.2.5` | Embedded Agents |
| `faction:corvid$13.3.1` | Setup Step 1 |
| `faction:corvid$13.3.2` | Setup Step 2 |
| `faction:corvid$13.4.1` | Birdsong: Craft |
| `faction:corvid$13.4.2` | Birdsong: Flip Plots |
| `faction:corvid$13.4.3` | Birdsong: Recruit |
| `faction:corvid$13.5.1` | Daylight: Move |
| `faction:corvid$13.5.2` | Daylight: Plot |
| `faction:corvid$13.5.3` | Daylight: Battle |
| `faction:corvid$13.5.4` | Daylight: Trick |
| `faction:corvid$13.6.1` | Evening: Exert |
| `faction:corvid$13.6.2` | Evening: Draw |
| `faction:corvid$13.7.1` | Bomb token |
| `faction:corvid$13.7.2` | Snare token |
| `faction:corvid$13.7.3` | Extortion token |
| `faction:corvid$13.7.4` | Raid token |

**Related general rules:**

- `rule:2.5` — Rule (definition of ruling a clearing)
- `rule:3.2.1` — Scoring for removing enemy buildings
- `rule:3.2.2` — Scoring for crafting items
- `rule:3.3.1` — Activating dominance cards
- `rule:4.2.1` — Standard movement (You Must Rule)
- `rule:4.3.3.1` — Maximum rolled hits (defender cap)
- `rule:4.3.5.1` — Extra hits
- `rule:1.4.2` — Interrupts rule
- `rule:1.4.3` — End of Turn (Exposure timing restriction)

**Related glossary entries:**

- `item:sword`, `item:crossbow` — relevant items for crafting priorities
- Pieces (general definitions): `rule:1.5`

**Hireling form:** The Corvid Conspiracy does not have a hireling listed in the p16 Law.

**Cross-faction interactions:**

- Woodland Alliance Outrage (`faction:woodland$8.2.6`) — triggered by moving Corvid warriors into sympathetic clearings, not by placing plot tokens.
- Vagabond Infamy (`faction:vagabond$9.2.9.3.1`) — if Vagabond is Hostile with Corvids, they gain VP for removing Corvid warriors in battle.
- Marquise Field Hospitals (`rule:6.2.3`) — warriors removed by Bomb return to keep clearing, not supply, limiting the Bomb's board-clearing value against Marquise.
- Favor of the Foxes / Mice / Rabbits cards — these remove all enemy pieces in clearings of a suit, which would include your plot tokens if you are "an enemy" of the player playing the card. Your warriors and plots are removed; you do not score from your own token being removed this way.
