# Rubric coverage: R3.6, RB.8, R2.6, R4.4, R2.4, R2.7
"""MCDA (triple-bottom-line) of four Australian options, plus the Appendix B3 consent-route scoring.

Analyst run 9 (21/10/2026, plan Q12). Writes results/mcda.md and results/mcda_scores.csv.

Alternatives: SQ (status quo), SMR (one BWRX-300 at Liddell), SMR_C1 (the same with initiative C1),
VRE (the same money on firmed renewables, same_money.py frame, GenCost 2023-24 2030 reading).
Criteria (7): lifecycle, avoided_per_dollar, cost, time, supply, social, legal.
Method: linear additive model; each criterion min-max normalised across the four options (local scale,
0 = worst, 1 = best), weights renormalised to sum to 1, total x 100.

Inputs: parameters_run9.yaml (MCDA choices, C1 cases, weights, B3 scores), parameters_run1.yaml via
same_money.base() (LCOE, LCA, grid, start years), parameters_run5.yaml (concrete price), parameters_run6.yaml
(T13 consent-route scores), results/hhi_summary.csv (enrichment HHI). The C1 saving is read ONLY from
parameters_run9.yaml c1_cases (the LCA is owned by a team member); choose the case with --c1-case.

Usage: python3 scripts/mcda.py [--c1-case new_2200]
"""
import argparse
import csv
import sys
from pathlib import Path

import numpy as np
import yaml

SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parent
sys.path.insert(0, str(SCRIPTS))
import same_money as sm  # noqa: E402  (re-uses the agreed same-money frame and trajectories)

R9 = yaml.safe_load((ROOT / "parameters_run9.yaml").read_text())["parameters"]
R5 = yaml.safe_load((ROOT / "parameters_run5.yaml").read_text())
R5 = R5.get("parameters", R5)
R6 = yaml.safe_load((ROOT / "parameters_run6.yaml").read_text())
R6 = R6.get("parameters", R6)
OUT_MD = ROOT / "results" / "mcda.md"
OUT_CSV = ROOT / "results" / "mcda_scores.csv"

ALTS = ["SQ", "SMR", "SMR_C1", "VRE"]
LABEL = {"SQ": "Status quo", "SMR": "One SMR at Liddell", "SMR_C1": "SMR + C1", "VRE": "Same money on firmed renewables"}
CRIT = list(R9["criteria"])
CLABEL = {"lifecycle": "Life-cycle CO2e (g/kWh)", "avoided_per_dollar": "CO2e avoided to 2050 (Mt per A$1 bn/yr)",
          "cost": "Cost, LCOE (A$/MWh)", "time": "First full year of new supply", "supply": "Supply concentration (HHI)",
          "social": "Social licence (T13 total, 5-15)", "legal": "Legal feasibility (B3 total, 4-12)"}
HIGHER_BETTER = {"lifecycle": False, "avoided_per_dollar": True, "cost": False, "time": False,
                 "supply": False, "social": True, "legal": True}
HORIZON = 2050


# ---------------------------------------------------------------- inputs
def hhi_row(stage, scenario):
    with open(ROOT / "results" / "hhi_summary.csv") as f:
        for r in csv.DictReader(f):
            if r["stage"] == stage and r["scenario"] == scenario:
                return float(r["hhi"])
    raise KeyError((stage, scenario))


def t13_totals(weights=None):
    cr = R6["consent_routes"]
    w = weights or cr["weight_sets"]["equal"]
    return {k: sum(w[c] * r["scores"][c] for c in cr["criteria"]) for k, r in cr["routes"].items()}


def b3_totals(weights, a_veto=None):
    b3 = R9["b3_routes"]
    out = {}
    for k, r in b3["routes"].items():
        s = dict(r["scores"])
        if a_veto is not None and k == "A_commonwealth":
            s["veto_points"] = a_veto
        out[k] = sum(weights[o] * s[o] for o in b3["objectives"])
    return out


def c1_case(name):
    return R9["c1_cases"]["cases"][name]


