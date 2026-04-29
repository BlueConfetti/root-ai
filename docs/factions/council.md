# Twilight Council

## At a Glance

**Identity**: You score by placing your assemblies in the right clearings and ruling them — not by running an army.

| | |
|---|---|
| **Reach** | 4 |
| **Complexity** | High |
| **Scoring tempo** | Slow-burn into punctuated bursts |
| **Color** | Brown (#944A2E) |
| **Icon** | faction-council |
| **Faction citation key** | `faction:council` |
| **Primary rule section** | `rule:17.` |

**Setup constraint**: Choose one corner clearing as your starting clearing and place 4 warriors there. Place 2 warriors in any other clearing — your choice of clearing is free (`faction:council$17.3.2`). You begin with all 6 assemblies on your Assemblies track.

The Twilight Council is a faction built around **assemblies** — tent-shaped pieces you deploy to clearings that carry governance authority over them. Your Birdsong is a card-reveal engine that generates movement, warriors, new assemblies, and battles. Your Evening converts those revealed cards into governing power, hands you a crafting window, and — through the Oversee step — scores you points based on how many Governing assemblies share clearings with enemy buildings or tokens. Your warrior pool of 20 (`faction:council$17.3.1`) is generous, but your board presence is only as valuable as the assemblies it supports.

---

## Win Condition

### Standard 30 VP Route

You score victory points through the Oversee step of Evening (`faction:council$17.6.4`): for each Governing assembly in a clearing that contains any enemy building or token, you score on a step scale — one Governing assembly with enemy presence scores 1 VP, two or three score 2 VP, four score 3 VP, five or six score 4 VP. Enemy buildings and tokens in a clearing count as a single condition; the number of them doesn't multiply the reward, but the number of qualifying Governing assemblies does.

You also score 1 VP incidentally during the Empower action when you rule the assembly in question (`faction:council$17.5.1.3`), and you score a point any time an enemy removes one of your assemblies via the standard rule about removing enemy buildings and tokens (`rule:3.2.1`) — though you also lose a Loyalist when that happens (`faction:council$17.2.2`).

Scoring 2–4 VP per Evening through Oversee is a realistic target once you have multiple Governing assemblies positioned alongside active enemy construction. Getting to 4 VP per turn means having four or more Governing assemblies with enemy presence, which requires both board spread and enemy cooperation in building near you.

### Dominance Card Path

You can activate a dominance card (`rule:3.3.1`) during Daylight once you have at least 10 VP. The Council has no faction ability that interacts distinctively with dominance; the path is viable but unremarkable. You lose your score marker and shift to a board-control win condition. Given that your scoring engine rewards passive coexistence with enemy buildings rather than clearing dominance, the dominance path cuts against your natural game plan and should be considered only when VP accumulation is stalled and board control is already in hand.

### Coalition Path

Not available — the Vagabond coalition rule applies only to the Vagabond (`rule:3.3.1`, `rule:9.2.8`).

### Tempo Classification

Slow-burn into punctuated. Early turns you are assembling infrastructure: placing assemblies, building your Loyalist pool, maneuvering for position. Scoring from Oversee is modest until you have Governing assemblies in clearings with real enemy presence. Once that infrastructure is in place — typically turns three or four — scoring can accelerate noticeably as multiple assemblies qualify each Evening.

---

## Setup

### Step-by-Step Placement

**Step 1**: Form a supply of 20 warriors (`faction:council$17.3.1`).

**Step 2**: Place 4 warriors in a corner clearing — this is your starting clearing. Place 2 warriors in any different clearing (`faction:council$17.3.2`).

**Step 3**: Fill your Assemblies track with your 6 assemblies (`faction:council$17.3.3`). All start on the track, not on the board.

### Setup Theory

**Corner choice**: You want to set up adjacent to clearings where enemy factions will build — your Oversee score depends on Governing assemblies being in clearings with enemy presence. Corners that are geographically close to militaristic factions (Marquise, Eyrie) are often better than isolated corners. You do not need a corner with any particular suit for your opening, since Birdsong card-reveals give you flexibility regardless of your starting suit.

**The second clearing**: The two warriors in a non-starting clearing are a meaningful early investment. Placing them in a clearing adjacent to your corner lets you rule that clearing immediately, which helps you Assemble there next Birdsong without discarding the revealed card (`faction:council$17.4.3`). Alternatively, placing them in a central clearing can establish a foothold where multiple factions converge — exactly where you want Governing assemblies to be.

**Neighbor considerations**: Being next to the Marquise or Eyrie is good for your Oversee score. They build frequently and reliably. Corvid Conspiracy, whose plot tokens count as buildings, also qualifies. Avoid starting directly beside the Woodland Alliance if you can — Sympathy tokens trigger Outrage (`rule:8.2.6`) when you move through their clearings, which taxes your Birdsong mobility, and the Alliance often avoids your clearings once governing restrictions apply.

**Opening hand priorities**: You want a mix of suits to maximize Birdsong flexibility. A hand with three different suits lets you take three different actions in Birdsong across three clearings. Bird cards are valuable as Empower fuel in Evening, so hold at least one if you have it. Discard cards whose suits don't match any clearing you can currently reach — a card you can't reveal does nothing.

---

## Faction Rules & Abilities

### Loyalists

You can hold up to 4 warriors on your player board as Loyalists (`faction:council$17.2.1`). Loyalists enter your pool through Entreat (`faction:council$17.2.4`) and Assemble (`faction:council$17.4.3`); you can remove them from the pool at any time and return them to your supply.

Loyalists are a buffer reserve. When you place an assembly in a clearing you don't rule (Assemble action), you may place any number of Loyalists at that assembly at the same time (`faction:council$17.4.3`), bolstering your warrior presence to contest or claim rule without spending additional card reveals.

**Edge case**: The Loyalist pool maximum is 4. If you have 4 Loyalists and an action would let you gain another, you simply cannot (the pool is full). Plan your Loyalist intake accordingly.

### Assemblies

Assemblies have two sides: Closed (closed tent) and Governing (open tent) (`faction:council$17.2.2`). They start on your Assemblies track; you place them via the Assemble action. When an enemy removes one of your assemblies, you lose 1 Loyalist (`faction:council$17.2.2`).

Assemblies return to your track when removed, not to a permanent discard. Your total stock of 6 is recoverable. However, losing Loyalists when assemblies are destroyed creates a compounding disadvantage: fewer Loyalists means less flexibility when deploying future assemblies into contested clearings.

### Governors

At any Governing assembly, enemies of the Council cannot activate crafting pieces and cannot place, take, remove, or flip pieces, except in battle (`faction:council$17.2.3`). The Vagabond is specifically noted: since the Vagabond's pawn is its crafting piece, the Vagabond cannot craft at a Governing assembly.

This is your primary pressure tool. The ability to lock enemies out of placing or building in a clearing is significant — it blocks the Marquise from building sawmills, the Duchy from scouting, the Corvids from placing plot tokens, and any faction from removing their own pieces outside of battle. Factions cannot voluntarily interact with their pieces at your Governing assemblies except by fighting.

**Edge case**: "Except in battle" means that combat in the clearing is unaffected. Governing restriction is purely an action restriction. It does not prevent routing from battle, ambush plays during a battle, or any effect that resolves as part of the battle sequence.

### Entreat

Any number of times on their turn, an enemy may force you to flip any of your assemblies to Closed (`faction:council$17.2.4`). After flipping it, you may either place any number of Loyalists at that assembly, or place 1 warrior in your Loyalists.

Entreat is a pressure valve for your opponents. When your Governing assembly is strangling a faction, they can pay this cost to re-open the clearing — but you benefit too. Taking Loyalists from an Entreat lets you reload warriors onto your board, setting up a future Assemble with built-in presence. Taking the Governing restriction back in the clearing you just lost is less immediate but not nothing: you can re-assert rule and flip it Governing again in Evening (`faction:council$17.6.3`).

**Important**: Enemies initiate Entreat on their own turn, any number of times. There is no cost beyond the flip itself. Factions under heavy Governor pressure will Entreat repeatedly. Your response is to use the Loyalists you gain as fuel to quickly recontest.

### Peacekeepers

When an enemy chooses another enemy as defender in a battle at an assembly, you add your warriors at that assembly as defending warriors (`faction:council$17.2.5`). Your warriors only take hits after the primary defender's warriors have been fully removed. Ignore Peacekeepers if the Vagabond is defending.

The Peacekeepers rule means your warriors at assemblies absorb overflow hits in battles you did not initiate. This is both a protection for other factions (they are less likely to be wiped out at your assemblies) and a slow drain on your warriors. You cannot ambush, use battle effects, or otherwise actively participate — you are strictly an absorbing shield (`faction:council$17.2.5`).

**Vagabond Allies**: If the Vagabond is Allied to you (`rule:9.2.9.2`) and attacks another enemy in battle, your warriors become attacking warriors instead of defending warriors (`faction:council$17.2.5.1`). This is the one exception where your warriors can be on the offensive side.

**Edge case**: Peacekeepers applies only when an enemy chooses another enemy as the defender. If you are the target of the attack, this rule does not apply. If the Vagabond is defending, ignore Peacekeepers entirely — no Council warriors are added.

### Crafting

You craft during the Inspire step of Evening by activating assemblies (`faction:council$17.2.6`, `faction:council$17.5.2`). Each assembly contributes crafting activation matching its clearing's suit. You do not craft during Daylight like most factions. If you craft no cards in Inspire, you draw one card per card-draw icon showing on your Assemblies track instead.

---

## Turn Structure

### Birdsong

Your entire Birdsong is a card-reveal engine (`faction:council$17.4`). Any number of times, you may reveal a card from your hand, placing it face-up in your play area. Each revealed card enables exactly one of four actions:

**Move**: Take a move from a clearing matching the revealed card (`faction:council$17.4.1`). Standard movement rules apply (`rule:4.2`).

**Recruit**: Place 1 warrior in a clearing matching the revealed card (`faction:council$17.4.2`).

**Assemble**: Place a Closed assembly and any number of Loyalists in a clearing matching the revealed card that has no assembly (`faction:council$17.4.3`). If you do not rule the clearing at the time of placement, discard the revealed card.

**Battle**: Initiate a battle in a clearing matching the revealed card (`faction:council$17.4.4`). If an assembly is present in that clearing, discard the revealed card.

Key mechanic: revealed cards stay in your play area. They return to your hand in Evening during Convene Woodfolk. Cards revealed in Birdsong cannot be used for any other purposes during Birdsong — they can't be spent for Entreat or crafting, for instance.

**Tension in card management**: Every card you reveal is a card you'll return in Evening, and each return gives you one Convene action (Banish, Agitate, or Empower). Revealing more cards in Birdsong means more Convene actions in Evening. However, Assemble discards the revealed card if you don't rule the clearing, and Battle discards the card if an assembly is there. These discard conditions reduce your Evening Convene actions. Plan which actions will cost you a card and which will not.

### Daylight

Daylight is minimal: the Sleep step (`faction:council$17.5.1`). You flip any assemblies ruled by enemies to Closed. This is mandatory in the sense that it happens at the start of Daylight, and you flip all assemblies that qualify.

Sleep is your recovery mechanism. An enemy who managed to wrest rule of a clearing with your assembly will find that assembly flipped Closed — stopping them from scoring off your governance and letting you recontest.

### Evening

Evening has five steps in order (`faction:council$17.5`):

**1. Convene Woodfolk** (`faction:council$17.5.1`): Return each revealed card to your hand one by one. For each card returned, you may take one action:

- **Banish** (non-bird cards only): Initiate a battle in a clearing with a matching assembly. Defending warriors are not removed when hit — instead, force them to move to a single destination you choose, ignoring rule (`faction:council$17.5.1.1`). This counts as a single move for triggering other effects. You cannot hit buildings or tokens, and you ignore rolled hits you take (but not ambush hits or extra hits). The warlord cannot take Banish hits because it cannot move outside the Lord of the Hundreds' turn. The Vagabond cannot take Banish hits because it is not a warrior. Hirelings cannot take Banish hits because they cannot be forced to move (`rule:22.3.4`).
- **Agitate** (non-bird cards only): Spend the returned card and choose a matching assembly. Place 1 warrior in your Loyalists, then flip the assembly Governing if it is Closed (`faction:council$17.5.1.2`). You cannot gain the Loyalist if you lack a matching assembly.
- **Empower** (bird cards only): Choose an assembly. Roll one battle die and remove that many Council warriors from it. You may either place these warriors in your Loyalists, or score 1 VP if you rule the assembly (`faction:council$17.5.1.3`).

**2. Inspire** (`faction:council$17.5.2`): Activate assemblies to craft cards. If you craft no cards, draw one card per card-draw icon showing on your Assemblies track.

**3. Adjourn** (`faction:council$17.5.3`): You may remove any of your assemblies. Then flip assemblies you rule to Governing.

**4. Oversee** (`faction:council$17.5.4`): Score VP based on Governing assemblies with any enemy buildings or tokens in the same clearing:
- 1 qualifying assembly: 1 VP
- 2–3 qualifying assemblies: 2 VP
- 4 qualifying assemblies: 3 VP
- 5–6 qualifying assemblies: 4 VP

**5. Draw and Discard** (`faction:council$17.5.5`): Draw 1 card. If you have more than 5 cards, discard to 5.

**Order matters**: Adjourn comes before Oversee. You flip assemblies you rule to Governing in Adjourn, and those flipped assemblies immediately count toward Oversee scoring in the same Evening. This means clearing rule during the turn — by banishing enemies away, recruiting to outnumber, or having your enemies Entreat their assemblies closed and then you recontest — can translate into scoring before the turn ends.

---

## Scoring Engine

| VP Source | Amount | Trigger | Timing |
|---|---|---|---|
| Oversee | 1–4 VP (see scale) | Governing assemblies with enemy buildings/tokens | Evening: Oversee step |
| Empower | 1 VP | Rule the chosen assembly; roll die, remove warriors | Evening: Convene Woodfolk |
| Remove enemy buildings/tokens | 1 VP each | Standard removal rule | Any time |
| Craft items | Varies by card | Crafting item during Inspire | Evening: Inspire step |
| Enemy removes your assembly | 0 VP (enemy scores 1 VP) | Enemy action | —; you lose 1 Loyalist |

The Oversee step is your primary engine. Everything else is secondary. Empower is a minor supplement — it scores only if you rule the assembly, and the die roll removes your warriors from it, which can weaken your ruling position. Crafting is situational. You should not budget your game plan around removal scoring.

---

## Playbook

### Opening (Turns 1–2)

Your first priority is placing assemblies in clearings where enemy construction will happen. Turn 1, reveal cards matching clearings adjacent to where you placed your 6 starting warriors, using Assemble to plant your first one or two assemblies. Prefer clearings you already rule so you keep the revealed card (not discarding it). Spend any leftover card reveals on Recruit to consolidate warrior count where your first assemblies are going.

In Evening, use Agitate on your planted assemblies to flip them Governing and build Loyalist reserves. The Adjourn step then flips assemblies you rule to Governing — if you already ruled through Agitate, any additional assemblies you rule become Governing in the same step.

Turn 2, begin spreading. Use Move reveals to push warriors toward central clearings or clearings bordering aggressive builders. Place your second or third assembly. If enemies have already built in clearings you control, your Oversee scoring begins immediately.

Do not try to play aggressively with Battle in the first two turns unless an enemy is poorly positioned and you can establish presence. Early battles in a clearing with an assembly cost you your revealed card (`faction:council$17.4.4`), reducing your Evening actions.

### Mid-Game Pivots

Watch for these signs and adjust accordingly:

**Sign: Enemies are entreatig you frequently.** They are getting out of your Governing locks. Pivot to placing Loyalists with Entreat payments, then using those Loyalists to rapidly re-assemble in the same clearings. Your assembly density can outpace their Entreat rate if you have the card throughput.

**Sign: Your warrior count in assemblied clearings is declining.** Peacekeepers absorbs overflow hits in battles you didn't start. If you're losing warriors to Peacekeepers attrition faster than you're recruiting, shift Birdsong reveals toward Recruit and use Empower to recycle warriors back to your Loyalist pool rather than scoring the 1 VP.

**Sign: An enemy is scoring fast with no buildings or tokens near your assemblies.** If that faction is a token-light or building-light insurgent (Woodland Alliance, Corvid), you may have a mismatch — your scoring depends on enemy presence. Consider using Banish to push their warriors out of your assemblied clearings (forcing them elsewhere where they may build), or pivot toward placing assemblies in clearings where other, building-heavier factions are active.

**Sign: You're sitting at 3–4 VP per Evening consistently.** You're ahead of pace. Focus on defense — keeping the assemblies you have governing, keeping warriors in them to maintain rule, and not overextending. A well-defended position with 3–4 assemblies scoring is often more reliable than reaching for a fifth or sixth.

### Endgame Routes

The most reliable finisher is a multi-assembly board position held through the last two turns. If you have four Governing assemblies with enemy presence, you score 3 VP per Evening. With five or six, you reach the cap of 4 VP per Evening. This compounds quickly: three turns at 4 VP is 12 points on top of whatever you accumulated.

Use Banish strategically in the final turns to shape which clearings are contested. Banishing warriors into clearings you don't care about, while leaving buildings and tokens behind (you cannot hit buildings or tokens in Banish — `faction:council$17.5.1.1`), clears warrior resistance from your assemblied clearings without disturbing the enemy presence you're scoring off.

If you are within reach of 30 VP and have a bird card in hand, check whether Empower can get you there — it scores immediately in Convene Woodfolk, before Oversee. A 1-VP Empower plus a strong Oversee result can close the game in a single Evening.

---

## Threat Factions

### Woodland Alliance

The Woodland Alliance (`rule:8.`) is your most structurally difficult opponent. Their sympathy tokens are buildings for purposes of placement rules — tokens count toward enemy presence in your clearings, which helps your Oversee score. But their Outrage ability (`rule:8.2.6`) fires whenever you move warriors into a sympathetic clearing, costing you a card from hand. Your Birdsong is built on moving warriors and placing assemblies, so Outrage creates a real tax on your card economy. If the Alliance is placing sympathy in clearings you need for assembly spread, you are paying to work in your own clearings.

Counter-play: Banish is effective against sympathy warriors (Alliance warriors in your clearings can be moved away without removing them). However, Banish fires off of non-bird revealed cards and moves warriors, not tokens — sympathy tokens stay. Your Governing assembly can lock the Alliance out of placing more sympathy tokens in that clearing (`faction:council$17.2.3`), which is the real long-term answer. Get Governing assemblies in key clearings before the Alliance floods them with sympathy.

### Lord of the Hundreds

The Warlord has a specific interaction with your Banish: the warlord cannot take Banish hits because it cannot be moved outside the Lord of the Hundreds' turn (`faction:council$17.5.1.1.1`). This means your Banish mechanic is partially neutralized against a faction whose key piece is the most dangerous warrior on the board. You can still Banish the Hundreds' regular warriors out of your clearings, but the warlord plants itself wherever it goes and cannot be displaced by your primary crowd-control action.

More broadly, the Lord of the Hundreds (`rule:14.`) is an aggressive, mobile faction that can rapidly contest clearings you've invested assemblies in. Their Oppress ability also doesn't generate the kind of passive building presence that helps your Oversee — when the Hundreds oppress a clearing, it typically means they've cleared enemy pieces, which may include your assembly context.

Counter-play: Rule your assemblied clearings well enough that the Hundreds must commit significant warriors to dislodge you, and use Peacekeepers to bleed their warrior count when they attack other enemies at your assemblies. You're unlikely to Banish the warlord out; focus on maintaining ruling warriors around your assemblies.

### Corvid Conspiracy

Corvids (`rule:13.`) place face-down plot tokens — which are buildings — into clearings. Because your Oversee step scores off enemy buildings and tokens, Corvid presence near your assemblies is actually beneficial to your score. The risk is the opposite: Corvids can Expose or Flip their own plots as part of their actions, meaning the building you're scoring off can suddenly move or change. Corvid Snare tokens also block movement into clearings — if they place a snare in a clearing with your assembly, you may find yourself unable to Move into it to maintain rule.

Counter-play: Governing assemblies restrict the Corvids from placing, removing, or flipping pieces (`faction:council$17.2.3`) — which includes their plot tokens. This is a meaningful lock: a Corvid who cannot flip or expose plots in a clearing loses their disruption toolkit there. Prioritize getting assemblies Governing in clearings the Corvids are working in.

### Marquise de Cat

The Marquise (`rule:6.`) builds reliably and in volume, which is the best possible context for your Oversee score. The tension is that the Marquise is also the faction most likely to have the warriors and field hospitals to remove your assemblies, dislodge you from rule, and trigger Keep-clearing restrictions. The Keep token (`rule:6.2.2`) blocks sympathy placement in that clearing — not relevant to you directly, but it shapes where the Marquise clusters, which you want to orbit.

Counter-play: Your Governing assembly in a sawmill-dense clearing will starve the Marquise's construction rhythm, since they cannot place buildings at a Governing assembly outside of battle. They will Entreat you to open it, which gives you Loyalists. Use those Loyalists to maintain warrior presence and re-govern quickly in Adjourn.

---

## Card Priorities

The Twilight Council has no faction-specific card deck. You draw from and craft the shared deck.

### Crafting Priorities

**High priority**:
- **Cobbler** (`card:ROOT-60 (Base Game)`) — "At start of Evening, may take a move." Extra movement in Evening can let you reach a key clearing for rule right before Adjourn flips assemblies Governing. Pairs tightly with your scoring engine.
- **Better Burrow Bank** (`card:ROOT-55 (Base Game)`) — "At start of Birdsong, you may draw one card. If you do, choose an enemy to draw one card." The card draw compensates for your aggressive reveals in Birdsong. Sharing the draw with an enemy is a minor cost; the extra card per turn sustains your reveal density.
- **Armorers** (`card:ROOT-51 (Base Game)`) — "In battle, may discard to ignore all rolled hits taken." Your warriors in assemblied clearings absorb hits as Peacekeepers. Armorers lets you cancel that damage in a critical battle. Situationally very strong.
- **Sappers** (`card:ROOT-94 (Base Game)`) — "In battle as defender, may discard to deal an extra hit." Useful if you're defending a critical assembly clearing.

**Situational**:
- **Royal Claim** (`card:ROOT-92 (Base Game)`) — "In Birdsong, may discard to score one point per clearing you rule." If you have wide board presence and rule several clearings, this can add 3–5 VP instantly. Scales with your spread.
- **Command Warren** (`card:ROOT-63 (Base Game)`) — "At start of Daylight, may initiate a battle." Extra battle action helps you contest clearings before Sleep, potentially reclaiming rule from an enemy just before your Adjourn flips assemblies.
- **Stand and Deliver!** (`card:ROOT-102 (Base Game)`) — You steal a card from an enemy in Birdsong. Useful for disrupting an enemy hand while supplementing your own reveal options.
- Favor of the Foxes/Mice/Rabbits — These clear all enemy pieces from a suit's clearings. They remove warriors but also buildings and tokens, which hurts your Oversee score in that suit temporarily. Use them to reclaim clearings that are heavily contested, not to wipe out the buildings you're scoring off.

**Low priority**:
- **Brutal Tactics** (`card:ROOT-58 (Base Game)`) — Costs you an enemy VP. You are generally not in the business of dealing extra hits; Peacekeepers keeps you from acting aggressively in battles anyway.
- **Scouting Party** (`card:ROOT-95 (Base Game)`) — Ignores ambushes as attacker. You rarely initiate important battles as the primary attacker; ambush protection matters less to you.

### Ambush Guidance

Hold ambush cards. You are often the defending side (or assisting defender via Peacekeepers), so the defensive use of Ambush! (`card:ROOT-46 (Base Game)` through `card:ROOT-49 (Base Game)`) — dealing 2 immediate hits as defender before the roll — is directly relevant. Since your warriors often serve as secondary defenders absorbing overflow hits, surviving to continue ruling a clearing is critical.

You can also reveal ambush cards in Birdsong for their suit (for Move, Recruit, Assemble, or Battle). If you do reveal them, you get the Convene action in Evening but you cannot use them as ambush cards in that battle. Prioritize keeping them in hand for defense unless you have a surplus.

### Dominance Card Considerations

Community consensus from early Homeland playtests suggests the Twilight Council's Oversee engine is reliable enough that dominance is rarely the correct path. Your scoring is passive and scales with enemy activity, so a game where you have a comfortable engine running typically favors staying on the VP track. Dominance cards can still be held and spent for suit fuel — spending a dominance card for its suit to reveal in Birdsong is legal and occasionally useful.

---

## Common Pitfalls

- **Placing assemblies in clearings with no enemy buildings or tokens and no prospect of them.** An assembly in an empty corner does nothing for your Oversee step. Every assembly you deploy should either be positioned where enemies will build, or positioned to lock an enemy's action economy via Governors. Assemblies in inert clearings are wasted pieces.

- **Letting your revealed card count in Birdsong fall.** You return revealed cards in Evening to trigger Convene Woodfolk actions. If you reveal only one card in Birdsong, you have only one Convene action. Your Agitate and Banish actions — the tools that flip assemblies Governing and shape the board — come entirely from Convene. Playing conservatively in Birdsong starves your Evening.

- **Burning revealed cards on Assemble in clearings you don't rule.** Assemble discards the revealed card if you don't rule the clearing. This is not always wrong — sometimes you need an assembly in a contested clearing — but doing this repeatedly drains your Evening actions. Prefer Assembling in clearings you rule, or reinforce to rule before you Assemble.

- **Ignoring the Sleep step strategically.** If an enemy rules a clearing with your assembly at the start of Daylight, Sleep flips it Closed. This is often treated as a loss, but it is also a signal: you are being outcompeted in that clearing. Continuing to fight for it with insufficient warriors wastes resources. Sometimes the right move is to Adjourn-remove the assembly and redeploy it somewhere more favorable.

- **Neglecting Loyalist management.** Loyalists are your flexibility buffer. Running dry on Loyalists means you cannot reinforce assemblies via Assemble and must pay from your supply (spending warriors instead of Loyalists). Refill them via Entreat payments and Empower — don't always chase the 1 VP from Empower when your Loyalist pool is depleted.

- **Letting the Warlord set up next to you without a plan.** Banish does not move the warlord. If the Lord of the Hundreds plants the warlord in a clearing with your assembly, you cannot use your primary clearing-control tool. Have a backup: recruit sufficient warriors to maintain rule despite the warlord's presence, or use normal battle to reduce the Hundreds' regular warrior count.

- **Overextending on assemblies.** You have 6 total. Spreading to six clearings early means each individual assembly is undersupported with warriors. If enemies contest multiple clearings simultaneously, you may lose several assemblies and their Loyalists at once, leaving you with an empty board and empty Loyalist pool in the same turn.

---

## Mechanic Clarifications

### Can enemies place pieces in a Governing assembly's clearing during their Birdsong or Daylight?

No. The Governors restriction (`faction:council$17.2.3`) prevents enemies from placing pieces except in battle. This applies in any phase — Birdsong, Daylight, or Evening. "Except in battle" is the only carve-out.

**Citation**: `faction:council$17.2.3`

---

### Does Banish trigger movement-based abilities (such as Alliance Outrage) for the warriors being moved?

Yes. Banish treats the forced move as a single move for triggering other effects (`faction:council$17.5.1.1`). Warriors banished into a sympathetic clearing would trigger Outrage, and similar movement-triggered abilities fire normally.

**Citation**: `faction:council$17.5.1.1`

---

### When does the Adjourn flip happen relative to Oversee?

Adjourn precedes Oversee in the Evening sequence (`faction:council$17.5`). Assemblies you flip to Governing in Adjourn count immediately in Oversee scoring during the same Evening.

**Citation**: `faction:council$17.5.3`, `faction:council$17.5.4`

---

### Does Entreat happen on the Council's turn or on other turns?

Enemies Entreat on their own turn, not the Council's (`faction:council$17.2.4`). Any number of times on an enemy's turn, that enemy may Entreat any assembly. The Council then gains Loyalists or places a warrior in Loyalists as the response.

**Citation**: `faction:council$17.2.4`

---

### Can the Council ambush, use battle effects, or play battle cards during Peacekeepers battles?

No. The Peacekeepers rule explicitly states: "The Council cannot ambush, use battle effects, etc." (`faction:council$17.2.5`). The Council is purely an absorbing shield in Peacekeepers scenarios.

**Citation**: `faction:council$17.2.5`

---

### Are hirelings affected by Governors?

Hirelings are enemy pieces to players other than their controller (`rule:22.3.2`). They are subject to the Governors restriction if they are an enemy. However, hireling actions are separate from controller actions (`rule:22.3.4`), so the hireling itself also cannot place pieces at a Governing assembly if it would count as an enemy action.

**Citation**: `faction:council$17.2.3`, `rule:22.3.2`, `rule:22.3.4`

---

### What counts as "enemy buildings or tokens" for Oversee?

Standard buildings (square cardboard pieces placed in slots) and tokens (circular cardboard pieces) belonging to enemy players (`rule:2.5`). Hireling buildings and tokens in a clearing count if that hireling is an enemy (`rule:22.3.2`). The Vagabond's items are not buildings or tokens — they are items (`rule:9.`). Ruins are not owned by any player and are not enemy pieces.

**Citation**: `faction:council$17.5.4`, `rule:2.5`, `rule:22.3.2`

---

## Reference Index

**Faction citation key**: `faction:council`

**Primary rule section**: `rule:17.`

**Related glossary entries**: `item:warrior` (warriors as Loyalists), `item:building`, `item:token`

**Hireling form**: Bat Messengers and Sunny Advocates (Homeland Hirelings Pack — not encoded in the base card YAMLs; verify in Homeland Hirelings Pack rules).

**Cross-faction interactions**:
- `rule:9.2.9.2` / `faction:council$17.2.5.1` — Vagabond Allied to Council: Council warriors become attacking warriors when the Allied Vagabond initiates battle.
- `faction:council$17.5.1.1.1` — Lord of the Hundreds warlord is immune to Banish.
- `faction:council$17.5.1.1.2` — Vagabond is immune to Banish (not a warrior).
- `faction:council$17.5.1.1.3` / `rule:22.3.4` — Hirelings are immune to Banish (cannot be forced to move).
- `rule:8.2.6` — Alliance Outrage fires when you move warriors into sympathetic clearings during Birdsong.
