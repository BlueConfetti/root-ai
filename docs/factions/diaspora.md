# Lilypad Diaspora

## At a Glance

The Lilypad Diaspora scores points by spending Woodland cards to cash in your
network of Peaceful enclaves — but enemy aggression can flip those enclaves to
Militant in an instant, turning your economic engine into a war machine you
didn't ask for.

| Field | Value |
|---|---|
| Reach | 7 (`rule:5.1`) |
| Complexity | High |
| Scoring Tempo | Punctuated (burst once Peaceful enclaves accumulate; volatile when flipped) |
| Color | Gold-green |
| Faction Icon | Frog |
| Faction Citation Key | `faction:diaspora` |
| Primary Rule Section | `rule:16.` |

**Setup constraints.** You start in a clearing on the river — not necessarily a
corner. You choose any river clearing at setup time (`faction:diaspora$16.3.2`).

---

## Win Condition

Your path to 30 VP runs through your Evening Integrate action
(`faction:diaspora$16.6.2`): you spend one card and score 1 VP for each
Peaceful enclave on the map whose clearing matches that card's suit. A single
Rabbit card spent while you have six Peaceful enclaves in Rabbit clearings
scores you 6 VP in one action. That is the engine you are building.

A secondary trickle comes from standard play: removing enemy buildings or
tokens scores 1 VP each (`rule:3.2.1`), and crafting items scores whatever the
card awards (`rule:3.2.2`). Neither of these will carry you to 30 on their own.

**Dominance path.** The Frog Dominance card adds a fifth dominance option to
the table. If you activate it (requiring 10 VP, like any dominance,
`rule:3.3.1`), you win at the start of your Birdsong if you rule at least two
enclaves on the river (`faction:diaspora$16.2.2.1`). This is a narrow
geographic condition — river clearings are contested and visible — but the card
also recruits the player holding Frog Dominance as a defender whenever the
Diaspora is attacked (`faction:diaspora$16.2.2.1.1`), which creates a strong
political incentive for another player to activate it. In a two-player game,
the Frog Dominance card is removed permanently before setup
(`faction:diaspora$16.3.3`).

**Standard Dominance.** You can activate any of the four Woodland dominance
cards normally. Because you control the frog suit via your enclaves, Militant
enclaves in the right clearings can make it easier to rule the three needed
clearings for a non-bird dominance win — but this is a situational route, not
a primary plan.

**Tempo.** Your VP output is slow while you are placing enclaves and managing
militants, then spikes sharply once you have five or more Peaceful enclaves
in matched clearings. The game's balance point is whether you can build that
network before opponents take too many points away from you or force your
enclaves Militant.

---

## Setup

Follow these four steps in order (`faction:diaspora$16.3`).

**Step 1 — Gather Pieces.** Take 20 warriors and 12 enclave tokens
(`faction:diaspora$16.3.1`).

**Step 2 — Place Warriors and Enclave.** Choose a clearing on the river and
place 5 warriors and 1 enclave on its Peaceful side there. This is your
starting clearing (`faction:diaspora$16.3.2`). You are not restricted to a
corner, though many river clearings happen to touch one. You do not need to
rule this clearing — you place regardless.

**Step 3 — Remove Dominance (two-player only).** If you are playing with only
two players, remove the Frog Dominance card from the game permanently
(`faction:diaspora$16.3.3`). In larger games, shuffle it in with the frog
cards.

**Step 4 — Shuffle Frog Cards.** Shuffle all frog cards (14 cards, or 13 if
Frog Dominance was removed) into the shared deck. Place the Pond placard near
the shared deck (`faction:diaspora$16.3.4`).

### Setup Theory

**Starting clearing choice.** Pick a river clearing that is adjacent to two or
three other clearings you want to expand into on turn one. Central river
clearings give more expansion options; edge river clearings are more
defensible. Either can work — the key is having neighbors you can reach with
Settle.

**Neighbor considerations.** You want opponents who will not immediately
attack your Peaceful enclaves. Factions with low aggression incentives in the
early game (Riverfolk Company, some Eyrie builds) are friendlier neighbors
than factions whose economy rewards clearing your tokens (Corvid Conspiracy,
Woodland Alliance). Marquise de Cat's aggressive expansion toward the river
can threaten your early enclaves. Try to start with at least one direction
where you have space to grow without drawing immediate fire.

