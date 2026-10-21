Rubric coverage: R3.6, RB.8, R2.6, R4.4, R2.4 (also supports R2.7, R3.5, R3.8, R4.3, R5.1, R5.2, R5.3)

<!--
CHANGELOG
- v1, 21/10/2026 (writer, Q14 part 1). First draft of §9 from `results/mcda.md` and `mcda_scores.csv` (analyst run 9, C1 case new_2200) and the numbers already in §6–§8; working in Appendix B7. Addresses the tracker's RB.8 "Missing" and R3.6 "Missing: §9 MCDA".
- C1 saving is parameterised: both cases (1,734 t, 2,200 t) are given and the figure that would fix a number is marked "[C1 saving: per final §6]" until the LCA re-base lands. T4 and T5 are new IDs; renumber at assembly (Q19).
- §8.1's "Note for §9" deleted in this pass, because §9 now cites Appendix B3 (legal-feasibility criterion).
- Presentation: R5.1 leads with the verdict; R5.3 about 640 body words excluding tables, captions and markers (hand estimate, about 1.25 p with two tables; confirm in Word); R5.4 Harvard; R5.5 Australian English.
-->

## 9 Triple-bottom-line evaluation and multi-criteria analysis

**Adopt C1 only as a schedule-neutral specification. For Australia, the same money on firmed renewables ranks first, ahead of the status quo and of an SMR at Liddell.** C1 is a real but marginal gain: SMR + C1 and a plain SMR differ by about 0.3–0.4% on life-cycle emissions. No weight set, input change or ±50% weight test we ran puts an SMR first.

### 9.1 Triple bottom line

The triple bottom line judges an option on its environmental, economic and social effects together. Table T4 applies it to the initiative at Darlington (C1 on Units 2–4) and to the Australian comparison at Liddell. Each cell is traced to the section that holds the evidence.

*Table T4. Triple-bottom-line summary: C1 at Darlington Units 2–4 and one BWRX-300 at Liddell.*
*Source: this study, from the sections cited in the last column. All inputs [TO VERIFY] as in those sections.*

| | Darlington, with C1 | Liddell (one unit) | Traced to |
|---|---|---|---|
| **Environment** | Plant 4.2 g CO₂e/kWh (90% interval 3.0–5.8). C1 saves 1,734 t (central) to 2,200 t per unit, 0.29–0.37% of a unit's life cycle [C1 saving: per final §6]. Unit 1 avoids 1.0–6.8 Mt CO₂e to 2050 | Same plant intensity. Avoids 0.67–3.9 Mt to 2050 from about 2040. The same money on firmed renewables avoids 10.9× more | §6.3, §7.2–7.3 |
| **Economy** | LCOE C$198/MWh at 7% (C$112–280 at 3–10%). C1's carbon value is C$0.49–0.60 m for Units 2–4 at 1,734 t per unit [C1 saving: per final §6], against C$1.8–2.9 m for each day of delay | SMR A$230–382/MWh in 2030 against A$89–125 for firmed renewables (2.9× at midpoints). No private owner could finance a first unit | §7.1, §7.3, §8.2 |
| **Society** | Power-weighted stance +1.07; no high-power actor opposed. The Williams Treaties First Nations lend C$700 m, converting to equity. C1 adds no new consent issue. Unit 1's fuel chain has no Russian stage | Stance −1.03. 61% support nuclear power, but 59% want the ban kept. No legal route is open (three routes score 5–8 of 12). Enrichment and conversion would be imported | §8.1, §8.3–8.5 |
| **Net** | Environment positive but marginal; economy small; society neutral. Feasible if schedule-neutral | Not feasible before 2040 on current law, cost and consent | §6–§8 |

### 9.2 Multi-criteria analysis

**Method.** We compared four options on seven criteria with a weighted sum, the standard compensatory method (Dodgson et al., 2009) [TO VERIFY]: the status quo (coal-heavy NSW grid), one SMR at Liddell, SMR + C1, and the same annual spend on firmed renewables. Each criterion is rescaled so the best option scores 1 and the worst 0. The criteria are life-cycle CO₂e, CO₂e avoided to 2050 per dollar, cost, first full year of new supply, supply concentration (HHI), social licence (Table T13) and legal feasibility (Appendix B3). Four weight sets reflect each group's stated priorities: equal; climate and cost (federal government); firm supply and sovereignty (Coalition, the most SMR-favourable set we could justify); and host community. Technology readiness level (TRL) is not scored (see limits below). Full working is in Appendix B7.

*Table T5. MCDA total scores (0–100) by weight set, and rank-reversal tests.*
*Source: this study, `scripts/mcda.py` (`results/mcda.md`; Appendix B7). SMR + C1 shown for the 2,200 t case; the 1,734 t case differs by under 0.005 point. Scores for social licence, legal feasibility and the weights are our judgement. [TO VERIFY]*

| Option | Equal | Climate and cost | Firm and sovereign | Host community |
|---|---:|---:|---:|---:|
| Firmed renewables, same money | **80.1** | **85.9** | **63.7** | **89.3** |
| Status quo | 52.4 | 41.7 | 60.0 | 55.0 |
| One SMR at Liddell | 29.7 | 24.0 | 43.6 | 20.4 |
| SMR + C1 | 29.7 | 24.0 | 43.6 | 20.4 |
| First place changed by a ±50% change in one weight (of 14 tests) | 0 | 0 | 2 | 0 |

