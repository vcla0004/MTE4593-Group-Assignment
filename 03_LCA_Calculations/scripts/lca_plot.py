# Rubric coverage: R5.2, R2.4
"""Common chart style for F1-F5 (one palette and style for the report and slides; plan section 3)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Reference categorical palette (light mode), fixed order; text never wears series colour.
BLUE, ORANGE, AQUA, YELLOW, MAGENTA, GREEN, VIOLET, RED = (
    "#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#6250d6", "#e34948")
INK, INK2, MUTED, GRID, SURFACE = "#0b0b0b", "#52514e", "#8a8984", "#e4e3df", "#ffffff"


def style():
    plt.rcParams.update({
        "figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "savefig.facecolor": SURFACE,
        "font.family": "DejaVu Sans", "font.size": 9.5,
        "axes.edgecolor": GRID, "axes.labelcolor": INK2, "axes.titlecolor": INK,
        "axes.titlesize": 11, "axes.titleweight": "bold", "axes.titlelocation": "left",
        "xtick.color": INK2, "ytick.color": INK2, "axes.grid": True, "grid.color": GRID,
        "grid.linewidth": 0.6, "axes.spines.top": False, "axes.spines.right": False,
        "legend.frameon": False, "legend.fontsize": 9,
    })


def save(fig, path, source_note=None):
    if source_note:
        fig.text(0.01, -0.035, source_note, fontsize=7.5, color=MUTED, ha="left", va="bottom")
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)


# Plain-English labels for parameters in charts and tables (review.md section 6 point 9; no variable names on figures)
LABELS = {
    "net_mwe": "Net output (MWe)",
    "capacity_factor": "Capacity factor",
    "design_life_yr": "Design life (years)",
    "concrete_intensity_m3_per_mwe": "Plant concrete (m³ per MWe)",
    "ostroleka_concrete_m3": "Plant concrete per unit (m³)",
    "ostroleka_steel_t": "Plant steel per unit (t)",
    "ef_concrete_opc_kg_per_m3": "OPC concrete factor (kg CO₂e/m³)",
    "c1_lc3_concrete_cut": "LC³ cut in concrete emissions",
    "c1_eligible_share": "Share of concrete eligible for LC³",
    "steel_intensity_t_per_mwe": "Plant steel (t per MWe)",
    "rebar_ratio_t_per_m3": "Rebar ratio (t per m³ concrete)",
    "forebay_concrete_m3": "Forebay shaft concrete (m³)",
    "rb_shaft_depth_m": "Reactor-building shaft depth (m)",
    "rb_basemat_thickness_m": "DPSC basemat infill thickness (m)",
    "rb_wall_thickness_m": "DPSC shaft-wall infill thickness (m)",
    "binder_scc_kg_per_m3": "Infill (SCC) binder content (kg/m³)",
    "binder_conv_kg_per_m3": "Structural concrete binder content (kg/m³)",
    "ef_gu_cement": "GU cement factor (kg CO₂e/t)",
    "ef_slag": "Slag cement factor (kg CO₂e/t)",
    "ef_concrete_other_kg_per_m3": "Aggregates, water, batching (kg CO₂e/m³)",
    "clinker_factor_gu": "Clinker in GU cement (t/t)",
    "slag_replacement_s1": "Slag share of binder (S1)",
    "lc3_clinker_factor": "Clinker in LC3 (t/t)",
    "lc3_gwp_reduction": "LC3 cut in binder emissions",
    "lc3_binder_uplift": "Extra binder LC3 needs to flow",
    "ef_rebar": "Rebar factor (t CO₂e/t)",
    "ef_plate_other": "Plate and equipment steel factor (t CO₂e/t)",
    "transport_concrete_km": "Concrete haul distance (km)",
    "transport_steel_km": "Steel haul distance (km)",
    "ef_truck_kg_per_tkm": "Truck factor (kg CO₂e per t-km)",
    "construction_other_uplift": "Other construction materials and site energy (uplift)",
    "enrichment_pct": "Fuel enrichment (% U-235)",
    "tails_assay_pct": "Enrichment tails assay (% U-235)",
    "burnup_gwd_per_t": "Fuel burnup (GWd/t)",
    "ef_mining_milling_kg_per_kgU3O8": "Mining and milling (kg CO₂e/kg U₃O₈)",
    "conversion_elec_kwh_per_kgU": "Conversion electricity (kWh/kg U)",
    "conversion_heat_kwh_per_kgU": "Conversion heat (kWh/kg U)",
    "conversion_grid_kg_per_kwh": "Conversion-plant grid (kg CO₂e/kWh)",
    "enrich_kwh_per_swu": "Centrifuge energy (kWh/SWU)",
    "enrich_grid_kg_per_kwh": "Enrichment-plant grid (kg CO₂e/kWh)",
    "fab_kwh_per_kgU": "Fabrication energy (kWh/kg U)",
    "fab_grid_kg_per_kwh": "Fabrication-plant grid (kg CO₂e/kWh)",
    "om_g_per_kwh": "Operation and maintenance (g/kWh)",
    "decom_g_per_kwh": "Decommissioning (g/kWh)",
    "backend_g_per_kwh": "Back end: spent fuel and disposal (g/kWh)",
}


def label(name):
    return LABELS.get(name, name)
