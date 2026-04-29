# Riverfolk Company

## At a Glance

**Identity**: A commercial faction that scores by selling three services to opponents and by placing trade posts — your pieces are currency before they are soldiers.

| Attribute | Value |
|---|---|
| Reach | 3 |
| Complexity | High |
| Scoring tempo | Punctuated (burst from trade posts; slow dividend trickle between them) |
| Color | Teal (`#5bc3bd`) |
| Icon | `faction-riverfolk` |
| Faction citation key | `faction:riverfolk` |
| Primary rule section | `rule:11.` |

**Setup constraints**: Your 4 starting warriors go into any clearings touching the river (`faction:riverfolk$11.3.2`). You have no keep and no corner anchor — you pick river clearings, not a starting corner.

---

## Win Condition

### Standard 30 VP Route

Your points come from two engines running in parallel.

The first is **trade posts**. You hold 9 trade posts on your faction board at game start (`faction:riverfolk$11.3.3`). Every time you place one, you score the VP listed on the space uncovered on your board (`faction:riverfolk$11.5.6.3`). The 9 placements are worth a combined 18 VP — you cannot reach 30 from trade posts alone.

The second is **dividends**. At the start of each of your Birdsong phases, if you have any trade posts on the map, you score one VP per two warriors in your Funds box (`faction:riverfolk$11.4.2`). This rewards accumulating funds between turns, but it also makes you a target: trade post removal costs you half your funds, rounded up, and removes that post from the game permanently (`faction:riverfolk$11.2.5.1`).

The gap between 18 and 30 must be closed through dividends, crafted-card VP, and the one VP per enemy building or token you remove in battle (`rule:3.2.1`). A typical winning line combines 14–18 VP from trade posts with steady dividend scoring of 2–4 VP per turn in the mid-game and late game.

### Dominance Card Path

You can activate a dominance card once you hold at least 10 VP (`rule:3.3.1`). Like every faction, you remove your VP marker and shift to a territorial win condition — rule the three clearings of a matching suit, or rule two opposite corners for Bird Dominance (`rule:3.3.1.1`, `rule:3.3.1.2`). Dominance is rarely the right call for Riverfolk. Your strength is economic, not territorial; you typically have few warriors on the map relative to ruling factions. It is a viable emergency option if opponents are catching you and you hold a lead, but it requires board presence you may not have built.

### Scoring Tempo

Your scoring is **punctuated**: quiet dividend trickles interrupted by bursts when you place a trade post (each one worth 1–4 VP depending on how many remain on your board). Early posts yield fewer points; later posts yield more. You accelerate toward 30 rather than cruise — which means your opponents will see the acceleration coming if they are paying attention.

---

## Setup

### Step-by-Step Walkthrough

1. Form a supply of 15 warriors (`faction:riverfolk$11.3.1`).
2. Place 4 warriors in any clearings that touch the river (`faction:riverfolk$11.3.2`). You are not restricted to the same clearing — spread them as you see fit.
3. Place all 9 trade posts on the matching spaces of your Trade Posts tracks on your faction board (`faction:riverfolk$11.3.3`). These tracks are also your crafting slots (see Faction Rules below).
4. Place 3 warriors in your Payments box as starting funds (`faction:riverfolk$11.3.4`).
5. Place 1 service marker on any space of each of your three Services tracks to set starting prices (`faction:riverfolk$11.3.5`).

### Positioning Your Warriors

You must place in river-touching clearings, which limits your choices but also gives you meaningful early-game board presence along the trade routes you intend to exploit. Spread across two or three distinct clearings when possible — this makes it easier to establish trade posts, since you need to be able to reach ruled clearings, and it prevents a single battle from wiping out all your funds at once.

Avoid clustering all four warriors in one clearing. Your dividends depend on warriors in your Funds box (not on the map), so board warriors are primarily setup tools for placing trade posts and generating board pressure.

### Choosing Starting Prices

You set your starting prices during setup (`faction:riverfolk$11.3.5`). Your prices can be anywhere on each track — typically 1 through 4. Consider these defaults as a starting point:

- **Hand Card**: 2 or 3. Your hand is visible to everyone (`faction:riverfolk$11.2.3`), so other players already know its value. Set higher if you hold ambush cards or high-value craftables.
- **Riverboats**: 1. This service sees low demand in most games. Raise only when river access is actively contested.
- **Mercenaries**: 2 or 3. This is your most consistently purchased service when warrior-heavy factions are present.