**Opening hand priorities.** Keep cards that match your intended expansion
clearings — these are what you will spend for Integrate. A hand with
representation in two or three suits gives you flexibility. Bird cards are
useful because you can treat them as any suit (`rule:2.1.1`). Frog cards that
appear in your opening hand can be set aside in the Pond or used for crafting
activations via their frog crafting icons (`faction:diaspora$16.2.1.2`), but
they cannot be spent for Integrate (`faction:diaspora$16.6.2`). Plan
accordingly.

---

## Faction Rules and Abilities

### Enclaves

Your 12 enclave tokens are double-sided: Peaceful on one face, Militant on the
other (`faction:diaspora$16.2.1`).

**Peaceful enclaves** add the frog suit to their clearing, making it
dual-suited — both the printed suit and frog are valid for matching purposes
(`faction:diaspora$16.2.1.1`). Other players moving into a dual-suited
clearing can match it with either suit for crafting costs, Outrage triggers,
and similar effects. This is a map-wide change that affects everyone.

**Militant enclaves** replace their clearing's printed suit with the frog suit.
The clearing is now frog-only (`faction:diaspora$16.2.1.1`). Any faction whose
economy depends on matching the printed suit (Woodland Alliance Outrage,
Lizard Cult garden placement, faction cards like Favor of the Foxes) finds the
clearing stripped of its original identity. This is an interference tool, not
just a defensive one.

**Matching.** A clearing with a Militant enclave can be matched with the frog
suit. A clearing with a Peaceful enclave can be matched with either the frog
suit or its printed clearing suit (`faction:diaspora$16.2.1.2`). This
distinction matters when you or an opponent are checking suit requirements.

### Frog Cards and the Pond

During setup, 14 frog cards enter the shared deck (`faction:diaspora$16.3.4`).
These cards bear the frog suit. Some carry frog crafting icons — the only way
to activate frog-suit crafting pieces. Many have effects that nominally force
the Diaspora to act; if you craft them yourself, you get to direct the effect
(`faction:diaspora$16.2.2`).

When a frog card would go to the shared discard pile, it goes instead to the
Pond — a separate face-up stack on the Pond placard (`faction:diaspora$16.2.3`).
The Pond's top card is visible to everyone.

**Drawing from the Pond.** Whenever any player draws cards, they may draw the
top card of the Pond instead of the shared deck — one substitution per draw
event (`faction:diaspora$16.2.3.1`). This matters most when you know a frog
card on top of the Pond matches a suit you need for Integrate.

**Reshuffling.** When the shared deck is reshuffled, all Pond cards are shuffled
back into it (`faction:diaspora$16.2.3.2`). The Pond does not persist across
reshuffles.

### Fears Come to Pass

After a battle where an enemy attacks a clearing containing a defending
Peaceful enclave, or when an enemy removes a Peaceful enclave outside battle,
flip all Peaceful enclaves with that enemy's pieces to Militant. Place 1
warrior at each flipped enclave (`faction:diaspora$16.2.5`).

This is your reactive radicalization mechanic. A single aggressive move by an
opponent can flip multiple enclaves in a chain if that opponent has pieces
scattered across your network. The chain is limited to enclaves with that
specific enemy's pieces — a different enemy does not trigger the same cascade.
The attacker cannot selectively target only one enclave to minimize the
cascade; Fears Come to Pass fires on the clearing attacked, and then catches
every other enclave with that enemy's pieces.

### Negotiations

Once during their turn, an enemy with faction pieces in a clearing with a
Militant enclave may flip it to Peaceful (`faction:diaspora$16.2.6`). If they
do not rule that clearing but another player does, the flipping player must
give the ruler one card. If the flipping player rules it, or no one rules it,
no payment is needed.

Negotiations is not your action — it belongs to your opponents. It creates a
political lever: opponents who want the Woodland suit restored (because
Militant enclave is blocking them) can take the diplomatic route rather than
fighting you. You benefit by getting a Peaceful enclave back.

### Swimmers

