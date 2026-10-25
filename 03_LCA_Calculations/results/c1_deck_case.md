Rubric coverage: R2.3, R2.6, R3.1, RB.6

# C1 re-run on the team deck's saving (final day, 25/10/2026)

**Deck case:** Ostrołęka BWRX-300 PIS 2023 (Table 14, p. 83) 50,000 m³ concrete per unit × eligible share × Pillai et al. (2019) M50 (OPC 380 − LC³ 270) = 0.110 t CO₂e/m³. Eligible share 20 / **40** / 60% → 10,000 / **20,000** / 30,000 m³ and 1,100 / **2,200** / 3,300 t per unit; Units 2–4 = 3,300 / **6,600** / 9,900 t. The ranges below are these eligibility scenarios, not a Monte Carlo. Volume and saving move together, so the saving per m³ is fixed. **Old case (alternative):** 1,734 t/unit, 13,081 m³ (lca-analyst 21/10, MC P5–P95 1,387–2,153).

Inputs: `parameters_run1.yaml` and `parameters_run5.yaml` keys `c1_deck_*` (new, status TO VERIFY; Ostrołęka and Pillai not yet in `sources.md`, because the LCA team member owns them), and `parameters_run9.yaml` `c1_cases` new_1100/new_2200/new_3300 (base new_2200). `c1_delay_days_high` is now 18.5 (was 14.6).
Reproduce: `python3 -I scripts/schedule_value.py` (deck, the default) and `--c1-case old_1734`; the same for `initiative_cost.py`; `python3 -I scripts/mcda.py --c1-case new_2200`. Outputs: `schedule_value.md` and `initiative_cost.md` (deck case), `schedule_value_old1734.md` and `initiative_cost_old1734.md` (old case), `mcda.md`/`mcda_scores.csv`. Grid, price and delay-cost inputs are unchanged.

## Every C1-dependent number: old → deck

