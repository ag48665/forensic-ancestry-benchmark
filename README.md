# Forensic Ancestry Benchmark

Benchmarking ancestry inference from forensic SNP profiles using population genetics and machine learning approaches.

## Overview

This project investigates the performance of ancestry-informative SNPs (AISNPs) for forensic ancestry inference using data from the 1000 Genomes Project.

The benchmark focuses on:

* Population differentiation of individual AISNP markers
* Genotype frequency distributions across continental populations
* Effects of SNP dropout on ancestry prediction
* Robustness of ancestry inference under degraded forensic DNA conditions

## Dataset

### Reference Population Dataset

Source:

* 1000 Genomes Project Phase 3

Superpopulations:

* AFR — African
* AMR — Admixed American
* EAS — East Asian
* EUR — European
* SAS — South Asian

Total individuals:

* 2504 reference samples

### Ancestry Informative Markers

The current benchmark includes:

| SNP        | Gene / Region | Forensic relevance           |
| ---------- | ------------- | ---------------------------- |
| rs2814778  | ACKR1 (Duffy) | African ancestry marker      |
| rs3827760  | EDAR          | East Asian ancestry marker   |
| rs1426654  | SLC24A5       | European pigmentation marker |
| rs16891982 | SLC45A2       | European pigmentation marker |
| rs12913832 | HERC2/OCA2    | Eye pigmentation marker      |

## Workflow

1. Download and validate 1000 Genomes metadata
2. Extract target SNPs from chromosome VCF files
3. Generate genotype tables
4. Merge genotypes with population metadata
5. Calculate population genotype frequencies
6. Visualize genotype distributions
7. Evaluate ancestry classification robustness

## Results

### Population Stratification

All five AISNPs demonstrated substantial differences in genotype frequencies across continental populations.

Examples:

* rs2814778 strongly differentiates African populations
* rs3827760 strongly differentiates East Asian populations
* rs1426654 and rs16891982 show strong European enrichment

### SNP Dropout Experiment

Random Forest ancestry classification was evaluated under simulated SNP dropout conditions.

Classification performance remained relatively stable across increasing dropout levels, demonstrating the challenges of ancestry prediction using limited marker sets.

## Repository Structure

data/

metadata/

results/

scripts/

manuscript/

## Generated Outputs

### Population Tables

* rs2814778_by_population.tsv
* rs3827760_by_population.tsv
* rs1426654_by_population.tsv
* rs16891982_by_population.tsv
* rs12913832_by_population.tsv

### Summary Table

* all_snp_population_genotype_counts.tsv

### Figures

* rs2814778.png
* rs3827760.png
* rs1426654.png
* rs16891982.png
* rs12913832.png

## Future Work

* Principal Component Analysis (PCA)
* Random Forest ancestry classification
* XGBoost ancestry classification
* SNP dropout benchmarking
* Comparison with published forensic AISNP panels
* Validation using additional public datasets

## Author

Agata Gabara

Independent Research Project

## License

MIT License