You treat rivers as paths (`faction:diaspora$16.2.7`, `rule:2.3`). You may move
along a river that fully links an origin and destination clearing, ignoring the
need to rule either end. This overrides the standard movement rule requiring
you to rule the origin or destination (`rule:4.2.1`). No other faction gains
this ability by default — it is yours uniquely until an effect shares it.

River movement lets you project force and place enclaves across the board
without relying on contiguous land paths. On many maps, the river shortcut
connects distant corners and can let you reach a second cluster of clearings
by turn two.

### Crafting

You craft by activating enclaves during your Birdsong (`faction:diaspora$16.2.8`,
`rule:16.4.1`). Each enclave's suit for crafting purposes matches its clearing:
a Peaceful enclave in a Fox clearing activates as Fox, a Militant enclave in
the same clearing activates as Frog. Frog crafting icons on frog cards require
a frog-suit enclave (i.e., a Militant enclave, or a Peaceful enclave in a
clearing that has been declared frog) to activate (`rule:4.1.1`).

---

## Turn Structure

### Birdsong

Your Birdsong has two steps, in order (`faction:diaspora$16.4`).

**Step 1 — Craft.** You may activate enclaves to craft cards in your hand
(`faction:diaspora$16.4.1`). This is optional and can be skipped. Crafting
here is your window to turn frog cards into persistent effects before the rally
or reconcile choice commits your tempo.

**Step 2 — Rally or Reconcile (mandatory choice, pick one).**

- **Rally:** Place 1 warrior at each Militant enclave (`faction:diaspora$16.4.2.1`).
  Warriors are placed from your supply. If your supply runs dry, you place
  warriors at as many Militant enclaves as supply allows. Rally is the fast
  path to warriors, but it locks you into more Militant enclaves staying
  Militant.

- **Reconcile:** Flip any number of Militant enclaves to Peaceful
  (`faction:diaspora$16.4.2.2`). Each time you flip one, if a player rules that
  clearing, that player draws 1 card (which may be from the Pond). You draw
  nothing — the draw goes to the ruler. If no one rules, no draw happens.
  Reconcile can span multiple enclaves in one Birdsong: flip three Militant
  enclaves, and up to three players may draw cards. This is diplomacy as
  resource transfer. Players who benefit from Reconcile have an incentive to
  let your enclaves stay Peaceful and to avoid attacking them.

The Rally/Reconcile choice is the most strategically loaded moment in your
turn. Rally when you need warriors and can afford the Retaliate burden. Reconcile
when you are ready to shift back toward scoring and want to build diplomatic
credit.

### Daylight

You may Settle or Provoke up to 3 times in any order and combination
(`faction:diaspora$16.5`).

**Settle.** Choose a clearing. You may move into it from any number of adjacent
clearings, once each (`faction:diaspora$16.5.1`). Then, you may either:

- Initiate a battle in that clearing, or
- Place a Peaceful enclave in that clearing, if the clearing has no enclave
  already and you rule it.

Settle combines movement and action into a single action slot. Moving from
multiple adjacent clearings simultaneously into the target is efficient — it
concentrates warriors without spending multiple moves. You must choose battle
or enclave placement, not both, after moving.

**Provoke.** Flip a Peaceful enclave to Militant, or place a Militant enclave
on the river or at a Diaspora warrior (`faction:diaspora$16.5.2`). Then place
1 warrior at each Militant enclave. Finally, discard a random card from your
hand. If you have no cards in hand, skip the discard. Provoke is how you
voluntarily generate warriors — you trade a card (random!) and convert your
scoring network to trigger the Rally bonus early. It is costly but sometimes
necessary when your supply of warriors is dangerously low.

A new Militant enclave placed on the river does not require you to rule — you
simply place it. A Militant enclave placed at a Diaspora warrior just requires
that warrior's presence.

### Evening

Your Evening has three steps, in order (`faction:diaspora$16.6`).

**Step 1 — Retaliate (mandatory).** You must battle at each Militant enclave
(`faction:diaspora$16.6.1`). If a Militant enclave has no enemy pieces in its
clearing, you do not battle there (there is no valid defender). If enemy pieces
are placed during this step at a Militant enclave that had no enemy pieces
when the step began, you must battle them — the obligation extends to pieces
that arrive mid-Retaliate. You must also battle Riverfolk Company Mercenaries
if they are the only way to battle. Retaliate is a cost, not an option: every
Militant enclave that has enemies in its clearing demands a battle, every
Evening, regardless of odds.

