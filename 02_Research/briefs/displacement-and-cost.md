Rubric coverage: R2.1, R2.3, R2.6, R2.7, R3.1, R3.5, R3.6, R3.7, R4.3, RB.6

# Brief: what one BWRX-300 displaces, what delay costs, and what the same money buys

For §7 (and inputs to §3, §8.2, §8.6, §9). Analyst run 1, 20/10/2026.

> **Read first: every number here is PROVISIONAL.** No primary source could be opened today: the proxy refused every primary host (see `02_Research/sources_run1.md`, "Access status"). The values are search-summary or secondary leads tagged [TO VERIFY], analyst assumptions, or placeholders for Sam's and Leroy's numbers. **The scripts are final. The inputs are not.** Once a person has opened each primary and corrected `parameters_run1.yaml`, re-running the three scripts updates every table. Nothing in this brief may go into the report or the deck as a cited fact until then.

Scripts and full working: `03_LCA_Calculations/scripts/{displacement,schedule_value,same_money}.py` → `03_LCA_Calculations/results/{displacement,schedule_value,same_money}.md` (Appendix B).

---

## Question 1. How much CO₂e does one BWRX-300 avoid at Darlington vs at Liddell?

**Short answer.** At today's average grid factors, the deck's "13× more in NSW" is arithmetically right: 1.50 vs 0.11 Mt/yr. But it rests on two choices that don't hold:
1. **Ontario's newest average is higher.** TAF reports 73.8 g/kWh for 2024 [TO VERIFY] against the deck's 53 g/kWh for 2023. With 73.8 the ratio drops to **9.3×**. A baseload unit in Ontario also displaces gas on the margin; at TAF's marginal lead (343 g/kWh) the ratio is only **1.9×**.
2. **Timing.** An SMR can't run at Liddell before about 2040 (CSIRO GenCost 2023-24 earliest-deployment lead [TO VERIFY that it covers SMRs]). On a Step Change-like trajectory, NEM coal is gone by 2038 (2024 ISP lead [TO VERIFY]).

Valued for the years each plant could actually run, Darlington Unit 1 from 2030 avoids **more CO₂e to 2050** (0.9–6.7 Mt, average to marginal-declining) than a Liddell unit from 2040 on the Step Change proxy (0.6 Mt). It is comparable to Liddell on the slow trajectory (3.8 Mt). **Liddell wins clearly only if the NEM stops decarbonising** (frozen grid: 16.5 Mt). Over the whole 60-year life the two sites are within a factor of about 2 (1.8–7.6 Mt vs 3.4–6.6 Mt), except in the frozen-grid upper bound. That is the R4.3 connection: the climate value of an SMR depends on when and against what it runs, not on today's coal share.

**One unit, 300 MWe × 8,760 h × 0.90 = 2.365 TWh/yr.** The deck's 2.37 is correct. SMR life cycle = 5.75 g/kWh, a placeholder (UNECE range midpoint).

| Displaced electricity | g CO₂e/kWh | t CO₂e avoided per year | Status |
|---|---|---|---|
| Ontario average 2022 (CER) | 35 | 69,000 | TO VERIFY |
| Ontario average 2023 (ontario.ca; **deck value**) | 53 | 112,000 | TO VERIFY |
| Ontario average 2024 (TAF) | 73.8 | 161,000 | TO VERIFY |
| Ontario marginal (TAF 2024 "MEF" slide) | 343 | 798,000 | TO VERIFY; definition ambiguous |
| Ontario gas generation (TAF 2021) | 472 | 1,103,000 | TO VERIFY |
| NSW average 2025 (NGA Factors scope 2) | 640 | 1,500,000 | TO VERIFY |
| Bayswater coal, sent out (upper bound) | 990 | 2,328,000 | TO VERIFY; old AEMO value |

**Cumulative, one unit (Mt CO₂e)**

| Case | to 2035 | to 2050 | whole 60-yr life |
|---|---|---|---|
| Darlington U1 from 2030, Ontario average trajectory (73.8 → 15 g/kWh by 2040) | 0.52 | 0.94 | 1.79 |
| Darlington U1 from 2030, marginal declining (343 → 15 by 2050, assumption) | 3.26 | 6.73 | 7.58 |
| Darlington U1 from 2030, marginal flat (upper bound) | 4.79 | 16.75 | 47.9 |
| Liddell from 2040, T1 Step Change proxy (coal gone 2038, floor 30 g/kWh) | 0 | 0.63 | 3.44 |
| Liddell from 2040, T2 slow (floor reached 2050) | 0 | 3.81 | 6.62 |
| Liddell from 2040, T0 frozen at 640 (upper bound) | 0 | 16.50 | 90.0 |
| Liddell from 2035 (Coalition-claim lead), T1 / T2 | 0.39 / 0.92 | 1.58 / 7.84 | 4.11 / 10.4 |

