# Underground Duchy

## At a Glance

**Identity:** A subterranean empire that tunnels onto the surface, builds citadels and markets to project power, and swells its turn with Parliamentary actions by swaying a cabinet of ministers — but suffers a cascading political collapse whenever its buildings are destroyed.

| Attribute | Value |
|---|---|
| Faction citation key | `faction:duchy` |
| Primary rule section | `rule:12.` |
| Reach | 8 (`rule:5.2.2`) |
| Complexity | Medium |
| Setup constraint | Corner clearing not occupied by another faction; if possible, diagonally opposite a rival's starting corner (`faction:duchy$12.3.3`) |
| Color | Sandy tan (`#eec4ab`) |
| Icon | `faction-duchy` |

**Scoring tempo:** Punctuated. The Duchy scores in concentrated bursts when it sways ministers and then transitions into a continuous scoring engine through lord-minister abilities in Parliament. Early game VP is sparse; mid-game VP accelerates sharply.

---

## Win Condition

### Standard Route (30 VP)

Your VP comes from three sources that compound each other. First, every time you sway a minister you score the VP listed on the faction board space that minister's crown occupied — higher-rank ministers uncover larger VP values (`faction:duchy$12.5.3.3`). Second, your three lord ministers (Baron of Dirt, Earl of Stone, Duchess of Mud) each score recurring VP during Parliament once swayed, rewarding you for keeping buildings and tunnels on the map (`faction:duchy$12.5.2`). Third, universal scoring — removing enemy buildings and tokens scores 1 VP per piece (`rule:3.2.1`), and crafting items scores their listed VP (`rule:3.2.2`).

The arc looks like: place buildings to gain rule, rule clearings to gain card diversity, spend cards to sway ministers, sway ministers to gain more actions, use more actions to expand, and use Parliament to score per turn. Once your lords are swayed and your buildings are intact, you can generate 3–6 VP per round passively.

### Dominance Path

You activate a dominance card during Daylight when you have at least 10 VP, then remove your score marker (`rule:3.3.1`). Your Parliament actions can help you reach three clearings of a suit or two corner clearings quickly, since the Brigadier and Marshal give you additional move and battle actions. The Duchy is reasonably suited to dominance when buildings are vulnerable — it lets you win without maintaining the VP lead that your opponents can attack by destroying buildings.

---

## Setup

### Placement Walkthrough

1. **Gather pieces.** Take 20 warriors and 3 tunnel tokens into your supply. Place the Burrow board near the map (`faction:duchy$12.3.1`–`faction:duchy$12.3.2`).
2. **Surface.** Choose a corner clearing that no other player has claimed as their starting corner, and, if possible, one diagonally opposite from a rival's starting corner. Place 2 warriors and 1 tunnel token in that clearing. This is your starting clearing (`faction:duchy$12.3.3`).
3. **Spread adjacency.** Place 2 warriors in each clearing adjacent to your starting corner, except the Burrow (`faction:duchy$12.3.3`). On the standard map this means roughly 4–6 warriors across 2–3 clearings immediately.
4. **Fill building tracks.** Place 3 citadels and 3 markets on their respective spaces on your faction board (`faction:duchy$12.3.4`).
5. **Collect ministers.** Place all 9 minister cards face up on your Unswayed Ministers pile (`faction:duchy$12.3.5`).
6. **Fill crown spaces.** Place 9 crowns on the VP spaces on your faction board (`faction:duchy$12.3.6`).

### Setup Theory

**Corner choice.** Diagonally opposite placement gives you two key advantages: it gives you the most map distance from your strongest rival (usually Marquise or Eyrie, who also want corners), and it tends to put different suit clearings between you and your opponents, which matters because swaying ministers requires pieces in clearings of matching suit. A corner with diverse adjacent suits (fox, rabbit, mouse) is better than one surrounded by two clearings of the same suit.

**Neighbor considerations.** The Duchy prefers aggressive neighbors to be far away. The Woodland Alliance and Corvid Conspiracy do not directly destroy buildings but can lock you out of clearings. The Marquise and Lord of the Hundreds do destroy buildings and will trigger Price of Failure repeatedly if they can reach you. Eyrie, at their most dangerous, can flood clearings quickly and remove your buildings while chasing rule. Try to pick a corner that puts slow or passive factions between you and the destructive ones.

