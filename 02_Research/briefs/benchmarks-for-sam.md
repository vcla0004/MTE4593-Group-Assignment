Rubric coverage: RB.6, R2.7, R2.5, R1.3, R1.4

# Benchmark brief for Sam: comparing our life-cycle result with the literature

For §6.5 (RB.6: "results compared with literature values, discrepancies explained"). Analyst run 1, 20/10/2026. Sam owns §6 and decides how to use this.

> **Status: none of the benchmark values below has been read in its primary source.** The proxy blocked unece.org, ipcc.ch and nrel.gov today. Values are from search summaries or secondary sources, tagged [TO VERIFY]. **Please open each primary yourself** (or ask Victor to) and fill the "Confirmed value" and "GWP basis" columns before citing. Full references are in `02_Research/sources_run1.md`.

## 1. The benchmarks

| Benchmark (source key) | Value for nuclear (lead) | What it covers | GWP basis | Where to check | Confirmed value |
|---|---|---|---|---|---|
| UNECE (2021), *Carbon Neutrality in the UNECE Region* (`unece2021`) | **5.1–6.4 g CO₂e/kWh** (several secondary sources agree) | Integrated cradle-to-grave LCA across 12 world regions, including the fuel cycle; large light-water reactor [TO VERIFY reactor type and size] | **Unknown: check the methods chapter** | Nuclear results chapter and the summary figure comparing technologies | [ ] |
| IPCC AR5 WGIII Annex III, Table A.III.2 (`ipcc2014_annex3`) | Commonly quoted as min 3.7, median 12, max 110 g CO₂e/kWh. **Not confirmed even in a search result**; treat as unknown | A review of published LCAs (the literature range, not a single new LCA) | **Unknown: check the Annex III methods text** | Table A.III.2, nuclear row; note which studies it draws on | [ ] |
| NREL (2021), *Life Cycle GHG Emissions from Electricity Generation: Update* (`nrel2021_lca`) | The 2012 harmonisation gives medians of **12–13 g CO₂e/kWh** (PWR, BWR) (secondary, CleanTechnica). 2021 median not yet seen | Harmonised estimates from about 3,000 LCAs (fact sheet) | **Unknown: check the fact sheet's notes** | Figure 2 (min, Q1, median, Q3, max by technology) | [ ] |
| Carless et al. (2016) and Geneski et al. (BWRX-300 Darlington, CNS proceedings) | Not searched in this run | SMR-specific LCAs (plan §4.1) | — | — | Gap |

**Comparators for §6.5 and §7 (UNECE, secondary):**
- Coal: 751 (IGCC) or 753 to 1,095 g/kWh (outlets disagree on the low end).
- Gas combined cycle: 403–513.
- Hydropower: 6–147.
- PV: 8–83.
- Wind: not found.

## 2. Why our number may differ, and how to explain it (R2.7, RB.6)

These are the usual reasons; state which apply.
1. **Boundary.** If the Granta Eco Audit covers only the initiative structures (concrete and steel) and the fuel cycle comes from literature, our total is a hybrid. Say which stages come from which source. A construction-only figure will sit far below every benchmark: the plan's §2.3 arithmetic puts the forebay concrete at roughly 0.1–0.2% of a UNECE-level life-cycle total. That is expected, not a discrepancy.
2. **Fuel cycle and enrichment.** The front end of the fuel cycle (mining, conversion, enrichment) is reported to be the largest share of nuclear's life-cycle emissions [TO VERIFY in UNECE]. The enrichment method (centrifuge vs legacy diffusion), the electricity mix powering enrichment, and ore grade all move it. Older studies in the IPCC and NREL sets include diffusion enrichment, which helps explain why their medians (about 12) sit above UNECE (about 5–6).
3. **SMR vs large reactor.** The benchmarks are mostly large reactors. An SMR may use more material per MWe, so the construction share can be higher [TO VERIFY with Carless et al. or Geneski et al.; no number found today].
4. **Denominator.** Capacity factor and design life change g/kWh in proportion. Use the same lifetime MWh as §7: 300 MWe × 8,760 × CF × life, from Leroy's sourced values. My scripts use CF 0.90 and 60 years as placeholders.
5. **GWP basis.** Record the GWP set (AR4, AR5 or AR6, GWP100) of each benchmark and of Granta's Eco Audit. For nuclear, most emissions are CO₂ from electricity and materials, so the choice of GWP set should matter much less than for gas, where methane leakage is significant. **Check the GWP basis; don't assume it.**
6. **Data year.** UNECE's inventories are recent; the IPCC (2014) and NREL (2012 harmonisation) sets draw on older studies.

## 3. Ontario grid factor for construction-stage electricity (your fix in plan §2.5 item 1)

Use the Ontario grid, not renewable electricity, for site electricity during construction (2025–2029).

| Option | g CO₂e/kWh | Year | Source key | Status |
|---|---|---|---|---|
| **Recommended central:** TAF annual average | 73.8 (the TAF webinar gives 73) | 2024 | `taf2025` | TO VERIFY |
| Ontario energy snapshot (deck value) | 53 | 2023 | `ontario_energy_snapshot` | TO VERIFY |
| Canada Energy Regulator | 35 | 2022 | `cer_ontario_profile` | TO VERIFY |
| High sensitivity: TAF marginal | 343 | 2024 | `taf2025` | TO VERIFY; definition ambiguous |

If Granta applies its own built-in grid mix for "Canada" or "Ontario", say which one and compare it with the table. Construction electricity is likely a small share of the total, so the low/high here is a sensible tornado bar rather than a headline issue.

## 4. Plugging your result into the displacement analysis

In `03_LCA_Calculations/parameters_run1.yaml`, set `smr_lca_g_per_kwh: value / low / high` to your central and range. Set `status` to `verified` and `source` to your results file. Then run:
```
python3 -I 03_LCA_Calculations/scripts/displacement.py
python3 -I 03_LCA_Calculations/scripts/schedule_value.py
python3 -I 03_LCA_Calculations/scripts/same_money.py
```
Also send your **C1 saving per unit (kt CO₂e)**. `schedule_value.md` turns it into "days of delay that would cancel the saving", which is the test for the schedule-neutral condition in the thesis.

From the sensitivity run: within the UNECE range, your life-cycle value changes the displacement results by under 5%. It becomes decisive only if it is well above the range (e.g. about 110 g/kWh) or on a nearly decarbonised grid. A result far from UNECE matters mainly for §6.5, not for §7.

## 5. Gaps

- None of the three benchmark values is confirmed in its primary. GWP basis unknown for all three.
- Carless et al. (2016) and Geneski et al. not yet located (plan §4.1).
- UNECE's wind range not found. It's needed for the firmed-renewables life-cycle value in `same_money.py`.
