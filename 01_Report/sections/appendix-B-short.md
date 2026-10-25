Rubric coverage: RB.5, R2.4, R2.7, R3.1, R3.6, R3.8 (also supports R2.1, R2.3, R4.3, RB.6)

## Appendix B. Policy, economics and supply calculations

Each subsection gives the formula, key inputs and result. Scripts are in `03_LCA_Calculations/scripts/` (`law_timelines.py`, `hhi.py`, `displacement.py`, `schedule_value.py`, `same_money.py`, `mcda.py`, `social_licence.py`). Scores marked "judgement" are our own, not sourced.

### B1 Legal and political pathway
Three laws bar an SMR at Liddell: *EPBC Act 1999* (Cth) s 140A; *ARPANS Act 1998* (Cth) s 10(2); *Uranium Mining and Nuclear Facilities (Prohibitions) Act 1986* (NSW) s 8. Each has a different veto holder (Commonwealth Parliament, NSW Parliament), plus the site owner AGL.

Senate arithmetic (Parliament of Australia, 2026; 76 seats):
- Majority = ⌊76/2⌋ + 1 = **39**.
- Largest pro-repeal bloc = Coalition 27 + One Nation 4 + Babet 1 = 32 (the last two are assumptions); shortfall = 39 − 32 = **7**.
- Adding every other crossbencher gives 36–37, still short. Labor 30 + Greens 10 = 40 blocks.

NSW repeal bill: introduced 19 November 2025, passed the Legislative Council 6 May 2026, stalled in the Assembly, lapses 28 November 2026.

Darlington licensing (Canadian Nuclear Safety Commission, 2021; 2025; 2026a; 2026b): application 31 October 2022 to licence to construct 4 April 2025 = 886 days ÷ 30.44 = **29.1 months**; environmental assessment start (May 2007) to licence = **17.9 years**.

### B2 Supply concentration (HHI)
Formula: share s = 100 × q / Σq; HHI = Σ s²; N_eq = 10,000 / HHI. Enrichment worked example (World Nuclear Association, 2025): Rosatom 29,133 / 68,077 = 42.79%, squared 1,831; sum with Urenco 646, CNNC 410, Orano 121 and Other 0.3 = **3,009**.

| Stage (base year) | HHI | Without Russia | Without Russia and China | Russia's share |
|---|---:|---:|---:|---:|
| Mining, by country (2024; World Nuclear Association, 2026) | 2,341 | 2,546 | 2,686 | 4.5% |
| Conversion, by company (World Nuclear Association, 2024) | 2,111 | 2,674 | 3,615 | 20.2% |
| Enrichment, by company (2025) | 3,009 | 3,599 | 5,621 | 42.8% |

Thresholds (US Department of Justice and Federal Trade Commission, 2023; 2010): above 1,800 is highly concentrated (2023); 1,500–2,500 moderate and above 2,500 high (2010). Mining by company, from the top three firms only, is 851–1,384 (midpoint 1,118), below 1,800.

Darlington demand (four units; burnup 45 GWd/t, 3.8% enrichment, assumed): 195.6 t natural U and 137.7 tSWU a year, which is **3.2% of Urenco USA's 4,300 tSWU** and 0.20% of world capacity (68,077). The project is too small to move the HHI.

### B3 Routes to a licensable SMR in Australia
Three routes scored 1 (poor) to 3 (good) on four objectives (judgement; hand calculation).

| Route | Veto points | Regulator readiness | Durability | Social licence | Total (of 12) |
|---|---:|---:|---:|---:|---:|
| A. Commonwealth-owned plant | 1 | 3 | 1 | 1 | 6 |
| B. Federal law overriding states | 1 | 2 | 1 | 1 | 5 |
| C. Cooperative state repeal | 1 | 1 | 3 | 3 | 8 |

Weight test (one objective doubled): regulator readiness × 2 gives A 9, B 7, C 9; durability × 2 gives A 7, B 6, C 11. Route B ranks last throughout. C1 levers (enforceability, speed, low risk; of 9): OPG specification 8, equity milestone 8, Ontario shareholder direction 7.

### B4 Displacement
Formulae: E = 300 MW × 8,760 h × 0.90 = 2,365,200 MWh/yr; avoided in year y = E × (EF_grid − EF_SMR) / 10⁶ t, with EF_SMR = 4.2 g/kWh (our Monte Carlo median).
- Static NSW grid (640 g/kWh; Department of Climate Change, Energy, the Environment and Water, 2025): 2,365,200,000 × (640 − 4.2) / 10⁶ = **1.50 Mt a year**.
- Static Ontario average 2024 (73.8 g/kWh; The Atmospheric Fund, 2025): 0.165 Mt a year; marginal (343 g/kWh): 0.80 Mt.
- Cumulative to 2050: Darlington Unit 1 from 2030 = **1.01–6.80 Mt**; Liddell from 2040 = **0.67–3.85 Mt** (Step Change proxy to slow transition); frozen NEM = 16.54 Mt.
- Liddell example: 2,365,200,000 × (30 − 4.2) / 10⁶ = 61,022 t a year; × 11 years = 671 kt.

