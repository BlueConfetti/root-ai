# Lizard Cult

## At a Glance

**Identity:** You score by spending cards to perform rituals — building gardens grants you rule and fuels a hand-size engine, while your acolytes (warriors martyred defending you) unlock movement, battle, and hostile takeovers on your terms.

| Property | Value |
|---|---|
| Reach | 2 |
| Complexity | High |
| Scoring tempo | Steady (with burst potential once gardens establish) |
| Color | Yellow |
| Icon | `faction-cult` |
| Faction citation key | `faction:cult` |
| Primary rule section | `rule:10.` |

**Setup constraints:** You claim a corner clearing not already taken by another faction, placed diagonally opposite an existing starting corner if possible (`faction:cult$10.3.2`). You begin with 4 warriors plus a garden in your starting corner, and 1 warrior in each adjacent clearing.

---

## Win Condition

### Standard 30 VP Route

Your victory points come almost entirely from the Score ritual: reveal a card during Daylight and immediately spend it — placing it in the Lost Souls pile — to score the points printed above the rightmost empty garden space of the matching suit (`faction:cult$10.5.3`). The key constraint is that you must already have at least one garden of that suit on the map; you also may only Score once per turn per suit. So your path to 30 VP is to establish gardens across multiple suits, then spend one card per suit scoring in each turn round.

A well-positioned Cult can score 2 to 6 VP per turn depending on how many suits have gardens on the board and how deep each suit's track has been progressed. The scoring track pays more VP per card as gardens are removed (leaving higher-value spaces uncovered), so the game rewards maintaining gardens over the full game rather than bursting.

### Dominance Card Path

Dominance is situationally viable. Because you do not discard cards to spend them in the normal sense (spending for Score places the card in Lost Souls rather than the discard), you can hold a dominance card without it interfering with your score engine. Activating a dominance card removes you from the VP track entirely (`rule:3.2`), so you must be confident you can hold the required clearings. Given your low Reach (2) and dependence on gardens for rule, dominance is rarely the plan but can be an emergency route if opponents repeatedly demolish your gardens and deny VP access.

### Scoring Tempo

Steady. You aim to score every single turn and fall behind if you miss even one round. Unlike factions that spike points in bursts, you accumulate VP slowly and consistently. This means your threat level is easy to underestimate early — but you will be at 20+ VP while opponents are still figuring out where the points came from.

---

## Setup

### Step-by-Step Placement

1. **Gather warriors** (`faction:cult$10.3.1`): Take 25 warriors from the supply as your faction warriors.
2. **Place warriors and opening garden** (`faction:cult$10.3.2`): Choose a corner clearing not already occupied as a starting corner by another faction. If possible, choose one diagonally opposite from an existing starting corner — this improves isolation. Place 4 warriors and 1 garden whose printed suit matches the clearing's suit in this corner. Place 1 warrior in each adjacent clearing.
3. **Choose Outcast** (`faction:cult$10.3.3`): Place your outcast marker on any of the three suit spaces in the Outcast box. This is your first Outcast. Choose carefully — it determines your crafting suit in the first Evening and influences your first conspiracies.
4. **Fill Gardens tracks** (`faction:cult$10.3.4`): Place your 14 remaining gardens on the Gardens tracks from right to left, filling each suit's track. Five gardens per suit total; you start with one on the map (the one placed in step 2), leaving 4 on each track for that suit and 5 on each of the other two tracks.

### Setup Theory

**Corner choice:** Prefer a corner with two adjacent clearings that have double building slots — those slots represent your future garden placements. More slots mean faster track progression. A corner whose adjacent clearings share your starting garden's suit lets you Build immediately with the cards you drew at game start.

**Starting Outcast:** Your opening Outcast is the most consequential setup decision. Pick a suit you either (a) hold matching cards for already — enabling early crafting or Score in turn 1 — or (b) expect opponents will discard heavily into the Lost Souls pile, which will naturally move the Outcast there in Birdsong.

**Neighbor considerations:** Avoid starting adjacent to high-aggression factions who will attack your gardens early (Marquise, Lord of the Hundreds). Ideally, start opposite the Marquise entirely — they will ignore you if you are not in their expansion path. The Woodland Alliance is dangerous later but rarely threatens you in the first two turns. The Eyrie is an interesting neighbor: their Turmoil cycles discard many cards, feeding your Lost Souls pile and influencing your Outcast.

