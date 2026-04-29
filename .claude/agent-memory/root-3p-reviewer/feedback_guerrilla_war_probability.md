---
name: Guerrilla War probability common error
description: Correct defender-probability figures for Alliance Guerrilla War; community sources often get these wrong or transposed.
type: feedback
---

With Guerrilla War (`faction:woodland$8.2.2`), the attacker takes the lower die and the defender takes the higher die.

Correct figures for destroying a sympathy token in one attack:
- **1 defending warrior**: P(lower die ≥ 1) = P(both dice ≥ 1) = (3/4)² ≈ 56%. Dealing 1 hit removes the warrior; token becomes defenseless (`rule:4.3.5.2`) and is also removed.
- **2 defending warriors**: P(lower die ≥ 2) = P(both dice ≥ 2) = (2/4)² = 25%.

The BGG Stevens guide (2019) has these transposed, attributing 25% to one warrior and 6% to two.

**Why:** The math is non-obvious and the error is easy to make when reasoning informally.
**How to apply:** When reviewing a source that cites Alliance defense probabilities, verify against these figures before accepting.
