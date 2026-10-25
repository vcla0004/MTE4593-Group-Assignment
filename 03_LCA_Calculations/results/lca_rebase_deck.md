Rubric coverage: R2.1, R2.2, R2.3, R2.4, R2.5, R2.6, R2.7, RB.5, RB.6

# LCA re-based on the team deck's case (25/10/2026)

lca-analyst, for Victor (Sam's red sections; Sam can review tonight). This replaces the 21/10 bottom-up model as the **main case** for §6, Appendices A and C, F1–F5 and T6. The bottom-up model (20,700 m³) is kept as a **cross-check**. The method is a screening LCA that follows ISO 14040/44 principles and has not been critically reviewed. The functional unit is 1 MWh net at the grid connection. The boundary is cradle to grave, GWP100.

**Granta EduPack was NOT run.** Only Sam can run it, and no Granta output exists. No number here or in F1–F5 comes from Granta. The set-up, with the new whole-plant masses, is in `granta_inputs.md` (re-base note).

**Verification.** Ostrołęka PIS (2023) and Pillai et al. (2019) were searched on 25/10. Both documents exist, but neither table could be opened: the mepr.gov.ua and IITM copies don't resolve from this session. Both stay **[TO VERIFY]** (`02_Research/sources_lca.md`). Every other input keeps its 21/10 status.

Reproduce: `python3 -I 03_LCA_Calculations/scripts/lca_baseline.py`, then `lca_scenarios.py`, then `lca_uncertainty.py` (about 5 s; seed 20261021; 20,000 draws). All inputs are in `parameters_lca.yaml`: the new section B0, plus the old sections A and C–H.

## 1. What changed and why

| Item | Main case (new) | Cross-check (old bottom-up) |
|---|---|---|
| Concrete per unit | **50,000 m³** (Ostrołęka PIS Table 14, p. 83; range 40,000–60,000, ±20% assumption) | 20,700 m³ (69 m³/MWe ESBWR × 300) |
| Steel per unit | **14,000 t** (same table; 11,200–16,800) | 9,900 t (33 t/MWe) |
| Concrete factor, S0 | **Pillai OPC 380 kg CO₂e/m³** for all plant concrete (330–420) | Binder-level: 854 kg/t GU × 350 or 450 kg/m³ + 30 → 329 / 414 kg/m³ |
| Steel factors | Unchanged: rebar 0.97 t/t (CRSI EAF; 0.89–1.99), plate/structural/equipment 1.73 t/t (BCCA; 1.22–2.50); rebar = 0.15 t/m³ × concrete = 7,500 t, plate = 6,500 t | Same factors; rebar 3,105 t, plate 6,795 t |
| C1 | **LC³ on 20 / 40 / 60% of plant concrete** (non-safety works first; DPSC infill only if qualified), cut 1 − 270/380 = 28.9% (Pillai), so **110 kg CO₂e/m³** | LC³ (37% binder cut) in DPSC infill + forebay (13,081 m³) |

**Concrete factor choice: Pillai's OPC 380 kg CO₂e/m³, not the old binder-level factors.** Three reasons:
- The C1 saving is defined as Pillai's 380 − 270. A baseline on a different per-m³ basis (329 or 414) would mix two studies in one subtraction. With 380 the saving is a clean fraction (28.9%) of the same factor.
- 380 sits between the old model's conventional (329) and SCC (414) mixes, and between the CRMCA Ontario 334 and benchmark 417 leads. Those values set the range 330–420.
- It keeps the concrete stage on one cited source. Its weakness: it is an Indian M50 mix, not an Ontario one (caveat 2).

Steel keeps the 21/10 North American factors, because Pillai gives none. The construction uplift (+50%, 25–150%) still covers other materials, site energy and any equipment outside the 14,000 t.

## 2. Inventory and construction (one unit, mode case: all inputs central)

| Item | Quantity | Factor | t CO₂e |
|---|---|---|---|
| C1-eligible concrete (40%) | 20,000 m³ | 380 kg/m³ | 7,600 |
| Other plant concrete | 30,000 m³ | 380 kg/m³ | 11,400 |
| Rebar | 7,500 t | 0.97 t/t | 7,275 |
| Plate, structural and equipment steel | 6,500 t | 1.73 t/t | 11,245 |
| Transport to site | concrete 15 km, steel 500 km | 0.10 kg/t-km | 880 |
| Other materials and site energy | +50% | | 19,200 |
| **Construction** | | | **57,600 (0.406 g/kWh)** |

Concrete and steel are now about equal: 19,000 t against 18,520 t CO₂e. In the old model steel was twice concrete. Resource use: 0.85 kg concrete and 0.099 kg steel per MWh. Fuel is unchanged: 20.7 g natural U and 0.0146 SWU per MWh; four units need 196 tU and 138 tSWU a year.

## 3. Headline

| Basis | Life-cycle g CO₂e/kWh |
|---|---|
| **Monte Carlo median, 90% interval** | **4.40 (3.24–6.05)** (mean 4.49) |
| Mode case (all inputs at their most likely value) | 2.86 |
| Range of medians across conversion-heat assumptions | **3.51–4.40** (fixed 26 kWh/kg U: 3.51 (2.80–4.39); log-uniform: 4.11 (3.06–6.12); triangular: 4.40) |
| Cross-check (bottom-up 20,700 m³), same draws | 4.20 (3.05–5.86); mode 2.70 |

The re-base adds about **0.2 g/kWh** (+5%) to the median, all of it from construction. The headline still rests on the fuel inputs.

## 4. Stage shares and hotspots

| Stage | Mode case g/kWh (share) | Expected, MC mean g/kWh (share) |
|---|---|---|
| Fuel: mining and milling | 1.024 (35.8%) | 1.261 (**28.1%**) |
| Fuel: conversion | 0.127 (4.4%) | 1.105 (**24.6%**) |
| Back end | 0.560 (19.6%) | 0.651 (14.5%) |
| O&M | 0.330 (11.5%) | 0.390 (8.7%) |
| Fuel: enrichment | 0.272 (9.5%) | 0.355 (7.9%) |
| Construction: other materials and site energy | 0.135 (4.7%) | 0.221 (4.9%) |
| Decommissioning | 0.110 (3.8%) | 0.167 (3.7%) |
| Construction: concrete | 0.134 (4.7%) | 0.135 (3.0%) |
| Construction: rebar | 0.051 (1.8%) | 0.077 (1.7%) |
| Construction: plate, structural and equipment steel | 0.079 (2.8%) | 0.074 (1.6%) |
| Fuel: fabrication | 0.036 (1.3%) | 0.043 (1.0%) |
| Construction: transport | 0.006 (0.2%) | 0.009 (0.2%) |
| **Total** | **2.864** | **4.487** |

**Groups (expected basis):**
- Fuel front end 61.6%
- Back end and decommissioning 18.2%
- O&M 8.7%
- **Construction 11.5%** (0.515 g/kWh)

On the mode basis the shares are 50.9 / 23.4 / 11.5 / **14.2%**. Construction's share has a Monte Carlo median of 11.5% (P5–P95 7.2–17.8%). The old model gave 7.5%.

**Hotspots:**
1. Mining and milling (28%) is the biggest.
2. Conversion (25%) is an uncertainty hotspot: it is only 0.13 g/kWh at its most likely value.
3. Back end (15%).

All concrete is 3.0–4.7% of the total. The C1-eligible concrete is 1.9% of the mode-case total.

## 5. C1 saving (LC³, Pillai 380 → 270 kg CO₂e/m³)

| Eligible share | m³/unit | t CO₂e/unit | Units 2–4 t | Share of life cycle: mode case | Share of life cycle: Monte Carlo median (P5–P95) | Clinker avoided t/unit (indicative) |
|---|---|---|---|---|---|---|
| 20% | 10,000 | **1,100** | 3,300 | 0.27% | **0.18%** (0.11–0.28) | 1,470 |
| **40% (central)** | 20,000 | **2,200** | **6,600** | 0.54% | **0.36%** (0.23–0.56) | 2,940 (Units 2–4: 8,820) |
| 60% | 30,000 | **3,300** | 9,900 | 0.81% | **0.54%** (0.34–0.84) | 4,410 |

- The 20/40/60% rows hold eligibility fixed. The Monte Carlo, with eligibility drawn as triangular 0.2/0.4/0.6 and the cut, volume and factor all varying, gives **2,217 t/unit (1,375–3,294)**, **6,651 t for Units 2–4 (4,124–9,881)** and **0.35% of the life cycle (0.19–0.61%)**. That is 0.0155 g/kWh at the central case.
- **Clinker** uses the old 350 kg/m³ binder and clinker factors of 0.92 (GU) and 0.50 (LC³). Pillai's M50 binder content is [TO VERIFY], so the clinker figures are indicative only.
- **Slag fallback (S1, 40% slag on the same 20,000 m³):** 2,288 t at the mode case; median 2,140 (1,310–3,238). LC³ beats slag in only **55%** of draws (LC³ minus slag: median +54 t, −588 to +766). This repeats the old finding that "slag nearly matches LC³", now more strongly.
- **Other scenarios** (Monte Carlo median, with the mode case after it):
  - S2b, LC³ on eligible concrete plus slag in all other concrete (upper bound): 5,517 t (4,346–6,841); mode 5,633.
  - S3 like-for-like steel, 953 t basemat plate plus 1,000 t forebay rebar (unchanged): 940 t (415–1,580); mode 566.
  - S3 whole-plant steel at EAF sections factors, the upper bound on 14,000 t: **6,428 t (2,521–11,486); mode 3,915**.
  - S3 world-average steel: −9,914 t (mode −12,655).
- **Values that depend on C1** (from `c1_deck_case.md`, already on 2,200 t):
  - Break-even delay: 11.6–18.5 days on the average grid factor; 1.7–1.8 days on the marginal factor. Across the saving's 90% interval this becomes about 7–28 and 1.1–2.7 days.
  - Carbon value: C$0.21–0.25 m per unit; C$0.63 / 0.76 m for Units 2–4. That is about 0.005% of C$13.2 bn. One day of delay (C$1.8–2.9 m) costs 2.4–4.6 times C1's whole carbon value.
  - Break-even premium: C$10.4–12.7/m³.

## 6. Tornado (F3) and Monte Carlo (F4)

- **Life-cycle intensity, ranked swings (mode case 2.86):**
  - Conversion heat 2.86 → 5.53 (2.67)
  - Mining factor 2.43 → 3.82 (1.39)
  - Back end 2.58 → 3.41 (0.83)
  - Burnup 3.28 → 2.60 (0.68)
  - Enrichment 2.69 → 3.36 (0.66)
  - O&M (0.50)
  - Enrichment-plant grid (0.43)
  - Construction uplift 2.80 → 3.13 (0.34)
  - Centrifuge energy (0.33)
  - Design life 3.07 → 2.76 (0.30)
- **Construction inputs:**
  - Plant steel 2.81 → 2.92 (0.11), plate factor (0.09), rebar factor (0.09).
  - Plant concrete 2.84 → 2.89 (0.06) and the OPC factor 2.84 → 2.89 (0.05): no concrete input moves the total by more than 0.06 g/kWh.
- **C1 saving, ranked swings (mode case 2,200 t):**
  - Eligible share 1,100 → 3,300
  - LC³ cut (0.22–0.39) 1,672 → 2,964
  - Plant concrete 1,760 → 2,640
  - OPC factor 1,911 → 2,432

  No other input moves the saving.
- **Set-up:** 45 ranged inputs are drawn independently (triangular, except net output, which is uniform 300–315). 29 of them affect the main case; the other 16 are bottom-up-only and drive the cross-check on the same draws. The cross-check clip rule applied in 696 of 20,000 draws (3.5%).

## 7. Comparison with published values (RB.6; benchmarks [TO VERIFY], `parameters_lca.yaml` section G)

| Source | g CO₂e/kWh | Ours vs it |
|---|---|---|
| **This study** | 4.40 median (3.24–6.05); range of medians 3.51–4.40 | |
| UNECE (2021), nuclear | 5.1–6.4 | Median below the range; our 90% interval overlaps it |
| IPCC AR5 WGIII Annex III (Schlömer et al., 2014) | 3.7 / 12 / 110 (min / median / max, as commonly quoted; not confirmed) | Near the minimum, well below the median. F5 draws this row only once it is verified |
| NREL harmonisation (Warner and Heath, 2012), light-water reactors | median 12 | About a third of it |
| EDF R&D (2024), French fleet | 3.7 (2.9–4.6) | Overlaps |
| Gibon and Hahn Menacho (2023), global 2020 | 6.1 | Below |
| Carless et al. (2016), Westinghouse SMR | 9.1 (5.9–13.2) | Below |
| Coal / gas combined cycle (UNECE, 2021) | 751–1,095 / 403–513 | Ours is about 170–250× and 90–120× lower (at 4.40) |

**Why ours is lower:**
1. High-grade Saskatchewan ore: our mining is 1.0–1.3 g/kWh, against about 2.8 at global-average grades (Gibon). This explains most of the gap to UNECE and Gibon.
2. Centrifuge-only enrichment, against the diffusion plants in older harmonised sets.
3. An energy-only fuel inventory with cut-offs (chemicals, cladding, upstream gas, capital goods), which biases the result low.
4. A 60-year life and CF 0.90. At 40 years the mode case rises from 2.86 to 3.07.

**What the re-base fixes:** construction is now **0.41 g/kWh (mode) and 0.50 (median; 0.35–0.74)**. That is close to EDF's large-reactor construction of about 0.59 (16% of 3.7). The old model's "construction possibly underestimated" reason (0.24–0.32) has largely closed. The SMR scale penalty now shows up: 167 m³ concrete per MWe, against 69 for the ESBWR and 138 for the ABWR (Peterson et al., 2005).

## 8. Key caveats

1. **Both new sources are unopened** ([TO VERIFY]). The headline moves little, because construction is about 11%. The C1 saving, however, scales one-for-one with the 50,000 m³ and with Pillai's 110 kg/m³.
2. **Pillai's factors are for Indian M50 mixes.** Ontario GU cement (854 kg/t) and a nuclear SCC mix may differ. The 330–420 and 22–39% ranges are our assumptions.
3. **Whether Ostrołęka's 50,000 m³ / 14,000 t is for the whole site or the nuclear island, and whether it includes equipment steel, is unknown.** If equipment is excluded, the uplift covers it. Darlington's 35 m shaft, forebay and tunnels may differ.
4. **The eligible share (20–60%) is a scenario, not data.** It is the largest driver of the saving.
5. **The S0 counterfactual still applies.** If OPG's mixes already contain slag, LC³'s increment on the 40% eligible concrete is about −90 t at the mode case. In other words, it is within noise (`lca_scenarios.md`).
6. **The model structure is not varied.** Inputs are drawn independently and the conversion-heat shape matters (range of medians 3.51–4.40).

## 9. Old → new: every number §6, Appendix A and Appendix C quote

Tables A3–A8, C1 (tornado rows), C2–C4 and T8 should be **re-copied whole** from `lca_baseline.md`, `lca_scenarios.md`, `lca_uncertainty.md`, `lca_tornado.csv` and `lca_montecarlo_summary.csv`. The rows below cover every number quoted in prose, captions and T6, plus the key table cells.

| Where | Quantity | Old (21/10 bottom-up) | New (main case) |
|---|---|---|---|
| §6 lead, 6.4, 6.5, C4, C5, F4 cap. | Life-cycle median (90% interval) | 4.2 (3.0–5.8); 4.18 (3.05–5.85) | **4.4 (3.2–6.1); 4.40 (3.24–6.05)** |
| §6 lead, 6.4, 6.5, C5 | Median with conversion heat at its central value | 3.3 (2.6–4.2); 3.31 | **3.5 (2.8–4.4); 3.51** |
| 6.4, C2 | Median, log-uniform conversion heat | 3.9 (2.9–5.9); 3.91 | **4.1 (3.1–6.1); 4.11** |
| §6 lead, 6.4, 6.5, C5 | Range of medians | 3.3–4.2 | **3.5–4.4** |
| 6.2, 6.4, F2/F3 cap., C1, C5 | Mode case | 2.7; 2.70; 2.701 | **2.9; 2.86; 2.864** |
| F2 cap., C1, C3 | Expected (MC mean) | 4.3; 4.28; 4.279 | **4.5; 4.49; 4.487** |
| C5 | Mean − mode gap; conversion part | +1.58; +0.97 | **+1.62; +0.98** |
| §6 lead, 6.2, C3 | Fuel front-end share (expected) | nearly two-thirds; 64%; 64.2% | **about 62%; 61.6%** |
| A8 | Fuel front end, mode case | 1.46 g/kWh (54%) | 1.46 (**50.9%**) |
| §6 lead, 6.2, C3, C6 | Construction share (expected) | about 7.5%; 0.321/4.279 | **11.5%; 0.515/4.487** (MC median 11.5%, 7.2–17.8) |
| A7, A8, 6.5 T9 | Construction, mode case | 34,381 t; 0.24 g/kWh (9.0%) | **57,600 t; 0.41 g/kWh (14.2%)** |
| 6.5 T9 | Construction range | 0.24–0.32 g/kWh | **0.35–0.74 (median 0.50)**: now close to EDF's ~0.59; edit the T9 row |
| 6.2, T6, A3, C2, C4 | Plant concrete per unit | 20,700 m³ (15,050–36,521) | **50,000 m³** (input range 40,000–60,000; MC 43,224–56,772) |
| 6.2, 6.3 f4, T6, A3, A7 | Plant steel per unit | 9,900 t (33 t/MWe) | **14,000 t** |
| T6 row | Whole-plant concrete; steel | 69 m³/MWe (34.5–138); 33 t/MWe (16.5–46), Peterson 2005 | **50,000 m³ (±20%); 14,000 t (±20%), BWRX-300 Ostrołęka sp. z o.o. (2023)** |
| T6 rows | Binder contents; GU 854; LC³ cut 37% (30–43%) | Main-case inputs | **Replace with: OPC concrete 380 kg CO₂e/m³ (330–420) and LC³ 270, cut 28.9% (22–39%), Pillai et al. (2019); eligible share 40% (20–60%), assumption.** Move the binder rows to the cross-check |
| 6.2, A3, C2 | C1 target concrete | 13,100 / 13,081 m³ (63% of plant); MC 12,216–15,606 | **20,000 m³ (40% eligible; 10,000–30,000)** |
| 6.2, A3 | DPSC geometry (3,226 + 5,855 + 4,000 m³; 9,081 m³; "69% of target") | Main case | **Cross-check only** |
| A3 | Rebar; plate | 3,105 t; 6,795 t | **7,500 t; 6,500 t** |
| A7 | Concrete; steel t CO₂e | 7,584; 14,767 ("steel about twice concrete") | **19,000; 18,520 ("about equal")** |
| A7 table | Transport; uplift | 570; 11,460 | **880; 19,200** |
| 6.2, A6 | Concrete; steel per MWh | 0.35; 0.070 kg | **0.85; 0.099 kg** |
| 6.2, A8, C3 | Mining (expected) | 1.26 g/kWh (29%); 1.258 (29.4%) | **1.26 (28%); 1.261 (28.1%)** |
| 6.2, C3 | Conversion (expected) | 1.09 (26%); 1.094 (25.6%) | **1.10 (25%); 1.105 (24.6%)** |
| 6.2, C3 | Back end (expected) | 0.65 (15%); 0.654 (15.3%) | **0.65 (15%); 0.651 (14.5%)** |
| A8 table | Total t per unit, mode case | 383,243 | **406,462** |
| A8 | Mode-case shares: mining / back end / O&M / enrichment / conversion | 37.9 / 20.7 / 12.2 / 10.1 / 4.7% | **35.8 / 19.6 / 11.5 / 9.5 / 4.4%** |
| A8 | Grouped, mode case | fuel 54.0, back end and decommissioning 24.8, O&M 12.2, construction 9.0% | **50.9 / 23.4 / 11.5 / 14.2%** |
| 6.2, A8 | C1 target concrete share, mode case | 1.3% (5,078 t; 0.036 g/kWh) | **1.9% (7,600 t; 0.054 g/kWh)** |
| §6 lead, 6.3, T8, A6, C4, F3/F4 cap. | C1 saving per unit | 1,740 / 1,734 (mode); 1,742 (1,387–2,153) | **2,200 (mode; 1,100–3,300 at 20/60%); 2,217 (1,375–3,294) MC** |
| §6 lead, 6.3, T8, A6, C4 | Units 2–4 | 5,200 / 5,201; 5,225 (4,161–6,458) | **6,600 (3,300–9,900); 6,651 (4,124–9,881) MC** |
| 6.3, A6 | Clinker avoided per unit; Units 2–4 | 2,304; 6,900 / 6,913 | **2,940; 8,820 (indicative)** |
| A6 | Clinker per MWh; per MWe | 0.016 kg; 7.7 t | **0.021 kg; 9.8 t** |
| §6 lead, 6.3 f2, T8, C4, C5 | C1 share of life cycle | about 0.3%; 0.29% (0.18–0.46) MC; 0.45% mode; 0.29–0.37% across conversion cases | **0.36% (0.23–0.56) at 40% fixed; 0.35% (0.19–0.61) with eligibility drawn; 0.54% mode; 0.18 / 0.36 / 0.54% at 20/40/60%; 0.36–0.45% across conversion cases** |
| 6.3 f2 | g/kWh saved | about 0.01 | **0.016** |
| A6 | Saving as % of target concrete | 34.1% | **28.9%** |
| 6.3, A6 structures table | DPSC 1,291 t; forebay 442 t | Main case | **Cross-check only** (main case has no per-structure split) |
| T8, C4 | S1 slag | 1,642 (1,205–2,113); mode 1,552; 0.28% (0.17–0.44); mode 0.41% | **2,140 (1,310–3,238); mode 2,288; 0.34% (0.18–0.60); mode 0.56%** |
| T8 | S1 Units 2–4; clinker | 4,657; 2,019 / 6,057 | **6,865; 2,576 / 7,728** |
| T8, C4 | S2b | 2,746 (1,809–4,107); mode 2,488; 0.46% (0.26–0.80); 7,464; 3,286 / 9,857 | **5,517 (4,346–6,841); mode 5,633; 0.89% (0.57–1.36); 16,898; 6,804 / 20,412** |
| 6.3 f3, C4 | LC³ − slag; P(LC³ > slag) | 97–181 t (−343 to +574); 64% | **+54 t median, −88 mode (−588 to +766); 55%** |
| 6.1, 6.3 f3, A6 | LC³ gain if S0 already has slag | about 100–180 t | **About −90 t at 40% slag (within noise)** |
| T8, 6.3 f4, C4 | S3 like-for-like | 566 (MC 941; 404–1,581); 0.15% / 0.16% | **566 (MC 940; 415–1,580); 0.14% mode / 0.15% MC** |
| 6.3 f4 | LC³ ÷ like-for-like steel | about 3× mode, 1.9× median | **3.9× mode, 2.4× median** |
| T8, 6.3 f4, A6, C4 | S3 upper bound, whole-plant steel | 3,714 (MC 4,731; 1,713–9,084); 11,142; 0.97% / 0.79% | **3,915 (MC 6,428; 2,521–11,486); 11,745; 0.96% / 1.03%** |
| 6.3 f4 | Upper bound vs LC³ | about twice LC³ | **1.8× mode, 2.9× median** |
| T8, 6.3 f4, C4 | S3 world-average | −8,399 (MC −6,695); −25,198; −2.19% / −1.11% | **−12,655 (MC −9,914); −37,965; −3.11% / −1.56%** |
| 6.3 f1 | Concrete share of target-structure emissions (5,078 vs 2,619 t); 530 t wall swing | Main case | **Cross-check only.** In the main case the eligible concrete is generic, so recast f1 as: the saving exceeds the largest non-eligibility swing (LC³ cut, 1,672–2,964 t) |
| §6 lead, 6.3 f5 | Break-even delay, average / marginal | 9–15 (9.2–14.6) / 1.3–1.4 days; 7.3–18.1 / 1.1–1.8 across the 90% interval | **11.6–18.5 / 1.7–1.8 days; about 7–28 / 1.1–2.7** (`c1_deck_case.md`) |
| 6.3 f2, end of 6.3 | Carbon value per unit; Units 2–4 | C$0.16–0.20 m; C$0.49–0.60 m | **C$0.21–0.25 m; C$0.63–0.76 m** |
| 6.3 f2 | Share of C$13.2 bn; one day of delay ÷ value | 0.004%; 3–6× | **About 0.005%; 2.4–4.6×** |
| 6.3 f2 | LC³ break-even premium | C$12.6–15.2/m³ (5.5–6.6%) | **C$10.4–12.7/m³ (4.6–5.5%)** |
| 6.4, C1, A1 | Ranged inputs; parameters in YAML | 40; 59 | **45 drawn (29 affect the main case); 68** |
| 6.4, C2, C3 | Tornado: conversion heat; mining; back end | 2.70→5.37; 2.26→3.65; 2.42→3.25 | **2.86→5.53; 2.43→3.82; 2.58→3.41** |
| C1 table | Burnup; enrichment; O&M; enrichment-plant grid | 3.117→2.435; 2.530→3.193; 2.541→3.041; 2.466→2.893 | **3.281→2.599; 2.694→3.357; 2.704→3.204; 2.629→3.056** |
| 6.4, C2, C3 | Concrete inputs' maximum swing; steel | ≤0.07; steel intensity 0.17; uplift 0.20 | **≤0.06; plant steel 0.11; uplift 0.34** |
| 6.4, C3, F3 cap. | Saving drivers | LC³ cut 1,406→2,015; wall 1,464→1,995; binder 1,590→2,021; flow 1,438; ±20–25% | **Eligible share 1,100→3,300; LC³ cut 1,672→2,964; plant concrete 1,760→2,640; OPC factor 1,911→2,432**. Geometry and binder rows are cross-check only |
| C1 | Clip rule | 706 draws (3.5%) | **Cross-check only: 696 (3.5%)**; the main case never clips |
| C4 | Fuel front end MC; mining MC | 2.746 (1.590–4.272); 1.258 | **2.764 mean, 2.661 median (1.586–4.280); 1.261** |
| C4 | Construction MC | 0.321 (0.198–0.484) | **0.515 mean, 0.500 median (0.347–0.736)** |
| 6.5 | Gas and coal multiples | 100–120×; 180–260× | **90–120×; 170–250×** (at 4.40) |
| 6.5 T9 | 40-year life | 2.70 → 2.82 | **2.86 → 3.07** |
| 6.5 | Position against UNECE and the literature | below UNECE; low end | Unchanged in direction: median below UNECE, 90% interval overlaps it |
| F1 caption | Boundary text | "C1 target structures" | **"C1 eligible concrete (20/40/60% of plant)"**; the figure is redrawn |
| F2–F5 | Files | old | **Redrawn, same filenames, no embedded titles.** F5 adds the cross-check row (4.2, 3.1–5.9) |
| A9, A10 | Granta | set up, not run | **Still not run** (only Sam can); the A10 masses are unchanged for the target structures; a whole-plant option is in `granta_inputs.md` |

## 10. Gaps

- **Ostrołęka Table 14 and Pillai Table 2 need a human to open them** (P5). Until then the C1 numbers and the main inventory are [TO VERIFY].
- **Leroy's plant data are still placeholders:** net MWe, CF, design life, burnup, enrichment.
- **Granta not run.**
- The governing qualification code for the DPSC infill (CSA N287.2 covers concrete containment; the BWRX-300 uses a steel-plate composite) is not confirmed here. That belongs to §8.1.