Grid trajectory, start year and post-coal floor dominate; the SMR's own life-cycle value moves the result by a few per cent.

### B5 Value of schedule
Formulae: daily output D = E / 365 = 6,480,000 kWh; gross loss per day = D × (EF_grid − EF_SMR) / 10⁶; break-even days = saving / loss per day.
- Ontario average (2035 factor 33.4 g/kWh): 189 t a day, so C1's 2,200 t is cancelled by **11.6 days** (net basis 18.5).
- Ontario marginal declining: 1,296 t a day, **1.7 days**.
- Units 2–4 saving (6,600 t) against delay to one unit: 34.9 days (average), 5.1 days (marginal).
- Carbon value of C1, Units 2–4: 6,600 t × C$95/t = C$0.63 m (C$0.76 m at C$115; Environment and Climate Change Canada, 2026).
- One-month slip of Units 2–4: deferred output 591,300 MWh × C$149 = C$88 m (Ontario Power Generation, 2026b); carrying cost on C$13.2 bn at 3–10% = C$33–110 m. Ratio to C1's carbon value: **29–175 times**.

### B6 Same money
Formulae: CRF = r(1 + r)ⁿ / ((1 + r)ⁿ − 1) = 0.0806 (7%, 30 years); energy ratio = SMR LCOE / renewables LCOE.
- Inputs (Graham, Hayward and Foster, 2024, as reported): SMR A$306/MWh (230–382), firmed renewables A$107/MWh (89–125), 2030; Darlington C$20.9 bn (Government of Ontario, 2025) at A$1.119 per C$.
- Energy ratio = 306 / 107 = **2.9×**; the same annual spend (A$0.72 bn) buys 6.8 TWh against 2.37 TWh.
- Capital only: C$5.225 bn × 1.119 × 0.0806 = A$471 m a year ÷ 2,365,200 MWh = **A$199/MWh**, buying 1.9× the energy.
- CO₂e avoided to 2050, renewables ÷ SMR, Liddell from 2040: 5.7× (frozen grid), 10.9× (slow transition), 26.0× (Step Change); range across cases tested 4.9–26.0×.
- Ontario average grid: SMR wins (−0.4×), because the grid falls below the renewables' assumed 30 g/kWh.

### B7 Multi-criteria analysis
Method (Dodgson et al., 2009): min–max normalisation s = (x − worst) / (best − worst); total T = 100 × Σ w_c s_c. Seven criteria: life-cycle CO₂e, CO₂e avoided per dollar, cost, first-power year, supply HHI, social licence, legal feasibility (last two judgement).

Worked example (SMR, equal weights): 0.99998 + 0.0921 + 0.0001 + 0.4545 + 0.5298 + 0 + 0 = 2.0766; T = 100 × 2.0766 / 7 = **29.7**.

| Weight set | Status quo | SMR | SMR + C1 | Firmed renewables |
|---|---:|---:|---:|---:|
| W0 equal | 52.4 | 29.7 | 29.7 | 80.1 |
| W1 climate and cost | 41.7 | 24.0 | 24.0 | 85.9 |
| W2 firm and sovereign | 60.0 | 43.6 | 43.6 | 63.7 |
| W3 host community | 55.0 | 20.4 | 20.4 | 89.3 |

Robustness: ±50% weight tests change first place in 2 of 56 cases (both in W2); under 20,000 random weight sets renewables rank first in 85.4%. C1 changes the SMR's life cycle from 4.200 to 4.1845 g/kWh (2,200 / 1.419 × 10¹¹ kWh = 0.0155 g/kWh), under 0.005 point of score.

### B8 Social licence and stakeholder working
- **Deaths avoided:** output 2.365 TWh a year × (death rate displaced − nuclear's 0.03 per TWh; Ritchie, 2020; Markandya and Wilkinson, 2007). Black coal (24.62): 2.365 × 24.59 = **58.2 a year** (upper bound); gas (2.82): **6.6 a year**.
- **Power-weighted stance** = Σ(power × stance) / Σ(power). Darlington: 46 / 43 = **+1.07**; Liddell: −37 / 36 = **−1.03** (scores are judgement).
- **Siting routes** (scored 1–3 on five criteria, judgement): Commonwealth-led 7; volunteer host 11; with First Nations equity 11; no SMR (firmed renewables) 14 of 15.
- **Financing** of C$20.9 bn (Government of Ontario, 2025): Canada Growth Fund 2.00 (9.6%), Building Ontario Fund 1.00 (4.8%), Canada Infrastructure Bank 0.97 (4.6%), Williams Treaties First Nations 0.70 (3.3%); remainder 16.23 (77.7%) from OPG's balance sheet, a subtraction rather than a reported figure.
