# Rubric coverage: R2.1, R2.2, R2.3, R2.4, R2.5, R2.6, R2.7, RB.5
"""Shared life-cycle model for one BWRX-300 at Darlington (section 6, Appendices A, C, D).

Imported by lca_baseline.py, lca_scenarios.py and lca_uncertainty.py. Reads parameters_lca.yaml only.
Functional unit: 1 MWh net electricity delivered at the plant's grid connection.
Reference flow: one BWRX-300 unit over its design life.

All emissions are kg CO2e unless noted; g CO2e/kWh == kg CO2e/MWh.

Stages
  construction  = (concrete + steel + transport) x (1 + construction_other_uplift)
  fuel front end = mining & milling + conversion + enrichment + fabrication   (bottom-up per kg U)
  O&M, decommissioning, back end = literature g/kWh (EDF 2024 shares, transferred)

Inventory basis (re-based 25/10/2026)
  basis="ostroleka" (MAIN, default): whole-plant quantities from the Ostrołęka BWRX-300 PIS (2023, Table 14):
      ostroleka_concrete_m3 and ostroleka_steel_t; all plant concrete at Pillai et al. (2019) OPC factor
      ef_concrete_opc_kg_per_m3 (per m3, all constituents). C1 target = c1_eligible_share of the plant concrete,
      LC3 cuts its per-m3 factor by c1_lc3_concrete_cut (1 - 270/380 at the central values).
  basis="bottomup" (CROSS-CHECK): the 21/10 model below (ESBWR-scaled 69 m3/MWe, binder-level factors,
      C1 targets = DPSC infill geometry + forebay shaft).

Scenarios (bottom-up basis: concrete of the C1 target structures only: DPSC reactor-building infill + forebay shaft;
main basis: the eligible share of plant concrete)
  S0  baseline, GU (Portland) cement binder
  S1  slag blend, slag_replacement_s1 of binder
  S2  LC3 (LC3-50) binder: GWP cut lc3_gwp_reduction, binder content x (1 + lc3_binder_uplift)
  S2b S2 in the target structures + S1 slag blend in all other plant concrete (upper bound, lever L1)
  S3lo / S3hi  baseline concrete with all steel at the low (EAF, high recycled content) / high
               (world-average, BOF-heavy) factors: the steel recycled-content sensitivity.
               S3lo is an UPPER BOUND: it puts all plant steel (incl. forgings and nuclear plate) on
               best-practice EAF sections factors.
  S3lfl        like-for-like S3 (steel_target_saving): the same low-end factors applied only to the known
               steel in the C1 target structures (DPSC basemat module plate + forebay rebar)
  S0slag       counterfactual baseline if OPG's mixes already contain slag: slag blend in ALL concrete.
               LC3's increment over it = S0slag - S2b (LC3 in targets, slag elsewhere)
"""
from math import pi, log
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
PARAMS_FILE = ROOT / "parameters_lca.yaml"
CONCRETE_DENSITY_T_PER_M3 = 2.4   # same density Sam used (9.6 million kg / 4,000 m3); README confirms the arithmetic
HOURS_PER_YEAR = 8760
MAIN_BASIS = "ostroleka"
BASES = ("ostroleka", "bottomup")


def load_raw():
    return yaml.safe_load(PARAMS_FILE.read_text())["parameters"]


def central(raw=None):
    raw = raw or load_raw()
    return {k: float(v["value"]) for k, v in raw.items()}


def varied_names(raw=None):
    """Parameters that carry a range (used by the tornado and the Monte Carlo)."""
    raw = raw or load_raw()
    out = []
    for k, v in raw.items():
        if k.startswith(("bm_", "mc_", "units_")):
            continue
        if v.get("dist", "tri") == "fixed":
            continue
        if float(v["low"]) == float(v["high"]):
            continue
        out.append(k)
    return out


def value_fn(x):
    """Separative potential V(x) = (2x - 1) ln(x / (1 - x))."""
    return (2 * x - 1) * log(x / (1 - x))


def enrichment_balance(xp_pct, xf_pct, xt_pct):
    xp, xf, xt = xp_pct / 100, xf_pct / 100, xt_pct / 100
    feed = (xp - xt) / (xf - xt)              # kg natural U per kg enriched U
    tails = feed - 1
    swu = value_fn(xp) + tails * value_fn(xt) - feed * value_fn(xf)   # kg-SWU per kg enriched U
    return feed, swu


