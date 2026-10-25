Rubric coverage: RB.4, RB.7, R4.2, R1.1, R1.3, R1.4

# Brief: Materials from extraction to end of life, and future material needs (analyst run 8, plan job Q5, 25/10/2026)

Drafted for Leroy's §5 and §10 (Leroy may reclaim). Keys: `02_Research/sources_run8.md` (new) and `sources.md` / `sources_lca.md`. **All sources are web-search leads, not opened: [TO VERIFY].** C1 numbers are from the deck case (`results/c1_deck_case.md`) and are not recalculated here.

## 1. Question
(a) How do the C1 binder options (LC³, Portland clinker, GGBFS slag) and the plant's steel move from extraction to end of life, in a nuclear setting? (b) Which material properties or processes are still missing (RB.7)?

## 2. Answer in brief
- **Binder.** LC³-50 halves the clinker, at about 50% clinker, 30% calcined clay, 15% limestone and 5% gypsum (Zunino_LC3_slides). The clay is calcined at about 800 °C (700–850 °C window), not sintered like clinker. At M50, Pillai et al. measured **270 vs 380 kg CO₂e/m³ (−29%)**, with 28-day strength of 56.7 vs 60.0 MPa (pillai2019_lc3). Slag is a blast-furnace by-product. It is proven in nuclear concrete (IJCSM_2026_NPPConcrete), but Ontario's blast furnaces are closing (Algoma, January 2026; Dofasco planned), so it is a shrinking supply (Algoma_2026_BFclosure; ArcelorMittal_Dofasco_2021).
- **Nuclear service.** For radiation, aggregate swelling matters more than the binder (Field_2015). LC³ resists chloride about ten times better than OPC but carbonates faster (LC3_Chloride_2025). In DP-SC modules the infill is enclosed by steel faceplates, which should limit carbonation exposure (inference). The open problem is the fresh concrete: calcined clay raises superplasticiser demand and lowers flow (UniBw_CC_SCC; IITM_LC3_Rheology).
- **End of life.** Activation is set by trace elements (Co-60, Eu-152, Eu-154), with Eu-152 the limiting nuclide (Greifswald_Activation). Most plant concrete is clearable, and only "a few per cent" stays radioactive waste (Thierfeldt_2019). How much europium and cobalt is in calcined clay is unknown, and it should be measured during qualification. This is a less obvious materials issue (R4.2).
- **Steel.** Scrap-EAF emits **0.67–0.69 t CO₂/t** against **2.33–2.34** for BF-BOF (worldsteel_2026_CO2). Nuclear-grade forgings cannot simply switch to scrap, because copper from scrap embrittles vessel steel under irradiation (CNSC_2023_EnvDegradation; NRC_RG199; Daehn_2017).

## 3. Life cycle of the C1 binder options
| Stage | Portland clinker (GU / OPC) | LC³ (calcined clay + limestone) | GGBFS slag (fallback) |
|---|---|---|---|
| **Extraction** | Limestone and shale quarried | Kaolinitic clay (lower-grade clays are usable; Pat_US8906155 covers clays with less than 40% kaolinite) plus limestone; half the clinker | None of its own: a by-product of iron blast furnaces |
| **Processing** | Kiln clinkering; process CO₂ from calcining limestone plus fuel | Clay calcined at **≈ 800 °C** (700–850 °C) with no limestone decarbonation in the clay step; inter-ground with clinker, limestone and gypsum. CO₂ per tonne of cement **−30% to −43%** (five leads, median 37%; lc3_reduction_leads) | Granulated and ground. EPD **146.6 kg CO₂e/t** (industry average; one plant 93.4) (sca_epd) |
| **Standards fit** | CSA A3001 GU | Type IT with **≤ 15% limestone** plus calcined clay; more limestone needs a standards change (Hooton_2023_ACI; CSA_A3000_23) | Established SCM; slag is "widely adopted" in NPP mixes (IJCSM_2026_NPPConcrete) |
| **Construction (DP-SC infill)** | SCC specified by NEDO-33926 Rev. 2 §5.2.1 (GEH_NEDO33926) | Higher superplasticiser demand, lower deformability, harder to keep workable; up to 40 vol.% calcined clay leaves 28-day strength unchanged (UniBw_CC_SCC; IITM_LC3_Rheology). Industry is patenting fixes (Sika PCE plus sugar-based admixture: Pat_US20230202926) | Lowers heat in thick sections; "high replacement levels" complicate fresh-concrete control (IJCSM_2026_NPPConcrete) |
| **Service: radiation and heat** | Main mechanism is aggregate swelling, near end of shield life at 80 years (Field_2015) | Same aggregates, so similar irradiation risk (inference). **No LC³ adiabatic heat-of-hydration data found [gap]** | Lower heat; long nuclear track record |
| **Service: durability** | Reference | Chloride diffusion about 1 order of magnitude lower; carbonation weaker (LC3_Chloride_2025). Faceplates enclose the infill (inference) | Good chloride resistance (not sourced here) |
| **Decommissioning** | Activated near the core: Co-60, Eu-152, Eu-154; Eu-152 above clearance to about 35 cm in the Greifswald shield (Greifswald_Activation) | Same issue. **Eu and Co content of calcined clay unknown [gap; RB.7]** | Same; slag chemistry adds no known activation advantage [not sourced] |
| **Waste class and reuse** | Most concrete cleared (IAEA-type criterion about 10 µSv/yr) and reused as backfill or aggregate; activated parts go to LLW (CNSC classes: LLW incl. VLLW, ILW, HLW, mine/mill) (Thierfeldt_2019; CNSC_WasteClasses) | Same route | Same route |

