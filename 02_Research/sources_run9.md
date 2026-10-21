Rubric coverage: R1.1, R3.6, R2.4

# Sources, analyst run 9 (21/10/2026, Q12 MCDA)
The coordinator should merge these into `02_Research/sources.md`. Both primaries could not be opened (gov.uk DNS failure; atap.gov.au and assets.publishing.service.gov.uk proxy 403; iea.org refused, pv-tech.org DNS failure). Status TO VERIFY: not citable until a human opens them.

### Dodgson_2009_MCA
- **Reference:** Dodgson, J.S., Spackman, M., Pearman, A. and Phillips, L.D. (2009) *Multi-criteria analysis: a manual*. London: Department for Communities and Local Government. Available at: https://www.gov.uk/government/publications/multi-criteria-analysis-manual-for-making-government-policy (Accessed: 21 October 2026).
- **Key findings (search summary only):** government guidance on MCA for appraising policy options; options scored against criteria with explicit weights. First published December 2000, amended January 2009.
- **Numbers:** none used.
- **Reliability:** official UK government guidance, widely cited. The linear additive model and 0-1 (or 0-100) local scales are attributed to it from memory of the method, NOT confirmed in the text: open chapter 6 before citing.
- **Used in:** `results/mcda.md` section 1 (method).

### iea2022_pv_supply
- **Reference:** International Energy Agency (2022) *Solar PV Global Supply Chains*. Paris: IEA. Available at: https://www.iea.org/reports/solar-pv-global-supply-chains (Accessed: 21 October 2026).
- **Key findings (search summary of the executive summary):** "China's share in all the manufacturing stages of solar panels (such as polysilicon, ingots, wafers, cells and modules) exceeds 80%"; set to rise above 95% for polysilicon and wafers based on capacity under construction. Released 7 July 2022.
- **Numbers:** > 80% (all stages); > 95% (polysilicon, wafers, projected).
- **Reliability:** primary intergovernmental report; quote seen only in a search summary. 2022 data; shares have likely risen since.
- **Used in:** `parameters_run9.yaml` pv_china_share_min; `results/mcda.md` supply criterion (HHI lower bound 6,400; 9,025 at 95%).
