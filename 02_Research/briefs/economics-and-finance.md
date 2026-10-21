Rubric coverage: R3.1, R2.3, RB.6, R3.6, R3.7, R3.5, R3.8, R1.3, R2.7

# Brief: economics, finance and market barriers (for §7 and §8.2)

Analyst run 5, 21/10/2026. Working: `03_LCA_Calculations/results/lcoe.md` and `results/initiative_cost.md`; parameters in `parameters_run5.yaml`; sources in `02_Research/sources_run5.md`. **Every external number is a search lead [TO VERIFY]. No primary could be opened (proxy).** The writer may draft from this, but no claim is citable at HD until Victor opens the primary and the fact-checker confirms it. This reuses `same_money.md` (run 1) and does not repeat it.

## Questions
1. What does an SMR cost per MWh against large nuclear and firmed renewables (GenCost), and what does Darlington's own budget imply at different discount rates?
2. What does NuScale/UAMPS teach about cost risk?
3. Who finances Darlington and who bears the risk?
4. What are the barriers to entry for SMR vendors (valuations, China's model, vendor concentration)?
5. What does initiative C1 cost per tonne of CO₂e avoided, and what is the saving worth at Canada's carbon price?

## Answers

**1. LCOE.** GenCost ranks SMRs as the highest-cost new build in every edition from 2023-24 to 2025-26. The 2025-26 final (15 July 2026) still bases SMR capital on Darlington, "revised downwards" for interest during construction (CSIRO 2026, lead). Its SMR numbers were **not found** (gap). Leads for the earlier editions: 2023-24 final, 2030: SMR A$230–382, large nuclear A$141–233, solar and wind with integration A$89–125 (NucNet 2024, pointer to CSIRO 2024). 2024-25: SMR up to A$487 in 2030 before any first-of-a-kind premium; firmed renewables A$80–122 (ministerial release quoting GenCost). Our own Darlington LCOE (C$20.9 bn, 4 × 300 MWe, CF 0.90, 60 years, vendor opex US$28/MWh) is **C$112/151/198/280 per MWh at 3/5/7/10% real** (A$125/169/221/313). It reproduces OPG's reported **C$149/MWh** (OEB, lead) at about **4.9%**, which is a regulated Crown-utility cost of capital, not a merchant one. The tornado ranks capex overrun (×1.75, the CFPP precedent) first (C$174–317) and the discount rate second (C$151–280). Opex, capacity factor and output move it much less. **Synthesis (R1.3):** our 7% value (A$221) sits just below GenCost's 2030 range because Darlington is a four-unit site with shared infrastructure. At 2030 the SMR costs about **2.2–2.9×** firmed renewables, less than run 1's 5.0× (see the conflict below).

**2. NuScale/UAMPS (CFPP, Idaho National Laboratory, Idaho; UAMPS is a Utah utility group).** The target price went from US$58/MWh (2020$) to US$89/MWh (July 2022$): +53% nominal, about +35% real. The US$89 was already **net of about US$30/MWh of IRA credits**, so the pre-subsidy price was about US$119 (+80% real). Project cost rose from US$5.3 bn to US$9.24 bn (×1.74; about US$20,000/kW). DOE had obligated US$232.8 m of a US$1.355 bn award (17%); net exposure was reported at about US$50 m. It was cancelled in November 2023 because subscription was unlikely, not because of licensing. **For translation to practice:** when offtakers carry the cost-overrun risk, they leave. A first SMR needs an owner who can absorb overruns (a rate base or the state).

**3. Darlington financing and risk.** OPG, an Ontario Crown corporation, is the majority owner and operator. The CIB lent C$970 m (2022, low-interest, rate undisclosed) for Phase 1 pre-construction. The Canada Growth Fund (up to C$2 bn, up to 15%) and Building Ontario Fund (C$1 bn, 7.5%) take minority equity in DNNP LP, in two tranches: SMR 1, then SMRs 2–4 "once project milestones are met". C$585 m was received in April 2026. The funders say the structure "temporarily share[s] certain risks that currently limit private sector interest". **Who bears what:** construction-cost and schedule risk sits mainly with OPG and so with Ontario ratepayers (through OEB payment amounts) and the province as shareholder. Federal and provincial funds take a share of equity risk. The CIB takes credit risk at a concessional rate. GE Vernova Hitachi's contract risk share was not found (gap). The milestone-conditional second tranche is the lever for C1.

**4. Barriers to entry.** The capital at risk is about C$17,400/kW before any revenue. The leading US developers are valued well above their revenue: NuScale's non-affiliate float was about US$5.3 bn against US$31.5 m of 2025 revenue (**168×**) and a US$690 m operating loss; Oklo's float was about US$7 bn with no revenue reported (Q3 2025); NANO's was US$704 m. Equity markets price future orders. Governments and rate bases are financing the first plants: DOE's US$800 m (December 2025) went to two designs (BWRX-300 at Clinch River, Holtec SMR-300 at Palisades). Canada's first is a BWRX-300. Against about 70 active designs (IAEA 2024), funded construction is concentrated on very few vendors, and the BWRX-300 appears in both countries. China's model is different: the State Council approves batches (10 units in 2025; 8 units, about CNY 160–170 bn, on 31 July 2026), and state-owned CNNC, CGN and SPIC build them, with no merchant financing step. **No Linglong One cost was found.** For Australia, no programme supports nuclear generation. The legal bans (§8.1) mean no vendor can enter, so the barrier is absolute until the law changes.

**5. Initiative C1.** The LC3 saving (Units 2–4) is 5,190 t CO₂e, or **0.132 t per m³** of target concrete (`lca.md`). At Canada's benchmark carbon price of C$95 (2025), C$110 (2026) and C$170 (2030), the saving is worth **C$0.49 m, 0.57 m and 0.88 m**. That justifies a premium of up to **C$12.6, 14.5 and 22.5 per m³** (about 5.5–9.8% of a C$229/m³ commodity price). The abatement cost depends on two unsourced numbers, the LC3 price premium and the qualification cost. At 0% premium and C$1 m qualification it is C$193/t; at +10% it is C$173/t with no qualification cost or C$366/t with C$1 m. If the LC3 production-cost discount passes through (−10%), it saves money. **For translation to practice:** the whole target-concrete package is about C$9 m (0.07% of the Units 2–4 capital), so money is not the barrier. One day of delay costs C$1.8–2.9 m (carrying cost or deferred output), which is more than the entire carbon value. The same finding holds in tonnes (`schedule_value.md`). So C1 must be schedule-neutral: qualify the mix during Unit 1, before the Units 2–4 decision expected in 2028.

**Non-technical solutions (R3.7), compared (R3.6).**

| Option | Who pays | What it fixes | Evidence | Weakness |
|---|---|---|---|---|
| A. Embodied-carbon condition on the CGF/BOF Units 2–4 tranche | Funds (no cash cost) | Puts a price on C1's saving that no market pays now | Tranche is milestone-conditional (CGF_BOF_2025); CGF reports financed emissions | Needs the funds to agree; 2028 timing |
| B. Contract clause for an EPD cap, modelled on the federal Standard on Embodied Carbon | OPG and ratepayers (≤ C$22/m³ at C$170/t) | Makes low-clinker concrete the default | TBS standard: 10% below the regional EPD baseline; cost-premium cap concept | Standard does not bind OPG (sources.md, inference); SCC classed as a 130% "specialised mix" |
| C. Fund qualification on Unit 1 mock-ups as an R&D cost (for example NRCan or CGF) | Public R&D budget (C$1–3 m, assumed) | Removes the schedule risk, which is the binding constraint | `initiative_cost.md` §5: one day of delay ≈ C$2–3 m | No sourced cost for qualification |
| D. Do nothing | — | — | — | Forgoes 5,190 t at near-zero cost |

Recommended: **C plus A** (fund qualification now, condition the second tranche). B is the fallback.

## Numbers table

| Quantity | Value | Source key | Status |
|---|---|---|---|
| Darlington budget, 4 units | C$20.9 bn (C$17,417/kW) | OPG_2025_Q1 | TO VERIFY |
| Own LCOE at 3/5/7/10% (case B, 60 yr) | C$112 / 151 / 198 / 280 per MWh | lcoe.md | calc, inputs TO VERIFY |
| Real rate that reproduces OPG's C$149 | 4.9% | lcoe.md | calc |
| Tornado top 2 | capex ×0.85/×1.75: C$174–317; rate 5/10%: C$151–280 | lcoe.md | calc |
| OPG DNNP LCOE | C$149/MWh (2024$) | opg_oeb_lcoe_lead | TO VERIFY |
| GenCost 2023-24, 2030 SMR / large nuclear / VRE | A$230–382 / 141–233 / 89–125 | csiro2024_gencost2324 | TO VERIFY |
| GenCost 2023-24, 2023 SMR | A$387–641 | csiro2024_gencost2324 | TO VERIFY |
| GenCost 2024-25, 2030 SMR (upper) / firmed VRE | up to A$487 / A$80–122 | dcceew_bowen_release_gencost2425 | TO VERIFY |
| GenCost 2025-26 draft, large nuclear | A$200–328 | cec2025_gencost2526_draft | TO VERIFY |
| GenCost 2025-26 final SMR; any 2050 values | not found | csiro2026_gencost2526 | GAP |
| CFPP price | US$58 (2020$) → 89 (Jul 2022$, net of about US$30 IRA) | NuScale_DCRA_2023, ieefa2023_nuscale | TO VERIFY |
| CFPP cost | US$5.3 → 9.24 bn; about US$20,000/kW | NuScale_DCRA_2023 | TO VERIFY |
| DOE CFPP | US$232.8 m obligated of US$1.355 bn | DOE_CFPP_2020 | TO VERIFY |
| CIB loan; CGF; BOF | C$970 m; up to C$2 bn (15%); C$1 bn (7.5%) | CIB_2022_Loan, CGF_BOF_2025 | TO VERIFY |
| NuScale float / revenue 2025 | US$5.3 bn / US$31.5 m (168×) | nuscale_10k_2025 | TO VERIFY |
| Oklo float; NANO float | about US$7 bn; US$703.8 m | oklo_10k_2025, nano_10k_fy2025 | TO VERIFY |
| DOE Gen III+ SMR awards | US$400 m TVA + US$400 m Holtec | doe2025_gen3smr | TO VERIFY |
| Canada carbon price | C$95 (2025), 110 (2026), 170 (2030) | eccc_benchmark, enbridge_eps | TO VERIFY |
| C1 saving per m³ | 0.132 t CO₂e/m³ | lca_results_2110 | from results |
| C1 carbon value at C$95–170 | C$0.49–0.88 m | initiative_cost.md | calc |
| Break-even premium at C$95–170 | C$12.6–22.5/m³ | initiative_cost.md | calc |
| One day of Units 2–4 delay | C$1.8–2.9 m | initiative_cost.md | calc |

## Conflicts (also in plan.md Interfaces)
- **Run 1 SMR LCOE year.** `parameters_run1.yaml` `smr_lcoe_aud` = A$514 (387–641) is labelled 2030, but NucNet gives that range as GenCost 2023-24's **2023** value. The 2030 value is A$230–382. `same_money.md` therefore probably overstates the renewables advantage by about 1.7× (5.0× → about 2.9×). Its conclusion survives, because renewables are still cheaper and earlier.
- **Darlington budget basis.** OPG says the C$20.9 bn includes "interest, escalation and contingency". The Globe and Mail and World Nuclear Report call it "2024 dollars". Our LCOE treats it as real 2024 C$ (biased high if escalation is inside it).
- **Vendor vs independent cost.** Rao et al. list the BWRX-300 at US$2,250/kW (vendor) against Darlington's about US$12,600/kW. This is a 5.6× gap for R1.3 (Steigerwald et al. 2023 argue vendor figures are systematically low).

## Open gaps (owner: Victor unless stated)
1. GenCost 2025-26 final: SMR, large nuclear and firmed-VRE LCOE for 2030 and 2050, and the WACC (one file: the accessible-text report on csiro.au).
2. OPG's C$149/MWh on the OEB record (exhibit number), with its WACC and life.
3. LC3 price in Ontario (RMI 2024 North America scenario is the best lead); cost of CSA N287.2 qualification (Victor/Leroy to ask OPG or a laboratory).
4. GEH's share of cost-overrun risk in the Darlington contract; whether OEB payment amounts pass DNNP overruns to ratepayers.
5. Linglong One cost; a primary State Council or NDRC notice for China's approvals.
6. BLS CPI and the Bank of Canada FX rate to replace two placeholders (both low-sensitivity).
