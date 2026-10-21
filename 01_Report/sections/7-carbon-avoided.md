Rubric coverage: R2.1, R2.3, R2.6, R2.7, R4.3, R3.1, R3.6, RB.5, RB.6 (also supports R3.5, R3.7, RB.8, R5.1, R5.2, R5.3)

<!--
CHANGELOG
- 21/10 night (coordinator): "Full cost" adds the 4.9× floor (A$198 / A$153), matching App B6 after fact-check M3.
- v1.1, 21/10/2026 (writer, Q8). Same-money numbers checked against the re-run `same_money.md` (GenCost 2030): "Capital cost alone" 2.0–2.9× at A$102 → 1.9–2.7× at A$107; Liddell 5.7/26.0/10.9/5.3× and Ontario −0.4/2.8× now in App B Table B27. §6 break-even aligned (TODOs 1 and 7 closed). Rubric items: R2.3, R3.1, RB.6.
- v1, 21/10/2026 (writer, Q4). First draft from Q2's re-based results (displacement, schedule_value, same_money), run 5 (lcoe, initiative_cost), both briefs and §6 v3; working in App B4–B6. Addresses review audit §2 (R2 "economic benefits ... appropriate to the scale of the proposal"; R4 "new feasible ideas or connections") and factcheck L47 (break-even working).
- Conflicts per plan §5: GenCost = run 5's 2030 reading (A$230–382, 2.9×), 5.0× stated as the alternative [TO VERIFY: GenCost table/year]; carbon price = federal path C$95 (2026) / C$115 (2030) [TO VERIFY]; C$170 used only for the conservative end of 30–223× (explained in B5.3).
- factcheck S2 (boundary mismatch) stated; deck's "13×" replaced by the timing-aware comparison; S3 (300 vs 315 MWe) and S9 (start year) left as TODOs.
- Presentation: R5.1 leads with the schedule finding; R5.2 T10, F6, F7 specified from results; R5.3 about 880 body words excluding table, captions and markers (about 1.75 p, hand estimate; confirm in Word); R5.4 Harvard; R5.5 Australian English.
- T10 is a new table ID; renumber at assembly (Q19).
-->

## 7 Carbon avoided: Ontario vs Liddell, the value of schedule, and the same money on firmed renewables

**For C1, schedule matters far more than concrete.** A one-month slip of Units 2–4 costs C$33–110 m in carrying cost and defers about C$88 m of output: **30–223 times the carbon value of C1's entire saving**. Per unit, the LC3 saving (about 1,740 t CO₂e, §6.3) is cancelled by **9–15 days of delay on Ontario's average grid factor, or 1.3–1.4 days on its marginal factor**. Timing also decides where an SMR helps the climate at all. Counted from when each plant could actually run, a Darlington unit avoids about as much CO₂e to 2050 as a Liddell unit (1.0–6.8 Mt against 0.67–3.9 Mt). Liddell wins clearly only if Australia's grid stops decarbonising. And at Liddell, the same money spent on firmed renewables avoids more CO₂e in every case we tested. Every input is provisional [TO VERIFY]; the working is in Appendices B4–B6.

**Method.** CO₂e avoided = output × (intensity of the displaced electricity − 4.2 g CO₂e/kWh, our life-cycle value from §6). The output is that of one 300 MWe unit at a 0.90 capacity factor, 2.365 TWh a year [TODO: Leroy: 300 vs 315 MWe net].
- An *average* factor is the grid's mean intensity.
- A *marginal* factor is the intensity of the generation that actually runs less (mostly gas in Ontario). It is the factor recommended for evaluating new supply (The Atmospheric Fund, 2025) [TO VERIFY].
- The grid trajectories are our own constructions from published anchor points [TODO: replace with the 2026 ISP Step Change and IESO series].

### 7.1 The value of schedule

**A saving of kilotonnes is undone by a few days of delay.** A unit that starts late gives up each day's displacement (Table T10). Counted to 2050 (the "gross" view), that loss is permanent. Over the plant's whole life (the "net" view), the lost time comes back at the end of life, but on a cleaner grid.

