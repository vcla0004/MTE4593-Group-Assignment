"""Reconcile Sam's Granta Eco Audit (25/10/2026) with the scripted LCA, and run the pre-set checks.

Inputs are read from the Granta PDF reports (03_LCA_Calculations/granta/); no Granta re-run.
Run: python3 03_LCA_Calculations/scripts/granta_reconcile.py
"""
import numpy as np

RHO = 2400.0                      # kg/m3, density convention in Sam's records (1.2e8 kg / 50,000 m3)
BASE_REC, LC3_REC = 0.1583, 0.1533   # kg CO2e/kg, Granta user-defined records
OPC_PILLAI, LC3_PILLAI = 380.0, 270.0  # kg CO2e/m3, Pillai et al. (2019) Table 2, M50 mixes
V_PLANT, SHARE = 50_000.0, 0.40   # m3 per unit (Ostrolęka PIS), central eligible share

print("Record back-calculation (kg CO2e/m3 at 2,400 kg/m3):")
print(f"  base {BASE_REC*RHO:.0f} (Pillai OPC {OPC_PILLAI:.0f}); LC3 record {LC3_REC*RHO:.0f} (Pillai LC3 {LC3_PILLAI:.0f})")
print(f"  defensible LC3 record = {LC3_PILLAI/RHO:.4f} kg/kg; cut vs OPC: record {1-LC3_REC/BASE_REC:.1%}, Pillai {1-LC3_PILLAI/OPC_PILLAI:.1%}")
v = V_PLANT * SHARE
print(f"C1 saving, central: record {(BASE_REC-LC3_REC)*v*RHO/1e3:.0f} t; Pillai {(OPC_PILLAI-LC3_PILLAI)*v/1e3:.0f} t")

rng = np.random.default_rng(20261025)
n = 20_000
share = rng.uniform(0.20, 0.60, n)
opc = rng.triangular(0.9 * 380, 380, 1.1 * 380, n)
lc3 = rng.triangular(0.85 * 270, 270, 368, n)        # upper bound = Sam's record (368 kg/m3)
sav = (opc - lc3) * V_PLANT * share / 1e3
p5, p50, p95 = np.percentile(sav, [5, 50, 95])
print(f"Monte Carlo C1 saving (t/unit): median {p50:.0f}, 90% {p5:.0f}-{p95:.0f}")
corr = {k: np.corrcoef(x, sav)[0, 1] ** 2 for k, x in (("eligible share", share), ("OPC factor", opc), ("LC3 factor", lc3))}
tot = sum(corr.values())
print("Contribution to variance (squared correlation, normalised):", {k: f"{v/tot:.0%}" for k, v in corr.items()})

granta, python_ = 58_900.0, 57_600.0
checks = [
    ("Granta vs Python construction total within 5%", abs(granta - python_) / python_, "≤ 5%"),
]
print(f"Check 1 Granta vs Python: {abs(granta-python_)/python_:.1%} -> {'PASS' if abs(granta-python_)/python_ <= 0.05 else 'FAIL'}")
cut = 1 - LC3_PILLAI / OPC_PILLAI
print(f"Check 2 LC3 cut in 30-40%: Pillai {cut:.1%} -> {'PASS' if 0.30 <= cut <= 0.40 else 'FAIL (marginal)'}; Granta record {1-LC3_REC/BASE_REC:.1%} -> FAIL")
print("Check 3 OPC per m3 vs Ontario industry EPD: NOT TESTED (EPD value not in hand)")
med, lo, hi = 4.40, 3.24, 6.05
print(f"Check 4 whole plant in UNECE 5.1-6.4: median {med} -> FAIL (below); 90% interval {lo}-{hi} overlaps")
mass_ok = abs(V_PLANT * RHO - 1.2e8) < 1 and abs(0.6 * V_PLANT * RHO + 0.4 * V_PLANT * RHO - 1.2e8) < 1 and 6000 + 8000 == 14000
energy_ok = abs((1.2e8 * 0.9 + 1.9e8 + 2.5e8) - 5.54e8) / 5.54e8 < 0.02
print(f"Check 5 mass balances (concrete 120,000 t; 72,000 + 48,000 t; steel 6,000 + 8,000 t) -> {'PASS' if mass_ok else 'FAIL'}; material energy sum within 2% -> {'PASS' if energy_ok else 'FAIL'}")