**Step 2 — Integrate (optional, once).** You may spend one card to score 1 VP
for each Peaceful enclave whose clearing matches the spent card's suit
(`faction:diaspora$16.6.2`). You cannot spend a frog card for Integrate — frog
is not a valid Integrate suit. You may Integrate only once per Evening; you
cannot spend two cards to score twice in the same Evening.

The multiplier here is what makes the engine powerful. Three Rabbit clearings
with Peaceful enclaves = 3 VP from a single Rabbit card. Six clearings across
two suits = potential 6 VP split across two turns' Integrations, but only one
suit per Evening.

**Step 3 — Draw and Discard.** Draw cards based on your Peaceful enclave count
(`faction:diaspora$16.6.3`):

| Peaceful Enclaves | Cards Drawn |
|---|---|
| 0–1 | 1 |
| 2–3 | 2 |
| 4–7 | 3 |
| 8+ | 4 |

Then discard down to 5 cards if over hand limit. Your card economy scales with
your Peaceful network — this is the second benefit of keeping enclaves Peaceful.

---

## Scoring Engine

| VP Source | Amount | Trigger | Timing |
|---|---|---|---|
| Integrate | 1 per matching Peaceful enclave | Spend 1 matching non-frog card | Evening, Step 2 |
| Crafting items | Per card | Craft an item card | Birdsong |
| Removing enemy buildings/tokens | 1 per piece | Remove in battle | Any battle |

The Integrate action is your primary engine. Everything else is incidental.

The secondary draw mechanic is not a VP source, but it is a scoring enabler:
more Peaceful enclaves mean more cards drawn, which means more Integrate
ammunition available in future turns.

---

## Playbook

### Opening (Turns 1–2)

Your turn-one goal is to establish a second enclave. You start with 1 Peaceful
enclave and 5 warriors. In Birdsong you must Rally or Reconcile — with only
one Militant enclave (none if you Rally without Militants), Reconcile cannot
flip anything, so you will Rally if you have a Militant enclave or simply must
choose Reconcile and do nothing if all enclaves are Peaceful. On turn one you
typically have no Militant enclaves (your starting enclave is Peaceful), so
Reconcile passes without effect and you begin Daylight.

In Daylight, Settle into an adjacent clearing with enough warriors to rule,
then place your second Peaceful enclave. Use your remaining Settle actions to
move warriors into position for more enclaves. Aim to end turn one with two or
three enclaves placed and your warriors spread toward clearings you can rule
turn two.

On turn two, Settle a third and fourth clearing. The card draw bonus kicks in
at 2–3 Peaceful enclaves: you will draw an extra card in Evening, which begins
to self-fund future Integrates. If you can Integrate with even a small yield
(2–3 VP) on turn two, do so — the early points matter.

Avoid Provoke in the opening unless your supply of warriors runs critically
short. The random-card discard is a tax you cannot afford when you are still
building your hand.

### Mid-Game Pivots

Once you have 4–6 Peaceful enclaves spread across two or three suits, your
Engine is online. At this point:

**If your network is intact:** Pursue an Integrate-heavy line. Each Evening,
cash in your highest-yield suit match. Use Settle to push enclaves into
adjacent clearings, prioritizing suits where you already have clusters.
Continue Reconciling in Birdsong rather than Rallying, unless threatened.

**If Fears Come to Pass fires repeatedly:** You are accumulating Militant
enclaves and warriors. Shift into a Retaliate-pressure mode: let the warriors
from Rally compound, fight battles in Evening to remove enemy tokens and score
incidental VP, then Reconcile aggressively in Birdsong once the threatening
faction backs off. Your goal is to buy enough peace to flip enclaves back and
resume scoring.

**Sign to switch — too many Militants:** If you have more than three or four
Militant enclaves, your Evening Retaliate step is forcing you into battles you
do not control. Prioritize Reconcile every Birdsong until you are back under
two Militants. The warriors from Rallying compound quickly; you may find
yourself with a substantial board presence after several forced Rallies, which
you can convert into pressure on a lagging faction.