def volumes(p):
    d, tb, tw, h = p["rb_shaft_diameter_m"], p["rb_basemat_thickness_m"], p["rb_wall_thickness_m"], p["rb_shaft_depth_m"]
    v_basemat = pi / 4 * d ** 2 * tb
    v_wall = pi * (d - tw) * tw * h           # annulus of mean diameter (d - tw)
    v_dpsc = v_basemat + v_wall
    v_forebay = p["forebay_concrete_m3"]
    v_scaled = p["concrete_intensity_m3_per_mwe"] * p["net_mwe"]
    v_total = max(v_scaled, v_dpsc + v_forebay)
    return {
        "basemat": v_basemat, "wall": v_wall, "dpsc": v_dpsc, "forebay": v_forebay,
        "target": v_dpsc + v_forebay, "scaled": v_scaled, "total": v_total,
        "other": v_total - v_dpsc - v_forebay, "clipped": v_scaled < v_dpsc + v_forebay,
    }


def binder_share_conv(p):
    """Share of a conventional GU concrete's per-m3 GWP that comes from the binder (bottom-up mix)."""
    b = p["binder_conv_kg_per_m3"] * p["ef_gu_cement"] / 1000
    return b / (b + p["ef_concrete_other_kg_per_m3"])


def main_mix_factor(p, mix):
    """Main basis: (kg CO2e per m3, t clinker per m3) for OPC (GU), LC3 or SLAG concrete.
    LC3: Pillai per-m3 cut. SLAG (fallback): the bottom-up slag blend's binder-level cut, scaled by the binder share.
    Clinker per m3 is indicative: it uses the bottom-up conventional binder content (Pillai's M50 binder TO VERIFY)."""
    ef = p["ef_concrete_opc_kg_per_m3"]
    b = p["binder_conv_kg_per_m3"] / 1000
    if mix == "GU":
        return ef, b * p["clinker_factor_gu"]
    if mix == "LC3":
        return ef * (1 - p["c1_lc3_concrete_cut"]), b * (1 + p["lc3_binder_uplift"]) * p["lc3_clinker_factor"]
    if mix == "SLAG":
        s = p["slag_replacement_s1"]
        cut = binder_share_conv(p) * s * (1 - p["ef_slag"] / p["ef_gu_cement"])
        return ef * (1 - cut), b * (1 - s) * p["clinker_factor_gu"]
    raise ValueError(mix)


def main_block(p, vol_m3, mix):
    ef, cl = main_mix_factor(p, mix)
    return {"vol": vol_m3, "binder_t": vol_m3 * p["binder_conv_kg_per_m3"] / 1000, "clinker_t": vol_m3 * cl, "kg": vol_m3 * ef}


def volumes_main(p):
    tot = p["ostroleka_concrete_m3"]
    elig = p["c1_eligible_share"] * tot
    return {"total": tot, "target": elig, "other": tot - elig, "scaled": tot, "dpsc": 0.0, "forebay": 0.0,
            "basemat": 0.0, "wall": 0.0, "clipped": False}


def binder_gwp_and_clinker(p, mix):
    """kg CO2e per t binder, t clinker per t binder, binder-content multiplier."""
    gu = p["ef_gu_cement"]
    if mix == "GU":
        return gu, p["clinker_factor_gu"], 1.0
    if mix == "SLAG":
        s = p["slag_replacement_s1"]
        return (1 - s) * gu + s * p["ef_slag"], (1 - s) * p["clinker_factor_gu"], 1.0
    if mix == "LC3":
        return gu * (1 - p["lc3_gwp_reduction"]), p["lc3_clinker_factor"], 1 + p["lc3_binder_uplift"]
    raise ValueError(mix)


def concrete_block(p, vol_m3, binder_kg_m3, mix):
    ef_b, cf, mult = binder_gwp_and_clinker(p, mix)
    binder_t = vol_m3 * binder_kg_m3 * mult / 1000
    gwp = binder_t * ef_b + vol_m3 * p["ef_concrete_other_kg_per_m3"]
    return {"vol": vol_m3, "binder_t": binder_t, "clinker_t": binder_t * cf, "kg": gwp}


SCENARIO_MIX = {          # (target-structure mix, other-concrete mix, steel case)
    "S0": ("GU", "GU", "central"),
    "S1": ("SLAG", "GU", "central"),
    "S2": ("LC3", "GU", "central"),
    "S2b": ("LC3", "SLAG", "central"),
    "S3lo": ("GU", "GU", "low"),
    "S3hi": ("GU", "GU", "high"),
    "S0slag": ("SLAG", "SLAG", "central"),
}


