Rubric coverage: R2.1, R2.3, R2.6, R2.7, R4.3, R3.1, R3.6, RB.5, RB.6 (also supports R3.5, R3.7, RB.8, R5.1, R5.2, R5.3)

<!--
CHANGELOG
- v1, 21/10/2026 (writer, job Q4, for Victor). First draft, from `results/displacement.md`, `schedule_value.md` and `same_money.md` (re-based by Q2 on 4.2 g/kWh), `results/lcoe.md` and `initiative_cost.md` (run 5), `briefs/displacement-and-cost.md`, `briefs/economics-and-finance.md` and §6 v3. Working: Appendix B4–B6.
  - review.md audit §2, R2 row ("economic benefits ... appropriate to the scale of the proposal"): displacement, schedule value and same money are now in the report text, sized to one unit and to Units 2–4, with C1's carbon value in C$.
  - review.md audit §2, R4 row ("new feasible ideas or connections"), and factcheck L47: the schedule finding leads the section, and the 1.3–15-day break-even now has working (App B5).
  - Conflict 1 (plan §5 Interfaces, GenCost year): run 5's reading used (2030 SMR A$230–382, energy ratio 2.9×); run 1's 5.0× stated as the alternative; marked [TO VERIFY: GenCost table/year].
  - Conflict 2 (carbon price): federal headline path from Q2 (C$95/t in 2026, C$115/t in 2030), [TO VERIFY]. The superseded C$170/t appears only where it sets the conservative bound of the 30–223× range.
  - factcheck S2 and displacement caveat 1: boundary mismatch (combustion-only grid factors vs life-cycle SMR) stated. Brief "Corrections to the deck": today's-factor ratio replaced by the timing-aware comparison; the NSW 640 g/kWh is called the NSW grid average, not coal.
  - factcheck S3 (300 vs 315 MWe) and S9 (Unit 1 start year): not resolved; TODOs kept.
  - Presentation: R5.1 (opens with the schedule finding; each subsection leads with its result); R5.2 (T10, F6 and F7 specified from results files, with captions and sources); R5.3 (about 870 words of body text excluding table, captions and markers, about 1.75 pages at 500 words a page; hand estimate, confirm in Word); R5.4 (Harvard, author forms as in sources.md); R5.5 (Australian English).
- Table ID T10 is new (T1–T9 are used or planned). Renumber at assembly (Q19).
-->

## 7 Carbon avoided: Ontario vs Liddell, the value of schedule, and the same money on firmed renewables

**For C1, schedule matters far more than concrete.** A one-month slip of Units 2–4 costs C$33–110 m in carrying cost alone and defers about C$88 m of output: **30–223 times the carbon value of C1's entire saving**. Per unit, the LC3 saving (about 1,740 t CO₂e, §6.3) is cancelled by **9–15 days of delay on Ontario's average grid factor, or 1.3–1.4 days on its marginal factor**. Timing also decides where an SMR helps the climate at all. Valued over the years each plant could actually run, a Darlington unit from 2030 avoids as much CO₂e to 2050 as a unit at Liddell from 2040, or more, unless Australia's grid stops decarbonising. And at Liddell, the same money spent on firmed renewables avoids more CO₂e by 2050 in every case tested. Every input is provisional [TO VERIFY]; the working is in Appendices B4–B6.

**Method.** All three calculations use §6's denominator: one 300 MWe unit at a 0.90 capacity factor, 2.365 TWh a year [TODO: Leroy: 300 vs 315 MWe net], with our life-cycle value of 4.2 g CO₂e/kWh. CO₂e avoided = output × (intensity of the displaced electricity − 4.2 g/kWh). An *average* factor is the grid's mean intensity. A *marginal* factor is the intensity of the generation that actually runs less, mostly gas in Ontario, and is the one recommended for evaluating new supply (The Atmospheric Fund, 2025) [TO VERIFY]. The grid trajectories are our own constructions from published anchor points, not AEMO or IESO series [TODO: replace with the 2026 ISP Step Change and IESO outlook series].

### 7.1 The value of schedule

**A plant that saves kilotonnes is undone by days.** Each day a unit starts late, it fails to displace that day's grid emissions (Table T10). Counted to 2050 (the "gross" view), that loss is final. Over the whole life (the "net" view), the lost month returns at the end of life, on a cleaner grid.