**Sign to switch — one suit dominates your network:** If most of your Peaceful
enclaves cluster in Rabbit clearings, plan your Integrate around Rabbit cards
and build your hand accordingly. Drawing from the Pond when a Rabbit frog card
sits on top is worth a detour.

**Diplomatic use of Reconcile:** When you Reconcile a clearing ruled by a
strong faction who would benefit from restoring the original suit, you are
paying them a card draw. Use this deliberately. Flipping a Militant enclave
ruled by the Eyrie in a suit their Decree needs costs you a warrior-generator
and gives them a card — but it might buy their neutrality for several turns.
That trade is worth running when the Eyrie has another faction in their
crosshairs.

### Endgame Routes

Your closing pattern is simple in structure but demands care in execution:
maximize Peaceful enclave count in two or three concentrated suits, hold cards
matching those suits, and cash in once per Evening at maximum yield.

If you have 8 or more Peaceful enclaves, you are drawing 4 cards per Evening
(`faction:diaspora$16.6.3`), which is the maximum. A single Integrate in a
suit with 5 enclaves scores 5 VP. Over two or three turns from 20 VP, you
close out.

**Protect your lead.** Once you are within striking distance of 30 VP, other
players have a strong incentive to attack your enclaves. Fears Come to Pass
will fire — plan for it. Keep one or two Militant enclaves intentionally in
defensible clearings to give yourself warrior reserves. Do not Reconcile
everything before the finish line.

**Dominance as a closer.** If you are stuck at 25+ VP and opponents are
actively blocking your Integrate path, a dominance card (standard or Frog) can
serve as a credible threat that forces table attention away from you and onto
the dominant player — buying you the turns you need to close.

---

## Threat Factions

### Marquise de Cat

The Marquise's economic model rewards building across the map and defending
those buildings with warriors. When you face the Marquise, her wide warrior
presence means she will often have pieces in clearings with your Peaceful
enclaves. One battle where she attacks your enclave triggers Fears Come to
Pass across every clearing she shares with you — potentially flipping four or
five enclaves Militant in a single action. She also has the Keep token
(`rule:6.2.2`), which prevents enemy tokens in its clearing; if the Keep sits
on a river clearing you want for your starting position, you cannot place an
enclave there via Settle (you cannot rule it without displacing her).

Counter-play: Start in a river clearing away from the Marquise's likely keep
placement. Avoid overlapping your enclave network with her building network
until mid-game when you have warriors to retaliate meaningfully. You can also
leverage Negotiate — she has pieces, so she can flip your Militant enclaves
Peaceful herself once she understands the suit-restoration benefit. Position
your Militant enclaves in clearings where she wants the original suit for
crafting or card play.

### Corvid Conspiracy

The Corvid's Flip conspiracy (`rule:13.5.3`) removes your buildings and tokens
(enclaves are tokens, `rule:2.5`) and places their own pieces. Removing a
Peaceful enclave outside battle triggers Fears Come to Pass — so a single Flip
conspiracy executed against one of your Peaceful enclaves can cascade into
multiple Militant flips across your whole network if the Corvid has scattered
face-down plots near your clearings. The Corvid also operates face-down,
making it hard to predict which clearing is about to be targeted.

Counter-play: Do not cluster too many Peaceful enclaves in the same Corvid-
adjacent region. Keep warriors present in clearings with high-value Peaceful
enclaves (many adjacencies, valuable suit matches) to force the Corvid to fight
for removal rather than using free plot resolution. Corvid plots are tokens too
— battling them scores VP and clears the threat.

### Woodland Alliance

The Alliance scores points from spreading Sympathy tokens and revolting. Their
Sympathy tokens do not directly attack your enclaves, but revolts require
bases in clearings matching an unbuilt base suit (`rule:8.4.1`). Your Militant
enclaves cover the printed suit with frog — a clearing with a Militant enclave
can no longer match fox, rabbit, or mouse for Woodland's revolt condition.
This makes you an inadvertent hard counter to Woodland expansion when you have
Militant enclaves in suits they need.