### Neighbor Considerations

You want opponents who buy services. High-warrior factions — Marquise de Cat, Eyrie Dynasties, Underground Duchy — generate the payment streams that convert into your funds. A game with multiple warrior-dense factions is good for you. The Woodland Alliance and Corvid Conspiracy generate fewer warriors and thus fewer potential service purchases.

The Vagabond pays for services differently: they exhaust items, and for each item exhausted the Riverfolk place one warrior in the Payments box (`faction:riverfolk$11.2.6.3`). This is reliable if a Vagabond is in the game, but the Vagabond cannot buy Mercenaries at all (`faction:riverfolk$11.2.7.3.2`).

---

## Faction Rules and Abilities

### Crafting

The Riverfolk have no crafting pieces in the traditional sense — no workshops, no hammers. Instead, you commit funds (warriors) to empty spaces on your Trade Posts tracks during Daylight (`faction:riverfolk$11.2.1`, `rule:4.1.1`). The suit of the space you place the warrior on provides the suit for crafting cost (`faction:riverfolk$11.5.3`).

This means crafting and trade post placement compete for the same track spaces. When you commit a fund to a track space to craft, that warrior does not go to the Committed box — it stays on the track. When you later place a trade post in a clearing, you must spend two funds of the ruling player, but the track itself holds your crafting placements as a record of available suits.

**Export**: Rather than gaining a card's listed benefit, you may instead discard it and place one Riverfolk warrior in the Payments box (`faction:riverfolk$11.5.3.1`). This is useful when the item is already claimed from the supply or when you need funds more than you need the effect. Per the FAQ, you must be able to actually craft the card in the first place to export it — you cannot export a card whose item is not in the supply (`faq:can-i-export-a-card`).

### Swimmers

The Riverfolk treat rivers as paths and may move along a river linking an origin and destination clearing, ignoring the standard movement requirement for rule (`faction:riverfolk$11.2.2`). This is your main mobility advantage. While other factions must rule the origin or destination to move (`rule:4.2.1`), you can slip along rivers regardless of who controls those clearings.

Note the language precisely: the river must *fully link* the origin and destination clearing. Rivers that do not form a direct connection between two clearings do not substitute as a path between them. You can also still use normal paths (`faction:riverfolk$11.2.2`).

On the Lake Map, the lake is treated as rivers, connecting all coastal clearings — your Swimmers ability applies in full, giving you the run of the map's waterways. On the Winter Map, the Raging River rule divides forests but does not affect your ability to move along it.

### Public Hand

Your hand is placed face up above your faction board for all to see (`faction:riverfolk$11.2.3`). This is the price you pay for selling cards as a service. If a random card is taken from you (for example by a Thief Vagabond or Stand and Deliver!), your hand is flipped face down, shuffled, drawn from, then flipped face up again.

The open hand shapes your service economy: opponents always know what they are buying when they take a Hand Card from you. This is a double-edged rule. You cannot bluff about card quality, but you also cannot be surprised by a player buying a card they didn't know you had.

### Funds

Funds are warriors in your Funds box (`faction:riverfolk$11.2.4`). Most of your Daylight actions cost funds — you commit or spend them to act. When you commit a fund, move the warrior to the Committed box. When you spend a fund, return the warrior to its owner's supply. Warriors in Committed or Payments do not count toward dividend scoring (`faction:riverfolk$11.4.2`).

The Payments box is your incoming revenue: warriors placed there by players who buy your services. At Gather Funds in Birdsong step 3, you move all warriors on your faction board (Funds, Payments, and Committed boxes) to the Funds box (`faction:riverfolk$11.4.3`). This resets your action economy each turn.

### Trade Posts

Placing a trade post scores VP immediately (`faction:riverfolk$11.2.5`). Your board has three tracks, one per suit (fox, rabbit, mouse). The points per placement increase as you empty the tracks — earlier placements yield 1 VP, later ones yield up to 4 VP.