**Renewables rank first under every weight set.** The SMR beats them only on life-cycle CO₂e (4.2 against 30 g/kWh) and on supply concentration (enrichment HHI 3,009 against at least 6,400 for solar PV). It loses on CO₂e avoided per dollar (10.9×), cost (2.9×), time (about 12 years later), social licence and legal feasibility.

**Rank reversal.** Of 56 weight changes of ±50%, two change first place. Both are under the firm-and-sovereign weights (life-cycle weight halved; supply weight × 1.5), and both hand first place to the status quo, not to the SMR. An SMR option ranks first only if life-cycle CO₂e carries at least 94% of the weight. In 20,000 random weight sets, renewables rank first in 85.4%, the status quo in 14.5% and an SMR option in 0.1%. Of 68 input tests (GenCost reading, first power in 2035 or 2045, grid path, C1 premium and delay), renewables stay first in 66; the other two go to the status quo.

**The status quo's second place over the SMR is a scaling artefact.** The status quo scores full marks on cost, supply and legal feasibility because it changes nothing. On fixed global scales instead of the four-option scale, the SMR moves above it under every weight set. Renewables stay first on both scales.

**SMR + C1 and SMR are indistinguishable.** C1 lowers life-cycle intensity from 4.200 to 4.188 g/kWh (1,734 t per unit, 0.29%) or 4.185 g/kWh (2,200 t, 0.37%) [C1 saving: per final §6]. That moves the weighted score by under 0.005 point, and its sign depends on the assumed C$1 m qualification cost. If C1 delays a unit, the CO₂e left unavoided outweighs the saving many times over (Appendix B7.5), so schedule neutrality decides whether C1 helps at all.

### 9.3 Verdict and limits

**Darlington: adopt C1 only as a schedule-neutral specification.** Pilot LC³ in eligible non-safety works first. Use steel-composite infill only if it is qualified on Unit 1 mock-ups; otherwise specify the slag blend (§8.6). The reason is the balance in Table T4: a 0.3–0.4% environmental gain, a carbon value smaller than one day of delay, and no new consent issue. Qualification must start in 2027 for the 2028 Units 2–4 decision (§8.6).

**Australia: the same money on firmed renewables.** An SMR at Liddell would need three things at once to compete in this frame: its cost gap closed to near renewables, first power well before 2040, and the legal and consent barriers removed first (Appendix B3 route C; Table T13). We would keep SMRs under review against Darlington's outturn cost.

**Limits of the analysis.**
- The social, legal and renewables-supply scores, and all four weight sets, are our judgement. The weights are our reading of each group's priorities, not elicited from them.
- The status quo's lead over the SMR depends on the scaling, as above. Only "renewables first" is robust to it.
- TRL is not scored because no TRL figure is yet in the report [TODO: Leroy §4.1]. Schedule risk enters only through first power: CSIRO's "2040 at the earliest" [TO VERIFY: Leroy §4.1], with the Coalition's 2035 and a 2045 case tested without changing the order.
- Costs come from GenCost (Graham, Hayward and Foster, 2024) and the renewables supply score from solar PV alone, standing in for batteries and wind (International Energy Agency, 2022) [TO VERIFY]. The 4.2 g/kWh base is from the earlier 20,700 m³ model, so the percentages above must be re-read from the final §6 [C1 saving: per final §6].

---

### IDs covered (towards the HD descriptor) and what is still missing

- **R3.6 (evaluation and comparison of solutions against non-technical objectives).**
  - Produced: a scored MCDA of the status quo, SMR, SMR + C1 and the same money on firmed renewables, with four weight sets, ±50% rank-reversal tests, random weights, input sensitivities and the scaling artefact (T5; B7).
  - Missing: TRL as a criterion; elicited rather than judged weights; no figure of scores by weight set.
- **RB.8 (triple-bottom-line evaluation of feasibility and effectiveness).**
  - Produced: T4, one cell per dimension and site, each traced to §6–§8, with a net verdict.
  - Missing: the final C1 numbers from the re-based §6.
- **R2.6 (arguments logical, justified, covering all important aspects).**
  - Produced: the verdict follows from T4 and T5 and states the conditions that would change it (94% life-cycle weight; the three Liddell conditions).
  - Missing: sources verified.
- **R4.4 (feasibility shown, or why not).**
  - Produced: C1 feasible only if schedule-neutral; an SMR at Liddell not feasible before 2040 on current law, cost and consent.
  - Missing: the Units 2–4 qualification time, still our planning assumption (§8.6).
- **R2.4 (methods clear, full working in the appendix).**
  - Produced: a four-sentence method here and formulas, worked examples and every input in B7.
  - Missing: §2 (methods summary) not yet written.

### Remaining TODOs

1. **[C1 saving: per final §6]** Replace the three marked places (T4 environment and economy cells; 9.2; limits) with the team's final C1 saving and share; re-run `python3 -I 03_LCA_Calculations/scripts/mcda.py --c1-case <case>` if the base case changes.
2. **[TODO: Leroy §4.1]** TRL figure and first-power dates; verify CSIRO "2040 at the earliest" covers SMRs.
3. **[TO VERIFY]** GenCost 2030 table and year; IEA (2022) PV shares; Dodgson et al. (2009) (gov.uk blocked).
4. **[TODO: sources.md]** Merge `Dodgson_2009_MCA` and `iea2022_pv_supply` from `sources_run9.md`.
5. **[Assembly, Q19]** Renumber T4/T5 and Table T13 reference; strip markers and the changelog.