However, the Alliance's Outrage ability (`rule:8.2.6`) fires when players
move warriors into Sympathetic clearings. Your Settle action moves warriors
frequently — if you move into a Sympathetic clearing, you trigger Outrage. You
hand the Alliance free cards and supporters, fueling their eventual revolt.

Counter-play: Track which clearings have Sympathy tokens before Settling.
Prefer Settling into non-Sympathetic clearings when you have options. When you
need to move through a Sympathetic clearing, do it in a concentrated push with
enough warriors to battle the Sympathy token away rather than sitting in the
clearing and fueling the Alliance.

### Lord of the Hundreds

The Warlord's Mob die (`rule:14.4.1`) and Rage step place his mobs broadly
across the board, and his Oppress scoring requires clearing enemy pieces from
clearings he rules. Your enclaves are tokens, and he will remove them for
both the VP and the Oppress condition. Because he ranges wide, he is likely to
have pieces in many of your clearings simultaneously — meaning a single battle
against a Peaceful enclave can cascade Fears Come to Pass across a large
portion of your network.

Counter-play: Your Retaliate step in Evening can actually help here: if the
Warlord has mobs in clearings with your Militant enclaves, you are fighting
him every Evening anyway, chipping his pieces. Prioritize Reconcile when the
Warlord is nearby to reduce the Militant enclave count and thus reduce the
cascade surface. A smaller Militant enclave footprint limits how much damage
Fears Come to Pass can do.

---

## Card Priorities

### Crafted-Card Tiers

You craft during Birdsong by activating enclaves (`faction:diaspora$16.4.1`).
Your crafting bandwidth is limited by how many enclaves you have, where they
sit, and whether they are Militant (frog suit) or Peaceful (dual-suited). Most
high-value craftable items require specific Woodland suits — fox, rabbit, or
mouse. To activate those, you need Peaceful enclaves in matching clearings.

**High Priority.**

`item:boot` (Cobbler, `card:ROOT-67 (Base Game)`) — extra move actions each turn. The Diaspora's strength is spreading enclaves across the board; extra moves let you concentrate warriors faster for Settle-and-place sequences.

`item:sword` (Sword-bearing craftable cards) — extra hits in battle help your
mandatory Retaliate battles and reduce warrior losses at Militant enclaves.

`item:coin` (Money card variants) — VP on craft, useful to spike points in mid-game when Integrate yield is still building.

`item:hammer` (craftable items providing bonus actions) — situationally useful;
primarily valuable if you have frog crafting icons available to activate.

**Situational.**

`item:crossbow` (Crossbow) — useful for removing hard-to-reach tokens without
battling. `card:Crossbow (Base Game)` lets you remove a single enemy token in
a clearing with a warrior — can pre-empt a Fears Come to Pass cascade by
removing enemy pieces before they multiply.

Persistent-effect cards that draw extra cards or give action bonuses can
compound your card engine. Evaluate based on your Peaceful enclave count: more
enclaves means more cards already; in late game, persistent action bonuses
matter more than card draw.

**Low Priority / Skip.**

Multi-suit crafting requirements are expensive for you unless you have enclaves
spread across multiple suit-matched clearings. Weigh activation cost against
the VP or effect before committing.

### Frog Cards

You cannot Integrate with frog cards — they are excluded from Integrate's
suit-matching (`faction:diaspora$16.6.2`). Their primary use for you is as
crafting activators (frog crafting icon) or as wild spends for items.

Bird cards in the standard deck are wild (`rule:2.1.1`); frog cards are not
treated as wild by any rule in p16. You can craft frog cards during Birdsong
if you have frog-suit crafting icons available. If an opponent crafts a frog
card whose effect forces the Diaspora to act, they choose the specifics — watch
for adversarial craft plays.

### Ambush Cards

Hold ambush cards to protect high-value Peaceful enclave clearings from attack.
An ambush in a clearing with several Peaceful enclaves (especially frog-suit
Peaceful enclaves that would trigger a cascade if attacked) can deter or
punish an aggressor. A fox, rabbit, or mouse ambush (`rule:2.1.2`) can be used
in any clearing matching that suit — remember that your Peaceful enclaves make
clearings dual-suited, so a Rabbit ambush works in any Rabbit or Frog clearing
that holds a Peaceful enclave. This effectively widens the pool of clearings
where you can ambush defenders.