*Table T10. Days of delay that cancel C1's LC3 saving, Darlington Units 2–4 (start 2035).*
*Source: this study, `scripts/schedule_value.py` (`results/schedule_value.md` §6; Appendix B5). Saving 1,734 t per unit and 5,201 t for Units 2–4 (§6.3); brackets give the range over the saving's 90% interval. Grid factors The Atmospheric Fund (2025) and Independent Electricity System Operator (2024) [TO VERIFY].*

| Ontario grid case | CO₂e lost per day of delay, one unit (t, gross / net) | Days that cancel one unit's saving (gross / net) | Days of delay to one unit that cancel all of Units 2–4's saving (gross / net) |
|---|---|---|---|
| Average, falling to 15 g/kWh by 2040 | 189 / 119 | 9.2 (7.3–11.4) / 14.6 (11.6–18.1) | 28 / 44 |
| Marginal (gas), leaving the margin by 2050 | 1,296 / 1,226 | 1.3 (1.1–1.7) / 1.4 (1.1–1.8) | 4.0 / 4.2 |

**The same holds in money.** At Canada's headline industrial carbon price of C$95/t in 2026 and C$115/t in 2030 (Environment and Climate Change Canada, 2026) [TO VERIFY], C1's 5,200 t across Units 2–4 is worth **C$0.49–0.60 m**. Even on the superseded C$170/t path, at the 95th-percentile saving, it reaches only C$1.10 m. Set against that:
- **Carrying cost:** a one-month slip of all three units costs C$33–110 m at 3–10% on C$13.2 bn. This is an upper bound, because it assumes all the capital is already spent.
- **Deferred output:** the slip defers about C$88 m of output at OPG's reported C$149/MWh [TO VERIFY; TODO: merge `opg_oeb_lcoe_lead` from sources_run5.md into sources.md].
- **Carbon alone:** the slip loses 10.9–118 kt CO₂e, 2.1–22.7 times C1's saving.

The 30–223× multiple is conservative: on the current price path alone, C1's value is lower and the multiple higher. The carbon value is also only a shadow price, because construction-material emissions appear to fall outside Ontario's industrial carbon pricing [TO VERIFY: analyst inference] (§8.2). **Being schedule-neutral is therefore the binding condition on C1, not a preference.** The mix must be qualified on mock-ups during Unit 1, before the Units 2–4 decision expected in 2028 [TO VERIFY] (§8.6).

### 7.2 What one BWRX-300 displaces: Darlington vs Liddell

**At today's grid factors, a unit at Liddell would avoid about nine times more CO₂e than one at Darlington. Timing closes most of that gap.**
- **NSW today:** the NSW grid average of 640 g/kWh (Department of Climate Change, Energy, the Environment and Water, 2025) [TO VERIFY] gives **1.50 Mt CO₂e a year**.
- **Ontario today:** its 2024 average of 73.8 g/kWh (The Atmospheric Fund, 2025) [TO VERIFY] gives 0.165 Mt, a ratio of **9.1×**. On Canada Energy Regulator (n.d.) data for 2022 (35 g/kWh) the ratio is 20.6×. On Ontario's marginal factor of 343 g/kWh (The Atmospheric Fund, 2025) [TO VERIFY definition], Darlington avoids 0.80 Mt a year and the ratio falls to **1.9×**.

The two plants would not run in the same years:
- **Darlington:** Unit 1 is planned from 2030 [TODO: Leroy: confirm the in-service date].
- **Liddell:** an Australian unit is unlikely before 2040, CSIRO's earliest deployment date for nuclear (Graham, Hayward and Foster, 2024) [TO VERIFY that it covers SMRs]. The Coalition claimed 2035 (ABC News, 2024) [TO VERIFY; secondary].
- **The NEM by then:** if coal leaves the NEM by 2038, as in AEMO's Step Change scenario (Australian Energy Market Operator, 2024) [TO VERIFY; secondary], a 2040 unit displaces a residual mix, which we assume to be 30 g/kWh [assumption].

**CO₂e avoided to 2050 (Figure F6):**
- **Darlington Unit 1 from 2030:** 1.0 Mt (average trajectory) to 6.8 Mt (marginal factor, declining).
- **Liddell from 2040:** 0.67 Mt (Step Change proxy) or 3.9 Mt (a slower transition). It reaches 16.5 Mt only if the grid stays at 640 g/kWh.
- **Whole life:** the two sites are close, at 2.0–7.8 Mt against 3.7–6.8 Mt.

The grid trajectory, the start year and the post-coal floor move these results by an order of magnitude. Capacity factor, net output and our own life-cycle interval (3.0–5.8 g/kWh: 630–702 kt) move them by a few per cent (Appendix B4). Each year Australia takes to change the law, license and build costs 0.19–1.50 Mt per unit to 2050 (§8.1).