**Opening hand priorities:** Keep any suited cards that match your chosen Outcast, or that match the suits of clearings you can rule adjacent to your start. Bird cards are nearly useless to you in Daylight (Hatred of Birds makes them ineligible for Build, Recruit, or Score; they are only useful for Sacrifice, `faction:cult$10.5.4`) — but do not discard them immediately since hand size matters for sustained scoring.

---

## Faction Rules and Abilities

### Crafting

You craft during Evening — not Daylight like most factions — by activating gardens whose printed suit matches the current Outcast suit (`faction:cult$10.2.1`). Each garden may be activated only once per craft (`rule:4.1.1`). The printed suit on the garden is what matters for crafting activation, not the suit of the clearing where the garden sits; this becomes relevant in games with the Lost City landmark or the Lilypad Diaspora, where a clearing's suit may differ from a building's printed suit.

**Edge case:** You can only craft during Evening, after you Return Revealed Cards but during the dedicated Craft step. Crafted cards go to the discard pile (or Lost Souls, per The Lost Souls Pile rule below), not back to your hand.

### Hatred of Birds

Bird cards are not wild for your rituals (`faction:cult$10.2.2`). Where other factions treat bird cards as any-suit wildcards for many purposes, you cannot use a bird card to Build, Recruit, or Score in a clearing. You may Sacrifice a warrior by revealing a bird card (`faction:cult$10.5.4`), but that is the only Daylight ritual bird cards unlock. Hold birds for Sacrifice when you need acolytes, but do not count on them for your main scoring actions.

### Revenge

Whenever one of your warriors is removed while defending in battle, it goes to the Acolytes box instead of your supply (`faction:cult$10.2.3`). This is your primary acolyte source under normal play. You do not gain acolytes when your warriors are removed as the attacker, or when removed by card effects outside of battle (such as Favor cards). Warriors removed by conversion conspiracies used against you — enemy factions do not have that ability — also do not trigger Revenge. Acolytes are finite; spend them deliberately.

**Edge case:** If your warriors are removed during a battle you initiated (you are the attacker), Revenge does not apply — your warriors return to supply normally. Only defensive removal triggers the acolyte pipeline.

### Pilgrims

You rule any clearing where you have at least one garden, regardless of warrior count (`faction:cult$10.2.4`). This overrides the Eyrie's Lords of the Forest ability (`rule:7.2.2`), which means you beat the Eyrie for rule in a clearing as long as you have a garden there. This rule is why gardens are so powerful defensively: a single garden grants rule even with zero warriors present, enabling Build rituals and protecting your scoring ability.

**Edge case:** Pilgrims grants rule, but rule alone does not prevent other factions from batttling in your clearing or placing pieces there. Other factions can still attack your gardens; they simply cannot dispute rule via warrior count.

### Fear of the Faithful

Whenever one of your gardens is removed from the map, you must discard a random card from your hand into the Lost Souls pile (`faction:cult$10.2.5`). This is a significant deterrent against attacking your gardens — but it is also a cascading risk to your hand size. Losing two gardens in a single attack can cut your hand from five to three cards, drastically limiting next turn's rituals. This is the primary leverage opponents have against you; protect gardens accordingly.

### The Lost Souls Pile

Whenever any card is spent or discarded by any player, it goes into the Lost Souls pile instead of the regular discard pile (`faction:cult$10.2.6`). This includes dominance cards. The Lost Souls pile sits in a distinct zone: dominance cards there are not available to take until the pile is cleared. In your Birdsong, you first read the pile to set the new Outcast, then flush it to the discard — at which point dominance cards become available again (`faction:cult$10.4.2`).

**Cross-faction interaction:** The Lilypad Diaspora has a conflicting rule (`faction:diaspora$16.2.3`) about where discarded cards go when both factions are in play. Consult the Golden Rule of Precedence (`rule:1.1`) if this interaction arises.

---

## Turn Structure

### Birdsong

Birdsong has three mandatory steps in this order (`faction:cult$10.4`):