All four Darlington units (U1 2030; U2–U4 2035): **2.4–18.5 Mt to 2050** (average trajectory to marginal-declining), 55 Mt as the marginal-flat upper bound.

**What moves the result (Liddell, 2040, T1; `displacement.md` §5).**
- Order-of-magnitude drivers: the grid trajectory, the start year, and, under T1, the post-coal floor intensity. The floor is a placeholder: 0–80 g/kWh moves the whole-life result from −0.8 to +10.5 Mt.
- A few per cent at most: capacity factor (0.80–0.95), net output, and the SMR's own life-cycle value within UNECE's range.
- The SMR's life-cycle value matters only in the 110 g/kWh stress case (IPCC max lead, unconfirmed). On a decarbonised grid that case turns the result negative.

So **Sam's number will barely change §7 unless it is far outside the UNECE range.** The decisive inputs are Leroy's dates and the ISP trajectory.

**Method points for §2 and §7 (R2.5, R2.7).**
1. The grid factors are combustion-only (scope 2) while the SMR value is life cycle, so the comparison understates displacement slightly. UNECE coal life cycle (751–1,095) is given as the boundary-consistent upper bound.
2. Liddell closed on 28 April 2023 [TO VERIFY, AER and news]. An SMR there would reuse the site and its grid connection but displaces the NEM mix, not Liddell. Bayswater intensity is therefore an upper bound only, and Bayswater's own closure date is a gap.
3. The trajectories are analyst constructions from anchor points, not AEMO or IESO series. They must be replaced with the 2026 ISP Step Change data and the IESO outlook.

## Question 2. What is a month of delay worth? (`schedule_value.md`)