Two caveats:
1. **The grid factors are combustion-only, while ours is life-cycle**, so displacement is slightly understated.
2. **Liddell closed in 2023** (Australian Energy Regulator, 2021) [TO VERIFY closure date]. An SMR there would reuse the site and its grid connection, but it would displace the NEM mix, not Liddell.

**The connection is that an SMR's climate value depends on when it runs and what it displaces, not on today's coal share (R4.3).** In Ontario the case rests on displacing marginal gas; at Liddell it rests on the NEM decarbonising slowly.

[Figure F6. CO₂e avoided by one BWRX-300 to 2050 and over its 60-year life: Darlington Unit 1 from 2030 (Ontario average trajectory; marginal, declining; marginal flat as upper bound) against Liddell from 2035 and 2040 (Step Change proxy; slow transition; frozen grid as upper bound). Inset: CO₂e lost per month of delay to one of Units 2–4, against C1's per-unit saving (1.73 kt). Data series in Tables B16 and B19. | Source: this study, scripts/displacement.py and scripts/schedule_value.py; grid factors The Atmospheric Fund (2025), Department of Climate Change, Energy, the Environment and Water (2025), Independent Electricity System Operator (2024), Australian Energy Market Operator (2024) [TO VERIFY]. | File: TODO: plot script not yet written; draw from results/displacement.md §3 and schedule_value.md §2]

### 7.3 The same money on firmed renewables

**At GenCost's 2030 costs, the money for one SMR unit would buy about 2.9 times as much energy from firmed renewables, which would avoid about 11 times more CO₂e to 2050 at Liddell.**

**Capital cost alone.** Darlington's C$20.9 bn (Ontario Power Generation, 2025) [TO VERIFY] is about A$23.4 bn at 1.119 AUD/CAD (Reserve Bank of Australia, 2025) [TO VERIFY]. Its capital alone costs A$199/MWh per unit at 7% over 30 years. That would buy 2.0–2.9 times the energy as firmed renewables at about A$102/MWh (Graham, Hayward and Foster, 2025) [TO VERIFY]. This is a lower bound, because it leaves out the SMR's operating and fuel costs.

**Full cost.** GenCost 2023-24 gives A$230–382/MWh for an SMR in 2030 against A$89–125 for solar and wind with integration costs (Graham, Hayward and Foster, 2024, as reported) [TO VERIFY: GenCost table/year]. At the midpoints, the same annual spend buys **2.9×** the energy (Figure F7). For a Liddell SMR from 2040 on the slower trajectory, renewables from 2028 [assumption] avoid **10.9×** more CO₂e to 2050. In the worst case for renewables that we tested (SMR A$230, renewables A$153 [assumption]), they still avoid 5.7× more. **Alternative reading:** if A$387–641 is the 2030 value rather than the 2023 value, the ratios are 5.0× and 19.1× (9.3–45.8× across start years and trajectories). The conclusion holds under either reading. The current edition, GenCost 2025-26, still ranks SMRs as the highest cost, but we could not retrieve its SMR values (Graham and Hayward, 2026) [TODO: GenCost 2025-26 SMR and firmed-renewables values].

**Comparison with our own costing (RB.6).** Our Darlington cost of A$221/MWh at 7% real sits just below GenCost's 2030 range, plausibly because Darlington shares infrastructure across four units. It matches OPG's reported C$149/MWh at a 4.9% discount rate (§8.2).

**Why renewables come out ahead.** They are cheaper per MWh and start about a decade earlier. Two caveats apply:
- 12 TWh a year of new renewables would itself shift the grid trajectory.
- Integration costs rise beyond GenCost's modelled renewable shares.

The Ontario rows use Australian costs and are indicative only (Appendix B6). **On carbon per dollar, then, an SMR at Liddell loses.** Its case must rest on other objectives (firm supply, land use, system security, and a hedge if renewables and transmission fall behind), which the §9 MCDA weighs (R3.6).

[Figure F7. Same money, Liddell: firmed renewables (from 2028) against one SMR unit (from 2040, slower transition), shown as the ratio of energy bought and of CO₂e avoided to 2050 under four cost cases: GenCost 2023-24 2030 midpoints (SMR A$306, renewables A$107: 2.9× / 10.9×); worst case for renewables (A$230 / A$153: 1.5× / 5.7×); the alternative reading (A$514 / A$102: 5.0× / 19.1×); the lowest SMR lead tested (A$198 / A$153: 1.3× / 4.9×). Data in Table B23. | Source: this study, scripts/same_money.py; costs Graham, Hayward and Foster (2024; 2025) and Kim and Macfarlane (2026) [TO VERIFY: GenCost table/year]. | File: TODO: plot script not yet written; draw from results/same_money.md §5]

### 7.4 What this means for the initiative

C1 changes neither where an SMR is worth building nor what it displaces. Its value depends entirely on not delaying the plant. For §9 this gives three inputs:
- **Environment:** "SMR + C1" differs from "SMR" by about 0.3%.
- **Economy:** C1's value is C$0.49–0.60 m, against C$33–110 m for each month of delay.
- **Feasibility:** C1 is feasible only if it is schedule-neutral.

---

### IDs covered (towards the HD descriptor) and what is still missing

- **R2.1 (strong quantitative analysis).** Produced: CO₂e avoided per year, to 2035/2050 and over the plant's life, for both sites; t CO₂e and C$ per day and month of delay; energy and CO₂e ratios for the same money. Missing: verified inputs; F6 and F7 drawn.
- **R2.3 ("economic benefits ... appropriate to the scale of the proposal").** Produced: C1's carbon value (C$0.49–0.60 m) and break-even days sized to Darlington Units 2–4; displacement per unit and for four units. Missing: verified carbon price and OPG LCOE; Leroy's net MWe, capacity factor and dates.
- **R2.6 (logical, well justified).** Produced: a single chain from the C1 saving to the schedule condition, gross and net views explained, and the counterfactual (same money) addressed. Missing: §9 to close the chain.
- **R2.7 (uncertainty realistically estimated).** Produced: average vs marginal factors, four Ontario and three NEM trajectories, start-year and floor sensitivity, the C1 saving's 90% interval carried into the break-even, and both GenCost readings. Missing: AEMO/IESO series in place of our constructed trajectories; 315 MWe in the sensitivity.
- **R4.3 (new, feasible connections).** Produced: schedule value against embodied carbon; timing-aware Ontario vs Liddell comparison. Missing: a source for the value of reusing Liddell's grid connection (brief gap).
- **R3.1, R3.6 (economic factors; comparison of solutions).** Produced: the same-money comparison and the GenCost cross-check, handed to §8.2 and §9. Missing: GenCost 2025-26 values; §9 MCDA.
- **RB.5, RB.6.** Produced: working in App B4–B6; our LCOE against GenCost and OPG. Missing: verification.
- **R5.1–R5.3.** Produced: leads with the schedule finding; one table and two specified figures; about 1.75 pages (hand estimate). Missing: Word page count; markers stripped at assembly.

### Remaining TODOs

1. **[TO VERIFY, P1, Victor]** GenCost 2023-24 final: is A$230–382 the 2030 SMR value and A$387–641 the 2023 value (NucNet lead)? If confirmed, set `smr_lcoe_aud` to 306 (230–382) and `vre_firmed_lcoe_aud` to 107 (89–125) in `parameters_run1.yaml` and re-run `same_money.py` so that every row of B6 is on one basis. Also GenCost 2025-26's SMR and firmed-renewables values.
2. **[TO VERIFY, Victor]** The federal industrial carbon price path (C$95 in 2026, C$115 in 2030) on canada.ca; if confirmed, run 5 sets the same values and re-runs `initiative_cost.py`.
3. **[TO VERIFY]** TAF 2025 average (73.8) and marginal (343, and its definition); NGA Factors 2025 NSW (640); CER 35; IESO 15 g/kWh by 2040; AEMO coal exit by 2038; the Liddell closure date; RBA rate; OPG's C$149/MWh (merge `opg_oeb_lcoe_lead` into sources.md); C$20.9 bn; the 2028 Units 2–4 decision.
4. **[TODO: Leroy]** Net MWe (300 vs 315: add 315 to the displacement sensitivity), capacity factor, Darlington Unit 1 and Units 2–4 start years, and whether CSIRO's 2040 covers SMRs.
5. **[TODO: analyst]** Replace the constructed trajectories with the 2026 ISP Step Change and IESO outlook series; source the post-coal floor and a renewables lead time (2028 is an assumption).
6. **[TODO: plot]** Draw F6 and F7 from the results files in the deck's chart style, and use the same PNGs on slides 9 and 14.
7. **[TODO: §6, Q8]** §6's lead and finding 5 say "1.4–15" and "10–15 days"; Q2's re-run gives 9.2–14.6 (average) and 1.3–1.4 days (marginal). Align §6 with Table T10.
