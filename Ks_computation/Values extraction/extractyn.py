import re
import csv
import math

# ========= INPUT / OUTPUT =========
input_file = "total_results_FULL.txt"
output_csv = "YN2000_ka_ks_results.csv"

# ========= REGEX PATTERNS =========
pair_pattern = re.compile(r"PAIR:\s+(.+?)\s+vs\s+(.+)")
yn_header = re.compile(r"\(B\)\s+Yang\s+&\s+Nielsen\s+\(2000\)")
yn_values = re.compile(
    r"^\s*\d+\s+\d+\s+([\d\.]+)\s+([\d\.]+)\s+([\d\.]+)\s+([\d\.]+)\s+([\d\.nan]+)\s+([\d\.nan]+)\s+\+\-\s+([\d\.nan]+)\s+([\d\.nan]+)\s+\+\-\s+([\d\.nan]+)"
)

results = []

current_gene1 = None
current_gene2 = None
inside_yn = False

# ========= PARSING =========
with open(input_file, "r") as f:
    for line in f:
        # Detect gene pair
        pair_match = pair_pattern.search(line)
        if pair_match:
            current_gene1 = pair_match.group(1)
            current_gene2 = pair_match.group(2)
            inside_yn = False
            continue

        # Detect YN2000 block
        if yn_header.search(line):
            inside_yn = True
            continue

        # Extract YN2000 values
        if inside_yn:
            m = yn_values.match(line)
            if m:
                try:
                    omega = float(m.group(5))
                except:
                    omega = math.nan

                try:
                    dN = float(m.group(6))
                except:
                    dN = math.nan

                try:
                    dS = float(m.group(8))
                except:
                    dS = math.nan

                try:
                    kappa = float(m.group(4))
                except:
                    kappa = math.nan

                results.append([
                    current_gene1,
                    current_gene2,
                    dN,
                    dS,
                    omega,
                    kappa
                ])

                inside_yn = False  # One comparison per pair
                continue

# ========= WRITE CSV =========
with open(output_csv, "w", newline="") as out:
    writer = csv.writer(out)
    writer.writerow([
        "gene1",
        "gene2",
        "dN_Ka_YN2000",
        "dS_Ks_YN2000",
        "omega_YN2000",
        "kappa"
    ])
    writer.writerows(results)

print(f"Extraction finished. {len(results)} pairs written to {output_csv}")
