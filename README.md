# Forensic Ancestry Benchmark

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20634314.svg)](https://doi.org/10.5281/zenodo.20634314)

Benchmarking machine learning and population genetics methods for forensic ancestry inference.

---

## Overview

This project evaluates the utility of ancestry-informative single nucleotide polymorphisms (AISNPs) for continental ancestry inference using publicly available population genetics datasets.

The study investigates:

* Population differentiation of individual AISNP markers
* Genotype frequency distributions across continental populations
* Population structure captured by a minimal AISNP panel
* Machine-learning-based ancestry classification
* The impact of SNP dropout on ancestry prediction performance

The project serves as a proof-of-concept benchmark for forensic ancestry inference using a small set of highly informative genetic markers.

---

## Dataset

### Reference Population Dataset

Source:

* 1000 Genomes Project Phase 3

Continental superpopulations:

* AFR — African
* AMR — Admixed American
* EAS — East Asian
* EUR — European
* SAS — South Asian

Total reference samples:

* 2,504 individuals

---

## Ancestry-Informative SNP Panel

Five widely studied ancestry-informative SNPs were selected for analysis.

| SNP        | Gene / Region | Forensic Relevance            |
| ---------- | ------------- | ----------------------------- |
| rs2814778  | ACKR1 (Duffy) | African ancestry marker       |
| rs3827760  | EDAR          | East Asian ancestry marker    |
| rs1426654  | SLC24A5       | Pigmentation-associated AISNP |
| rs16891982 | SLC45A2       | European pigmentation marker  |
| rs12913832 | HERC2/OCA2    | Eye pigmentation marker       |

---

## Methods

### Data Processing

Genotype data were obtained from the 1000 Genomes Project Phase 3 release. Target AISNPs were extracted from chromosome-specific VCF files and merged with population metadata.

### Population Frequency Analysis

Genotype frequencies were calculated for each AISNP across all continental superpopulations to evaluate population differentiation.

### Principal Component Analysis

Principal Component Analysis (PCA) was performed using numerically encoded genotypes from the five AISNP markers. PCA was used to assess the extent to which the selected markers capture continental population structure.

### Machine Learning Classification

Four supervised machine-learning models were evaluated:

* Support Vector Machine (SVM)
* Logistic Regression
* Random Forest
* Decision Tree

Models were trained to predict continental ancestry labels and evaluated on a held-out test dataset.

### Feature Importance Analysis

Random Forest feature importance scores were used to estimate the relative contribution of each AISNP to ancestry classification performance.

### SNP Dropout Benchmark

Progressive SNP dropout experiments were performed to evaluate classification robustness under conditions that mimic partial genetic profiles and degraded forensic DNA samples.

---

## Workflow

1. Download and validate 1000 Genomes metadata
2. Extract target AISNPs from VCF files
3. Generate genotype tables
4. Merge genotypes with population metadata
5. Calculate genotype frequencies
6. Visualize population distributions
7. Perform PCA
8. Train machine-learning classifiers
9. Evaluate SNP dropout effects
10. Compare classifier performance

---
## Reproducibility

All analyses can be reproduced from the scripts contained in the repository.

Main benchmark scripts:

- scripts/26_rf_5snp.py
- scripts/32_logistic_regression_5snp.py
- scripts/33_decision_tree_5snp.py
- scripts/37_svm_5snp.py
- scripts/35_rf_cross_validation.py
- scripts/36_cv_model_comparison.py

---
## Results

### Population Differentiation

All five AISNPs demonstrated substantial differences in genotype frequencies across continental populations.

Key observations include:

* rs2814778 showed strong African specificity.
* rs3827760 showed strong East Asian enrichment.
* rs16891982 showed strong European enrichment.
* rs1426654 and rs12913832 exhibited substantial population differentiation across multiple continental groups.

These findings confirm that even a small AISNP panel captures meaningful continental population structure.

---

### Principal Component Analysis

Principal Component Analysis revealed clear separation among continental populations using only five AISNPs.

The first principal component explained 52.7% of the total variance, while the second principal component explained 27.6%, accounting for 80.3% of the overall genetic variation.

African samples formed a distinct cluster, whereas East Asian populations were primarily separated along the second principal component. European populations occupied a separate region of PCA space, while Admixed American populations displayed broader dispersion consistent with mixed continental ancestry.

These results demonstrate that a minimal AISNP panel can capture substantial population structure within the 1000 Genomes reference dataset.

---

### Machine Learning Performance

Classification performance was evaluated using four machine-learning algorithms.

| Model               | Accuracy |
| ------------------- | -------: |
| SVM                 |    91.2% |
| Logistic Regression |    90.8% |
| Random Forest       |    90.6% |
| Decision Tree       |    90.2% |

The Support Vector Machine achieved the highest observed classification accuracy (91.2%), although performance differences among classifiers were modest.

Classification performance was highest for African, East Asian, European, and South Asian populations, while Admixed American populations showed lower classification accuracy, consistent with their mixed ancestry composition.

---

### Feature Importance Analysis

Random Forest feature importance analysis identified rs2814778 as the most informative marker for continental ancestry classification.

| SNP        | Importance |
| ---------- | ---------: |
| rs2814778  |      0.315 |
| rs16891982 |      0.226 |
| rs3827760  |      0.216 |
| rs1426654  |      0.172 |
| rs12913832 |      0.072 |

The importance ranking is consistent with established forensic genetics literature and reflects known patterns of population differentiation.

---

### SNP Dropout Benchmark

Random Forest ancestry classification was evaluated under simulated SNP dropout conditions.

Classification accuracy decreased progressively as markers were removed from the panel, demonstrating the loss of ancestry information associated with incomplete genetic profiles.

Despite this reduction in information, classification performance remained relatively robust at moderate levels of SNP dropout, highlighting the value of highly informative AISNP markers in forensic applications.

---

## Repository Structure

```text
data/
metadata/
results/
scripts/
manuscript/
```

---

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

* results/plots/rs2814778.png
* results/plots/rs3827760.png
* results/plots/rs1426654.png
* results/plots/rs16891982.png
* results/plots/rs12913832.png

---

## Limitations

This study evaluated only five representative ancestry-informative SNPs. Although high continental classification accuracy was achieved, larger AISNP panels would likely improve performance, particularly for admixed populations and fine-scale ancestry inference.

Additionally, the benchmark focused on continental ancestry classification and does not address subcontinental population structure.

---

## Future Work

Future development of this benchmark will include:

* Expansion to the complete Kidd 55 AISNP panel
* Evaluation of XGBoost and ensemble classifiers
* Simulation of forensic DNA degradation scenarios
* Validation using independent population datasets
* Investigation of fine-scale population structure
* Assessment of ancestry prediction under missing genotype conditions

---

## Conclusions

A small panel of five ancestry-informative SNPs successfully reproduced known continental population structure within the 1000 Genomes reference dataset.

Principal Component Analysis, genotype frequency distributions, and machine-learning classification results consistently demonstrated substantial ancestry information contained within the selected markers.

These findings validate the analytical workflow and support future development of machine-learning-based forensic ancestry prediction using larger AISNP panels and degraded genotype profiles.

---

## References

1000 Genomes Project Consortium. *A global reference for human genetic variation.* Nature. 2015.

Kidd KK, Speed WC, Pakstis AJ, et al. *Progress toward an efficient panel of SNPs for ancestry inference.* Forensic Science International: Genetics. 2014.

Phillips C. *Forensic genetic analysis of biogeographical ancestry.* Forensic Science International: Genetics. 2015.

Jobling MA, Gill P. *Encoded evidence: DNA in forensic analysis.* Nature Reviews Genetics. 2004.

---

## Author

**Agata Gabara**

Independent Researcher

---

## License

MIT License
