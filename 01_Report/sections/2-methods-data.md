Rubric coverage: R2.4, R2.1, R2.6, R1.4, RB.5 (also supports R2.5, R2.7, R3.6, R5.1, R5.3)
<!-- Changelog 25/10 (writer, Q21): M10 DCCEEW and "2030"; M11b MCDA option defined; M4 Granta token kept. -->


<!--
CHANGELOG
- v3, 25/10/2026 (writer, final cut): cut to the plan's target (about 320 words); LCA detail left to §6.1; GenCost reading deleted (home §7.3); HHI and MCDA caveats shortened (App B2.5, B7); global data-quality sentence added; search line now points to App E; Granta placeholder token left once for the coordinator.
-->

## 2 Methods and data

**Four methods carry the numbers: a screening life-cycle assessment (LCA), grid displacement with a schedule break-even, a concentration index for fuel supply, and a multi-criteria analysis. Scripts and parameter files regenerate every figure (Appendix A1).** Values are taken from the documents cited, or, where marked "as reported", from the secondary source named. Where readings differ we give the range, and our own assumptions and inferences are labelled as such.

**LCA.** A screening study following ISO 14040/14044 principles (International Organization for Standardization, 2006a; 2006b), not critically reviewed: functional unit 1 MWh of net electricity at the grid connection, cradle to grave (§6.1). The screening model is scripted in Python and Granta was used for [TODO-GRANTA].

**Displacement and schedule.** One unit (300 MWe net assumed; an OPG filing gives 315, within our sensitivity range) supplies 2.365 TWh a year and avoids that output × (grid factor − SMR factor). The *average* factor is the grid's mean intensity; the *marginal* factor is that of the plant displaced (The Atmospheric Fund, 2025). Ontario's are 73.8 and 343 g/kWh; NSW uses 640 (DCCEEW, 2025). Future grids are our trajectories from published anchor points. Start years are 2030 at Darlington (Ontario Power Generation, 2025a) and 2040 at the earliest in Australia (Graham, Hayward and Foster, 2024). The *schedule break-even* is the delay that cancels a saving S: S ÷ (daily output × grid-factor gap) (Appendix B4–B5).

**Supply concentration.** The Herfindahl–Hirschman index (HHI) sums squared percentage market shares (0 to 10,000), by country for mining and by company capacity for conversion and enrichment. Above 1,800 is highly concentrated (US Department of Justice and Federal Trade Commission, 2023; the 2010 scale uses 2,500). Capacity is not contracts, and "without Russia" adds no capacity (Appendix B2).

**Multi-criteria analysis (MCDA).** A weighted sum (Dodgson et al., 2009) scores four options (status quo, one SMR at Liddell, the same SMR built with C1's concrete, firmed renewables) on seven criteria (life-cycle CO₂e, CO₂e avoided per dollar, cost, time to first power, supply concentration, social licence, legal feasibility), each min-max normalised. Four weight sets are our judgement, not elicited. Robustness: each weight ±50%, 20,000 random sets and input changes (Appendix B7).

**Search strategy and patent search:** Appendix E.

---

### IDs covered
- **R2.4, R2.1, R2.6, RB.5:** each method has its definition or formula, inputs and a pointer to the working.
- **R1.4:** standards and agencies named; search and patent log in Appendix E.

### Remaining TODOs
1. The Granta placeholder in the LCA paragraph (coordinator).