**Trade Disruption** is the major risk. When any trade post is removed by an opponent (in battle, or via a Favor card wiping the clearing), you lose half your current funds rounded up, and that trade post is permanently removed from the game (`faction:riverfolk$11.2.5.1`). The post never comes back. Losing posts late in the game when you hold many funds is catastrophic — both for your dividend engine and your raw scoring.

Trade posts also gate how many services other players can buy per turn. Each player starts with one service purchase per turn. They gain one additional purchase per clearing where they have both a trade post and their own faction pieces (`faction:riverfolk$11.2.6.2`). Getting posts into clearings where active buyers operate multiplies the number of transactions per turn.

### Buying Services

At the start of another player's Birdsong, that player may buy your services by placing warriors from their supply into your Payments box equal to the cost on your Services track (`faction:riverfolk$11.2.6`, `faction:riverfolk$11.2.6.1`). You cannot refuse — no consent is required (`faq:can-the-riverfolk-refuse`).

The Vagabond exhausts items instead of placing warriors; for each item exhausted, one Riverfolk warrior enters the Payments box (`faction:riverfolk$11.2.6.3`).

### Riverfolk Services

You offer three services (`faction:riverfolk$11.2.7`):

**Hand Card** (`faction:riverfolk$11.2.7.1`): The buyer takes any card from your face-up hand. They may purchase this service multiple times per turn, provided they have access to enough trade posts granting extra purchases. This is your card-draw-for-others economy. Because your hand is public, the buyer knows exactly what they are getting.

**Riverboats** (`faction:riverfolk$11.2.7.2`): The buyer treats rivers as paths until end of their turn. This grants river mobility without the permanent Swimmers ability you hold. Useful for factions locked out of river routes by ruling requirements.

**Mercenaries** (`faction:riverfolk$11.2.7.3`): During Daylight and Evening of the buyer's turn, except when battling the Riverfolk themselves, the buyer treats your warriors on the map as their own for rule and for battle. They cannot move them, count them toward dominance, or remove them except by taking hits. Your warriors remain your faction pieces — Field Hospitals cannot save them, Duchy's Sway Ministers cannot use them.

When the buyer takes hits in battle using Mercenaries, they must split hits: odd hits come from their own warriors first, or their own buildings and tokens if no warriors (including Riverfolk) remain in the clearing (`faction:riverfolk$11.2.7.3.1`). The Vagabond cannot buy Mercenaries (`faction:riverfolk$11.2.7.3.2`). Per the FAQ, Mercenaries can be used to battle hirelings controlled by the Riverfolk — they just cannot battle the Riverfolk themselves (`faq:can-riverfolk-mercenaries-battle-hirelings`).

---

## Turn Structure

### Birdsong

Your Birdsong has three mandatory steps in this exact order (`faction:riverfolk$11.4`):

1. **Protectionism** (`faction:riverfolk$11.4.1`): If your Payments box is empty, place 2 warriors into it. This is your floor — you always start each Gather Funds with at least 2 warriors flowing through if no one bought services. Without trade posts out attracting buyers, this baseline prevents you from going completely dry.

2. **Score Dividends** (`faction:riverfolk$11.4.2`): If there are any trade posts on the map, score 1 VP per 2 warriors in your Funds box (round down). Warriors in Payments or Committed do not count. This step rewards holding large funds over turns, but holding large funds also advertises your score — opponents will target your trade posts to drain you.

3. **Gather Funds** (`faction:riverfolk$11.4.3`): Move all warriors on your faction board (Payments, Committed, and current Funds) to the Funds box. This is your resource reset. All payments received from buyers last turn become available actions this turn.

The order matters. Dividends are scored before Gather Funds, so you score based on the Funds box as it stood at the end of your previous turn (minus whatever you spent in Daylight). Payments you received during other players' turns are not yet in your Funds box when dividends score — they arrive in Funds after dividends, via Gather Funds.

### Daylight

Your Daylight is entirely fund-driven. You can take the following actions in any order and number (`faction:riverfolk$11.5`):

**Move** (`faction:riverfolk$11.5.1`): Commit 1 fund. Take a move action. As Swimmers, you can move along rivers without needing rule (`faction:riverfolk$11.2.2`). Standard movement rules otherwise apply — you move warriors from one clearing to an adjacent clearing via a path or linking river (`rule:4.2`).