def model(p, scenario="S0", raw=None, basis=MAIN_BASIS):
    tgt_mix, oth_mix, steel_case = SCENARIO_MIX[scenario]
    # ---- lifetime output ----
    mwh_yr = p["net_mwe"] * HOURS_PER_YEAR * p["capacity_factor"]
    mwh_life = mwh_yr * p["design_life_yr"]
    eta = p["net_mwe"] / p["thermal_mwt"]

    # ---- concrete ----
    if basis == "ostroleka":
        v = volumes_main(p)
        c_dpsc = main_block(p, v["target"], tgt_mix)          # "target" = eligible share (non-safety works first)
        c_fore = main_block(p, 0.0, tgt_mix)
        c_oth = main_block(p, v["other"], oth_mix)
        steel_t = p["ostroleka_steel_t"]
    elif basis == "bottomup":
        v = volumes(p)
        c_dpsc = concrete_block(p, v["dpsc"], p["binder_scc_kg_per_m3"], tgt_mix)
        c_fore = concrete_block(p, v["forebay"], p["binder_conv_kg_per_m3"], tgt_mix)
        c_oth = concrete_block(p, v["other"], p["binder_conv_kg_per_m3"], oth_mix)
        steel_t = p["steel_intensity_t_per_mwe"] * p["net_mwe"]
    else:
        raise ValueError(basis)
    concrete_kg = c_dpsc["kg"] + c_fore["kg"] + c_oth["kg"]

    # ---- steel ----
    if steel_case == "central":
        ef_r, ef_o = p["ef_rebar"], p["ef_plate_other"]
    else:
        raw = raw or load_raw()
        ef_r, ef_o = float(raw["ef_rebar"][steel_case]), float(raw["ef_plate_other"][steel_case])
    rebar_t = min(p["rebar_ratio_t_per_m3"] * v["total"], steel_t)
    other_steel_t = steel_t - rebar_t
    rebar_kg = rebar_t * ef_r * 1000
    plate_kg = other_steel_t * ef_o * 1000

    # ---- transport (A4) ----
    conc_t = v["total"] * CONCRETE_DENSITY_T_PER_M3
    transport_kg = (conc_t * p["transport_concrete_km"] + steel_t * p["transport_steel_km"]) * p["ef_truck_kg_per_tkm"]

    bulk_kg = concrete_kg + rebar_kg + plate_kg + transport_kg
    other_constr_kg = bulk_kg * p["construction_other_uplift"]
    construction_kg = bulk_kg + other_constr_kg

    # ---- fuel front end (per MWh) ----
    kwh_e_per_kgU = p["burnup_gwd_per_t"] * 24000 * eta          # 1 GWd/tU = 24,000 kWh_th per kg U
    encU_kg_per_mwh = 1000 / kwh_e_per_kgU
    feed, swu = enrichment_balance(p["enrichment_pct"], p["feed_assay_pct"], p["tails_assay_pct"])
    natU_kg_per_mwh = encU_kg_per_mwh * feed
    swu_per_mwh = encU_kg_per_mwh * swu
    mining = natU_kg_per_mwh * p["ef_mining_milling_kg_per_kgU3O8"] / p["u3o8_u_mass_fraction"]
    conversion = natU_kg_per_mwh * (p["conversion_elec_kwh_per_kgU"] * p["conversion_grid_kg_per_kwh"]
                                    + p["conversion_heat_kwh_per_kgU"] * p["ef_natgas_heat_kg_per_kwh"])
    enrichment = swu_per_mwh * p["enrich_kwh_per_swu"] * p["enrich_grid_kg_per_kwh"]
    fabrication = encU_kg_per_mwh * p["fab_kwh_per_kgU"] * p["fab_grid_kg_per_kwh"]

    g = {   # g CO2e per kWh by stage
        "Construction: concrete": concrete_kg / mwh_life,
        "Construction: rebar": rebar_kg / mwh_life,
        "Construction: plate, structural and equipment steel": plate_kg / mwh_life,
        "Construction: transport to site": transport_kg / mwh_life,
        "Construction: other materials and site energy": other_constr_kg / mwh_life,
        "Fuel: mining and milling": mining,
        "Fuel: conversion": conversion,
        "Fuel: enrichment": enrichment,
        "Fuel: fabrication": fabrication,
        "Operation and maintenance": p["om_g_per_kwh"],
        "Decommissioning": p["decom_g_per_kwh"],
        "Back end: spent fuel and disposal": p["backend_g_per_kwh"],
    }
    total_g = sum(g.values())
    return {
        "scenario": scenario, "basis": basis, "mwh_yr": mwh_yr, "mwh_life": mwh_life, "eta": eta,
        "vol": v, "c_dpsc": c_dpsc, "c_fore": c_fore, "c_oth": c_oth, "concrete_kg": concrete_kg,
        "steel_t": steel_t, "rebar_t": rebar_t, "other_steel_t": other_steel_t,
        "rebar_kg": rebar_kg, "plate_kg": plate_kg, "transport_kg": transport_kg,
        "bulk_kg": bulk_kg, "other_constr_kg": other_constr_kg, "construction_kg": construction_kg,
        "target_concrete_kg": c_dpsc["kg"] + c_fore["kg"],
        "target_clinker_t": c_dpsc["clinker_t"] + c_fore["clinker_t"],
        "all_clinker_t": c_dpsc["clinker_t"] + c_fore["clinker_t"] + c_oth["clinker_t"],
        "feed": feed, "swu_per_kg": swu, "encU_kg_per_mwh": encU_kg_per_mwh,
        "natU_kg_per_mwh": natU_kg_per_mwh, "swu_per_mwh": swu_per_mwh,
        "g": g, "total_g": total_g, "total_t_life": total_g * mwh_life / 1000,
        "construction_g": construction_kg / mwh_life,
        "fuel_g": mining + conversion + enrichment + fabrication,
    }