### Dominance Cards

Do not discard standard dominance cards carelessly — they can be spent for
their suit if you need to fuel an Integrate in a tight turn. A Bird dominance
card in hand is a flexible resource (`rule:2.1.4`). The Frog Dominance card,
if it enters your hand, is worth holding if another player might activate it
for the Enclave Defense benefit (`faction:diaspora$16.2.2.1.1`). You cannot
activate a dominance card until you have at least 10 VP (`rule:3.3.1`).

---

## Common Pitfalls

- **Overextending Provoke early.** Provoke discards a random card and produces
  Militant enclaves — both are costs you cannot easily recover. Using Provoke
  more than once or twice in the opening burns your hand and creates Retaliate
  obligations that eat your Evening tempo.

- **Ignoring Retaliate odds.** You must battle at every Militant enclave with
  enemy pieces. If you Rally and accumulate multiple Militant enclaves in
  clearings where a strong faction has many warriors, you are forced into
  losing battles that destroy your warriors faster than you can replenish them.
  Count your Militant enclaves before you Rally.

- **Spreading too thin.** Twelve enclaves across twelve different clearings may
  look like board presence, but it dilutes your Integrate yield: one per suit
  per clearing means one VP per card spent. Cluster enclaves in two or three
  suits to build multiplicative Integrate turns.

- **Not tracking Fears Come to Pass cascades.** If one faction has pieces near
  many of your Peaceful enclaves, a single attack can flip six enclaves
  simultaneously. Before settling into a clearing adjacent to an aggressive
  faction's main body, count how many of your Peaceful enclaves share that
  faction's pieces. The cascade is not limited to adjacent enclaves — it hits
  every enclave with that faction's pieces anywhere on the board.

- **Spending frog cards for Integrate.** Frog cards cannot be spent to score
  Integrate (`faction:diaspora$16.6.2`). Holding a hand of frog cards while
  announcing Integrate produces nothing. The Pond can return frog cards to the
  deck on reshuffle, but mid-game frog-heavy draws are a real hazard if the
  deck has not reshuffled yet.

- **Reconcile without diplomatic context.** Reconcile gives card draws to the
  rulers of the cleared clearings, not to you. Blindly Reconciling all Militant
  enclaves when no one rules them accomplishes nothing. Identify which Reconcile
  targets are politically valuable (ruled by a faction you want to placate) and
  which can wait.

- **Neglecting river movement.** Swimmers (`faction:diaspora$16.2.7`) lets you
  move along rivers ignoring rule — this is a significant mobility advantage on
  most maps. Forgetting this ability and routing your warriors purely by land
  paths often costs two or three turns of positioning.

---

## Mechanic Clarifications

### Q: Can a Peaceful enclave count as both its printed suit and frog for matching on the same effect?

**Resolution.** Yes. A Peaceful enclave makes the clearing dual-suited
(`faction:diaspora$16.2.1.1`). Any effect that asks whether a clearing matches
a suit can match against either the printed suit or frog. This applies to
Integrate (you spend a Fox card and score all Peaceful enclaves in Fox
clearings — a Peaceful frog enclave in a Fox clearing counts), to crafting
activation (`rule:4.1.1`), and to movement rule checks.

**Citation.** `faction:diaspora$16.2.1.2`

---

### Q: If I Reconcile a Militant enclave, does the suit immediately return to printed?

**Resolution.** Yes. Flipping a Militant enclave to Peaceful restores the
clearing to dual-suited (printed + frog) immediately. If an opponent had
Militant frog suppressing their Outrage trigger or crafting match, that
suppression ends when you Reconcile.

**Citation.** `faction:diaspora$16.2.1.1`

---

### Q: Does Fears Come to Pass trigger if the Vagabond removes a Peaceful enclave?

**Resolution.** The Vagabond can remove tokens with certain item actions.
Fears Come to Pass fires when "an enemy removes a Peaceful enclave outside
battle" (`faction:diaspora$16.2.5`). The Vagabond is a player and counts as
an enemy unless in coalition. Removing a Peaceful enclave outside battle (e.g.,
via Torch) would trigger Fears Come to Pass for the Vagabond's player. Note:
the Vagabond can go hostile or increase infamy only if enemy warriors are
present for witness (`rule:9.2.9.3`), but Fears Come to Pass does not require
witnesses — it fires on the removal itself.