**Battle** (`faction:riverfolk$11.5.2`): Commit 1 fund. Initiate a battle in a clearing with your warriors. Standard battle rules apply (`rule:4.3`). You are rarely a combat powerhouse — most of your warriors are funds, not fighters. Battle judiciously: to remove a threatening piece, to defend a trade post, or to establish rule for a placement.

**Craft** (`faction:riverfolk$11.5.3`): Commit funds to craft a card. Instead of going to Committed, place the warriors on empty spaces of the Trade Posts tracks matching the crafting cost suits. This fills track spaces with warriors, which temporarily blocks those spaces for future crafting placements but lets you craft high-value cards. Remember Export as an alternative (`faction:riverfolk$11.5.3.1`).

**Draw** (`faction:riverfolk$11.5.4`): Commit 1 fund to draw a card. With a public hand, every opponent sees what you drew. Card draw is your hand refill mechanism — use it when you have funds to spare and when your hand is thin.

**Recruit** (`faction:riverfolk$11.5.5`): Spend (not commit) 1 fund to place a warrior in any clearing with a river. Spending returns the warrior to its owner's supply rather than the Committed box. Recruiting builds the board presence needed to rule clearings and enables trade post placement later.

**Establish Trade Post with Garrison** (`faction:riverfolk$11.5.6`): Spend 2 funds. Choose any clearing without a trade post that is ruled by any player (`faction:riverfolk$11.5.6.1`). Spend 2 funds of the player who rules that clearing (`faction:riverfolk$11.5.6.2`) — those warriors return to their owners' supplies. Place the matching trade post and 1 warrior in the clearing, then score the VP uncovered on your board (`faction:riverfolk$11.5.6.3`).

Note that placing a trade post requires the clearing to be ruled by *any* player — including yourself. The ruling player's warriors are the 2 funds you spend (return to their supply). If you rule the clearing, you spend 2 of your own warriors.

### Evening

Your Evening has two steps in order (`faction:riverfolk$11.6`):

1. **Discard Cards** (`faction:riverfolk$11.6.1`): If you hold more than 5 cards, discard down to 5.

2. **Set Costs** (`faction:riverfolk$11.6.2`): You may move each service marker to any space on its track. You reprice every service every turn — there is no lock-in.

Repricing is a powerful and often underutilized part of your turn. You can respond to what happened during the round: raise Mercenaries if a faction just grew threatening; lower Hand Card if your hand is weak this cycle; spike a price the turn you expect no one will buy to signal it is off limits.

---

## Scoring Engine

| VP Source | Amount | Trigger | Timing |
|---|---|---|---|
| Trade post placement | 1–4 VP per post (track-dependent) | You place a trade post | Daylight (your turn) |
| Score Dividends | 1 VP per 2 funds in Funds box | Trade posts exist on map | Birdsong step 2 |
| Crafting items | Varies by card | You craft an item-granting card | Daylight (any turn you craft) |
| Enemy building/token removed | 1 VP per piece | You remove an enemy building or token in battle | Daylight (any battle you initiate or defend) |

**Trade post value by placement order**: The first posts placed yield fewer points; later posts yield more. The exact distribution is printed on your faction board tracks — typically 1, 1, 1, 2, 2, 2, 3, 3, 4 across all nine slots (the precise values are on the board; verify against your physical copy). The cumulative maximum is 18 VP from all nine placements.

**Dividend floor**: With no trade posts, dividends do not score (`faction:riverfolk$11.4.2`). With posts established and a Funds box holding 4 warriors, you score 2 VP per turn — 20 VP over 10 turns, but the game will not last 10 full turns at this pace. Realistically, dividends contribute 4–10 VP across a game, depending on when you establish posts and how large your funds grow.

**Opportunity scoring**: Every battle you initiate where you remove a building or token scores you 1 VP (`rule:3.2.1`). This is minor but not nothing — it rewards being somewhat aggressive rather than purely passive.

---

## Playbook

### Opening (Turns 1–2)

Your primary goal in the first two turns is to establish your first one or two trade posts and set service prices that generate payment flow.

Begin turn 1 by assessing the board state after setup. Who rules river-adjacent clearings? Those are your first trade post targets. You need a ruled clearing — ruled by anyone — plus 2 funds of the ruling player to establish a post (`faction:riverfolk$11.5.6.1`, `faction:riverfolk$11.5.6.2`). With 3 starting funds (from Step 4 of setup) flowing through Gather Funds into your Funds box turn 1, you can spend 2 to place a post and have 1 left for a recruit.