**Step 1 — Adjust Outcast** (`faction:cult$10.4.1`): Look at the Lost Souls pile, ignoring all bird cards. The non-bird suit with the most cards present becomes the new Outcast. Move the outcast marker to that suit showing its Outcast face. If that suit was already the Outcast, flip the marker to its **Hated** side instead. If no single suit holds the most cards (a tie for first among the non-bird suits), the marker stays on its current suit and flips to Hated if it is not already Hated.

The distinction between Outcast and Hated matters throughout your turn: Hated gives a one-acolyte discount on all conspiracies (`faction:cult$10.4.3`).

**Step 2 — Discard Lost Souls** (`faction:cult$10.4.2`): Move all cards in the Lost Souls pile to the regular discard pile. Dominance cards are now available for any player to take.

**Step 3 — Perform Conspiracies** (`faction:cult$10.4.3`): Spend acolytes from the Acolytes box, returning them to your supply, to perform conspiracies. You may perform any number in any order. All conspiracies must target clearings matching the current Outcast suit. If the Outcast is Hated, each conspiracy costs one fewer acolyte.

The three conspiracies are:
- **Crusade** (2 acolytes; 1 if Hated): Initiate a battle in an Outcast clearing, or move at least one warrior from an Outcast clearing and optionally initiate a battle in the destination clearing. This is your primary mobility tool and offensive option.
- **Convert** (2 acolytes; 1 if Hated): Replace one enemy warrior in an Outcast clearing with one of your warriors. You must be able to both remove the enemy warrior and place your warrior (`faq:convert-sanctify-must-complete`).
- **Sanctify** (3 acolytes; 2 if Hated): Replace one enemy building in an Outcast clearing with a garden of the Outcast suit. Same completion requirement applies.

Note that movement via Crusade still follows standard movement rules (`rule:4.2`) — you must rule the origin or destination clearing. Pilgrims can give you rule at the destination if you already have a garden there.

### Daylight

You may reveal any number of cards from your hand into your play area and perform one ritual per revealed card, in any order and number (`faction:cult$10.5`). Revealed cards cannot be used for any other purposes during Daylight — they are effectively locked as ritual fuel.

The four rituals are:
- **Build** (`faction:cult$10.5.1`): Reveal a non-bird suited card. In a clearing you rule whose suit matches the card, place a garden whose printed suit also matches the clearing suit. You must rule the clearing and there must be an open building slot. This is how you place gardens manually rather than through Sanctify.
- **Recruit** (`faction:cult$10.5.2`): Reveal a non-bird suited card. In any clearing matching the card's suit, place a warrior. No rule requirement for Recruit — you can place warriors in clearings you do not control, as long as the suit matches.
- **Score** (`faction:cult$10.5.3`): Reveal a card and spend that same card (placing it in Lost Souls). Score the VP printed above the rightmost empty garden space of the matching suit. You cannot Score if no gardens of that suit are currently on the map. You may Score only once per turn per suit. Bird cards cannot be used for Score.
- **Sacrifice** (`faction:cult$10.5.4`): Reveal a bird card. Place one of your warriors from the map or supply into the Acolytes box. This is the only ritual bird cards enable, and the only way to generate acolytes outside of Revenge (being attacked while defending).

Revealed cards that you do not spend for Score return to your hand in Evening. Only cards spent via Score (and cards crafted) leave your hand this way.

### Evening

Evening has three mandatory steps in this order (`faction:cult$10.6`):

**Step 1 — Return Revealed Cards** (`faction:cult$10.6.1`): All cards you revealed this Daylight return to your hand. This restores your hand to its pre-Daylight state minus anything you spent for Score.

**Step 2 — Craft** (`faction:cult$10.6.2`): Optionally craft by activating gardens whose printed suit matches the current Outcast suit. Standard crafting rules apply (`rule:4.1`). Gardens used for crafting are not removed — activation just means you are using them as your crafting source.

**Step 3 — Draw and Discard** (`faction:cult$10.6.3`): Draw one card, plus one additional card per uncovered draw bonus symbol on your Gardens tracks. Then, if you hold more than five cards, discard down to five cards of your choice. Discards go to the Lost Souls pile.

The draw bonuses on your Gardens tracks (uncovered as you remove garden pieces from the track onto the map) are critical — they directly increase your hand size, which is the fuel for more rituals each Daylight.

---

## Scoring Engine

