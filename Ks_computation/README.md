Ks Computation – Arabidopsis lyrata
Overview

This directory contains the complete computational workflow used to estimate synonymous substitution rates (Ks) between paralogous gene pairs in Arabidopsis lyrata.
The analysis aims to reconstruct the duplication history of the genome by identifying signatures of ancient gene and whole-genome duplication (WGD) events through genome-wide Ks distributions.

Directory Structure
Ks_computation/
├── Pairs Generation/
├── Main Computation/
├── Values extraction/
├── Plotting/


Each folder corresponds to a well-defined step of the pipeline described below.

Pipeline Description
STEP 1 — Proteome Cleaning and Isoform Verification

Prior to duplication analysis, the A. lyrata proteome was filtered to retain only chromosome-anchored proteins.
Scaffold-derived sequences were excluded, and the dataset was verified to ensure that each gene was represented by a single isoform.

Results:

Total protein entries: 32,667

Chromosome-mapped proteins: 31,478

Scaffold proteins excluded: 1,189

STEP 2 — Homology Detection and Gene Family Clustering

An all-versus-all BLASTp search was performed on the cleaned proteome to identify homologous protein pairs.
BLAST hits were filtered using the following thresholds:

Sequence identity ≥ 30%

Alignment coverage ≥ 50%

Filtered homologous pairs were clustered into gene families using the Markov Cluster Algorithm (MCL) with an inflation parameter of I = 2.0.

Results:

Number of MCL gene families: 4,162

Total genes assigned to families: 27,611

STEP 3 — Paralogous Pair Generation (Pairs Generation/)

For each MCL gene family, all possible pairwise combinations of genes were generated using a Python script based on the itertools.combinations method.

This exhaustive strategy was used to capture the full duplication history of the genome.

Results:

930,717 unique paralogous gene pairs

Output file containing ~1.86 million gene ID entries

STEP 4 — Ks Computation Pipeline (Main Computation/)

Synonymous (Ks) and non-synonymous (Ka) substitution rates were computed for all paralogous gene pairs using an automated shell-based pipeline.

For each gene pair, the following steps were executed:

Extraction of protein and CDS sequences from genome-wide FASTA files

Protein sequence alignment using MUSCLE

Conversion to codon-based nucleotide alignment using PAL2NAL

Estimation of Ka and Ks values using PAML yn00, following the
Yang & Nielsen (2000) codon-based maximum likelihood model

Input files:

Paralog pair list

Protein FASTA file

CDS FASTA file

yn00.ctl control file

Output:

final_results_FULL.txt: raw cumulative Ka/Ks results for the entire genome

STEP 5 — Values Extraction (Values extraction/)

Raw PAML output files were parsed using a dedicated Python script to extract:

Ks (synonymous substitution rate)

Ka (non-synonymous substitution rate)

Ka/Ks ratio (ω)

The extracted values were stored in a clean tabular format for downstream analysis.

Output:

final_ks_results.csv

A quality-control step was performed to inspect the distribution and basic statistics of the obtained Ks values.

STEP 6 — Ks Distribution Analysis and Plotting (Plotting/)

Genome-wide Ks distributions were generated using all validated paralogous gene pairs.

This step included:

Removal of saturated values (e.g. Ks > 5 or Ks = 99)

High-resolution visualization using a large number of bins

Identification of peaks corresponding to ancient duplication events

Final output:

Arabidopsis_Lyrata_Whole_Genome_Ks_Final.png

Biological Interpretation

The resulting Ks distribution reveals two major peaks:

Ks ≈ 0.8, corresponding to the At-α whole-genome duplication event

Ks ≈ 1.8, corresponding to the At-β duplication event

These results are consistent with previously published evolutionary models of the Arabidopsis lineage and support the role of polyploidy in shaping the genome of Arabidopsis lyrata.
