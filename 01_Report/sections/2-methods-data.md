Rubric coverage: R2.4, R2.1, R2.6, R1.4, RB.5 (also supports R2.5, R2.7, R3.6, R5.1, R5.3)

<!--
CHANGELOG
- v1, 21/10/2026 (writer, Q16 part 1). First draft from results/mcda.md, hhi.md, displacement.md, schedule_value.md, lca.md, sources.md. Inventory numbers and break-even days left as [per final §6] and [per final §7] (LCA being finalised). Granta stated as not run [TODO: H2]. Search strategy [TODO: App E] (no search log in 02_Research/).
- Length: about 560 words of body text (hand count of the draft below), about 1.1 pages; if over, cut the GenCost sentence to §8.2 first.
-->

## 2 Methods and data

**Four methods carry the numbers (a screening life-cycle assessment, grid displacement with a schedule break-even, a concentration index for fuel supply, and a multi-criteria analysis), and every figure regenerates from the scripts and parameter files in `03_LCA_Calculations/` (Appendix D).**

**Life-cycle assessment (LCA).** A screening study following ISO 14040/14044 principles (International Organization for Standardization, 2006a; 2006b), not critically reviewed, so it supports no public comparative claim. *Functional unit:* 1 MWh of net electricity at the plant's grid connection (results in g CO₂e/kWh). *Reference flow:* one BWRX-300 unit, 300 MWe × 8,760 h × 0.90 × 60 years = 1.419 × 10⁸ MWh. *Boundary:* cradle to grave. Construction materials and the fuel front end (mining, conversion, enrichment, fabrication) are built from process data; operation, decommissioning and the back end use per-kWh literature values. Omitted items (cladding, conversion chemicals, plant capital goods, recycling credits) bias the result low. *Model:* a Python script multiplying quantities by published emission factors, with a Monte Carlo analysis and tornado chart for uncertainty (Appendix C); inventory and results [per final §6]. **The Granta EduPack Eco Audit has not yet been run and no number here comes from it** [TODO: H2].

**Displacement and schedule.** One unit supplies 2.365 TWh a year and avoids that output × (grid factor − SMR factor). The *average* factor is the mean intensity of the grid; the *marginal* factor is that of the plant that backs off when new supply arrives (The Atmospheric Fund, 2025). Ontario's are 73.8 and 343 g/kWh (2024); we report both because the difference decides the answer. For New South Wales we use 640 g/kWh, a location-based factor that excludes upstream emissions (Department of Climate Change, Energy, the Environment and Water, 2025). Future grids are our own trajectories from published anchor points, shown as ranges. Start years are October 2030 for Darlington Unit 1 (Ontario Power Generation, 2025) and 2040 at the earliest for Australia (Graham, Hayward and Foster, 2024) [TO VERIFY]. The *schedule break-even* is the delay that cancels an embodied saving S: S ÷ (daily output × grid-factor gap) [per final §7]. For cost we read GenCost 2023-24 at 2030 as A$230–382/MWh for SMRs against A$89–125 for firmed wind and solar, so the same money buys 2.9× the renewable energy; the alternative reading, A$387–641, gives 5.0× [TO VERIFY: table and year].

**Supply concentration.** The Herfindahl–Hirschman index (HHI) is the sum of squared percentage market shares (0 to 10,000), computed for mining by country and for conversion and enrichment by company capacity. Above 1,800 is "highly concentrated" (US Department of Justice and Federal Trade Commission, 2023); we also report the 2010 scale (1,500 and 2,500) because mining falls between them. Caveats: it is a merger-review screen, not a legal test of supply risk; capacity is not contracts or stockpiles; inventories are excluded; "without Russia" re-divides shares with no new capacity; inputs are secondary extracts [TO VERIFY] (Appendix B).

**Multi-criteria analysis (MCDA).** A weighted-sum model (Dodgson et al., 2009) scores four options (status quo, one SMR at Liddell, SMR plus C1, the same money on firmed renewables) on seven criteria: life-cycle CO₂e, CO₂e avoided per dollar, cost, time to first power, supply concentration, social licence and legal feasibility. Each criterion is min-max normalised across the options (best 1, worst 0). Four weight sets (equal, federal government, Coalition, host community) are our reading of each group's priorities, not elicited. Robustness: each weight moved ±50% (56 tests), 20,000 random weight sets, and input changes. Social licence and legal scores are our judgement.

**Search strategy.** [TODO: App E: databases, search strings and dates.]

---

### IDs covered (towards the HD descriptor) and what is still missing
- **R2.4:** each method has a definition or formula, inputs and a pointer to the working. Missing: final §6 inventory and §7 break-even days.
- **R2.1, R2.6:** quantitative method and the logic from method to claim.
- **R1.4:** standards and agencies named (ISO, DOJ/FTC, CSIRO, DCCEEW). Missing: Appendix E search log; primaries still [TO VERIFY].
- **RB.5:** working sits in Appendices A–D; this section summarises it.

### Remaining TODOs
1. [per final §6] inventory and Monte Carlo set-up; [per final §7] break-even days.
2. [TODO: H2] Granta Eco Audit; if not run by Thu 12:00, the "not yet run" sentence stands.
3. [TODO: App E] search databases, strings and dates (Leroy).
4. Merge into the reference list: ISO 14040 and 14044 (sources.md), DOJ/FTC 2023, Dodgson et al. (2009; sources_run9.md). Open Dodgson ch. 6 and GenCost 2023-24 (2030 SMR row) before relying on them.