Recruit early. A warrior placed in a river clearing via Recruit (`faction:riverfolk$11.5.5`) expands your board presence, lets you threaten rule in more clearings, and makes your Mercenaries service more valuable to potential buyers.

Set Mercenaries at 2 or 3 if multiple warrior-heavy factions are present. Set Hand Card at 2–3 unless your hand holds something obviously valuable (ambush cards, Favor cards). Set Riverboats at 1 unless you see a specific player who urgently needs river access.

On turn 2, try to place your second trade post. Two posts on the map immediately enables buyers who already share a clearing with one post to purchase two services per turn. This compounds your income quickly.

### Mid-Game Pivots

By the mid-game you should have 3–5 trade posts out and a regular payment stream. Watch for these signals:

**Dividend scoring becoming meaningful**: Once you have 6+ funds in your Funds box and posts on the map, dividends generate 3 VP or more per turn. This is when opponents will start seriously considering removing your posts. If you see a faction building toward a Favor card (`card:ROOT-73 (Base Game)`, `card:ROOT-74 (Base Game)`, `card:ROOT-75 (Base Game)`) in clearings where your posts sit, raise your Hand Card price to deny it or reposition your warriors.

**Trade post saturation**: If another faction's pieces are filling clearings where you want to post, use battle to establish rule or to deny the clearing to them. Commit a fund, enter battle, remove their pieces — then post the next turn.

**Service demand shifts**: When a faction moves toward a dominant position, demand for Mercenaries and Riverboats will rise. Adjust prices upward during Evening. If no one is buying Hand Card and your hand is weak, drop the price to 1 temporarily to encourage purchases and thin your hand before you draw better cards.

**Maintain diplomatic neutrality**: Community consensus holds that aggressive pricing when someone urgently needs a service generates long-term hostility. Some players argue that spiking prices in crisis moments is optimal short-run play, but experienced tables often respond by targeting your trade posts at the first opportunity. Consistent, moderate pricing builds the reputation that generates steady passive income.

### Endgame Routes

When you reach roughly 20 VP, you need to close the last 10 quickly before the table recognizes your threat and starts attacking your posts.

The fastest close is a burst of trade post placements combined with accumulated dividends. If you hold 5–7 funds in your Funds box heading into a late-game turn, you can score 2–3 VP from dividends at Birdsong, then spend funds in Daylight to place 1–2 trade posts (each worth 3–4 VP at this stage of your board), adding up to 9–12 VP in a single round.

Hold high-value craftables and craft them the turn you push — Favor cards score VP from items while also disrupting opponents' piece density (`card:ROOT-73 (Base Game)`, `card:ROOT-75 (Base Game)`).

If you need a longer runway, suppress your visible funds. Spend aggressively in Daylight even if the action itself is low-value — committing funds to draw cards or recruit keeps your Funds box smaller at dividend-scoring time, reducing what opponents see as your threat level. Then build funds back up the turn before your push.

---

## Threat Factions

### Woodland Alliance

The Woodland Alliance spreads sympathy tokens across the Woodland, frequently in the same clearings you want to trade post into. More critically, they generate Favor cards (`card:ROOT-73 (Base Game)`, `card:ROOT-74 (Base Game)`, `card:ROOT-75 (Base Game)`) through Revolts and can craft them to devastate your posts in a suit. A single Favor card removes all enemy pieces in its suit's clearings — that can strip multiple trade posts and trigger repeated Trade Disruption penalties.

Your counter: monitor which suits the Alliance is establishing bases in. If they have a Fox base and your Fox trade posts are clustered, start placing in Rabbit or Mouse clearings instead. You can also hold Ambush cards (`card:ROOT-46 (Base Game)` through `card:ROOT-49 (Base Game)`) to blunt their battles, and your Public Hand means they can — and will — buy Ambush cards from you. Price accordingly.

The Alliance purchases services rarely due to low warrior counts, so they are rarely strong revenue generators for you. Treat them primarily as a threat to manage, not a client to cultivate.

### Marquise de Cat