*Table T10. Days of delay that cancel C1's LC3 saving, Darlington Units 2–4 (start 2035).*
*Source: this study, `scripts/schedule_value.py` (`results/schedule_value.md` §6; Appendix B5). Saving 1,734 t per unit and 5,201 t for Units 2–4 (§6.3). Brackets give the range over the saving's 90% interval. Grid factors: The Atmospheric Fund (2025); Independent Electricity System Operator (2024) [TO VERIFY].*

| Ontario grid case | CO₂e lost per day of delay, one unit (t, gross / net) | Days that cancel one unit's saving (gross / net) | Days of delay to one unit that cancel all of Units 2–4's saving (gross / net) |
|---|---|---|---|
| Average, falling to 15 g/kWh by 2040 | 189 / 119 | 9.2 (7.3–11.4) / 14.6 (11.6–18.1) | 28 / 44 |
| Marginal (gas), leaving the margin by 2050 | 1,296 / 1,226 | 1.3 (1.1–1.7) / 1.4 (1.1–1.8) | 4.0 / 4.2 |

**In money the gap is wider.** Canada's industrial carbon price is C$95/t in 2026, rising to C$115/t in 2030 (Environment and Climate Change Canada, 2026) [TO VERIFY]. At those prices, C1's 5,200 t across Units 2–4 is worth **C$0.49–0.60 m**. Even at the superseded C$170/t and the 95th-percentile saving, it is worth only C$1.10 m. A one-month slip of the three units does far more damage:
- It costs C$33–110 m in carrying cost (3–10% a year on their C$13.2 bn). This is an upper bound, because it assumes all the capital has already been spent.
- It defers about C$88 m of output at OPG's reported C$149/MWh [TO VERIFY; TODO: merge `opg_oeb_lcoe_lead` into sources.md].
- It loses 10.9–118 kt CO₂e, 2.1–22.7 times C1's saving.

The carbon value is also only a shadow price. Construction-material emissions appear to fall outside Ontario's industrial carbon pricing [TO VERIFY: analyst inference] (§8.2), so nobody is paid for the saving. **Schedule neutrality is therefore the binding condition on C1.** The mix must be qualified on mock-ups during Unit 1, before the Units 2–4 decision expected in 2028 [TO VERIFY] (§8.6).

### 7.2 What one BWRX-300 displaces: Darlington vs Liddell

**At today's grid factors, a unit at Liddell would avoid about nine times more CO₂e than one at Darlington. Timing closes most of that gap.**
- **NSW:** on the NSW grid average of 640 g/kWh (Department of Climate Change, Energy, the Environment and Water, 2025) [TO VERIFY], one unit avoids **1.50 Mt a year**.
- **Ontario, average:** on the 2024 average of 73.8 g/kWh (The Atmospheric Fund, 2025) [TO VERIFY], it avoids 0.165 Mt. NSW's figure is **9.1×** larger, or 20.6× on Canada Energy Regulator (n.d.) data for 2022.
- **Ontario, marginal:** on the marginal factor of 343 g/kWh (The Atmospheric Fund, 2025) [TO VERIFY definition], Darlington avoids 0.80 Mt and the ratio falls to **1.9×**.

**The two plants would not run in the same years.**
- Darlington Unit 1 runs from 2030 [TODO: Leroy: in-service date].
- An Australian unit is unlikely before 2040, CSIRO's earliest date for nuclear (Graham, Hayward and Foster, 2024) [TO VERIFY that it covers SMRs]. The Coalition claimed 2035 (ABC News, 2024) [TO VERIFY; secondary].
- If coal leaves the NEM by 2038, as in AEMO's Step Change scenario (Australian Energy Market Operator, 2024) [TO VERIFY; secondary], a 2040 unit displaces only a residual mix (30 g/kWh, assumed).

**CO₂e avoided to 2050 (Figure F6):**
- **Darlington Unit 1:** **1.0–6.8 Mt**, from the average trajectory to the declining marginal factor.
- **Liddell:** **0.67–3.9 Mt**, from the Step Change proxy to a slower transition. It reaches 16.5 Mt only if the NEM stays at 640 g/kWh.
- **Whole life:** the two sites are close, at 2.0–7.8 Mt against 3.7–6.8 Mt.

**What moves the results.** The grid trajectory, the start year and the post-coal floor move them by an order of magnitude. Capacity factor, net output and our life-cycle interval (3.0–5.8 g/kWh, which gives 630–702 kt) move them by only a few per cent (Appendix B4). Each year Australia takes to change the law, license and build costs 0.19–1.50 Mt per unit to 2050 (§8.1).