| VP Source | Amount | Trigger | Timing |
|---|---|---|---|
| Score ritual | VP printed at rightmost empty garden space | Spend matching non-bird card | Daylight |
| Enemy building removed in battle | 1 VP per building | You deal the hit | During battle (any phase) |
| Enemy token removed in battle | 1 VP per token | You deal the hit | During battle (any phase) |

The Score ritual is your dominant engine. Battle-removal VP is minor and secondary — your warriors are expensive to move and primarily used defensively.

The VP per Score ritual is determined by the gardens track position. Scores go up as gardens are removed from the track (placed on the map). With only one garden of a suit placed, the highest-value track spaces remain covered; as you place more gardens, you uncover higher-value scoring spaces (`faction:cult$10.5.3`). Community sources report that two gardens per suit enables reliable 2 VP per Score, and five gardens in a single suit can yield 4 VP per Score — though the exact printed values per space are on the physical faction board rather than in the Law.

Scoring once per suit per turn means your theoretical ceiling per turn equals the number of suits in which you have gardens on the map multiplied by the value at each suit's rightmost empty space. A board position with two gardens in all three suits scores up to 6 VP per turn if you hold three matching cards.

---

## Playbook

### Opening (Turns 1–2)

Your first priority is getting a garden placed in at least one adjacent clearing and scoring on turn 1. Missing turn 1 scoring creates a VP deficit that is difficult to recover from because your opponents will use those same turns to establish their own engines.

Turn 1 goal: reveal a card matching a clearing you rule (your starting corner, with its garden, or an adjacent clearing you can rule by building there). Build a garden. Then reveal the same suit card again — if you hold two matching cards — and Score. If you can only build, accept that and plan to Score on turn 2.

Choose your opening Outcast to match whatever suit you hold the most cards in. If your hand is all birds, this is a weak open — accept it and focus on Recruiting to prepare for Sacrifice chains.

By the end of turn 2 you want: at least one garden per suit you intend to score in, at least one uncovered draw bonus on your Gardens track, and enough warriors distributed to be able to defend any gardens you have placed.

### Mid-Game Pivots

**When to shift scoring width:** If you have been scoring only one suit and an opponent begins targeting those gardens, branch into a second suit immediately. One suit is fast to establish but fragile; two suits offers redundancy.

**When to use Conspiracies:** Conspiracies are often underutilized. If the Outcast is Hated, Convert costs only 1 acolyte — a very efficient action to remove a threatening warrior and gain presence in the Outcast clearing. When the Outcast aligns with a suit where a rival is building (Woodland Alliance bases, Eyrie roosts, Marquise recruiters), a Sanctify can redirect a building slot to a garden at three acolytes — or two if Hated.

**Reading the Lost Souls pile:** You see what is in the pile during Birdsong. If you notice the pile is split evenly between two suits, the Outcast will flip to Hated on its current suit — plan your acolyte spending around the discount. If opponents are discarding heavily in one suit, anticipate the shift and move warriors into Outcast clearings of that suit in preparation.

**When to Sacrifice:** If acolytes are low and conspiracies are unavailable or not useful, Sacrifice lets you convert warriors directly into acolytes using bird cards you cannot otherwise use productively. Do not sacrifice map warriors carelessly — every warrior removed from a clearing may cost you rule of a garden-bearing clearing.

### Endgame Routes

Once you are above 20 VP, your opponents will be looking to tear down your gardens. This is when Fear of the Faithful works hardest against you — losing two gardens in a late turn can cascade into three discards and a near-empty hand. Protect key clearings by maintaining warrior presence.

If you are within five turns of 30 VP and scoring consistently, resist the temptation to over-extend with Sanctify. Sanctifying one garden too many can invite a single Favor of the Foxes (`card:ROOT-73 (rootbasegame)`) or Favor of the Mice (`card:ROOT-74 (rootbasegame)`) to set you back dramatically. Play conservatively: score two to three cards per turn rather than building out to maximum gardens when already in the lead.

If opponents are successfully dismantling your gardens, pivot to Convert-heavy conspiracy turns to deny them pieces and regain control of key clearings, then rebuild gardens as you re-establish rule.

---

## Threat Factions

### Eyrie Dynasties