def raw_matrix(c1_name, ov=None):
    """Raw performance of the four options. ov = scenario overrides."""
    ov = ov or {}
    p = sm.base()
    for k in ("lc_smr", "lc_vre", "smr_start_aus", "vre_start", "ef_vre", "ef_smr", "floor"):
        if k in ov:
            p[k] = ov[k]
    grid = ov.get("grid_case", R9["mcda_choices"]["grid_case"])
    ef = sm.traj(p)[grid]
    mwh = sm.annual_mwh(p)
    life_kwh = mwh * 1000 * p["life"]
    case = c1_case(c1_name)
    saving_t = case["saving_t_per_unit"]
    d_lca = saving_t * 1e6 / life_kwh  # g/kWh removed by C1
    # C1 cost: premium on the treated concrete + one-off qualification + optional delay carrying cost (all A$)
    prem = float(ov.get("c1_premium", R9["c1_premium_base_frac"]["value"]))
    qual = float(ov.get("c1_qual", R9["c1_qualification_base_cad"]["value"]))
    delay = ov.get("c1_delay_days", 0.0)
    conc_price = float(R5["concrete_price_cad_m3"]["value"])
    cap_unit_aud = p["budget"] * p["fx"] / p["units"]
    c1_cad = prem * conc_price * case["volume_m3_per_unit"] + qual
    c1_aud = c1_cad * p["fx"] + delay * cap_unit_aud * p["r"] / 365
    crf = sm.crf(p["r"], p["n"])
    d_cost = c1_aud * crf / mwh
    start = p["smr_start_aus"]
    spend = mwh * p["lc_smr"]  # A$/yr, same annual spend for SMR and VRE (same_money.md section 4)
    ef_c1 = p["ef_smr"] - d_lca
    av_smr = sm.cum(p, ef, start, HORIZON, mwh, p["ef_smr"]) / 1e6
    lost = delay / 365 * mwh * (ef(start) - ef_c1) / 1e9  # Mt not avoided during the delay (MWh x g/kWh = kg)
    av_c1 = sm.cum(p, ef, start, HORIZON, mwh, ef_c1) / 1e6 - lost
    av_vre = sm.cum(p, ef, p["vre_start"], HORIZON, spend / p["lc_vre"], p["ef_vre"]) / 1e6
    sq = R9["sq_conventions"]
    hhi_smr = hhi_row("Enrichment", ov.get("hhi_row", R9["mcda_choices"]["smr_supply_hhi_row"]))
    pv = ov.get("pv_share", R9["pv_china_share_min"]["value"])
    hhi_vre = pv ** 2 * 10000  # lower bound: one supplier alone contributes share^2
    t13 = t13_totals()
    smr_social = max(v for k, v in t13.items() if k != "R4_no_nuclear")
    b3eq = b3_totals(R9["b3_routes"]["weight_sets"]["equal"])
    smr_legal = max(b3eq.values())
    sq_cost = p["lc_vre"] if ov.get("sq_cost_as_vre") else sq["cost_aud_mwh"]
    sq_supply = hhi_vre if ov.get("sq_supply_as_vre") else sq["supply_hhi"]
    M = {
        "SQ": dict(lifecycle=p["nsw"], avoided_per_dollar=0.0, cost=sq_cost, time=sq["first_year"],
                   supply=sq_supply, social=ov.get("sq_social", sq["social_t13"]), legal=sq["legal_b3"]),
        "SMR": dict(lifecycle=p["ef_smr"], avoided_per_dollar=av_smr / (spend / 1e9), cost=p["lc_smr"],
                    time=start, supply=hhi_smr, social=smr_social, legal=smr_legal),
        "SMR_C1": dict(lifecycle=ef_c1, avoided_per_dollar=av_c1 / (mwh * (p["lc_smr"] + d_cost) / 1e9),
                       cost=p["lc_smr"] + d_cost, time=start + delay / 365, supply=hhi_smr,
                       social=smr_social, legal=smr_legal),
        "VRE": dict(lifecycle=p["ef_vre"], avoided_per_dollar=av_vre / (spend / 1e9), cost=p["lc_vre"],
                    time=p["vre_start"], supply=hhi_vre, social=t13["R4_no_nuclear"],
                    legal=R9["mcda_choices"]["vre_legal_b3"]),
    }
    extra = dict(d_lca=d_lca, d_cost=d_cost, saving_t=saving_t, life_kwh=life_kwh, av_smr=av_smr, av_c1=av_c1,
                 av_vre=av_vre, spend=spend, mwh=mwh, lost=lost, c1_aud=c1_aud, p=p, grid=grid)
    return M, extra


def global_bounds(p):
    g = R9["global_scale_bounds"]
    vmax = 1e9 / min(p["lc_vre"], 89.0) * p["nsw"] / 1e6 * (HORIZON - 2026 + 1) / 1e6  # Mt per A$1 bn/yr
    return {"lifecycle": g["lifecycle_g_per_kwh"], "avoided_per_dollar": [0, vmax], "cost": g["cost_aud_mwh"],
            "time": g["first_year"], "supply": g["supply_hhi"], "social": g["social_t13"], "legal": g["legal_b3"]}


