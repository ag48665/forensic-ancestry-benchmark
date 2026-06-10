# Forensic Ancestry Benchmark

Benchmarking ancestry inference from forensic SNP profiles using population genetics and machine learning approaches.

## Overview

This project investigates the utility of ancestry-informative SNPs (AISNPs) for forensic ancestry inference using publicly available population-genetics datasets.

The benchmark focuses on:

* Population differentiation of individual AISNP markers
* Genotype frequency distributions across continental populations
* Effects of SNP dropout on ancestry prediction
* Robustness of ancestry inference under degraded forensic DNA conditions

---

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

| SNP | Gene / Region | Forensic relevance |
|------|------|------|
| rs2814778 | ACKR1 (Duffy) | African ancestry marker |
| rs3827760 | EDAR | East Asian ancestry marker |
| rs1426654 | SLC24A5 | Pigmentation-associated AISNP |
| rs16891982 | SLC45A2 | European pigmentation marker |
| rs12913832 | HERC2/OCA2 | Eye pigmentation marker |

---

## Workflow

1. Download and validate 1000 Genomes metadata
2. Extract target SNPs from chromosome VCF files
3. Generate genotype tables
4. Merge genotypes with population metadata
5. Calculate population genotype frequencies
6. Visualize genotype distributions
7. Evaluate ancestry classification robustness

---

## Key Findings

* Five real AISNPs were extracted from the 1000 Genomes dataset.
* All markers demonstrated substantial population stratification.
* rs2814778 showed strong African specificity.
* rs3827760 showed strong East Asian enrichment.
* rs16891982 showed strong European enrichment.
* Results support the feasibility of ancestry inference using small AISNP panels.

---

## Results

### Population Distribution of Ancestry-Informative SNPs

Five ancestry-informative SNPs were extracted from the 1000 Genomes Phase 3 dataset and evaluated across five continental superpopulations (AFR, AMR, EAS, EUR and SAS).

The rs2814778 variant demonstrated strong African specificity. Homozygous alternative genotypes were observed predominantly in AFR individuals and were nearly absent in EUR, EAS and SAS populations.

The rs3827760 marker showed strong enrichment of the alternative allele in East Asian populations.

The rs1426654 marker displayed substantial population differentiation across continental groups.

The rs16891982 marker exhibited strong enrichment within European populations.

The rs12913832 variant also showed substantial population differentiation, with elevated frequencies of alternative genotypes in European populations.

Together, these findings confirm that a small AISNP panel captures substantial continental population structure within the 1000 Genomes reference dataset.

---

## Example Figures

### rs2814778 (ACKR1)

![rs2814778](results/plots/rs2814778.png)

### rs3827760 (EDAR)

![rs3827760](results/plots/rs3827760.png)

---

## Population Stratification

All five AISNPs demonstrated substantial differences in genotype frequencies across continental populations.

Examples:

* rs2814778 strongly differentiates African populations.
* rs3827760 strongly differentiates East Asian populations.
* rs16891982 shows strong European enrichment.
* Multiple AISNPs provide complementary ancestry information.

---

## SNP Dropout Experiment

Random Forest ancestry classification was evaluated under simulated SNP dropout conditions.

Classification performance remained relatively stable across increasing dropout levels, demonstrating the challenges of ancestry prediction using limited marker sets.

---

## Conclusions

A small panel of five ancestry-informative SNPs successfully reproduced known continental population structure in the 1000 Genomes dataset.

The results validate the analytical workflow and support further development of machine-learning-based forensic ancestry prediction models using larger AISNP panels and degraded genotype profiles.

---

## Repository Structure

```text
data/
metadata/
results/
scripts/
manuscript/