The Eyrie is your most common and most dangerous aggressor. Their Decree demands constant action and drives them to battle and move — often directly into your clearings — with a speed that most factions cannot match. Their Lords of the Forest (`rule:7.2.2`) would normally let them claim rule by warrior count, but your Pilgrims ability means any clearing with a garden is yours regardless (`faction:cult$10.2.4`). The real danger is that the Eyrie's recruiter placement and battle actions come in series; they can attack a clearing, remove your garden, trigger Fear of the Faithful, and cost you both the garden and a random card in a single battle.

Counter-play: Keep warriors in garden clearings. Eyrie warriors removed while attacking you do not give you acolytes (Revenge only triggers on your defensive removals). Turmoil cycles are windows: when the Eyrie goes into Turmoil, they lose their board tempo and are temporarily less threatening. If the Outcast aligns with an Eyrie clearing at that moment, Convert or Crusade aggressively.

### Marquise de Cat

The Marquise expands steadily and will build sawmills and workshops in clearings adjacent to yours. Their The Keep token (`rule:6.2.2`) locks placement in one corner, but their workshops spread widely. Cats can Sanctify your gardens by destroying them in battle — and they have the warriors to do so. Favor of the Foxes or Favor of the Mice are particularly brutal against you if the Marquise crafts one, as they remove all enemy pieces from a suit's clearings (`card:ROOT-73 (rootbasegame)`, `card:ROOT-74 (rootbasegame)`).

Counter-play: Avoid placing gardens in clearings directly adjacent to the Marquise's main production chain. Focus gardens in corners and isolated clearings. Let the Marquise fight the Eyrie or Woodland Alliance. If the Marquise scores too fast, target a workshop-dense clearing with Sanctify when your Outcast aligns.

### Woodland Alliance

The Woodland Alliance's Outrage ability (`rule:8.2.6`) means moving into sympathetic clearings costs your opponents cards — which go into the Lost Souls pile. This can actually help you, indirectly shifting your Outcast. The real threat is later in the game when the Alliance revolts and places bases: a base in a clearing you need removes your ability to Build there (bases take a building slot), and a revolt removes all warrior-class pieces in the clearing, which could wipe out your garden presence before the base appears. The Alliance's guerrilla tactics also indirectly deny you clearings by making those clearings costly for opponents to travel through, reducing the pile-churning that feeds your Outcast.