def normalise(M, scale="local", p=None):
    S = {a: {} for a in ALTS}
    for c in CRIT:
        vals = [M[a][c] for a in ALTS]
        if scale == "local":
            lo, hi = min(vals), max(vals)
        else:
            lo, hi = global_bounds(p)[c]
        for a in ALTS:
            x = M[a][c]
            if hi == lo:
                s = 1.0
            elif HIGHER_BETTER[c]:
                s = (x - lo) / (hi - lo)
            else:
                s = (hi - x) / (hi - lo)
            S[a][c] = min(max(s, 0.0), 1.0)
    return S


def norm_w(w):
    t = sum(w[c] for c in CRIT)
    return {c: w[c] / t for c in CRIT}


def totals(S, w):
    w = norm_w(w)
    return {a: 100 * sum(w[c] * S[a][c] for c in CRIT) for a in ALTS}


def ranking(T):
    return sorted(ALTS, key=lambda a: -T[a])


def rank_str(T):
    return " > ".join(f"{a} {T[a]:.1f}" for a in ranking(T))


def collapse(order):
    """Order with SMR and SMR_C1 merged (they differ by < 0.1 point by construction)."""
    out = []
    for a in order:
        b = "SMR*" if a in ("SMR", "SMR_C1") else a
        if b not in out:
            out.append(b)
    return out


WSETS = {k: v["weights"] for k, v in R9["weight_sets"].items()}


