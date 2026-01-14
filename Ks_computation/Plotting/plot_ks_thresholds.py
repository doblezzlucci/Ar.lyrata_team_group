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
ks = ks[ks != 99]  # remove yn00 saturation

print(f"Total numeric Ks (≠99): {len(ks)}")

# ======================
# COMMON PARAMETERS
# ======================
bin_width = 0.02
thresholds = [5, 10, 20]

# ======================
# PLOTTING
# ======================
for thr in thresholds:
    ks_thr = ks[ks <= thr]
    bins = np.arange(0, thr + bin_width, bin_width)

    print(f"Ks ≤ {thr}: {len(ks_thr)} values")

    plt.figure(figsize=(10, 6))

    plt.hist(
        ks_thr,
        bins=bins,
        color="lightblue",
        edgecolor="black",
        linewidth=0.25,
        alpha=0.6
    )

    plt.xlabel("Ks (synonymous substitutions per site)", fontsize=12)
    plt.ylabel("Frequency (number of gene pairs)", fontsize=12)
    plt.title(f"Ks distribution (YN2000, Ks ≤ {thr}, Ks ≠ 99)", fontsize=14)

    plt.tight_layout()
    plt.savefig(f"Ks_distribution_YN2000_Ks_le_{thr}.png", dpi=300)
    plt.show()