**Opening hand.** You need cards to sway squire ministers (2 cards each) and to Dig (1 card to place a tunnel). Your first turn will likely include at least one Build action and one Sway, so a hand with two distinct suits gives you flexibility. Bird cards are especially valuable early because they count as any suit both for swaying (matching a clearing of that suit you occupy) and for Dig. Discard single-suit pairs that don't match adjacent clearings you can rule.

---

## Faction Rules and Abilities

### Crafting

You craft during Evening by activating citadels and markets (`faction:duchy$12.2.1`). Both citadels and markets are treated identically for crafting purposes — each one in a clearing of suit X provides one activation of suit X. With up to 6 buildings on the map spread across different-suit clearings, you can potentially activate three or more suits in a single Evening, making you one of the strongest crafting factions once your buildings are established.

Note that you can only activate each building once per turn (`rule:4.1.1`). Because your buildings are also what Parliament scores off (Baron of Dirt and Earl of Stone), every building you place is simultaneously a crafting engine, a rule contributor, a scoring target for opponents, and an escalation of your own lord VP.

### The Burrow

The Burrow is an additional board space — unsuited, adjacent to every clearing that currently has a tunnel token (`faction:duchy$12.2.2`). It is important to understand what this means precisely:

- The Burrow is adjacent to each tunnel-clearing. It is treated as a clearing for movement and placement purposes relevant to the Duchy — it is an unsuited clearing defined by `faction:duchy$12.2.2`, not one of the map's printed clearings.
- Non-Duchy pieces cannot be placed in or moved into the Burrow (`faction:duchy$12.2.2`). Your warriors in the Burrow are protected.
- The Duchy always rules the Burrow, even with zero pieces there (`faction:duchy$12.2.2`). The Burrow cannot be contested.
- When you Dig to place a new tunnel, that clearing becomes adjacent to the Burrow, and warriors you move from the Burrow to the new clearing emerge directly there.

The Burrow functions as both a staging area and a reservoir. Warriors placed in the Burrow during Birdsong accumulate there until you Dig them out or move them to the surface through existing tunnels.

**Edge cases.** The Burrow is not a clearing on the map. It does not have a suit, does not have building slots, and cannot be battled. However, standard Move actions can move warriors from the Burrow to an existing tunnel clearing and back, because the Burrow is adjacent to all tunnel clearings (`faction:duchy$12.2.2`) and you always rule the Burrow (satisfying the rule-origin requirement in `rule:4.2.1`). Dig is not the only way to surface warriors — it is a special action that places a new tunnel and immediately moves up to 4 warriors from the Burrow to that new clearing in one action (`faction:duchy$12.5.1.5`). For existing tunnels, a standard Move action suffices.

### The Price of Failure

Whenever any number of Duchy buildings are removed in any single event, the following happens in order (`faction:duchy$12.2.3`):

1. Return your swayed minister of highest rank (lord > noble > squire) to your Unswayed Ministers pile.
2. Remove its crown from the game permanently.
3. Discard a random card from your hand.

This is the faction's defining risk. Note several sharp edges:

- "Any number" removed in one event counts as one trigger. An opponent removing two of your buildings at once triggers Price of Failure once, not twice.
- The crown is gone permanently — you cannot sway back to that rank slot. Each time Price of Failure fires, you permanently reduce your maximum swayed ministers by one.
- The returned minister goes back to unswayed, but without its crown, you cannot sway it again unless you still have a crown of that rank. Once both crowns of a rank are removed, all ministers of that rank are locked permanently unswayed.
- You choose which minister to return when you have multiple swayed ministers of the highest affected rank (`faction:duchy$12.2.3`).

The cascade risk is real: an opponent who removes one of your buildings can trigger Price of Failure, which discards a random card from your hand, which might be a card you needed for swaying or Digging, and the loss of the minister reduces your action count for future turns.

### Tunnels

You have three tunnel tokens (`faction:duchy$12.2.4`). Tunnels serve two functions: they make the clearing adjacent to the Burrow (enabling Burrow-movement), and they are the prerequisite for Dig deployments (which land warriors directly from the Burrow into the tunnel clearing).

