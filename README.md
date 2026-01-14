# Arabidopsis Lyrata comparative Analysis 

## Transposable elements analysis 

for  transposable elements the analysis  was run   for each of the 8 chromosome file  of Arabidopsis lyrata 
and also  toplevel assembly on Arabidopsis Lyrata And Arabidopsis Thaliana .
All the scripts for downstream analysis would be performed on saved on files folder for each of the 8 chromosome of A.Lyrata as well as A.lyrata toplevelel genome assembly (All lyrata)  and A.thaliana toplevelel genome assembly folders  (All thaliana)

 ### TE distribution 
 
The R notebook "TE_distribution.Rmd "  runs on RepeatMasker output file ( Galaxy_statitics.txt)  would generate TE distribution plots for families 

### Kimura plot

The R notebook "Kimura_plot.Rmd "  runs on RepeatMasker output file (Galaxy_catalogue.txt)  would generate Kimura plot divergences  for most abundant families of LTR (Gypsy and Copia) 

###  LTR insertion according to chromosome positions 

The R notebook "Inerstion_deltion_LTR_counts_plot__lyrata.Rmd "  run on RepeatMasker output file (Galaxy_output_log.tabular)  would generate Inerstion and deltion of LTR_counts 
plot as well as the fraction of insertion in a chromosome position   and fraction of insertion in a chromosome position according to the kimura score plot   

## Ks computation

The `Ks_computation/` directory contains the complete computational workflow
used to estimate synonymous substitution rates (Ks) between paralogous gene
pairs in *Arabidopsis lyrata*.

This analysis follows a codon-based maximum likelihood framework
(PAML yn00; Yang & Nielsen, 2000) and is used to reconstruct the duplication
history of the genome by identifying signatures of ancient gene and
whole-genome duplication events.

### Pipeline overview

The workflow is structured into the following main steps:

1. **Pairs Generation** – exhaustive generation of paralogous gene pairs
   from MCL gene families
2. **Main Computation** – protein alignment (MUSCLE), codon alignment
   (PAL2NAL), and Ka/Ks estimation using PAML yn00
3. **Values extraction** – parsing and formatting of raw Ks outputs
4. **Plotting** – genome-wide Ks distribution analysis and visualization

For full technical details, parameters, and biological interpretation,
see [`Ks_computation/README.md`](Ks_computation/README.md).