The Marquise builds everywhere and recruits heavily, making her both your best client and a persistent threat. Her large warrior presence makes Mercenaries attractive and generates substantial Payments flow. But her Workshops and Sawmills fill building slots in clearings you want, and her Keep (`rule:6.2.2`) blocks placement in the corner clearing she anchors.

She can also decide, at any point, that your trade posts are blocking her plans and simply battle them out. Field Hospitals (`rule:6.2.3`) mean removing her warriors from your posts costs her nothing — she just cycles them back. If the Marquise is pulling away in VP, other factions will pay for Mercenaries to fight her, which is good for you. But if the table lets her run, the same Mercenaries revenue dries up as fights become one-sided.

Keep your posts in clearings she does not heavily contest. Support her opponents' ability to fight her via low Mercenary prices — keeping the war alive keeps the market for your services open.

### Eyrie Dynasties

The Eyrie runs a Decree engine that demands river moves and specific battle targets each turn. This makes them one of your most reliable clients for Riverboats and Hand Cards — they often cannot fulfill their Decree without your services. Because the Eyrie must complete every column of their Decree or go into Turmoil (`rule:7.7`), they will pay almost any price when they need a service to survive.

The risk is that a strong Eyrie scores quickly — Lords of the Forest (`rule:7.2.2`) gives them rule-on-ties, enabling rapid VP accumulation — and you do not want anyone else reaching 30 before you do. Keep Eyrie prices at a level that earns you revenue without becoming their engine. Raise Hand Card prices when their hand is thin to force them to draw cards themselves rather than buying from you.

### Corvid Conspiracy

The Corvids place Plots in clearings you want to inhabit or trade post into. Snares (`rule:13.7.2`) and Extortion (`rule:13.7.3`) can disrupt your ability to move warriors into clearings and establish the board presence that makes Mercenaries valuable. Their low warrior count means low service revenue from them directly.

Some players argue the Corvids are a secondary threat at best, since they do not mass-remove your posts the way Favor cards do. The more pressing concern is that they operate in clearings across the map and their Exposure ability (`rule:13.2.4`) can reveal your hand when it is not already public information — which it already is. Against Corvids, the more meaningful risk is Snare placements blocking your warrior positioning.

---

## Card Priorities

### Crafted-Card Tiers

**Top priorities**:

- **Favor of the Foxes** (`card:ROOT-73 (Base Game)`), **Favor of the Mice** (`card:ROOT-74 (Base Game)`), **Favor of the Rabbits** (`card:ROOT-75 (Base Game)`): Each has a multi-suit craft cost (verify against your physical card) and removes all enemy pieces in its matching clearings when crafted. This is both a board wipe and a VP engine — you score 1 VP per enemy building and token removed (`rule:3.2.1`). Your crafting track can commit multiple funds of the same suit, making these achievable. Community consensus rates these as your highest-priority crafts when you hold them. They are especially devastating against the Woodland Alliance (remove all sympathy in a suit) and the Marquise (remove buildings). Use them the turn you push for the win, or to surgically clear a clearing you want to post into.

- **Armorers** (`card:ROOT-51 (Base Game)`): A persistent effect that lets you discard it in battle to ignore all rolled hits taken. As a faction with few warriors on the map, surviving an attack on your trade posts matters. Discard in a key defensive battle to preserve both your warriors and the post itself.

- **Sappers** (`card:ROOT-94 (Base Game)`): As defender, discard to deal an extra hit. Pairs well with Armorers as a defensive suite. If you hold both, you become a meaningful deterrent to aggression.

- **Royal Claim** (`card:ROOT-92 (Base Game)`): In Birdsong, discard to score 1 VP per clearing you rule. With late-game board presence and multiple trade posts, you can rule several clearings simultaneously. This is a burst VP card that fits your endgame push.

**Situational**:

- **Tax Collector** (`card:ROOT-105 (Base Game)`): Once in Daylight, remove one of your warriors from the map to draw a card. You already pay funds to draw (`faction:riverfolk$11.5.4`), so Tax Collector gives you a free draw but costs a board warrior. Useful when your hand is dry and your board presence is already strong.

- **Cobbler** (`card:ROOT-60 (Base Game)`): At start of Evening, take a move. Extends your mobility slightly. Useful when you need a final repositioning that your funds could not cover, or to reach a clearing for a trade post next turn.