**Scale for one BWRX-300 (illustration, assumptions labelled).** 50,000 m³ of concrete (ostroleka2023_pis) × 2.4 t/m³ (assumed density) = **120,000 t**. If "a few per cent" means 2–5% (assumption), **2,400–6,000 t** would be radioactive concrete waste at decommissioning, and the rest clearable. This is why the trace-element content of a new binder matters at end of life, not only its CO₂.

**Synthesis (R1.3).** The CO₂ case for LC³ is strong and independent of who measures it: −29% per m³ at matched M50 (Pillai) and a −37% median per tonne of cement across five estimates. The weak points sit elsewhere: (i) self-consolidating flow in congested DP-SC modules; (ii) heat in thick sections (no LC³ data); (iii) qualification against a topical report written for conventional SCC. Slag avoids (ii) and (iii) but faces supply decline, which is why the report keeps LC³ as the target and slag as the fallback.

## 4. Life cycle of structural and reactor steel
| Stage | Structural and DP-SC plate, rebar | Nuclear-grade plate and forgings (RPV, nozzles) |
|---|---|---|
| **Quantity** | 14,000 t steel per unit (all steel, Ostrołęka PIS); the Unit 1 DP-SC basemat module alone is about 952 t (opg_basemat_story) | RPV made by BWXT, Cambridge, Ontario (GEV_2025_BWXT_RPV). Grade and forging source not found [gap] |
| **Extraction and making** | BF-BOF (ore plus coking coal) **2.33 t CO₂/t**; scrap-EAF **0.68**; DRI-EAF **1.43** (2022–24 means; worldsteel_2026_CO2). Ontario is moving to EAF (Algoma blast furnace closed 18 Jan 2026) | Low-alloy steel (ASME SA-508 type). ASME limits Cu 0.2%, P 0.025%, S 0.025%, which the CNSC calls too loose to prevent irradiation embrittlement (CNSC_2023_EnvDegradation) |
| **Service** | Corrosion and composite action with the infill | Neutron embrittlement driven by Cu and P; RG 1.99 assumes 0.35 wt% Cu if unknown (NRC_RG199). Environmental degradation in small LWRs is reviewed by the CNSC (CNSC_2023_EnvDegradation) |
| **End of life** | Most structural steel is clearable and recyclable. Plate near the core is activated (Co-60 from cobalt impurities) [no number sourced] | RPV internals and vessel are activated, likely ILW/LLW (class depends on activity; CNSC_WasteClasses) |

**Why scrap-EAF is not a drop-in for nuclear grades.** Copper from wiring and motors accumulates in scrap and can't be removed in the melt. Above about 0.1 wt% it causes hot shortness, and producers dilute it with DRI or pig iron (Daehn_2017). Copper is also the main irradiation-embrittlement element in vessel steel (NRC_RG199). So the low-carbon route for nuclear plate is **DRI-EAF or diluted scrap with controlled residuals**, not ordinary scrap-EAF.

**Illustrative stake (for the lca-analyst to reconcile, not for the report as is).** 14,000 t × (2.33 − 0.68) = **23,100 t CO₂** per unit, if all of the plant's steel moved from BF-BOF to scrap-EAF crude-steel averages. This is a theoretical ceiling: it ignores fabrication and the nuclear-grade limits above. It is about 6× the LCA's own whole-plant steel bound of 3,714 t (`results/lca_scenarios.md`, built on the old quantity model). The gap is probably the 14,000 t quantity combined with route-average factors, but it needs checking before §10 quotes any steel figure. Steel remains outside C1.

