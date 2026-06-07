\# Forensic Ancestry Benchmark



Benchmarking machine learning and population genetics methods for forensic ancestry inference from degraded SNP profiles.



\## Aim



This project evaluates how SNP dropout affects forensic ancestry prediction using ancestry-informative SNP profiles.



\## Methods



Planned methods:



\- PCA + nearest centroid

\- Random Forest

\- XGBoost

\- simulated SNP dropout



\## Data



\- 1000 Genomes Project

\- Kidd Lab 55 AISNP panel





\## Results



The rs2814778 variant showed strong population stratification across the

1000 Genomes reference panel.



The C allele frequency was highest in African populations (96.4%),

intermediate in admixed American populations (7.8%), and nearly absent in

European (0.6%), East Asian (0%), and South Asian (0%) populations.



These findings are consistent with previously reported distributions of the

Duffy-null allele and confirm the validity of the benchmark dataset.



!\[Figure 1](../results/figures/figure1\_rs2814778\_frequency.png)



Figure 1. Frequency of the rs2814778 C allele across 1000 Genomes

superpopulations.





\### SNP Dropout Experiment



Random Forest classification accuracy was evaluated under simulated SNP dropout.



Accuracy remained relatively stable across dropout levels from 0% to 75%, ranging from 21.6% to 23.4%.



!\[Figure 2](../results/figures/figure2\_dropout\_accuracy.png)



Figure 2. Effect of SNP dropout on ancestry classification accuracy.