If all three tunnels are already on the map when you are prompted to place a new tunnel, you may first remove any tunnel from the map, freeing up a slot (`faction:duchy$12.2.4`). This lets you reposition your tunnel network as the game evolves.

---

## Turn Structure

### Birdsong

Place one warrior in the Burrow, plus one additional warrior per warrior icon currently showing on your faction board (`faction:duchy$12.4`). The number of warrior icons visible increases as you sway ministers — each minister card covers a portion of your faction board, and icons showing beneath already-swayed cards reflect your recruitment rate. Early game, you place 1 warrior per turn. Mid-game with several squires swayed, you may place 3–4.

This is your passive army generation. The Burrow accumulates warriors that you then deploy via Dig or standard movement through tunnels.

### Daylight

Daylight has three sequential steps: Assembly, then Parliament, then Sway. You must resolve them in this order (`faction:duchy$12.5`).

#### Assembly

Take up to two actions in any order and any combination (`faction:duchy$12.5.1`):

- **Build.** Reveal one card to place a citadel or market in a matching clearing you rule (`faction:duchy$12.5.1.1`). The card is revealed, not spent — it returns to your hand in Evening unless it is a bird card, which is discarded instead (`faction:duchy$12.6.1`).
- **Recruit.** Place one warrior in the Burrow (`faction:duchy$12.5.1.2`).
- **Move.** Take one move (`faction:duchy$12.5.1.3`).
- **Battle.** Initiate one battle (`faction:duchy$12.5.1.4`).
- **Dig.** Spend one card to place a tunnel in a matching clearing without a tunnel. Then immediately move up to 4 warriors (at least 1) from the Burrow to that clearing (`faction:duchy$12.5.1.5`). If all three tunnels are on the map, you may first remove one tunnel before placing the new one.

Two Assembly actions is your base rate. You can repeat the same action twice (two builds, two moves, etc.).

#### Parliament

Take the action of each swayed minister once, in any order you choose (`faction:duchy$12.5.2`). Each minister provides exactly one action per turn. With all 9 ministers swayed, Parliament gives you 9 additional actions.

The nine ministers and their actions:

| Minister | Rank | Action |
|---|---|---|
| Marshal | Squire | Take one move (`card:ROOT-11 (Underworld)`) |
| Captain | Squire | Initiate one battle (`card:ROOT-7 (Underworld)`) |
| Foremole | Squire | Reveal any card to place a citadel or market in any clearing you rule, matching or not (`card:ROOT-10 (Underworld)`) |
| Brigadier | Noble | Take up to two moves or initiate up to two battles (`card:ROOT-6 (Underworld)`) |
| Mayor | Noble | Take the action of any swayed noble or squire (`card:ROOT-12 (Underworld)`) |
| Banker | Noble | Spend any number of cards of the same suit to score VP equal to the number spent (`card:ROOT-4 (Underworld)`) |
| Baron of Dirt | Lord | Score 1 VP per market on the map (`card:ROOT-5 (Underworld)`) |
| Earl of Stone | Lord | Score 1 VP per citadel on the map (`card:ROOT-9 (Underworld)`) |
| Duchess of Mud | Lord | Score 2 VP if all three tunnels are currently on the map (`card:ROOT-8 (Underworld)`) |

**Important ordering notes.** The Brigadier gives up to two moves or up to two battles — these are alternatives, not both simultaneously. You choose one type per Brigadier action: either take up to two moves, or initiate up to two battles. You cannot split one move and one battle from a single Brigadier use. The Mayor copies any swayed noble or squire action at the time Mayor is used, meaning Mayor can copy Brigadier for another set of moves or battles, or copy Banker for another suit-dump, or even copy Foremole. Mayor cannot copy lord actions. Banker lets you convert accumulated same-suit cards directly to VP — this is not limited, so a hand of five fox cards turns into 5 VP in one action.

#### Sway

You may sway exactly one minister this turn (`faction:duchy$12.5.3`):