# ---------------------------------------------------------------- analysis
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--c1-case", default=R9["c1_cases"]["base"], choices=list(R9["c1_cases"]["cases"]))
    args = ap.parse_args()
    base_case = args.c1_case
    rows = []
    L = []
    w = L.append

    M, X = raw_matrix(base_case)
    S = normalise(M)
    p = X["p"]
    base_T = {k: totals(S, ws) for k, ws in WSETS.items()}

    def add_rows(block, scen, c1, Mx, Sx, wname, pert, T):
        rk = ranking(T)
        for a in ALTS:
            rows.append(dict(block=block, scenario=scen, c1_case=c1, weight_set=wname, perturbation=pert,
                             alternative=a, **{f"raw_{c}": round(Mx[a][c], 4) for c in CRIT},
                             **{f"norm_{c}": round(Sx[a][c], 5) for c in CRIT},
                             total=round(T[a], 3), rank=rk.index(a) + 1))

    for k, T in base_T.items():
        add_rows("base", "base", base_case, M, S, k, "none", T)

    # ---- +/-50% perturbation
    f = float(R9["weight_perturbation_frac"]["value"])
    pert = []
    for k, ws in WSETS.items():
        b_order = ranking(base_T[k])
        for c in CRIT:
            for fac in (1 - f, 1 + f):
                w2 = dict(ws)
                w2[c] = ws[c] * fac
                T = totals(S, w2)
                o = ranking(T)
                tag = f"{c} x{fac:.1f}"
                add_rows("perturb", "base", base_case, M, S, k, tag, T)
                pert.append(dict(set=k, tag=tag, top_changed=o[0] != b_order[0],
                                 order_changed=collapse(o) != collapse(b_order),
                                 pair_flip=(o.index("SMR") < o.index("SMR_C1")) != (b_order.index("SMR") < b_order.index("SMR_C1")),
                                 order=" > ".join(o), T=T))

    # ---- random weights (Dirichlet on the simplex)
    rw = R9["random_weights"]
    rng = np.random.default_rng(int(rw["seed"]))
    W = rng.dirichlet(np.ones(len(CRIT)), int(rw["draws"]))
    Smat = np.array([[S[a][c] for c in CRIT] for a in ALTS])
    tot = W @ Smat.T
    first = np.argmax(tot, axis=1)
    first_share = {a: float(np.mean(first == i)) for i, a in enumerate(ALTS)}
    smr_best = np.maximum(tot[:, 1], tot[:, 2])
    p_smr_over_vre = float(np.mean(smr_best > tot[:, 3]))

    # ---- threshold: weight on one criterion (others in proportion to equal) at which the SMR family ranks first
    thresh = {}
    grid_w = np.linspace(0, 1, 2001)
    for i, c in enumerate(CRIT):
        hit = None
        for wc in grid_w:
            wv = np.full(len(CRIT), (1 - wc) / (len(CRIT) - 1))
            wv[i] = wc
            t = Smat @ wv
            if max(t[1], t[2]) > max(t[0], t[3]) + 1e-12:
                hit = wc
                break
        thresh[c] = hit

    # ---- input sensitivities (base weights only)
    SCEN = [
        ("base", {}),
        ("GenCost alternative reading (SMR 514 / VRE 102)", dict(lc_smr=float(p_get("smr_lcoe_2023_alt_aud")), lc_vre=float(p_get("vre_firmed_lcoe_2425_alt_aud")))),
        ("Worst case for renewables (SMR 198 / VRE 153)", dict(lc_smr=float(p_get("smr_lcoe_low_alt_aud")), lc_vre=float(p_get("vre_firmed_lcoe_high_assumption_aud")))),
        ("SMR first power 2035 (Coalition 2024 claim)", dict(smr_start_aus=int(p_get("aus_start_coalition")))),
        ("SMR first power 2045 (late case)", dict(smr_start_aus=int(p_get("aus_start_late")))),
        ("Renewables first year 2030", dict(vre_start=int(p_get("vre_first_year", "high")))),
        ("Grid NEM-T1 (Step Change proxy)", dict(grid_case="NEM-T1-StepChange-proxy")),
        ("Grid NEM-T0 (frozen at 640)", dict(grid_case="NEM-T0-frozen")),
        ("Renewables life cycle 83 g/kWh", dict(ef_vre=float(p_get("vre_firmed_lca_g_per_kwh", "high")))),
        ("Enrichment HHI without Russia and China (5,621)", dict(hhi_row=R9["mcda_choices"]["smr_supply_hhi_alt_row"])),
        ("PV China share 95% (HHI 9,025)", dict(pv_share=float(R9["pv_china_share_min"]["high"]))),
        ("SQ cost = renewables LCOE", dict(sq_cost_as_vre=True)),
        ("SQ supply = renewables HHI", dict(sq_supply_as_vre=True)),
        ("SQ social 11 / 14", None),
        ("C1 not schedule-neutral (+14.6 days)", dict(c1_delay_days=float(R9["c1_delay_days_high"]["value"]))),
        ("C1 premium +20%, qualification C$3 m", dict(c1_premium=float(R9["c1_premium_base_frac"]["high"]), c1_qual=float(R9["c1_qualification_base_cad"]["high"]))),
        ("Global scales (fixed bounds)", "global"),
    ]
    scen_out = []
    for name, ov in SCEN:
        if ov is None:
            res = []
            for v in (11, 14):
                Mx, _ = raw_matrix(base_case, dict(sq_social=v))
                Sx = normalise(Mx)
                res.append({k: totals(Sx, ws) for k, ws in WSETS.items()})
                for k in WSETS:
                    add_rows("scenario", f"SQ social {v}", base_case, Mx, Sx, k, "none", res[-1][k])
            scen_out.append((name, {k: f"{collapse(ranking(res[0][k]))[0]} / {collapse(ranking(res[1][k]))[0]}" for k in WSETS},
                             {k: " / ".join(" > ".join(collapse(ranking(r[k]))) for r in res) for k in WSETS}))
            continue
        if ov == "global":
            Mx, Sx = M, normalise(M, "global", p)
        else:
            Mx, _ = raw_matrix(base_case, ov)
            Sx = normalise(Mx)
        Ts = {k: totals(Sx, ws) for k, ws in WSETS.items()}
        for k in WSETS:
            add_rows("scenario", name, base_case, Mx, Sx, k, "none", Ts[k])
        scen_out.append((name, {k: collapse(ranking(Ts[k]))[0] for k in WSETS},
                         {k: " > ".join(collapse(ranking(Ts[k]))) for k in WSETS}))

    # ---- C1 cases: SMR vs SMR + C1
    c1_out = []
    for cname in R9["c1_cases"]["cases"]:
        Mx, Xx = raw_matrix(cname)
        Sx = normalise(Mx)
        Ts = {k: totals(Sx, ws) for k, ws in WSETS.items()}
        for k in WSETS:
            add_rows("c1_case", "base", cname, Mx, Sx, k, "none", Ts[k])
        Md, Xd = raw_matrix(cname, dict(c1_delay_days=float(R9["c1_delay_days_high"]["value"])))
        Mq, _ = raw_matrix(cname, dict(c1_qual=0.0))
        Sq = normalise(Mq)
        Tq = {k: totals(Sq, ws) for k, ws in WSETS.items()}
        c1_out.append((cname, Mx, Xx, Ts, Md, Xd, Tq))

    # ---- B3 routes
    b3 = R9["b3_routes"]
    b3_new = {k: b3_totals(ws) for k, ws in b3["weight_sets"].items()}
    b3_old = {k: b3_totals(ws, a_veto=b3["a_veto_points_old"]) for k, ws in b3["weight_sets"].items()}

    # ---------------------------------------------------------------- write CSV
    with open(OUT_CSV, "w", newline="") as fcsv:
        wr = csv.DictWriter(fcsv, fieldnames=list(rows[0].keys()))
        wr.writeheader()
        wr.writerows(rows)

    # ---------------------------------------------------------------- write MD
    case = c1_case(base_case)
    w("Rubric coverage: R3.6, RB.8, R2.6, R4.4, R2.4, R2.7\n")
    w("# MCDA: status quo vs one SMR at Liddell vs SMR + C1 vs the same money on firmed renewables\n")
    w(f"Generated by `03_LCA_Calculations/scripts/mcda.py` (analyst run 9, 21/10/2026). C1 case: **{base_case}** "
      f"({case['saving_t_per_unit']:,} t CO2e/unit; switch with `--c1-case`, or `c1_cases.base` in `parameters_run9.yaml`). "
      "Raw scores per option, criterion, weight set and perturbation are in `results/mcda_scores.csv`. "
      "**PROVISIONAL:** most inputs are TO VERIFY (primaries blocked) and three criteria (supply for renewables, social licence, legal feasibility) "
      "rest on our scored judgement. The ranking is a structured comparison, not a measurement.\n")

    w("## 1. Method (full working)\n")
    w("- **Model:** linear additive (weighted-sum) MCDA, the standard compensatory model in the UK government MCA manual (Dodgson et al., 2009) [TO VERIFY: gov.uk blocked 21/10].")
    w("- **Scoring:** each criterion is min-max normalised across the four options (local scale): s = (x - worst)/(best - worst), so the best option scores 1 and the worst 0. "
      "Lower is better for life-cycle CO2e, cost, first-power year and HHI; higher is better for CO2e avoided per dollar, social licence and legal feasibility. Fixed global scales are tested in section 6.")
    w("- **Total:** T = 100 x sum_c w_c s_c, with weights renormalised to sum to 1.")
    w(f"- **Avoided per dollar:** cumulative CO2e avoided to {HORIZON} for the same annual spend, each option from its own first year (same_money.md section 4 frame): "
      f"spend = {X['mwh']:,.0f} MWh/yr x A${p['lc_smr']:.0f}/MWh = A${X['spend']/1e9:.3f} bn/yr; renewables buy spend / A${p['lc_vre']:.0f} = {X['spend']/p['lc_vre']/1e6:.2f} TWh/yr from {p['vre_start']}. "
      f"Avoided = sum over years of MWh x (grid factor - option's life-cycle factor), grid = {X['grid']} (linear 640 g/kWh in 2025 to {p['floor']:.0f} in 2050). "
      f"SMR {X['av_smr']:.2f} Mt, renewables {X['av_vre']:.2f} Mt to 2050; divided by A${X['spend']/1e9:.3f} bn/yr.")
    w(f"- **C1 (SMR + C1):** life-cycle reduction = saving / lifetime output = {X['saving_t']:,} t x 1e6 g / ({X['mwh']:,.0f} MWh x 1,000 x {p['life']} yr = {X['life_kwh']:.3e} kWh) "
      f"= **{X['d_lca']:.4f} g/kWh** ({X['d_lca']/p['ef_smr']:.2%} of {p['ef_smr']} g/kWh). C1 cost = premium x C$229/m3 x {case['volume_m3_per_unit']:,} m3 + qualification "
      f"(base: 0% premium, C$1.0 m) x {p['fx']} AUD/CAD, annualised at CRF({p['r']:.0%}, {p['n']} yr) = {sm.crf(p['r'], p['n']):.4f} over {X['mwh']:,.0f} MWh = **+A${X['d_cost']:.3f}/MWh**. "
      "Base case: schedule-neutral (the §8.6 condition); the delay case adds the unit's carrying cost (A$ capital share x 7%/365 per day) and the CO2e not avoided during the delay.")
    w("- **Time and deliverability:** first full year of new supply. TRL is **not scored**: no TRL figure exists yet in the sections or briefs [TODO: Leroy §4.1]; schedule risk enters through the 2035 and 2045 first-power cases (section 6) and the C1 delay case.")
    w("- **Supply:** HHI of the most concentrated stage of each option's supply chain. SMR: enrichment, 2025 capacity (hhi.md). Renewables: lower bound share^2 x 10,000 from China's share of every PV manufacturing stage, > 80% (IEA, 2022) [TO VERIFY: iea.org refused 21/10]; PV stands in for the whole firmed-renewables chain (batteries and wind not assessed).")
    w("- **Social and legal:** the SMR takes its best route's total under equal weights: T13 R2/R3 (social_licence.md section 7) and App B3 route C (section 8 below). Renewables take T13 R4 and the B3 maximum (no nuclear prohibition engaged).")
    w("- **Status quo conventions (do-nothing reference):** NSW 2025 grid factor as its 'life cycle' (scope 2, a boundary mismatch, but SQ is last on this criterion whatever the boundary), nothing avoided, no new cost, no new supply chain, first year = 2050 (no new supply in the horizon), social 13 (nothing to consent to, but no benefits reach the Upper Hunter: fairness 1), legal 12. SQ cost and supply conventions are tested in section 6.\n")

    w("## 2. Performance matrix (raw values) and source of every score\n")
    w("| Criterion | Status quo | One SMR at Liddell | SMR + C1 | Firmed renewables | Source (status) |")
    w("|---|---|---|---|---|---|")
    src = {
        "lifecycle": "SMR: results/lca.md (team LCA, median 4.2; old 20,700 m3 model, re-base pending). C1: c1_cases. VRE: 30 g/kWh assumption inside UNECE (2021) PV 8-83 [TO VERIFY]. SQ: NGA Factors 2025 NSW 640 [TO VERIFY]",
        "avoided_per_dollar": "same_money.py frame; GenCost 2023-24 2030 LCOEs [TO VERIFY]; NEM-T2 trajectory (assumption); start years below",
        "cost": "GenCost 2023-24 final, 2030: SMR 230-382 (mid 306), firmed VRE 89-125 (mid 107) [TO VERIFY: csiro.au blocked]; C1 cost: parameters_run5/run9 (assumptions)",
        "time": "SMR: CSIRO 'deployment from 2040 at the earliest' (GenCost 2023-24) [TO VERIFY: Leroy §4.1]; §8.1 sets Coalition 2035 against CSIRO 2040. VRE: 2028 assumption (2027-2030). SQ: convention",
        "supply": "SMR: hhi.md enrichment 2025 (WNA/company capacities) [TO VERIFY]. VRE: IEA (2022) China > 80% of every PV stage [TO VERIFY]. SQ: convention",
        "social": "social_licence.md section 7, T13 (parameters_run6.yaml consent_routes; our judgement, evidence keys there)",
        "legal": "App B3 Table B13, route C best (parameters_run9.yaml b3_routes; our judgement; route A corrected, section 8)",
    }
    fmt = {"lifecycle": "{:.4f}", "avoided_per_dollar": "{:.2f}", "cost": "{:.2f}", "time": "{:.2f}", "supply": "{:,.0f}", "social": "{:.0f}", "legal": "{:.0f}"}
    for c in CRIT:
        w(f"| {CLABEL[c]} | " + " | ".join(fmt[c].format(M[a][c]) for a in ALTS) + f" | {src[c]} |")
    w("\n## 3. Normalised scores (local scale, 1 = best of the four)\n")
    w("| Criterion | " + " | ".join(LABEL[a] for a in ALTS) + " |")
    w("|---|---|---|---|---|")
    for c in CRIT:
        w(f"| {c} | " + " | ".join(f"{S[a][c]:.4f}" for a in ALTS) + " |")

    w("\n## 4. Weight sets and results\n")
    w("Weights are our reading of each group's stated priorities, not elicited from them (parameters_run9.yaml rationale).\n")
    w("| Set | " + " | ".join(CRIT) + " | Rationale |")
    w("|---|" + "---|" * (len(CRIT) + 1))
    for k, v in R9["weight_sets"].items():
        nw = norm_w(v["weights"])
        w(f"| {k} | " + " | ".join(f"{nw[c]:.3f}" for c in CRIT) + f" | {v['rationale']} |")
    w("\n| Set | " + " | ".join(LABEL[a] for a in ALTS) + " | Ranking |")
    w("|---|---|---|---|---|---|")
    for k, T in base_T.items():
        w(f"| {k} | " + " | ".join(f"{T[a]:.1f}" for a in ALTS) + f" | {' > '.join(ranking(T))} |")

    w(f"\n## 5. Each weight varied by +/-{f:.0%} (then renormalised): rank-reversal check\n")
    w("'Top' = first place changes; 'order' = the order changes with SMR and SMR + C1 merged (they differ by < 0.1 point); 'pair' = SMR and SMR + C1 swap.\n")
    w("| Set | Cases tested | Top changes | Order changes | SMR / SMR + C1 swaps | Cases that change the order |")
    w("|---|---|---|---|---|---|")
    for k in WSETS:
        P_ = [x for x in pert if x["set"] == k]
        ch = [f"{x['tag']} ({x['order']})" for x in P_ if x["order_changed"]]
        w(f"| {k} | {len(P_)} | {sum(x['top_changed'] for x in P_)} | {sum(x['order_changed'] for x in P_)} | {sum(x['pair_flip'] for x in P_)} | {'; '.join(ch) if ch else 'none'} |")
    w(f"\nRandom weights ({int(rw['draws']):,} Dirichlet(1,...,1) draws, seed {rw['seed']}): share of draws in which each option ranks first: "
      + ", ".join(f"{LABEL[a]} {first_share[a]:.1%}" for a in ALTS) + f". SMR (best of SMR, SMR + C1) above renewables in {p_smr_over_vre:.1%} of draws.\n")
    w("Threshold: weight on one criterion (the other six sharing the rest equally) at which an SMR option first ranks first: "
      + "; ".join(f"{c} {('%.3f' % thresh[c]) if thresh[c] is not None else 'never'}" for c in CRIT) + ".\n")

    w("## 6. Input sensitivities (base weights; first place, then full order with SMR merged)\n")
    w("| Change | " + " | ".join(WSETS) + " |")
    w("|---|" + "---|" * len(WSETS))
    for name, top, order in scen_out:
        w(f"| {name} | " + " | ".join(f"{top[k]}: {order[k]}" for k in WSETS) + " |")

    w("\n## 7. SMR vs SMR + C1, under each C1 case\n")
    w("Environmental criterion (life cycle) and the knock-on to the other two criteria C1 touches. 'Delay' = C1 not schedule-neutral (+14.6 days, results/schedule_value.md, old-case break-even used as an illustrative delay).\n")
    w("| C1 case | Saving (t/unit) | Life cycle SMR -> SMR + C1 (g/kWh) | Difference | Avoided to 2050, SMR -> SMR + C1 (Mt) | Cost +A$/MWh | Score gap (points of 100): " + ", ".join(WSETS) + " | Score gap if qualification costs nothing | With delay: avoided change (kt) |")
    w("|---|---|---|---|---|---|---|---|---|")
    for cname, Mx, Xx, Ts, Md, Xd, Tq in c1_out:
        gaps = ", ".join(f"{Ts[k]['SMR_C1'] - Ts[k]['SMR']:+.4f}" for k in WSETS)
        gq = ", ".join(f"{Tq[k]['SMR_C1'] - Tq[k]['SMR']:+.5f}" for k in WSETS)
        w(f"| {cname} ({c1_case(cname)['status']}) | {Xx['saving_t']:,} | {Mx['SMR']['lifecycle']:.3f} -> {Mx['SMR_C1']['lifecycle']:.4f} | "
          f"{Xx['d_lca']:.4f} g/kWh ({Xx['d_lca']/Mx['SMR']['lifecycle']:.2%}) | {Xx['av_smr']:.3f} -> {Xx['av_c1']:.3f} | {Xx['d_cost']:.3f} | {gaps} | {gq} | {(Xd['av_c1'] - Xd['av_smr']) * 1000:+.1f} (saving {Xx['saving_t']/1000:.1f} kt; lost {Xd['lost'] * 1000:.1f} kt) |")
    w("\nThe two C1 cases named in the brief: **old_1734** and **new_2200**. Both change the SMR's life-cycle intensity by well under 1% (0.29% and 0.37% of 4.2 g/kWh), "
      "which moves the weighted score by thousandths of a point and never changes the SMR's place against the other options. "
      "The gap is slightly negative in the base case because the assumed C$1 m qualification cost (+A$0.04/MWh) outweighs, on these scales, a 0.016 g/kWh gain on a criterion whose range is 636 g/kWh; with no qualification cost it turns positive but stays below 0.001 point. "
      f"If C1 slips the unit by 14.6 days, the CO2e not avoided during the delay ({c1_out[0][5]['lost'] * 1000:.1f} kt) is {c1_out[0][5]['lost'] * 1e6 / R9['c1_cases']['cases']['new_2200']['saving_t_per_unit']:.0f}x the new_2200 saving, so SMR + C1 then avoids less than the plain SMR: the schedule-neutral condition decides the sign. "
      "Denominator caveat: the 4.2 g/kWh base comes from the old 20,700 m3 model; the team member's re-based LCA (Ostrołęka 50,000 m3) will change the life-cycle total, so the percentage for new_2200 must be re-read from that result.\n")

    w("## 8. Appendix B3: consent routes scored (scripted; route A corrected)\n")
    w("Route A's 'fewest veto points' score is **1, not 2**: the fact-check (`01_Report/factcheck/I-pass3-batch1a.md`, M2) found that route A still needs a s 109 override of the NSW 1986 Act or a NSW repeal, so it faces the Senate, NSW or the High Court, and the site owner, like routes B and C. Scores 1 = poor, 3 = good (our judgement).\n")
    w("| Route | " + " | ".join(b3["objectives"]) + " | " + " | ".join(b3["weight_sets"]) + " | Old A = 2: " + ", ".join(b3["weight_sets"]) + " |")
    w("|---|" + "---|" * (len(b3["objectives"]) + len(b3["weight_sets"]) + 1))
    for rk, r in b3["routes"].items():
        sc = dict(r["scores"])
        w(f"| {r['label']} | " + " | ".join(str(sc[o]) for o in b3["objectives"]) + " | "
          + " | ".join(f"{b3_new[k][rk]:.0f}" for k in b3["weight_sets"]) + " | " + ", ".join(f"{b3_old[k][rk]:.0f}" for k in b3["weight_sets"]) + " |")
    best = {k: [r for r, v in t.items() if v == max(t.values())] for k, t in b3_new.items()}
    w("\nBest route per weight set (corrected): " + "; ".join(f"{k}: {', '.join(v)}" for k, v in best.items())
      + ". With A = 1, route C (cooperative) ranks first under equal weights (8) and doubled durability (11), and **ties** route A under doubled regulator readiness (9 each); the old claim that route A ranks first when readiness is valued more no longer holds. "
      "Every SMR route scores 5-8 of 12 against 12 for non-nuclear options. The MCDA legal input (best SMR route under equal weights = 8) is the same with A = 1 or 2.\n")

    w("## 9. Reading\n")
    top = {k: ranking(T)[0] for k, T in base_T.items()}
    w("- Ranking per weight set: " + "; ".join(f"**{k}**: {rank_str(T)}" for k, T in base_T.items()) + ".")
    n_top = sum(x["top_changed"] for x in pert)
    flips = "; ".join(f"{x['set']} {x['tag']} ({x['order']})" for x in pert if x["top_changed"])
    w(f"- Firmed renewables rank first under all four weight sets. Of {len(pert)} +/-50% changes, {n_top} change first place ({flips or 'none'}): both in the firm-and-sovereign set, and both hand first place to the status quo, not to the SMR. No change puts an SMR option above renewables.")
    w(f"- The SMR beats renewables only on life-cycle CO2e (4.2 vs 30 g/kWh) and supply concentration (enrichment HHI 3,009 vs at least 6,400 for PV), and loses on CO2e avoided per dollar ({M['VRE']['avoided_per_dollar'] / M['SMR']['avoided_per_dollar']:.1f}x), cost ({M['SMR']['cost'] / M['VRE']['cost']:.1f}x), time ({M['SMR']['time'] - M['VRE']['time']:.0f} years later), social licence and legal feasibility. An SMR option ranks first only if life-cycle CO2e carries at least {thresh['lifecycle']:.0%} of the weight.")
    w("- The status quo takes second place on local scales because its conventions (no new cost, no new supply chain, no legal change) score full marks on three criteria. On fixed global scales the SMR moves above the status quo under every set (section 6), so the SMR-vs-status-quo order is a scaling artefact; renewables first is not.")
    w("- SMR + C1 and SMR are indistinguishable in the MCDA under both C1 cases: C1 is worth doing only as a schedule-neutral add-on, never a reason to choose the SMR.")
    w("- Translation to practice: no single non-carbon criterion can carry an SMR to first place (section 5 thresholds: 'never' for all six), because renewables or the status quo beat it on each. "
      "An Australian SMR at Liddell therefore needs three things at once before it is competitive in this frame: a cost gap closed to near renewables, first power well before 2040, and the legal and consent barriers removed first (B3 route C; T13 R2/R3). "
      "Until then the MCDA points to the same money on firmed renewables for Australia, with SMRs kept under review against Darlington's outturn cost.\n")
    w("## 10. Gaps\n")
    w("- TRL and Leroy's first-power dates (§4.1) not yet in the repo: time criterion uses CSIRO 2040 [TO VERIFY: Leroy §4.1].")
    w("- C1 saving for new_2200 is a placeholder until the team member's re-based LCA lands; the life-cycle denominator changes with it.")
    w("- Renewables supply HHI uses PV only (batteries, wind turbines, transmission not assessed); IEA 2022 not opened.")
    w("- Social, legal and weight sets are our judgement, not elicited from stakeholders. DCLG manual not opened (gov.uk blocked).")
    OUT_MD.write_text("\n".join(L) + "\n")
    print("\n".join(f"{k}: {rank_str(T)}" for k, T in base_T.items()))
    print("first-share", first_share, "smr>vre", p_smr_over_vre, "thresh", thresh)


def p_get(name, key="value"):
    return float(sm.P[name][key])


if __name__ == "__main__":
    main()
