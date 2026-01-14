import sys
import itertools

# Input and Output files
input_file = "gene_families_filtered.tsv"
output_file = "pairs_clean.tsv"

# Dictionary to store families: {family_id: [gene1, gene2, ...]}
families = {}

print(f"Reading {input_file}...")

with open(input_file, 'r') as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) >= 2:
            gene = parts[0]
            family = parts[1]
            if family not in families:
                families[family] = []
            families[family].append(gene)

print(f"Found {len(families)} families. Generating pairs...")

count = 0
with open(output_file, 'w') as out:
    for fam_id, genes in families.items():
        # Generate all unique pairs (combinations of 2)
        for g1, g2 in itertools.combinations(genes, 2):
            out.write(f"{g1}\t{g2}\n")
            count += 1

print(f"Done! Generated {count} pairs in '{output_file}'.")