- **Command Warren** (`card:ROOT-63 (Base Game)`): At start of Daylight, initiate a battle. Gives you a free battle before your fund-spending begins. Good if you need to clear a clearing of enemy pieces to rule it for a post.

- **Stand and Deliver!** (`card:ROOT-102 (Base Game)`): In Birdsong, take a random card from an enemy — they score 1 VP. Your hand is public, so you already lose some hand secrecy advantage; this gives you additional cards to sell. The VP gift to the target is a cost to weigh.

**Skip or export**:

- Most item-granting craftables with no text (Foxfolk Steel, Mouse-in-a-Sack, Woodland Runners, etc.) are lower priority unless you are going for item VP to close the last few points. They may be worth more as exports (`faction:riverfolk$11.5.3.1`) to build funds than their immediate VP.

### Ambush Hold/Play Guidance

Your hand is public, so opponents know when you hold an Ambush. This cuts both ways: buyers purchasing your hand cards may specifically seek an Ambush, which you should price accordingly. Hold Ambush cards primarily as deterrents — opponents who see you hold one may think twice before attacking your trade posts. Play them when an attack would remove a post or heavily drain your warriors.

### Dominance Card Considerations

You can buy dominance cards into your hand and sell them via Hand Card service. Community consensus holds that this is occasionally useful for diplomatic reasons but not a primary strategy. The more relevant use is simply not holding them when you do not need them — export them or sell them quickly.

---

## Common Pitfalls

- **Hoarding funds without posts on the map**: Dividends require trade posts on the map (`faction:riverfolk$11.4.2`). Sitting on 8 funds before placing your first post scores nothing. Get posts out early to start the dividend clock.

- **Pricing yourself out of sales**: If you set all services at cost 4, no one buys. No purchases means no Payments, which means weak funds, which means weak actions. You need revenue flowing. Moderate pricing generates the warrior flow that powers your turns.

- **Pricing too low and becoming someone else's engine**: The inverse problem. Setting Mercenaries at 1 for a faction who would pay 3 means you are subsidizing their board dominance. Find the price that buyers will pay without giving it away.

- **Placing all posts in one suit's clearings**: If your posts cluster in a single suit, a single Favor card erases them all and triggers multiple Trade Disruption penalties. Spread your placements across fox, rabbit, and mouse clearings to reduce single-card wipe risk.

- **Assuming your board warriors are just funds**: Your warriors on the map are also your trade post garrison requirement (`faction:riverfolk$11.5.6.3`) and your board presence for rule. Do not leave the board completely empty; you need warriors positioned near the clearings you want to post into.

- **Over-relying on dividends and never placing posts**: The dividend route requires a large steady Funds box and multiple turns to pay off. If you never place posts, you cannot score dividends and cap your trade post revenue at zero. Dividends supplement post placement — they do not replace it.

- **Ignoring the Gather Funds step timing**: Payments from buyers in other players' Birdsong phases do not count toward dividends until after they pass through Gather Funds. Many new players misread the dividend scoring as applying to everything in their Payments box. Dividends score only on your Funds box as it exists at step 2 (`faction:riverfolk$11.4.2`), before Gather Funds runs at step 3 (`faction:riverfolk$11.4.3`).

- **Forgetting that spent funds leave the game**: Spending a fund returns that warrior to its owner's supply (`faction:riverfolk$11.5`). If you spend funds belonging to an opponent to place a trade post (`faction:riverfolk$11.5.6.2`), those warriors are gone from the game — they do not come back to you. This is the correct interpretation, but players sometimes expect spent funds to flow back.

---

## Mechanic Clarifications

### Can a player refuse to buy services?

No. Consent is never required for actions in Root (`rule:1.3.3`). Once a player pays the cost, they receive the service. The Riverfolk cannot refuse to sell (`faq:can-the-riverfolk-refuse`). Conversely, a player cannot be forced to buy services they do not want.

### When exactly do dividends score?

Dividends score at Birdsong step 2, before Gather Funds at step 3 (`faction:riverfolk$11.4.2`, `faction:riverfolk$11.4.3`). Warriors in your Payments box — including payments just received during the last round's Birdsong phases — have not yet moved to Funds when dividends score. They count only at the next dividend step. This is the key timing question for Riverfolk: your end-of-turn Funds box size is what you score off, not the next morning's total.

