import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ======================
# INPUT
# ======================
csv_file = "YN2000_ka_ks_results.csv"

# ======================
# LOAD & CLEAN Ks
# ======================
df = pd.read_csv(csv_file)
df["dS_Ks_YN2000"] = pd.to_numeric(df["dS_Ks_YN2000"], errors="coerce")

ks = df["dS_Ks_YN2000"].dropna()
ks = ks[ks != 99]   # remove yn00 saturation
ks = ks[ks <= 5]    # biologically interpretable range

print(f"Number of Ks values plotted: {len(ks)}")

# ======================
# HISTOGRAM PARAMETERS
# ======================
bin_width = 0.02
bins = np.arange(0, 5 + bin_width, bin_width)

# ======================
# PLOT (NO KDE)
# ======================
plt.figure(figsize=(10, 6))

plt.hist(
    ks,
    bins=bins,
    color="lightblue",
    edgecolor="black",
    linewidth=0.2,
    alpha=0.7
)

plt.xlabel("Ks (synonymous substitutions per site)", fontsize=12)
plt.ylabel("Frequency (number of gene pairs)", fontsize=12)
plt.title("Ks distribution (Ks ≤ 5)", fontsize=14)

plt.tight_layout()
plt.savefig("Ks_distribution_YN2000_hist_only.png", dpi=300)
plt.show()