1. **Choose a minister** from your Unswayed pile. You must have a crown of that rank still on your faction board (`faction:duchy$12.5.3.1`).
2. **Reveal the required cards.** Squires require 2, nobles 3, lords 4 (`faction:duchy$12.5.3.2`). For each card you reveal, you must have at least one Duchy piece in a clearing matching that card's suit. Each such clearing lets you reveal one card — having pieces in a fox clearing lets you reveal one fox card, not multiple. Bird cards are wild and still require you to have a piece in a clearing of the suit you choose to treat them as.
3. **Take the minister, place the crown, score VP.** Move the minister card above your faction board. Place a crown of that rank on the minister card. Score the VP listed on the space now uncovered on your faction board (`faction:duchy$12.5.3.3`).

You can sway only one minister per Daylight, regardless of how many actions or how many crowns you have. The once-per-turn limit is hard.

### Evening

Evening has three steps in order (`faction:duchy$12.6`):

1. **Discard and return revealed cards.** Discard any bird cards you revealed during Daylight (for Build, Foremole, or Dig). Return all other revealed cards to your hand. This means non-bird cards used for Build and Foremole effectively cost nothing beyond the card's tempo; bird cards are permanently spent.
2. **Craft.** Activate citadels and markets to craft cards from your hand (`faction:duchy$12.6.2`). Citadels and markets are identical for crafting.
3. **Draw and discard.** Draw one card plus one per card draw icon showing on your faction board. If you hold more than 5 cards afterward, discard down to 5.

The card draw icons are uncovered on your faction board as you sway ministers — more ministers mean more cards per turn, compounding your engine further.

---

## Scoring Engine

| VP Source | Amount | Trigger | Timing |
|---|---|---|---|
| Sway minister (squire) | Listed on board space | When minister is swayed | Daylight — Sway step |
| Sway minister (noble) | Listed on board space | When minister is swayed | Daylight — Sway step |
| Sway minister (lord) | Listed on board space | When minister is swayed | Daylight — Sway step |
| Baron of Dirt (lord) | 1 per market on map | Passive, each Parliament | Daylight — Parliament |
| Earl of Stone (lord) | 1 per citadel on map | Passive, each Parliament | Daylight — Parliament |
| Duchess of Mud (lord) | 2 if all 3 tunnels on map | Passive, each Parliament | Daylight — Parliament |
| Banker (noble) | 1 per card of same suit spent | Active, player discretion | Daylight — Parliament |
| Remove enemy building/token | 1 per piece | When removed in battle | Daylight — Parliament or Assembly |
| Craft item | Listed on card | When crafted | Evening — Craft step |

The lords are the recurring engine. With all 6 buildings on the map and all 3 tunnels placed, Baron of Dirt generates 3 VP per turn, Earl of Stone generates 3 VP per turn, and Duchess of Mud generates 2 VP per turn — that is 8 VP per round from three minister actions alone, which closes 30 VP in about 4 turns from that point. In practice, you will not have all buildings intact that late, but even two lords active with 4–5 buildings on the map generates 4–6 passive VP per turn. This is the engine you are building toward.

The Banker is a secondary engine for card-rich turns. It converts cards directly to VP at 1:1 with no suit restriction beyond same-suit matching. In late game when you have 4+ card draw icons showing and a large hand, Banker can fire for 3–5 VP.

---

## Playbook

### Opening (Turns 1–2)

Your first two turns establish the minimum viable position: at least one building on the map, your first sway completed, and a second tunnel placed.

**Turn 1 priority.** Use both Assembly actions: Build in your starting clearing (or an adjacent one you rule), then Dig to a second clearing, deploying Burrow warriors there. This gives you a building, a new tunnel clearing, and pieces spread across two clearings with different suits. In Sway, sway your first squire — Foremole or Brigadier are the most commonly prioritized first swayed ministers (community data suggests Brigadier is swayed in the vast majority of competitive games early because two moves or two battles per Parliament turn dramatically expands action economy from turn 2 onward). Score the VP from the uncovered space.

**Turn 2.** With your first minister in Parliament, you have an extra action. Continue building. If you can reach a clearing of a different suit, sway a second squire. The Marshal adds another move, letting you spread further. By the end of turn 2, you want: 2–3 buildings on the map across different suits, 2 ministers swayed, and pieces present in at least 2 different suit clearings to enable noble sways on turn 3.

