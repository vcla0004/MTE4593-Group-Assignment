Rubric coverage: RB.3, R1.1, R1.3, R1.4, R2.5

# Brief: State of the technology, projects, TRL and timelines (analyst run 8, plan job Q5, 25/10/2026)

Drafted for Leroy's §4.1–4.2 (Leroy may reclaim). Source keys: `02_Research/sources_run8.md` (new) and `sources.md` / `sources_lca.md` (existing). **Every source here is a web-search lead, not opened: all [TO VERIFY].** No `parameters_lca.yaml` value changes (the LCA side is with Victor); two leads for the lca-analyst are in §5.

## 1. Question
What is the current state of SMR technology, how ready is the BWRX-300 we build our initiative on, and when could an SMR first run in Australia?

## 2. Answer in brief
- No light-water SMR runs anywhere on land yet. The only SMR-class plant in commercial operation in the comparison set is China's gas-cooled HTR-PM (210 MWe, since December 2023) (WNN_2023_HTRPM). China's ACP100 "Linglong One" has finished non-nuclear commissioning but had not reached criticality by May 2026, as far as the leads show (WNN_Linglong_Steam).
- The BWRX-300 is the Western design closest to operation: a construction licence at Darlington (April 2025), with Unit 1 due in service in October 2030 (CNSC_2025_LTCDecision; OPG_OEB_EB-2025-0297_D2-4-1), and a US construction permit for TVA's Clinch River (29 September 2026, after a 14-month review) (GEV_2026_ClinchRiverCP). Our rating is TRL 6–7: licensed and under construction, but no unit has operated.
- NuScale shows that regulatory approval doesn't make a project viable. The 77 MWe US460 design was approved in May 2025 (NRC_NuScale_US460), yet the first plant (UAMPS, 462 MWe) was cancelled in November 2023 when the cost estimate reached US$9.24 bn, about US$20,000/kW (UAMPS_NuScale_2023; NuScale_DCRA_2023).
- Australia: the Coalition claimed 2035 for first SMR power (2037 for large plants), while CSIRO says 2040 at the earliest (ABC_2024_SevenSites; csiro2024_gencost2324). Darlington's own timeline supports CSIRO's date (§4).

## 3. T2: Projects, status and TRL (≤ 6 rows)
TRL ratings are the analyst's, against DOE G 413.3-4A: TRL 8 is an "actual system completed and qualified through test and demonstration", and TRL 9 an actual system "operated under the full range of operating mission conditions" (DOE_2015_TRAGuide).

| Project (owner) | Design | MWe | Status (Oct 2026) | First power | TRL and basis |
|---|---|---|---|---|---|
| Darlington Unit 1 (OPG), Clarington, Ontario | GEH BWRX-300 (BWR, natural circulation) | 300 (GEH); 315 net in OPG's OEB filing | Licence to construct 4 Apr 2025 (to 31 Mar 2035); RHP-1 lifted 30 Mar 2026; basemat module set 22 Apr 2026; operating-licence application Mar 2026 | In service **Oct 2030** (OEB filing) | **6–7**: licensed, being built, never operated. TRL 8 only after commissioning |
| Darlington Units 2–4 (OPG) | BWRX-300 | 3 × 300 | Inside the C$20.9 bn budget but **not licensed**: needs a further licence to construct; approval to proceed "expected in 2028" | 2034–2036 (2023 plan; may have moved) | 6–7 (same design). **This is where C1 applies** |
| Clinch River Unit 1 (TVA), Tennessee | BWRX-300 | 300 | NRC construction permit **29 Sep 2026** (14-month review); no construction date; cost-share talks ongoing | Not announced [gap] | 6–7. A second regulator has now accepted the design |
| Linglong One (CNNC), Hainan | ACP100 (integral PWR) | 125 (385 MWt) | First concrete 13 Jul 2021; cold tests Oct 2025; non-nuclear steam test done; no criticality by 20 May 2026 (lead) | Target H1 2026 (missed, per leads) | **7**: complete plant in commissioning, no nuclear operation yet |
| HTR-PM (Huaneng/CNNC/Tsinghua), Shidaowan | Pebble-bed HTGR, 2 × 250 MWt | 210 | Grid 20 Dec 2021; commercial operation 6 Dec 2023; reported at 2 × 200 MWt | **2021** | **8–9**: operating, but reportedly below rated power |
| Carbon Free Power Project (UAMPS/NuScale), Idaho | NuScale VOYGR-6 / US460 | 6 × 77 = 462 | **Cancelled 8 Nov 2023** (subscription shortfall); design approved May 2025 | None (was 2029) | **6**: design approved, no unit built |

