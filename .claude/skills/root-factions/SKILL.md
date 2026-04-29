---
name: root-factions
description: Use when reasoning about a specific Root faction — strategy, playbook, threat matchups, scoring, card priorities, common pitfalls, or faction-specific rule clarifications. Wraps the in-depth faction profile docs at docs/factions/.
user-invocable: true
allowed-tools:
  - "Read"
  - "Grep"
---

# Root Faction Profiles Lens

Reference recipe for the 13 in-depth faction profile docs. Each profile follows
a fixed 12-section spine. Use this skill to find a faction's strategic context,
playbook, threat matchups, and clarifications.

Profiles are p16-only and **derivative**. When a profile conflicts with the Law,
the Law wins. Profiles are the right starting point for *strategy*, *playbook*,
and *clarification* questions; `rules.yml` / `faq.yml` are the right starting
point for adjudication.

## Files

13 profiles + index at `docs/factions/`:

| Faction | File | Citation key | Primary rule |
|---|---|---|---|
| Marquise de Cat | `marquise.md` | (none — cite via `rule:6.X`) | `rule:6.` |
| Eyrie Dynasties | `eyrie.md` | `eyrie` | `rule:7.` |
| Woodland Alliance | `woodland.md` | `woodland` | `rule:8.` |
| Vagabond | `vagabond.md` | `vagabond` | `rule:9.` |
| Lizard Cult | `cult.md` | `cult` | `rule:10.` |
| Riverfolk Company | `riverfolk.md` | `riverfolk` | `rule:11.` |
| Underground Duchy | `duchy.md` | `duchy` | `rule:12.` |
| Corvid Conspiracy | `corvid.md` | `corvid` | `rule:13.` |
| Lord of the Hundreds | `warlord.md` | `warlord` | `rule:14.` |
| Keepers in Iron | `keepers-iron.md` | (none — cite via `rule:15.X`) | `rule:15.` |
| Lilypad Diaspora | `diaspora.md` | `diaspora` | `rule:16.` |
| Twilight Council | `council.md` | `council` | `rule:17.` |
| Knaves of the Deepwood | `knaves.md` | `knaves` | `rule:18.` |

Index: `docs/factions/README.md`. Design spec:
`docs/superpowers/specs/2026-04-28-faction-profiles-design.md`.

## Profile Section Spine

Every profile has these 12 H2 sections in this exact order:

1. **At a Glance** — identity, Reach, complexity, setup constraints, citation key, primary rule section
2. **Win Condition** — 30 VP path, Dominance, Coalition (Vagabond), scoring tempo
3. **Setup** — placement walkthrough + setup theory (best corner, neighbors, opening hand)
4. **Faction Rules and Abilities** — unique abilities with edge-case notes and citations
5. **Turn Structure** — Birdsong / Daylight / Evening with action-by-action edge cases
6. **Scoring Engine** — table of every VP source with timing and trigger
7. **Playbook** — Opening / Mid-game pivots / Endgame routes
8. **Threat Factions** — curated 2–4 opponents whose goals cross yours, with counters
9. **Card Priorities** — crafted-card tiers, items, Ambush hold/play, Dominance, what to spend
10. **Common Pitfalls** — losing patterns specific to this faction
11. **Mechanic Clarifications** — Law-ambiguity sidebars + FAQ pointers
12. **Reference Index** — citation key, primary rule section, glossary refs, hireling form, cross-faction interactions

## Lookup Recipes

**Open the profile for a faction** — slug = citation key where one exists, lowercase display-name slug otherwise:
```
Read docs/factions/<slug>.md
```

**Jump to a specific section** — H2 headers match the section names in the spine:
```
grep -n "^## <Section Name>" docs/factions/<slug>.md
```
Then `Read` from that offset.

**Find clarifications and FAQ pointers for a faction**:
```
grep -nA 30 "^## Mechanic Clarifications" docs/factions/<slug>.md
```

**Find threat-matchup notes for a faction**:
```
grep -nA 60 "^## Threat Factions" docs/factions/<slug>.md
```

**Search across all 13 profiles for a keyword** (card name, item, rule cite):
```
grep -rn "<keyword>" docs/factions/
```

## Output Contract for Callers

- **Profiles are derivative.** When relaying a mechanical claim from a profile, prefer citing the underlying `rule:X.Y.Z` / `faction:KEY$X.Y.Z` / `faq:<stub>` that the profile already cites — not the profile itself. Profiles do the rule-lookup work; pass the citation through.
- **Strategy claims are judgment, not rules.** When a profile says "do X," "expect Y," or "this is a high-threat matchup," that is the profile's analysis. Treat as one perspective; cross-check primary sources or community discussion when stakes are high.
- **Honor the profile's caveats.** Profiles flag community-sourced strategic claims with phrasing like "Community consensus..." or "Some players argue..." Pass these caveats through; do not promote a community claim to a rule citation.
- **When profile content conflicts with the Law**, the Law wins. Flag the conflict to the user; the profile should be updated separately.
- **Profiles cover p16 only.** For p4/p6 questions, go directly to the older `rules.yml` files; profiles do not track printing differences.