**Bird-card management.** Bird cards are spent permanently on Build and Dig. On Sway, they can represent any suit but require you to hold a piece in a matching clearing. Do not burn all your birds on Build — they are more valuable for swaying nobles (3 cards required) when your position does not have three distinct suits covered.

### Mid-Game Pivots

The mid-game asks you to sway your three nobles (Brigadier, Mayor, Banker) while beginning to protect or expand your building base. You have 4–6 buildings on the map and are approaching lord-sway territory.

**If opponents are passive:** Aggressively build to maximize buildings before swaying lords. More buildings at the moment you sway Baron of Dirt and Earl of Stone means more VP per turn from those ministers. Dig a third tunnel to unlock Duchess of Mud scoring immediately after swaying her.

**If opponents are targeting your buildings:** Consider the "smol mole" approach noted in community discussion — delay building expansion, focus on swaying ministers with warriors spread across many clearings, and keep a small building footprint so Price of Failure fires less. Once nobles are swayed (especially Mayor and Banker), you can generate VP through Banker on card-heavy turns without needing buildings on the map. Community sources note this approach, flagging that it was discussed more prominently in pre-p16 contexts; the trade-off between building VP and building vulnerability is still relevant under current rules.

**Pivot signal — sway lords when:** You can protect at least 4 buildings in your territory and you have enough pieces in 4 distinct clearings to reveal 4 cards for a lord sway. Rushing lord swaying with undefended buildings is a trap — a single building removal loses you the lord immediately.

**The Mayor combo.** Once Mayor is swayed, Mayor can copy Brigadier, giving you effectively three moves/battles from those two ministers alone. Then if Mayor copies Banker on another turn, you double your VP from cards. Prioritize Mayor if your hand is growing but your board is contested.

### Endgame Routes

With lords active, you enter a closing window. The key question is whether you can keep buildings on the map long enough to score out.

**Route 1: Lord engine.** Keep all 6 buildings on the map and all 3 tunnels placed. Use Parliament's three lord actions every turn for 6–8 passive VP. Use Banker to convert surplus cards. Reach 30 in 3–5 turns once all lords are active.

**Route 2: Banker finisher.** If your buildings are too threatened to rely on lords, accumulate a large hand through your card draw icons and fire Banker for large VP swings. Two Banker activations in consecutive turns (Banker + Mayor-copies-Banker) can net 8–10 VP in a single Parliament if you have been hoarding matching cards.

**Route 3: Battle and craft.** Use your Brigadier, Marshal, and Captain to fight aggressively into high-slot clearings, build after winning rule, and craft high-value items in Evening. Combat VP and crafting VP can supplement a stalling lord engine.

**Endgame signal.** Watch your total per-turn VP rate. If lords are delivering 6+ VP per turn, you are on a fast clock. Alert opponents will recognize this and try to trigger Price of Failure. Deploy warriors defensively around your most valuable buildings in clearings where you currently have rule — forcing opponents to commit combat resources to destroy them.

---

## Threat Factions

### Marquise de Cat

The Marquise's industrial expansion overlaps directly with your territory goals, and her ability to build many workshops means she can deny rule in clearings you need for card-diversity swaying. More critically, the Marquise's Field Hospitals (`rule:6.2.3`) make her warriors nearly inexhaustible to remove, while her wood-spending recruitment means she can mass warriors quickly to contest and destroy your buildings. Every building removal she causes fires Price of Failure.

**Counter-plays.** Dig into her supply chain clearings — placing a tunnel near her sawmills lets you drop warriors from the Burrow directly into contested territory. Battle her before she can build defensive depth. Prioritize clearings where she is overextended. The Foremole's off-suit build is useful here: if you rule a clearing you can reach, Foremole can place a building without the card-suit matching requirement that would otherwise limit Assembly Build.

### Eyrie Dynasties

The Eyrie at speed moves more warriors per turn than almost any faction and builds Roosts aggressively to score. An Eyrie player who resolves Turmoil repeatedly is less dangerous; an Eyrie who has locked in a powerful Decree is a race you need to win or disrupt. The Eyrie's Lords of the Forest (`rule:7.2.2`) bonus for ruling more clearings means they are contesting the same territory you want for swaying.

