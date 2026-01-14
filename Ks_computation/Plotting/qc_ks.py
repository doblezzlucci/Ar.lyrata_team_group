import pandas as pd
import numpy as np

# ======================
# INPUT
# ======================
csv_file = "YN2000_ka_ks_results.csv"

# ======================
# LOAD DATA
# ======================
df = pd.read_csv(csv_file)
df["dS_Ks_YN2000"] = pd.to_numeric(df["dS_Ks_YN2000"], errors="coerce")

ks = df["dS_Ks_YN2000"]
total = len(ks)

# ======================
# NON-OVERLAPPING COUNTS
# ======================
n_nan = ks.isna().sum()
n_99 = (ks == 99).sum()
n_gt_10_real = ((ks > 10) & (ks < 99)).sum()
n_5_10 = ((ks > 5) & (ks <= 10)).sum()
n_0_5 = ((ks >= 0) & (ks <= 5)).sum()

# ======================
# CLEAN KS FOR STATS
# ======================
ks_clean = ks.dropna()
ks_clean = ks_clean[ks_clean != 99]
ks_clean = ks_clean[ks_clean <= 5]

# ======================
# STATISTICS
# ======================
mean_ks = ks_clean.mean()
std_ks = ks_clean.std()

# ======================
# REPORT
# ======================
print("\n=== Ks QUALITY CONTROL REPORT ===\n")

print(f"Total gene pairs processed        : {total}")

print("\n--- Ks category counts ---")
print(f"Ks == 99 (yn00 saturation)        : {n_99}")
print(f"10 < Ks < 99                     : {n_gt_10_real}")
print(f"5 < Ks ≤ 10                      : {n_5_10}")
print(f"0 ≤ Ks ≤ 5                       : {n_0_5}")

print("\n--- Ks statistics (0 ≤ Ks ≤ 5, Ks ≠ 99) ---")
print(f"Number of Ks used                : {len(ks_clean)}")
print(f"Mean Ks                          : {mean_ks:.4f}")
print(f"Standard deviation Ks            : {std_ks:.4f}")

print("\n========================================\n")