**Two caveats.**
- The grid factors count combustion only, while ours is a life-cycle value, so displacement is slightly understated.
- Liddell closed in 2023 (Australian Energy Regulator, 2021) [TO VERIFY closure date]. An SMR there would reuse the site and its grid connection, but it would displace the NEM mix, not Liddell.

**So an SMR's climate value depends on when it runs and what it displaces, not on today's coal share.** In Ontario the case rests on displacing marginal gas. At Liddell it rests on the NEM decarbonising slowly.

[Figure F6. CO₂e avoided by one BWRX-300 to 2050 and over its 60-year life: Darlington Unit 1 from 2030 (Ontario average trajectory; marginal, declining; marginal flat as upper bound) against Liddell from 2035 and 2040 (Step Change proxy; slow transition; frozen grid as upper bound). Inset: CO₂e lost per month of delay to one of Units 2–4, against C1's per-unit saving (1.73 kt). Data series in Tables B17 and B20. | Source: this study, scripts/displacement.py and scripts/schedule_value.py; grid factors The Atmospheric Fund (2025), Department of Climate Change, Energy, the Environment and Water (2025), Independent Electricity System Operator (2024), Australian Energy Market Operator (2024) [TO VERIFY]. | File: TODO: plot script not yet written; draw from results/displacement.md §3 and schedule_value.md §2]

### 7.3 The same money on firmed renewables

**At GenCost's 2030 costs, the money for one SMR unit would buy about 2.9 times as much energy from firmed renewables, which would avoid about 11 times more CO₂e to 2050 at Liddell.**

**Full cost.** GenCost 2023-24 gives A$230–382/MWh for an SMR in 2030, against A$89–125 for solar and wind with integration costs (Graham, Hayward and Foster, 2024, as reported) [TO VERIFY: GenCost table/year]. At the midpoints, the same spend buys **2.9×** the energy (Figure F7). Suppose the renewables start in 2028 [assumption] and the SMR in 2040, on the slower trajectory. The renewables then avoid **10.9×** more CO₂e to 2050, and still 5.7× more in the worst case we tested for them (SMR A$230 against renewables A$153 [assumption]), or 4.9× if the SMR also costs only A$198 (Table B28).

**Alternative reading.** We read A$387–641 as GenCost's 2023 value. If it is the 2030 value instead, the ratios are 5.0× and 19.1× (9.3–45.8× across cases). The conclusion holds either way. GenCost 2025-26 still ranks SMRs as the highest-cost option (Graham and Hayward, 2026) [TODO: its SMR and firmed-renewables values].

**Capital cost alone.** Darlington's C$20.9 bn (Ontario Power Generation, 2025) is about A$23.4 bn (Reserve Bank of Australia, 2025) [TO VERIFY]. At 7% over 30 years that capital alone costs A$199/MWh. That is already enough to buy 1.9–2.7× the energy from renewables at about A$107/MWh (Graham, Hayward and Foster, 2024) [TO VERIFY].

**Check against our own costing.** Our full Darlington cost of A$221/MWh at 7% real sits just below GenCost's 2030 range, plausibly because four units share infrastructure. It matches OPG's reported C$149/MWh at a 4.9% discount rate (§8.2).

**Why renewables come out ahead.** They are cheaper per MWh and start about a decade earlier. Two limits apply: that much new renewable output would itself shift the grid trajectory, and integration costs rise beyond the renewable shares GenCost models. The Ontario rows use Australian costs and are indicative only (Appendix B6). **On carbon per dollar, an SMR at Liddell loses.** Its case has to rest on firm supply, land use, system security and a hedge against renewables or transmission falling behind, and §9 weighs these.

[Figure F7. Same money, Liddell: firmed renewables (from 2028) against one SMR unit (from 2040, slower transition), as the ratio of energy bought and of CO₂e avoided to 2050 under four cost cases: GenCost 2023-24 2030 midpoints (SMR A$306, renewables A$107: 2.9× / 10.9×); worst case for renewables (A$230 / A$153: 1.5× / 5.7×); the alternative reading (A$514 / A$102: 5.0× / 19.1×); the lowest SMR lead tested (A$198 / A$153: 1.3× / 4.9×). Data in Table B28. | Source: this study, scripts/same_money.py; costs Graham, Hayward and Foster (2024; 2025) and Kim and Macfarlane (2026) [TO VERIFY: GenCost table/year]. | File: TODO: plot script not yet written; draw from results/same_money.md §5]

### 7.4 What this means for the initiative

C1 changes neither where an SMR is worth building nor what it displaces, and its value depends entirely on not delaying the plant. It gives §9 three inputs:
- **Environment:** "SMR + C1" differs from "SMR" by about 0.3%.
- **Economy:** C1 is worth C$0.49–0.60 m, against C$33–110 m for each month of delay.
- **Feasibility:** C1 stands or falls on schedule neutrality.

---

### IDs covered (towards the HD descriptor) and what is still missing

- **R2.1 (strong quantitative analysis).** Produced: CO₂e avoided per year, to 2050 and over the plant's life, for both sites; t CO₂e and C$ per day and per month of delay; energy and CO₂e ratios for the same money. Missing: verified inputs; F6 and F7 drawn.
- **R2.3 ("economic benefits ... appropriate to the scale of the proposal").** Produced: C1's carbon value (C$0.49–0.60 m) and break-even days sized to Darlington Units 2–4; displacement per unit and for four units (App B4). Missing: verified carbon price and OPG LCOE; Leroy's net MWe, capacity factor and dates.
- **R2.6 (logical, well justified).** Produced: one chain from C1's saving to the schedule condition; gross and net views explained; the counterfactual (same money) addressed. Missing: §9 to close the chain.
- **R2.7 (uncertainty realistically estimated).** Produced: average vs marginal factors, Ontario and NEM trajectories, start-year and floor sensitivity, the C1 saving's 90% interval carried into the break-even, both GenCost readings. Missing: AEMO/IESO series in place of constructed trajectories; 315 MWe in the sensitivity.
- **R4.3 (new, feasible connections).** Produced: schedule value against embodied carbon; the timing-aware Ontario vs Liddell comparison. Missing: a source for the value of reusing Liddell's grid connection.
- **R3.1, R3.6 (economic factors; comparison of solutions).** Produced: the same-money comparison and GenCost cross-check, handed to §8.2 and §9. Missing: GenCost 2025-26 values; the §9 MCDA.
- **RB.5, RB.6.** Produced: working in App B4–B6; our LCOE against GenCost and OPG. Missing: verification.
- **R5.1–R5.3.** Produced: leads with the schedule finding; one table and two specified figures; about 1.75 pages (hand estimate). Missing: Word page count; markers stripped at assembly.

### Remaining TODOs

1. **[TO VERIFY, P1, Victor]** GenCost 2023-24 final: is A$230–382 the 2030 SMR value and A$387–641 the 2023 value (NucNet lead)? `same_money.py` now runs on A$306 (230–382) and A$107 (89–125), with A$514 / A$102 as the alternative reading; if the table says otherwise, change `parameters_run1.yaml` and re-run. Also GenCost 2025-26's SMR and firmed-renewables values.
2. **[TO VERIFY, Victor]** The federal industrial carbon price path (C$95 in 2026, C$115 in 2030) on canada.ca; if confirmed, run 5 adopts it and re-runs `initiative_cost.py`.
3. **[TO VERIFY]** TAF 2025 average (73.8) and marginal (343, and its definition); NGA Factors 2025 NSW (640); CER 35; IESO 15 g/kWh by 2040; AEMO coal exit by 2038; the Liddell closure date; the RBA rate; OPG's C$149/MWh (merge `opg_oeb_lcoe_lead` from sources_run5.md into sources.md); C$20.9 bn; the 2028 Units 2–4 decision.
4. **[TODO: Leroy]** Net MWe (300 vs 315; add 315 to the displacement sensitivity), capacity factor, the Unit 1 and Units 2–4 start years (the context card has Unit 1 in service October 2030), and whether CSIRO's 2040 covers SMRs.
5. **[TODO: analyst]** Replace the constructed trajectories with the 2026 ISP Step Change and IESO outlook series; source the post-coal floor and a renewables lead time (2028 is an assumption).
6. **[TODO: plot]** Draw F6 and F7 from the results files in the deck's chart style, and use the same PNGs on slides 9 and 14.