## 5. RB.7: future material properties and processes needed
| Need | Why it matters to our initiative | What the evidence says now | Next step and owner |
|---|---|---|---|
| **1. Qualified SCC LC³ for DP-SC infill** | C1 depends on it; Units 2–4 design window, with approval expected in 2028 (ANS_2026_Darlington) | Flow: higher SP demand (UniBw; IITM), with admixture patents emerging (Sika; BASF/CR&T Pat_US11939273). Heat: **no data**. Shrinkage: governs faceplate composite action (route brief). Durability: chloride much better, carbonation worse but enclosed. Strength −5.5% at M50 (Pillai). Calcined clay has no nuclear precedent (route brief) | Mock-up DP-SC panels with LC³ SCC (flow through diaphragm holes, adiabatic temperature rise, shrinkage, push-out tests), timed to CNSC hold points; GEH, OPG, cement supplier |
| **2. Low-activation binder data** | Sets the decommissioning waste volume; Eu-152 limits clearance | Eu-152 and Co-60 dominate activated concrete; no data for calcined clay | Measure Eu and Co in candidate clays during qualification (cheap; adds a decommissioning criterion) |
| **3. Low-residual EAF/DRI nuclear plate** | Steel emits more than concrete in the LCA; Ontario mills are going EAF | Scrap-EAF 0.68 vs BF-BOF 2.33 t/t; Cu control limits scrap use in irradiated steel | Qualify DRI-fed EAF plate to ASME grades for non-RPV structures first (inference) |
| **4. Laser enrichment** | Enrichment is the most concentrated fuel-cycle step (HHI 3,009, Russia about 41–43%) | GLE (Silex 51%, Cameco 49%) Paducah licence application accepted 4 Aug 2025; up to 8 wt%; tails re-enrichment; Cameco to take all output (NRC_GLE_PLEF; Silex_ASX_2026_Offtake). Banned in Australia by EPBC s140A and ARPANS s10 | Track the NRC licence (company expects early 2027). Energy per SWU not sourced [gap] |
| **5. Waste forms** | SMRs may produce 2–30× more waste volume per unit energy for three non-BWRX designs (Krall_2022, contested) | ANSTO Synroc: HIP ceramic (1,000 °C, 30 MPa) with large volume reduction vs cement, pre-commissioning (ANSTO_Synroc); Canada's used fuel goes to the NWMO deep repository (NWMO_2024_SiteSelection) | Australian capability (Synroc) as an export of know-how, not a reason to build (R4.3) |

## 6. Translation to practice
- The binder decision is a **qualification problem with a deadline**, not a chemistry problem. LC³'s CO₂ benefit is settled, but its SCC behaviour in DP-SC modules is not. Test panels must report before the Units 2–4 design freeze.
- Adding trace-element (Eu, Co) limits to the binder specification ties C1 to end-of-life waste, a link the report can claim as indirect (R4.2).
- Slag stays the fallback, but its supply is tied to Ontario blast furnaces that are closing. Over a 60-year fleet horizon that favours LC³.

## 7. Numbers table
| Quantity | Value | Source or working |
|---|---|---|
| LC³-50 composition | 50 / 30 / 15 / 5% clinker / clay / limestone / gypsum | Zunino_LC3_slides |
| Clay calcination | ≈ 800 °C (700–850 °C) | Zunino_LC3_slides; Li et al. 2019 |
| M50 concrete GWP | OPC 380, LC³ 270 kg CO₂e/m³ (−28.9%) | pillai2019_lc3; (380−270)/380 |
| M50 28-day strength | 60.0 vs 56.7 MPa (−5.5%) | pillai2019_lc3 |
| LC³ cement GWP reduction | 30–43%, median 37% | lc3_reduction_leads |
| Slag EPD | 146.6 kg CO₂e/t (93.4 plant) | sca_epd |
| Limestone cap, Type IT | ≤ 15% | Hooton_2023_ACI |
| LC³ chloride diffusion | ≈ 1/10 of OPC | LC3_Chloride_2025 |
| Steel route intensity | BF-BOF 2.33–2.34; scrap-EAF 0.67–0.69; DRI-EAF 1.36–1.47 t CO₂/t | worldsteel_2026_CO2 |
| SA-508 limits | Cu 0.2, P 0.025, S 0.025 wt% | CNSC_2023_EnvDegradation |
| Cu hot-shortness threshold | ≈ 0.1 wt% | Daehn_2017 (via review) |
| Eu-152 depth above clearance | ≈ 35 cm | Greifswald_Activation |
| Concrete mass, one unit | 120,000 t | 50,000 m³ × 2.4 t/m³ (assumed) |
| Radioactive concrete at EOL | 2,400–6,000 t | 2–5% (assumed reading of "a few per cent") |
| Steel route switch ceiling | 23,100 t CO₂/unit | 14,000 × (2.33−0.68); not for citation until reconciled |

## 8. Open gaps
- LC³ adiabatic heat of hydration and shrinkage in SCC: none found. **This is the key RB.7 data gap.**
- NEDO-33926 §6.2.1 cement-type limits (not opened).
- RPV grade, forging source, and activated-steel waste class for the BWRX-300.
- Eu and Co contents of calcined clays; GGBFS chloride data (not sourced here).
- The 23,100 t vs 3,714 t steel gap (to the lca-analyst).
- Every key above is unopened: the 2.4 t/m³ density and the 2–5% reading are assumptions.