def lc3_saving(p, raw=None, scenario="S2", basis=MAIN_BASIS):
    """Saving vs S0 for one unit: t CO2e (concrete A1-A3 only), clinker avoided t, % of the S0 life cycle.

    The construction uplift scales bulk materials for unmodelled items; it is NOT applied to the saving, because
    changing the binder does not change copper, cabling or site energy. The saving is therefore the change in
    concrete A1-A3 only (transport is unchanged by binder choice).
    """
    b, s = model(p, "S0", raw, basis), model(p, scenario, raw, basis)
    t = (b["concrete_kg"] - s["concrete_kg"]) / 1000
    clinker = b["all_clinker_t"] - s["all_clinker_t"]
    return {"t_per_unit": t, "clinker_t_per_unit": clinker,
            "pct_life_cycle": 100 * t / b["total_t_life"],
            "pct_target_concrete": 100 * t / (b["target_concrete_kg"] / 1000),
            "g_per_kwh": t * 1000 / b["mwh_life"],
            "base": b, "scen": s}


def steel_target_saving(p, raw=None):
    """Like-for-like S3 (t CO2e per unit): the S3-low steel factors applied only to the known steel in the C1
    target structures, i.e. the DPSC basemat module (plate factor) and the forebay rebar (rebar factor).
    The DPSC shaft-wall plate is not known (no source) and is excluded, so this is a floor for the target steel."""
    raw = raw or load_raw()
    lo_o, lo_r = float(raw["ef_plate_other"]["low"]), float(raw["ef_rebar"]["low"])
    plate = p["dpsc_basemat_steel_t"] * (p["ef_plate_other"] - lo_o)
    rebar = p["forebay_rebar_t"] * (p["ef_rebar"] - lo_r)
    return {"t_per_unit": plate + rebar, "plate_t": plate, "rebar_t": rebar,
            "steel_t": p["dpsc_basemat_steel_t"] + p["forebay_rebar_t"]}


def steel_whole_saving(p, raw=None, scenario="S3lo", basis=MAIN_BASIS):
    """Whole-plant S3 (t CO2e per unit) vs the central steel factors; positive = lower emissions."""
    b, s = model(p, "S0", raw, basis), model(p, scenario, raw, basis)
    return ((b["rebar_kg"] + b["plate_kg"]) - (s["rebar_kg"] + s["plate_kg"])) / 1000


def slag_baseline_counterfactual(p, raw=None, slag_fraction=None, basis=MAIN_BASIS):
    """If S0 already contains slag (all plant concrete at slag_fraction), what LC3 in the targets adds.
    Returns the counterfactual S0 total and LC3's increment (S0slag vs S2b), per unit."""
    q = dict(p)
    if slag_fraction is not None:
        q["slag_replacement_s1"] = slag_fraction
    b0 = model(p, "S0", raw, basis)
    s0 = model(q, "S0slag", raw, basis)
    s2 = model(q, "S2b", raw, basis)
    inc = (s0["concrete_kg"] - s2["concrete_kg"]) / 1000
    return {"slag_fraction": q["slag_replacement_s1"], "s0slag_total_g": b0["total_g"] - (b0["concrete_kg"] - s0["concrete_kg"]) / b0["mwh_life"],
            "s0slag_vs_gu_t": (b0["concrete_kg"] - s0["concrete_kg"]) / 1000,
            "lc3_increment_t": inc, "lc3_increment_pct_life": 100 * inc / (b0["total_t_life"] - (b0["concrete_kg"] - s0["concrete_kg"]) / 1000),
            "lc3_increment_clinker_t": s0["all_clinker_t"] - s2["all_clinker_t"]}


def fmt(x, nd=0):
    if abs(x) >= 1000 and nd == 0:
        return f"{x:,.0f}"
    return f"{x:,.{nd}f}"