**Counter-plays.** If you have the Brigadier, use battle actions to contest Eyrie clearings where they are building Roosts. Roosts in your territory double as both Eyrie VP generators and threats to your buildings if they battle you. The Eyrie often spreads thin — a well-placed Dig can flood a Roost clearing with 4 warriors from the Burrow, giving you rule and a build opportunity in one action. Force Turmoil when possible by contesting clearings their Decree requires.

### Woodland Alliance

The Alliance generates sympathy and can spark revolts in clearings you need for card diversity and building placement. A revolt removes all enemy pieces from a clearing and establishes a base (`faction:woodland$8.4.1`), which destroys any Duchy buildings there — triggering Price of Failure. The Alliance's spread is slow but their bases make them harder to remove.

**Counter-plays.** The Duchy is more resistant to Outrage (`faction:woodland$8.2.6`) than factions that need to move warriors often, since your warriors often come from the Burrow directly into clearings rather than crossing sympathetic clearings. Still, watch for sympathy spreading into clearings adjacent to your tunnels. Battle Alliance bases early when you can; losing a base is expensive for them, and bases trigger revolts. Do not let them build up sympathy in your primary building clearings without contesting it.

### Corvid Conspiracy

Corvids place plot tokens that flip to remove pieces or swap buildings, and their snares constrain movement (`faction:corvid$13.7.2`). A Corvid Extortion or Bomb plot in a clearing where you have 3+ buildings can simultaneously remove buildings and trigger Price of Failure. Corvids do not score from your building destruction directly but can destabilize your engine as a threat to force other opponents' attention.

**Counter-plays.** Prioritize clearing Corvid plots in clearings with your buildings. Use your battle actions via Brigadier and Captain to remove Corvid warriors before their plots flip. Corvids are generally weaker in direct combat, so your warrior superiority from Burrow deployments can neutralize them if you reach their plot clearings in time.

---

## Card Priorities

### Crafted Items

The Duchy's 6 buildings across multiple suits make you one of the most capable crafting factions once established. Your best targets:

**Top priority.** `item:sword` cards (Sword items score 2 VP each and improve combat), `item:crossbow` (provides extra hit in battle), `item:coin` (scores VP directly), `item:tea` (heals or converts to VP via persistent cards). In general, prioritize items that score VP immediately (2–3 VP on craft) since you often have enough actions to battle and build; you do not need persistent movement items like `item:boot` the way Vagabond does.

**Situational.** Persistent effect cards that give card draw, extra VP on building placement, or combat bonuses. Worth crafting in mid-game when your action economy via Parliament is strong.

**Skip.** Cards with multi-suit crafting requirements are impossible for you — your buildings each provide one suit, not mixed activations (`rule:4.1.1`). Do not hold these hoping to craft them.

### Ambush Cards

Hold at least one ambush card if opponents are militarily aggressive. The Duchy does not have any special ambush ability, but an ambush in a clearing where an opponent is trying to remove your buildings can save a minister. Given that Price of Failure fires on any building removal, a single ambush protecting a citadel can prevent a cascade that would cost you a lord minister and a random hand card.

### Dominance Cards

Dominance is viable for the Duchy when your buildings are too exposed to maintain a VP lead. The Brigadier and Marshal give you strong movement to achieve three clearings of a suit or two corner clearings. Sway the Brigadier before committing to dominance, then use Parliament to race to the positional requirement. Note that once you activate dominance, your crowns are no longer linked to VP scoring, but Parliament still functions — your minister actions continue.

### Cards to Hold vs. Spend

The core tension: Build and Foremole reveal non-bird cards and return them, but spend bird cards permanently. Sway consumes cards from your hand. Banker converts cards to VP.

Hold a multi-suit hand through early game for sway flexibility — you need up to 4 distinct suit-presence matching to sway lords. Once all lords are swayed, convert surplus same-suit cards via Banker rather than holding them. The hand cap is 5 (`faction:duchy$12.6.3`), so with high card draw icons showing, you will regularly be forced to discard — use Banker as your discard valve before Evening's forced discard.