| Quantity | Old (1,734 t) | Deck central 2,200 t (1,100–3,300) | Results file | Sections that quote the old value (grep, 25/10) |
|---|---|---|---|---|
| Per-unit saving; Units 2–4 | 1,734 t; 5,201 t (5.2 kt) | 2,200 t (1,100–3,300); 6,600 t (3,300–9,900) | schedule_value §6 | "1,734": 0, 4.3, 6, 7, 9-tbl-mcda, 11, App A, B, C. "5,201/5.2 kt": 4.3, 6, 7, App A, B, C. "[C1 saving: per final §6]" markers: 0, 8.6, 9-tbl-mcda, 11, App B |
| Break-even delay per unit, average factor (ON-avg-traj, gross–net) | 9.2–14.6 days (9–15) | **11.6–18.5 days (12–18)**; 1,100 t: 5.8–9.2; 3,300 t: 17.5–27.7 | schedule_value §6 | "9–15 days": 0, 4.3, 6, 7, 8.1, 11. "9.2–14.6": 6, App B. "14.6": 6, 7, App B |
| Break-even delay per unit, marginal factor (ON-marginal-declining, gross–net) | 1.3–1.4 days | **1.7–1.8 days**; 1,100 t: 0.8–0.9; 3,300 t: 2.5–2.7 | schedule_value §6 | "1.3–1.4": 4.3, 6, 7, 8.1, 11, App B |
| Whole Units 2–4 saving vs one unit late (avg; marginal) | 28–44 days; 4.0–4.2 days | 35–55 days; 5.1–5.4 days | schedule_value §6 | check App B |
| Carbon value, Units 2–4, at C$95 / C$115 per t | C$0.49 / 0.60 m (0.40–0.74) | **C$0.63 / 0.76 m** (range 0.31–1.14) | initiative_cost §4; schedule_value §7 | "C$0.49", "0.49–0.60": 4.3, 6, 7, 8.2, 9-tbl-mcda, App B |
| Carbon value at superseded C$170 | C$0.88 m (high 1.10) | C$1.12 m (high 1.68) | same | "C$0.88": 4.3 |
| Break-even concrete premium per m³ of LC³ concrete (C$95–115/t) | C$12.6–15.2/m³ (5.5–6.6% of C$229) | **C$10.4–12.7/m³** (4.6–5.5% of C$229; 3.6–7.6% across C$167–290). Same for every eligibility share | initiative_cost §3 | "12.6–15.2", "15.2": 6, 8.2 |
| Qualification budget the carbon price covers at 0% premium | C$0.49–0.60 m | C$0.63–0.76 m | initiative_cost §3 | as carbon value |
| C$1 m qualification spread over Units 2–4 saving | C$190/t (text; script now gives 193) | C$152/t | initiative_cost §2 | "C$190": 8.2 |
| Abatement cost, 0% / +10% premium, C$1 m qualification | C$193 / 366 per t | C$152 / 360 per t | initiative_cost §7 | check 8.2, 9 |
| Abatement cost Monte Carlo P5 / median / P95 | −3 / 372 / 765 C$/t | −40 / 337 / 737 C$/t (V and S correlated) | initiative_cost §6 | check 8.2 |
| One month's Units 2–4 slip ÷ C1 carbon value (all paths) | 30–223× | **20–175×** | schedule_value §7 | "30–223": 7, 11, App B |
| Same, current path only | 44–223× (B5.4 "44×", formerly 45×) | **29–175×** | schedule_value §7 | "44–223", "44×", "45×", "0.743": App B |
| Month's slip in carbon ÷ C1 saving | 2.1–22.7× | 1.6–17.9× | schedule_value §7 | "2.1–22.7": 7, App B |
| One day of delay (C$1.8–2.9 m) vs C1's whole carbon value | at most C$0.60 m | at most C$0.76 m (1.14 at 60% eligibility) | initiative_cost §5 | 4.3, 7, 8.2 |
| MCDA: life-cycle change from C1 | 0.29% (old), 0.37% (2,200 t) | 0.18% / **0.37%** / 0.55% of 4.2 g/kWh | mcda §7 | 9-tbl-mcda |
| MCDA ranking (base new_2200) | VRE > SQ > SMR ≈ SMR+C1 (80/52/30/30) | **unchanged**: VRE 80.1 > SQ 52.4 > SMR 29.7 ≈ SMR+C1 29.7 under equal weights, same order under all four weight sets; score gap SMR+C1 − SMR −0.0015 (+0.0005 with no qualification cost); 2 of 56 ±50% weight tests flip first place; SMR first only if life-cycle weight ≥ 94% | mcda §§4–7 | 9, 9-tbl-mcda |
| MCDA "not schedule-neutral" delay | 14.6 days → 25.5 kt lost at Liddell = 12× the saving | **18.5 days → 32.3 kt lost = 15×** the 2,200 t saving | mcda §7 | "12×": App B |

## Reading
- The deck's larger saving lengthens the break-even delay by about 27% (2,200/1,734). C1 is still cancelled by **under three weeks** of delay to a unit on Ontario's average factor and by **under two days** on the marginal factor. The schedule-neutral condition still decides whether C1 helps or hurts the climate.
- The break-even price per m³ **falls** (C$12.6–15.2 → 10.4–12.7) because the deck saving per m³ (0.110 t) is lower than the old model's (0.133 t). The total carbon value **rises** (C$0.49–0.60 m → 0.63–0.76 m) because more concrete is treated.
- One day of delay (C$1.8–2.9 m) still costs more than C1's whole carbon value, even at 60% eligibility and C$115/t (C$1.14 m).
- The MCDA ranking holds: C1 moves the SMR's score by thousandths of a point.

## Still open
- Ostrołęka PIS 2023 and Pillai et al. (2019) need full Harvard entries (the LCA team member's `sources_lca.md`). Every deck key stays TO VERIFY until then.
- The MCDA life-cycle denominator (4.2 g/kWh) still comes from the old 20,700 m³ model. Re-read the percentages once the re-based LCA total exists.
- The writer needs to replace the section values in the last column (Victor's sections only; propose changes to teammates' sections in `review.md`).
- Figures F6 and F7 (coordinator request, 25/10): `results/F6_displacement.png` (CO₂e avoided to 2050, from displacement.md §3) and `results/F7_same_money.png` (energy and CO₂e ratios, four cost cases, from same_money.md §5), drawn by `scripts/fig_f6_f7.py`. F6 has no delay inset: the §7 caption's inset and "1.73 kt" should be dropped, or changed to the deck's 2.2 kt.