Sources by row: CNSC_DNNP_Page, CNSC_RHP_Page, opg_basemat_story, OPG_OEB_EB-2025-0297_D2-4-1, ANS_2026_Darlington, opg_dnnp; GEV_2026_ClinchRiverCP, ANS_2026_ClinchSE; WNN_Linglong_Steam; WNN_2023_HTRPM; UAMPS_NuScale_2023, NuScale_DCRA_2023, NRC_NuScale_US460.

**Synthesis (R1.3).**
1. *Build times.* HTR-PM took 9 years from first concrete to grid (Dec 2012 to Dec 2021) and 11 years to commercial operation. Linglong One's planned 58-month build (July 2021 + 58 months = May 2026) has already slipped, if the May 2026 PRIS reading still holds. State-led Chinese projects also overrun, so the vendors' "factory-style" speed is not yet proven anywhere.
2. *Licensing speed has improved.* Darlington's licence to construct took 29 months (Oct 2022 to Apr 2025) and Clinch River's permit 14 months. The second review was faster because it reused the CNSC–NRC joint work on the same design (NRC_CNSC_2025_JointReport), which is the "fleet" benefit SMR advocates claim.
3. *Cost, not licensing, killed NuScale.* US$9.24 bn / 462 MW ≈ **US$20,000/kW**, even with a US$89/MWh target price that was already net of IRA credits. Darlington's C$20.9 bn / 1,200 MW = **C$17.4 m/MW** (C$17,400/kW). Both are first-of-a-kind numbers.

## 4. BWRX-300 at Darlington: design data
| Item | Value | Source | Status and note |
|---|---|---|---|
| Net output | **300 MWe** (GEH); **315 MW net** (OPG OEB filing, Exhibit A1-4-3) | gevernova_bwrx300_gd; OPG_OEB_EB-2025-0297_D2-4-1 | Conflict unresolved. Keep 300 as central and 315 as a sensitivity (the current model already does this). One WNA database page reads 280 MWe (lead, not used) |
| Thermal power | 870 MWt (≈ 34.5% net efficiency at 300 MWe) | arxiv2025_smr_overview | Preprint; replace with CNSC_GNF2_Ref or ONR_BWRX_Step2_Fuel |
| Capacity factor | **95%** design value (IAEA ARIS, as quoted by Fermi Energia) | FermiEnergia_SMR | Vendor-supplied design figure. The model's 0.90 central (0.80–0.95) is a reasonable first-of-a-kind discount; 0.95 now has a lead for the upper bound |
| Design life | **60 years** (GE Vernova; CNSC staff CMD 24-H3-1B); 65 years reported for Ontario | GEV_UKSMR_Technology; cnsc_cmd24_h3_1b | Two independent leads agree on 60 |
| Fuel | GNF2 10×10 BWR fuel, **240 bundles**, UO₂ in Zircaloy-2, reload enrichment **3.8% average, 4.95% maximum** | arxiv2025_smr_overview; GEV_UKSMR_Technology; CNSC_GNF2_Ref | The enrichment figures still rest on the preprint. **Burnup: not found [gap]** |
| Cycle length | **12–24 months**, refuelling outage **10–15 days**; PNNL work "could support" 36–48 months | GEV_UKSMR_Technology; GEV_PNNL_Fuel | Vendor claims |
| Fabrication | Global Nuclear Fuel–Americas (US); enrichment Urenco USA plus Orano; uranium and conversion Cameco | OPG_2023_fuel | Site (Wilmington, NC) still TO VERIFY |
| Passive safety | Natural circulation (no recirculation pumps); **isolation condensers** passively cool the core for **7 days** without power or operator action (Category C passive system, IAEA-TECDOC-626); indefinite cooling if the pools are topped up | GEH_FactSheet; App E patents US 10,867,712 B2 and US 12,308,130 B2 | Vendor claim; the NRC/CNSC review documents are the check |
| Structure | **DP-SC** (diaphragm-plate steel-plate composite): two steel faceplates tied by diaphragm plates with concrete flow holes, filled with **self-consolidating concrete**; Purdue tests under seismic loads; codes: AISC N690 (modified) and ASME for containment | GEH_NEDO33926; NRC_CNSC_2025_JointReport; DOE_2025_DPSC | C1 targets this infill |
| Reactor building | Below-grade **vertical right-cylinder shaft**, sunk by open caisson; Unit 1 basemat module 37 m diameter, about 952 t, set 35 m below ground on 22 Apr 2026 | DOE_GEH_VerticalShaft; opg_basemat_story; App E US 2020/0208517 A1 | DOE says vertical-shaft construction could save more than a year (projection) |
| Concrete claim | "More than 50% less concrete per MW" than GEH's 1,520 MWe ESBWR | GEH_JAIF_2018; GEH_AI_2021 | **Vendor claim; check it against the cross-check below** |