### Can Mercenaries be used to battle Riverfolk-controlled hirelings?

Yes. The restriction is only that Mercenaries cannot be used when battling the Riverfolk themselves. Hirelings controlled by the Riverfolk are a separate matter — battling them is permitted (`faq:can-riverfolk-mercenaries-battle-hirelings`, `faction:riverfolk$11.2.7.3`).

### Can you start a battle with only Riverfolk Mercenaries in the clearing (no buyer warriors)?

Yes. The FAQ explicitly confirms this, and notes that without buyer warriors present, there are no buyer pieces to split hits with (`faq:when-i-hire-riverfolk-mercenaries`). This makes Mercenaries especially flexible — a buyer with no board presence in a clearing can still use your warriors to initiate there.

### What happens when you export a card?

You discard the card and place one Riverfolk warrior in the Payments box (`faction:riverfolk$11.5.3.1`). However, you must be able to craft the card in the first place — if the item is not in the supply, you cannot export (`faq:can-i-export-a-card`). Export is not a universal "discard for income" button.

### Does Trade Disruption trigger for each post removed, or once per event?

It triggers each time a post is removed. If a Favor card removes pieces in multiple clearings with trade posts, each post removed triggers a separate Trade Disruption (`faction:riverfolk$11.2.5.1`). The "remove half of funds, rounded up" calculation applies freshly after each removal.

### Can the Vagabond buy Hand Card or Riverboats?

Yes, both. The Vagabond can buy Hand Card and Riverboats. Only Mercenaries are off-limits to the Vagabond (`faction:riverfolk$11.2.7.3.2`). The Vagabond pays with items rather than warriors (`faction:riverfolk$11.2.6.3`).

---

## Reference Index

**Faction citation key**: `faction:riverfolk`

**Primary rule section**: `rule:11.`

**Related glossary entries**: `item:sword`, `item:crossbow` (from craftable cards you might hold); `item:boot`, `item:hammer` (relevant when interacting with Vagabond service payments)

**Related rules**:
- `rule:2.3` — Rivers (Key Concepts, general rivers rule)
- `rule:2.5` — Rule (defines rule/tie-breaking used in trade post placement eligibility)
- `rule:3.2.1` — Removing Buildings and Tokens (universal VP from building/token removal)
- `rule:3.3` — Dominance Cards
- `rule:4.1` — Craft (Key Actions)
- `rule:4.2` — Move (Key Actions, including You Must Rule exception referencing `faction:riverfolk$11.2.2`)
- `rule:4.3` — Battle (Key Actions)
- `rule:1.2.1` — Public and Private Information: Hands (establishing hands-are-private general rule, with Riverfolk as the named exception)

**Hireling form**: Riverfolk Flotilla (`card:ROOT-194 (riverfolk-hirelings)`) and Otter Divers (`card:ROOT-195 (riverfolk-hirelings)`). These are the large and small Riverfolk-flavored hirelings. Cross-reference hireling rules at `rule:22.` for general control and activation mechanics.

**Cross-faction interactions**:
- Vagabond: pays for services with items, cannot buy Mercenaries (`faction:riverfolk$11.2.6.3`, `faction:riverfolk$11.2.7.3.2`); Vagabond does not go Hostile with Riverfolk if Mercenaries are removed in battle against the Vagabond (`faction:riverfolk$11.2.7.3.2`).
- Marquise de Cat: Field Hospitals cannot affect Riverfolk Mercenary warriors — they are not Marquise warriors (`rule:1.4.3`, `faction:riverfolk$11.2.7.3`).
- Underground Duchy: Cannot use Sway Ministers on Riverfolk Mercenary warriors (`faction:riverfolk$11.2.7.3`).
- Lord of the Hundreds: A clearing with a mob, a Riverfolk Mercenary warrior, and no enemy pieces counts for Oppression; a clearing with only a Riverfolk Mercenary warrior (no Hundreds piece) does not (`faq:what-is-required-for-hundreds-to-oppress`).
- Woodland Alliance: Outrage does not trigger when another faction moves into a sympathetic clearing generally, but if the Riverfolk remove sympathy (e.g., in battle), Outrage triggers as normal (`rule:8.2.6`).