Counter-play: Monitor where the Alliance is placing sympathy tokens. If sympathy is spreading toward your core garden clearings, Sanctify an Alliance base early if possible (a 3-acolyte conspiracy converts it to a garden and removes the base's building slot competition). Otherwise, recruit warriors into Alliance-adjacent clearings to make the sympathy removal costs unfavorable for them.

### Lord of the Hundreds

The Warlord expands fast, rules many clearings, and generates significant battle pressure. Their pieces are removed for Oppress VP only when they rule without enemy pieces, meaning a Cult warrior in their clearing actively disrupts their score engine. This creates an interesting asymmetry: the Warlord will frequently attack you to clear your warriors, which feeds your Revenge pipeline and generates acolytes. Community discussion suggests the Hundreds matchup can actually be productive for acolyte farming — you absorb battles, collect acolytes, and Convert or Sanctify back.

Counter-play: Place single warriors in Hundreds-controlled clearings to deny oppression. Sacrifice warriors into acolytes if you need them but do not have defensive battles lined up. When the Outcast aligns with a Warlord stronghold's suit, a Sanctify can neutralize a key piece of their engine at a decisive moment.

---

## Card Priorities

### Crafted-Card Tiers

**Top priorities:**
- `card:ROOT-55 (rootbasegame)` **Better Burrow Bank**: In Birdsong, draw a card and give an enemy a card. This is your best persistent card. It effectively extends your hand every turn, fueling more rituals. Community consensus across multiple strategy sources names this the Cult's highest-priority craft.
- `card:ROOT-92 (rootbasegame)` **Royal Claim**: Score 1 VP per clearing you rule in Birdsong. Your Pilgrims ability gives you rule in every garden clearing; mid-game you can rule four to six clearings, making this a significant VP spike. Craft as early as possible.
- `card:ROOT-105 (rootbasegame)` **Tax Collector**: Remove one of your warriors to draw a card. Hand size is your resource; Tax Collector converts warrior presence into cards, which is exactly the trade you want to make when warriors are not actively defending gardens.
- `card:ROOT-63 (rootbasegame)` **Command Warren**: Initiate a battle at the start of Daylight. Gives you offensive battle access outside of Conspiracies, useful when the Outcast does not align with where you need to fight.

**Situational:**
- `card:ROOT-51 (rootbasegame)` **Armorers**: Ignore all rolled hits taken in one battle. Your gardens are fragile; Armorers in hand can neutralize a devastating attack. Best against high-hit factions like Eyrie with Commander.
- `card:ROOT-94 (rootbasegame)` **Sappers**: Deal an extra hit as defender. You are often defending; extra defensive hits feed Revenge by increasing the chance your attacker survives (keeping the battle going longer), though Sappers itself does not directly generate acolytes.
- `card:ROOT-60 (rootbasegame)` **Cobbler**: Take a move in Evening. Your warriors are normally locked to Conspiracy movement in Birdsong; Cobbler gives you an extra repositioning opportunity outside that constraint.
- `card:ROOT-102 (rootbasegame)` **Stand and Deliver!**: Take a random card from an enemy in Birdsong. Useful for hand manipulation and disrupting opponents who hold specific suits.

**Skip or low priority:**
- `item:sword`, `item:crossbow` — combat items. Your battle output is low-priority and you have few ways to use combat items consistently.
- `card:ROOT-58 (rootbasegame)` **Brutal Tactics**: Costs you VP via the opponent's gain for each extra hit. Your battles are already defensive; this actively counteracts your interests.

### Ambush Guidance

Hold ambush cards matching suits of your most important garden clearings (`card:ROOT-46 (rootbasegame)` through `card:ROOT-49 (rootbasegame)`). Fear of the Faithful already punishes garden destruction; an ambush deterrent compounds the cost for attackers. Do not spend ambushes speculatively — they are most valuable as a known-to-your-opponent threat that discourages attacks in the first place.

### Dominance Considerations

Dominance cards (`card:ROOT-67 (rootbasegame)` through `card:ROOT-70 (rootbasegame)`) are generally not your primary plan. However, holding one as insurance is viable — it can be swapped into your hand in Daylight using the standard dominance card rules (`rule:3.2.1`). If an opponent surges ahead and your gardens are intact across the required suit clearings, a late-game dominance play can win when VP accumulation would take too long.

### Card Economy Principles

Reveal cards freely in Daylight — they return to your hand in Evening unless spent for Score. The cost of revealing is zero. The cost of Scoring is one card (placed in Lost Souls). Therefore, score as many suits as you can each turn, spending one card per suit. Cards spent for Score feed the Lost Souls pile, which influences next turn's Outcast. Spend cards of the suit you want to become (or stay as) Outcast to nudge the pile in your favor.

---

## Common Pitfalls

- **Missing turn 1 scoring.** You need a matching card in hand and a garden on the map. If you cannot score turn 1, prioritize building a garden first and score turn 2. Missing two turns of scoring early is almost unrecoverable.

- **Over-relying on one suit.** Building five gardens in one suit maximizes per-card VP but leaves you with a single point of failure. One Favor card removes all your scoring in an entire suit instantly. Two suits is the practical minimum; three is ideal.

- **Ignoring draw bonuses.** Gardens on the map also uncover draw bonus symbols on your Gardens tracks. More draws mean more ritual fuel. Players who build gardens purely for Scoring without tracking draw bonuses fall behind on hand quality.

- **Spending all cards on non-Score rituals.** Recruit and Build are necessary, but they do not score points. Turn over-investment in warriors (Recruit) delays gardens (Build) and cuts into Scoring. Score at least once per turn even in early turns.

- **Hoarding acolytes.** Acolytes not spent are opportunity cost. When the Outcast is Hated, conspiracies cost one fewer acolyte — this is often the right time to spend aggressively, not save.

- **Sacrificing map warriors carelessly.** Warriors on the map defending gardens anchor your rule (combined with Pilgrims). Sacrificing a warrior from a garden clearing to gain an acolyte can cost you rule of that clearing if the garden is then removed, triggering Fear of the Faithful.

- **Letting opponents discard into a favorable Outcast for free.** Track the Lost Souls pile throughout the round. If a suited card is discarded late in another player's turn, it counts toward next Birdsong's Outcast calculation. Anticipate where the Outcast will land, not just where it is.

- **Treating bird cards as dead cards.** They are useless for Build/Recruit/Score but unlock Sacrifice. If you have more bird cards than you can use for Sacrifice, you may need to discard them in Evening — putting them into Lost Souls, which does not count for Outcast resolution (birds are ignored when tallying the pile).

---

## Mechanic Clarifications

### Must Convert/Sanctify complete fully?

**Q:** Can you use Convert to only remove an enemy warrior without placing your own? Can you use Sanctify to only remove a building without placing a garden?

**Resolution:** No. The Law requires you to complete the conspiracy — you must both remove the enemy piece and place your own. If you cannot place your warrior or garden (e.g., no garden pieces remaining or no supply warriors), you cannot perform the conspiracy at all.

**Citation:** `faction:cult$10.4.3`; `faq:convert-sanctify-must-complete`

---

### Does Revenge trigger on attack, not just defense?

**Q:** If your warriors are removed while you are the attacker in a battle, do they go to Acolytes?

**Resolution:** No. Revenge specifies removal while defending. Warriors removed when you are the attacker return to supply normally.

**Citation:** `faction:cult$10.2.3`

---

### Pilgrims vs. Lords of the Forest

**Q:** If the Eyrie has more warriors in a clearing where you have a garden, who rules?

**Resolution:** You do. Pilgrims explicitly overrides the Eyrie's Lords of the Forest ability. Having any garden in a clearing grants you rule regardless of warrior counts.

**Citation:** `faction:cult$10.2.4`, `rule:7.2.2`

---

### Lost Souls pile and Dominance cards

**Q:** Can a player take a dominance card from the Lost Souls pile?

**Resolution:** No. Dominance cards in the Lost Souls pile are not available to take. They only become available after they are moved to the regular discard in Step 2 of your Birdsong (`faction:cult$10.4.2`).

**Citation:** `faction:cult$10.4.2`

---

### Crafting suits and gardens off-suit

**Q:** You have a fox garden in a mouse clearing. Does that garden provide a mouse crafting hammer or a fox crafting hammer for the Cult?

**Resolution:** The garden's printed suit (fox) is what matters for Cult crafting, not the clearing's suit. The Cult activates gardens "whose printed suit matches the Outcast suit." If the Outcast is fox, this garden can be activated even though it sits in a mouse clearing. (`faction:cult$10.2.1`). The parenthetical note in the Law specifies this interaction is relevant in games with the Lost City or Lilypad Diaspora.

**Citation:** `faction:cult$10.2.1`

---

### Score ritual and no-garden restriction

**Q:** Can you Score a suit via the Score ritual if you have no gardens of that suit currently on the map?

**Resolution:** No. The Score ritual explicitly requires that at least one garden of the matching suit be on the map (`faction:cult$10.5.3`).

**Citation:** `faction:cult$10.5.3`

---

## Reference Index

**Faction citation key:** `faction:cult`

**Primary rule section:** `rule:10.`

**Related glossary / item references:**
- `item:boot` — standard movement item (relevant for Vagabond interactions)
- `item:crossbow` — combat item (craftable if Outcast suit matches)
- `item:hammer` — crafting activation concept (`rule:4.1.1`)

**Hireling form:** The Lizard Cult does not have a dedicated hireling in the base Marauder/Riverfolk/Underworld hireling sets. Check expansion content for any future addition.

**Cross-faction interactions:**

| Faction | Interaction | Rule |
|---|---|---|
| Eyrie Dynasties | Pilgrims overrides Lords of the Forest | `faction:cult$10.2.4`, `rule:7.2.2` |
| Lilypad Diaspora | Competing rule about where spent/discarded cards go | `faction:cult$10.2.6`, `faction:diaspora$16.2.3` |
| Riverfolk Company | Crafting suit exceptions via Lost City | `faction:cult$10.2.1`, `faction:riverfolk$11.2.1` |
| Woodland Alliance | Alliance Outrage triggers Lost Souls discards (feeding Outcast) | `rule:8.2.6`, `faction:cult$10.2.6` |
| Vagabond | Vagabond aid and trade interactions normal; no special Cult-Vagabond rule | `rule:9.2.8` |

**Key FAQ entries:**
- `faq:convert-sanctify-must-complete` — Convert and Sanctify must be completed fully; cannot partially execute.