**Cross-check of the concrete claim (R1.3, RB.6).** The ESBWR needs 69 m³/MWe (peterson2005). Half of that is 34.5 m³/MWe, or **10,350 m³** for a 300 MWe unit. The Ostrołęka project information sheet gives **50,000 m³** per BWRX-300 (ostroleka2023_pis), which is 50,000 / 300 = **167 m³/MWe**: 2.4 times the ESBWR intensity and 4.8 times what the vendor claim implies. Steel shows the same pattern: 14,000 t / 300 = 46.7 t/MWe, against 33 t/MWe for the ESBWR (1.4×). The likely explanation is boundary, not error. The vendor ratio compares nuclear-island buildings, while the Ostrołęka figure covers the whole site (inference; TO VERIFY in the PIS Table 14 notes). Either way, **a small reactor does not mean small concrete**, and that is what makes C1 worthwhile.

## 5. Australia's earliest date
| Claim | Date | Basis | Source |
|---|---|---|---|
| Coalition policy (June 2024) | **2035** SMRs; **2037** large plants | Seven Commonwealth-owned sites, including Liddell | ABC_2024_SevenSites (news; the 19 June 2024 Coalition release is still to be found) |
| CSIRO GenCost 2023-24 | **2040** earliest | Development time of at least 15 years: no pipeline, legal, safety and security requirements | csiro2024_gencost2324 |
| Federal Government | "well into the 2040s" | Cites GenCost | Bowen_Statements |
| Current Coalition (2026) | No date; would "repeal all legislative prohibitions" | Needs the Senate | ABC_2026_CoalitionEnergyPlan; Liberal_2026_EnergyPlan |

**Darlington as a yardstick (analyst inference).** Darlington had an operating nuclear utility, a licensed site (site-preparation licence 2012, after an environmental assessment that began in 2007) and an experienced regulator. It still needs **8 years from licence application to power** (Oct 2022 to Oct 2030). Australia has none of these, and the two federal bans (EPBC s140A, ARPANS s10) would have to be repealed first; the pro-repeal Senate bloc is ≤ 32 of the 39 votes needed (briefs/law-and-regulation.md). As an illustration: repeal no earlier than about 2029, then about 3 years to set up a power-reactor licensing regime and a site licence (assumption), then Darlington's 8 years, gives **about 2040**. This matches CSIRO and the report's first-power assumption (≈ 2040 at Liddell), and it makes 2035 look unreachable. The 2029 and 3-year inputs are assumptions, not sourced.

## 6. Translation to practice (for §4.2 and §4.3)
- C1 needs a design that is licensed but not frozen. Darlington Units 2–4 fit: same design, budget in place, licence still to come, and approval expected in 2028. This is a real window, not a hypothetical one.
- Clinch River's permit shows the DP-SC design is now accepted by two regulators, so an LC3 infill qualified at Darlington could carry over to TVA's units. That is the fleet multiplier for C1.
- For Australia the binding constraint is time to first power (≈ 2040), not technology readiness. By then the BWRX-300 should be TRL 9 if Darlington Unit 1 runs from 2030.

## 7. Numbers table
| Quantity | Value | Working or source |
|---|---|---|
| Darlington licence review | 29 months | Oct 2022 to Apr 2025 |
| Clinch River permit review | 14 months | GEV_2026_ClinchRiverCP |
| Darlington, application to in service | 8.0 years | Oct 2022 to Oct 2030 |
| HTR-PM, first concrete to grid / to commercial operation | 9 / 11 years | Dec 2012 to Dec 2021 / Dec 2023 |
| Linglong One planned completion | May 2026 | 13 Jul 2021 + 58 months |
| NuScale CFPP specific cost | US$20,000/kW | 9.24 bn / 462,000 kW |
| Darlington specific cost | C$17,400/kW | 20.9 bn / 1,200,000 kW |
| Concrete intensity: ESBWR / vendor-implied BWRX-300 / Ostrołęka | 69 / 34.5 / 167 m³/MWe | peterson2005; ×0.5; 50,000/300 |
| Steel intensity: ESBWR / Ostrołęka | 33 / 46.7 t/MWe | peterson2005; 14,000/300 |
| Net efficiency | 34.5% | 300/870 |

## 8. Open gaps and interfaces
- **To the lca-analyst (no re-run requested):** design life 60 years now has a second lead (GEV_UKSMR_Technology); the capacity-factor upper bound of 0.95 has a lead (FermiEnergia_SMR); burnup is still unsourced; 300 vs 315 MWe is unresolved.
- Primaries to open (Victor): IAEA PRIS (Linglong One status; blocked host), the OEB exhibit (Units 2–4 dates), NEDO-33926 §5.2.1, the GNF2 CNSC reference (burnup), the Coalition's June 2024 release, and GenCost 2023-24 (does the 2040 statement cover SMRs?).
- No Clinch River first-power date was found.