**Citation.** `faction:diaspora$16.2.5`

---

### Q: Does attacking an enclave clearing trigger Fears Come to Pass if there is no Peaceful enclave there — only warriors?

**Resolution.** No. Fears Come to Pass fires after a battle where an enemy
attacks "a defending Peaceful enclave" (`faction:diaspora$16.2.5`). If there
is no Peaceful enclave in the clearing, the trigger condition does not occur —
even if you have warriors there. Targeting only warriors avoids the cascade.

**Citation.** `faction:diaspora$16.2.5`

---

### Q: If I Reconcile an enclave in a clearing ruled by me, do I draw a card?

**Resolution.** No. Reconcile says "if a player rules it, they draw 1 card"
(`faction:diaspora$16.4.2.2`). "A player" in Root typically refers to any
player. However, the draw goes to the ruler of the clearing, which could be
you. If you rule the clearing you are Reconciling, you draw the card. This is
unusual and worth knowing — ruling your own Militant enclaves lets you draw
on your own Reconcile.

**Citation.** `faction:diaspora$16.4.2.2`

---

### Q: Can an enemy use Negotiations to flip a Militant enclave during the Diaspora's Retaliate step, preventing the battle?

**Resolution.** Negotiations is usable "once during their turn" — meaning the
enemy player's turn, not yours (`faction:diaspora$16.2.6`). They cannot use
Negotiations during your Evening Retaliate step. The mandatory Retaliate
battles cannot be averted by Negotiations.

**Citation.** `faction:diaspora$16.2.6`

---

### Q: Can the player holding Frog Dominance decline to add warriors as Enclave Defense?

**Resolution.** The Enclave Defense rule states that the player with Frog
Dominance "adds their faction warriors there as defending warriors"
(`faction:diaspora$16.2.2.1.1`). The word "adds" reads as mandatory rather
than optional — but verify with your table and the current FAQ, as this clause
was added in the Homeland Expansion and community consensus is still forming.

**Citation.** `faction:diaspora$16.2.2.1.1`

---

## Reference Index

**Faction citation key.** `faction:diaspora`

**Primary rule section.** `rule:16.`

**Related glossary items.** `item:boot`, `item:sword`, `item:coin`,
`item:hammer`, `item:crossbow`

**Hireling form.** The Lilypad Diaspora does not have a standalone hireling
form in p16. Enclave Defense (`faction:diaspora$16.2.2.1.1`) involves other
players' warriors defending on behalf of the Diaspora under the Frog Dominance
condition, but this is not a hireling.

**Cross-faction interactions.**

- *Twilight Council — Peacekeepers.* If both the Council's Peacekeepers ability
  (`rule:17.2.5`) and Enclave Defense (`faction:diaspora$16.2.2.1.1`) apply to
  the same battle, the Diaspora chooses the combination of Council warriors and
  Enclave Defense warriors to take hits after their own
  (`faction:diaspora$16.2.2.1.2`).

- *Riverfolk Company — Mercenaries.* You must battle Riverfolk Mercenaries
  during Retaliate if they are the only way to battle in a Militant enclave's
  clearing (`faction:diaspora$16.6.1`). This is an exception to the general
  principle that Mercenaries are available to anyone.

- *Woodland Alliance — Outrage.* Moving warriors into a Sympathetic clearing
  during Settle triggers Outrage (`rule:8.2.6`). Diaspora warriors are standard
  faction warriors; they are not exempt.

- *Vagabond — Enclave removal.* The Vagabond removing a Peaceful enclave
  outside battle triggers Fears Come to Pass (`faction:diaspora$16.2.5`).
  Inside battle, the standard battle rules apply.

- *Clearing suit — all factions.* Your Militant enclaves replace the printed
  clearing suit with frog (`faction:diaspora$16.2.1.1`). Any faction whose
  economy depends on the printed suit of a clearing (Woodland Alliance Outrage,
  Lizard Cult garden matching, faction card effects) is affected. This is the
  Diaspora's most widespread map-level interference.