**Short answer.**
- **Darlington Units 2–4 (from 2035):** one month's delay to one unit forfeits about **5 kt CO₂e** (average trajectory) to **39 kt** (marginal declining). That is **16–117 kt for the three-unit programme**.
- **Break-even delay:** a 1 kt embodied-carbon saving is cancelled by **0.8 days** (marginal) to **5.6 days** (average) of delay, counted to 2050 (gross). The net, whole-life figures are similar (0.8–8.4 days).
- **What it means for C1:** whatever LC3 saves per unit (Sam's number, likely kilotonnes, per plan §2.3), it is wiped out by **days to weeks of slip**. "Schedule-neutral" is a hard condition for the initiative, not a nicety.

| Case | Gross kt per month of delay | Days of delay that cancel a 1 kt saving (gross / net) |
|---|---|---|
| Darlington U1 2030, average trajectory | 9.1 | 3.4 / 4.2 |
| Darlington U1 2030, marginal declining | 51.6 | 0.6 / 0.6 |
| Darlington U2–U4 2035, average trajectory | 5.4 | 5.6 / 8.4 |
| Darlington U2–U4 2035, marginal declining | 39.1 | 0.8 / 0.8 |
| Liddell 2040, T1 | 4.8 | 6.4 / none (flat after 2038) |
| Liddell 2040, T2 | 52.9 | 0.6 / 0.6 |

The "net" column credits the lost month back at end of life, on a cleaner grid. On a flat grid that makes net loss zero by construction, so use the gross (carbon-budget-to-2050) view in the report and the net view as a sensitivity.

**Year-scale delay in Australia (R3.4, R3.5).** Each year it takes to repeal the bans, license and build costs **0.19 Mt (T1), 0.81 Mt (T2) or 1.50 Mt (frozen grid) of CO₂e avoided to 2050** per unit (2035 vs 2040 start). For Darlington, a two-year slip of Unit 1 costs 0.21–1.21 Mt to 2050.

## Question 3. What would the same money buy in firmed renewables? (`same_money.md`)

**Short answer.**
- C$20.9 bn ≈ **A$23.4 bn** at 1.119 AUD/CAD [TO VERIFY RBA rate].
- **Capital charge.** Annualised at 7% over 30 years, Darlington's capital alone is **A$199/MWh** per unit share; the 3–10% range gives A$126–262/MWh. For Unit 1 plus common infrastructure it is A$294/MWh. That is consistent with GenCost's SMR range (lead A$387–641/MWh) once O&M and fuel are added.
- **Capital-only comparison.** The capital charge alone would buy **2.0–2.9× the energy as firmed renewables** at the GenCost lead of A$102/MWh. This is a lower bound, because it ignores the SMR's O&M and fuel.
- **Full-cost comparison.** On GenCost LCOE the ratio is **5.0×** (3.4–6.3×). The worst case for renewables tested (SMR A$198, VRE A$153) is 1.3×.

| Metric (NSW 2025 grid, 640 g/kWh) | SMR | Firmed renewables |
|---|---|---|
| t CO₂e avoided per A$1 m | 1,234 | 5,980 |
| Gross cost per t CO₂e avoided | A$810 | A$167 |

**By 2050, at Liddell.** The same annual spend as one SMR unit (A$1.22 bn/yr) puts **11.9 TWh/yr** of firmed renewables on the grid from 2028 (start year is an assumption). It avoids **9–49× more CO₂e to 2050** than the SMR starting in 2040, and **5×** even in the worst case for renewables (`same_money.md` §5).

For Ontario (indicative only, GenCost costs), renewables win against the marginal factor (5×). Against the very low average they lose, because their placeholder life-cycle value (30 g/kWh) is higher than Ontario's future average. That is a real property of a near-clean grid, but it depends on placeholders.

**Translation to practice (R3.5, R3.6).** On carbon per dollar and carbon by 2050, an SMR at Liddell is dominated by firmed renewables in every tested case. The case for an SMR in Australia therefore has to rest on non-carbon-cost objectives: firm supply, land use, system strength, reuse of coal sites and their grid connections and workforce, and a hedge if renewables and transmission fall behind. That is where the MCDA (§9) must weigh it.

## Non-technical solutions and implementation steps these numbers support (R3.7)

1. **Make C1 schedule-neutral by contract.** Qualify the LC3 mix on Unit 1 mock-ups (2025–2029), so Units 2–4 specify an already-qualified mix. Add a procurement clause that the low-carbon mix may not sit on the critical path. Use the break-even table (days per kt) as the decision rule.
2. **Price the delay in project decisions.** For OPG, at 5–39 kt CO₂e per unit-month and any stated carbon price, the value of schedule exceeds the value of the concrete saving. Report that alongside cost.
3. **For Australia, frame an SMR as a hedge, not a cheaper abatement route.** The policy question becomes "what is the option value of keeping nuclear available if the ISP trajectory slips (T2 or T0)?" Each year of delay costs 0.2–1.5 Mt per unit. That argues for deciding early on the legal question (EPBC s140A, ARPANS s10: run 2), even if the decision is not to build.
4. **Coal-site reuse.** Liddell's grid connection and site are the non-obvious asset (R4.3). Quantifying their value needs a source (connection cost avoided). **Gap:** no source found in this run.

## Open gaps (each blocks a citation)

| Gap | Needed for | Who |
|---|---|---|
| Open every primary in `sources_run1.md` and confirm or correct the values in `parameters_run1.yaml` (status → "verified 2x/10") | All numbers | Victor (human; agents are blocked) |
| GenCost **2025-26 final** (15 July 2026): 2030 SMR LCOE range, firmed-VRE LCOE/SLCOE, WACC, build times, capital costs | `smr_lcoe_aud`, `vre_firmed_lcoe_aud`, `discount_rate`, `vre_first_year` | Victor |
| 2026 ISP Step Change: NEM emissions (Mt) and generation (TWh) by year | Replace trajectories T1/T2 and the floor | Victor |
| IESO Annual Planning Outlook emissions forecast; TAF 2025 marginal factor definition | Ontario trajectory and marginal | Victor |
| Bayswater closure date (AGL) and current CDEII factor | Upper bound | Victor |
| Whether CSIRO's "2040 earliest" covers SMRs; the Coalition's 2035/2037 claims | Australian start years | Leroy |
| Darlington Unit 1 and Units 2–4 in-service dates (current) | Start years | Leroy |
| Net MWe, capacity factor, design life (sourced) | Annual output | Leroy → Sam |
| SMR life-cycle g CO₂e/kWh (central, low, high) | `smr_lca_g_per_kwh` | Sam (Wed 12:00) |
| C1 saving per unit (kt CO₂e) | Break-even days | Sam |
| Firmed-VRE life-cycle intensity (UNECE wind and PV, plus storage) | `vre_firmed_lca_g_per_kwh` | Victor |
| Value of reusing a coal site's grid connection | §8.6 (R4.3) | Victor |

## Corrections to the deck (slide "location", and slide "verdict")

- **Arithmetic is correct:** 2.37 TWh, 1.5 Mt, 0.11 Mt, 13×.
- **Inputs and framing:**
  1. Ontario 53 g/kWh is the 2023 figure; TAF's 2024 figure (73.8) gives 9.3×. Marginal (343) gives 1.9×.
  2. NSW 640 g/kWh is a 2025 factor applied to a reactor that couldn't run before about 2040.
  3. "13× more carbon in NSW" should become something like: *"At today's grid factors an SMR saves about 9× more in NSW than in Ontario. But it could not run in NSW before about 2040, when the grid will be far cleaner, so the gap mostly closes."* Wording is for Victor to decide once the values are verified.
- **Source labels:** the slide credits "DCCEEW (2025)" and "Ontario Government (2024)". Neither primary has been opened yet.
- **Verdict slide:** "About 1.5 Mt CO₂e avoided a year replacing NSW coal" conflates the NSW **average** factor (640) with coal (about 990). Either say "replacing average NSW grid power" or use the coal factor and call it an upper bound.