---

## Common Pitfalls

- **Swaying lords before your buildings are defended.** Lords are the engine, but each one requires 4 cards to sway and is immediately vulnerable to Price of Failure. Sway a lord into a board state where at least 4 buildings are in clearings you dominate, then protect them.

- **Neglecting Dig early.** Assembly's two actions can all be spent on Build, leaving warriors stuck in the Burrow. Dig opens a new tunnel, lands 1–4 warriors on the surface, and gives you a new clearings-presence for swaying next turn. At least one Dig in the first two turns is almost always correct.

- **Burning bird cards on Build.** Assembly Build discards bird cards permanently (`faction:duchy$12.6.1`). Non-bird cards revealed for Build return to hand. Using a bird card to Build when a same-suit card exists in your hand wastes it; save birds for Sway flexibility or hold them for ambush.

- **Failing to spread piece presence before swaying nobles.** Noble sways require 3 cards revealed, each matching a clearing where you have a Duchy piece. If you have pieces in only one or two suit-clearings, you cannot sway nobles regardless of hand size. Dig and Move to spread pieces into diverse-suit clearings before attempting noble-sway.

- **Losing both crowns of a rank.** Price of Failure removes crowns permanently. Once both crowns of a rank are gone, every minister of that rank is permanently locked unswayed. This effectively hard-caps your engine. Do not let building exposure get so severe that two Price-of-Failure triggers in the same rank wipe out an entire tier. Keep reserves in contested clearings to prevent building removal.

- **Ignoring hand size.** Duchy draws well with minister icons showing, but the 5-card cap means excess cards are lost in Evening unless you Banker them first. Schedule a Banker use before Evening discard on turns where you will draw above cap.

- **Over-committing to the Burrow.** The Burrow is safe, but warriors there do nothing until deployed. Recruiting into the Burrow via Assembly is only 1 warrior per action and requires a Dig or move to surface them. Rely on Birdsong's passive Burrow placement and use Assembly for Build, Battle, and Dig rather than spending Assembly actions on Recruit unless you specifically need more Burrow depth.

---

## Mechanic Clarifications

### Q: Do I trigger Price of Failure once or multiple times if several buildings are removed in a single event?

**Resolution.** Once, regardless of how many buildings are removed simultaneously (`faction:duchy$12.2.3`). "Whenever any number of Duchy buildings are removed" means one event, not one per building. An opponent who removes two of your buildings at once in a single battle round triggers the same single Price of Failure as removing one building.

**Citation.** `faction:duchy$12.2.3`

---

### Q: Can my warriors move from the Burrow without using Dig?

**Resolution.** Yes. The Burrow is adjacent to each clearing with a tunnel token (`faction:duchy$12.2.2`). Standard move actions can move warriors from the Burrow to a tunnel clearing (you always rule the Burrow, satisfying the rule-origin requirement at `rule:4.2.1`). Dig is a special action that places a new tunnel and moves up to 4 warriors directly from Burrow to the new tunnel clearing in one action. Standard moves through existing tunnels use Assembly Move, Marshal, or Brigadier actions.

**Citation.** `faction:duchy$12.2.2`, `rule:4.2.1`

---

### Q: Does the Foremole's "any clearing you rule" override the suit requirement for building?

**Resolution.** Yes. Foremole says "place a citadel or market in any clearing (matching or not) you rule" (`faction:duchy$12.5.2`). This is the distinguishing feature from Assembly Build, which requires a matching clearing. The card revealed for Foremole still costs a bird card permanently if it is a bird (`faction:duchy$12.6.1`); otherwise it is revealed and returned. The Foremole is a squire, so it is the first rank affected by Price of Failure if your lords and nobles are already swayed.

**Citation.** `faction:duchy$12.5.2`, `faction:duchy$12.6.1`

---

### Q: Can Mayor copy a lord minister's action?

**Resolution.** No. Mayor says "take the action of any swayed noble or squire" (`faction:duchy$12.5.2`). Lord actions (Baron of Dirt, Earl of Stone, Duchess of Mud) are excluded. Mayor can copy Brigadier, Banker, Marshal, Captain, or Foremole. Mayor cannot copy another Mayor.

**Citation.** `faction:duchy$12.5.2`

---

### Q: When I Sway a minister, what exactly counts as "a piece in a clearing"?

**Resolution.** Any Duchy piece counts, including warriors and buildings (`faction:duchy$12.5.3.2`). The Burrow is not a suited clearing, so pieces in the Burrow do not let you reveal a card of any suit. One Duchy piece in a fox clearing lets you reveal one fox card. Two pieces in the same fox clearing still only allows one fox card to be revealed — the rule specifies each clearing, not each piece.

**Citation.** `faction:duchy$12.5.3.2`

---

### Q: Can I remove a tunnel during setup or only via Dig?

**Resolution.** Tunnel removal is only permitted when the Duchy is prompted to place a tunnel and all three are already on the map (`faction:duchy$12.2.4`). You cannot remove a tunnel as a standalone action. During Dig, if all tunnels are placed, you may first remove any one tunnel, then place the new one in the matching clearing.

**Citation.** `faction:duchy$12.2.4`

---

### Q: Do revealed non-bird cards used for Assembly Build return to my hand even if I did not end up swaying a minister this turn?

**Resolution.** Yes. The return of revealed non-bird cards happens in Evening as a distinct step — "discard bird cards you revealed this turn, then return all other cards you revealed this turn to your hand" (`faction:duchy$12.6.1`). Whether you subsequently sway a minister is irrelevant to this return.

**Citation.** `faction:duchy$12.6.1`

---

## Reference Index

| Attribute | Value |
|---|---|
| Faction citation key | `faction:duchy` |
| Primary rule section | `rule:12.` |
| Reach | 8 |
| Faction board color | `#eec4ab` |

### Glossary Entries

- `item:sword` — combat item, relevant for crafting priority
- `item:crossbow` — provides extra hit, strong craft target
- `item:boot` — movement item; lower priority for Duchy given Burrow mobility
- `item:coin` — VP item, strong craft target
- `item:tea` — VP/utility item
- `item:sack` — lower priority
- `item:hammer` — crafting tool; primarily Vagabond-focused but craftable by Duchy

### Hireling Form

The Underground Duchy has two associated hirelings:

- **Sunward Expedition** (`card:ROOT-184 (Underworld Hirelings)`) — the promoted/full form
- **Mole Artisans** (`card:ROOT-185 (Underworld Hirelings)`) — the demoted/smaller form

These are separate pieces from the Duchy faction and function under the hireling rules (`rule:22.`).

### Cross-Faction Interactions

- **Vagabond coalitions.** A Vagabond can form a coalition with the Duchy player (`rule:9.2.8`). The Duchy's standard scoring and minister engine continues; the Vagabond wins if the Duchy's VP marker reaches 30.
- **Riverfolk Mercenaries.** The Duchy can hire Riverfolk mercenaries for battles (`rule:11.2.7`). Hired mercenaries do not count as Duchy pieces for swaying purposes — the rule requires "at least one Duchy piece in a clearing" (`faction:duchy$12.5.3.2`), and mercenaries are Riverfolk faction pieces treated as yours for battle, not Duchy pieces.
- **Woodland Alliance Outrage.** Moving Duchy warriors into a sympathetic clearing triggers Outrage (`faction:woodland$8.2.6`). Moving warriors out of the Burrow via a Move action to a sympathetic tunnel clearing triggers Outrage. A Dig that moves warriors from the Burrow into a newly tunneled clearing that is sympathetic also triggers Outrage for the movement component.
- **Corvid Snares.** A snare token in a clearing prevents enemy pieces from being placed in or moved from that clearing (`faction:corvid$13.7.2`). A snare in a tunnel clearing does not block the Burrow adjacency itself but does prevent standard moves into that tunnel clearing, which effectively isolates that tunnel from normal Burrow-to-surface movement. Dig into a snared clearing would also be blocked.
- **Keepers in Iron — Delve.** The Keepers delve relics from forests in clearings they rule (`rule:15.`). The Duchy's citadels and markets do not directly interact with Delve, but if Keepers contest a clearing and remove your buildings, Price of Failure fires.
