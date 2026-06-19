# Machine Learning and Population Genetics Benchmark for Forensic Ancestry Inference

[![Version DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20643550.svg)](https://doi.org/10.5281/zenodo.20643550)

Benchmarking machine learning and population genetics methods for forensic ancestry inference using ancestry-informative SNP markers and publicly available genomic datasets.

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

## Project Highlights

✔ Analysis of 2,504 individuals from the 1000 Genomes Project

✔ Evaluation of ancestry-informative SNP markers

✔ Principal Component Analysis of population structure

✔ Comparison of four machine-learning classifiers

✔ Feature importance analysis

✔ SNP dropout robustness benchmarking

✔ Reproducible genomic data analysis workflow

---

## Main Result

![PCA Population Structure](results/plots/pca_population_structure.png)

Principal Component Analysis demonstrates clear separation of major continental populations using only five ancestry-informative SNPs.

---

## Dataset

### Reference Population Dataset

**Source**

* 1000 Genomes Project Phase 3

### Continental Superpopulations

* AFR — African
* AMR — Admixed American
* EAS — East Asian
* EUR — European
* SAS — South Asian

### Total Reference Samples

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

## Research Questions

This benchmark addresses several key questions:

1. Can a minimal AISNP panel capture continental population structure?
2. Which AISNPs contribute most strongly to ancestry classification?
3. How accurately can machine-learning models infer ancestry from a highly reduced marker panel?
4. How robust is ancestry prediction when markers are progressively removed?
5. Which classification algorithms perform best under minimal-marker conditions?

---

## Skills Demonstrated

### Population Genetics

* Population structure analysis
* Ancestry-informative marker evaluation
* Allele and genotype frequency analysis
* Continental ancestry inference
* Forensic genetics workflows

### Machine Learning

* Random Forest
* Support Vector Machine (SVM)
* Logistic Regression
* Decision Tree Classification
* Model comparison and evaluation
* Feature importance analysis
* Cross-validation

### Bioinformatics

* VCF processing
* Genomic data analysis
* SNP extraction and filtering
* Principal Component Analysis (PCA)
* Population-scale dataset analysis
* Reproducible computational workflows

---

## Methods

### Data Processing

Genotype data were obtained from the 1000 Genomes Project Phase 3 release. Target AISNPs were extracted from chromosome-specific VCF files and merged with population metadata.

### Population Frequency Analysis

Genotype frequencies were calculated for each AISNP across all continental superpopulations to evaluate population differentiation.

### Principal Component Analysis

Principal Component Analysis (PCA) was performed using numerically encoded genotypes from the five AISNP markers.

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

Clone the repository and execute the benchmark scripts:

```bash
git clone https://github.com/ag48665/forensic-ancestry-benchmark

cd forensic-ancestry-benchmark

pip install -r requirements.txt
```

### Core Benchmark Scripts

* scripts/26_rf_5snp.py
* scripts/32_logistic_regression_5snp.py
* scripts/33_decision_tree_5snp.py
* scripts/37_svm_5snp.py
* scripts/35_rf_cross_validation.py
* scripts/36_cv_model_comparison.py

All analyses can be reproduced from the scripts included in the repository.

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

* PC1 explained 52.7% of total variance.
* PC2 explained 27.6% of total variance.
* Combined variance explained: 80.3%.

African samples formed a distinct cluster, whereas East Asian populations were primarily separated along the second principal component. European populations occupied a separate region of PCA space, while Admixed American populations displayed broader dispersion consistent with mixed ancestry.

---

### Machine Learning Performance

| Model               | Accuracy |
| ------------------- | -------: |
| SVM                 |    91.2% |
| Logistic Regression |    90.8% |
| Random Forest       |    90.6% |
| Decision Tree       |    90.2% |

The Support Vector Machine achieved the highest classification accuracy.

---

## Results at a Glance

| Analysis                    | Main Finding                                                       |
| --------------------------- | ------------------------------------------------------------------ |
| Genotype Frequency Analysis | Strong population differentiation across all five AISNPs           |
| PCA                         | Clear continental population clustering                            |
| SVM Classification          | Highest classification accuracy (91.2%)                            |
| Random Forest               | Strong predictive performance and interpretable feature importance |
| Feature Importance          | rs2814778 identified as the most informative marker                |
| SNP Dropout Benchmark       | Classification remained robust despite marker loss                 |

---

## Key Takeaway

Using only five verified ancestry-informative SNPs extracted directly from 1000 Genomes Phase 3 VCF files, machine-learning classifiers achieved approximately 91% continental ancestry classification accuracy.

Despite the extremely small marker panel, PCA, genotype frequency analysis, and supervised machine-learning approaches consistently recovered major continental population structure.

These results demonstrate that a minimal set of highly informative markers can provide robust ancestry inference and establish a benchmark framework for future forensic genetics and population genomics studies.

---

### Feature Importance Analysis

| SNP        | Importance |
| ---------- | ---------: |
| rs2814778  |      0.315 |
| rs16891982 |      0.226 |
| rs3827760  |      0.216 |
| rs1426654  |      0.172 |
| rs12913832 |      0.072 |

Random Forest feature importance analysis identified rs2814778 as the most informative marker for continental ancestry classification.

---

### SNP Dropout Benchmark

Random Forest ancestry classification was evaluated under simulated SNP dropout conditions.

Classification accuracy decreased progressively as markers were removed from the panel, demonstrating the loss of ancestry information associated with incomplete genetic profiles.

Despite this reduction, classification performance remained relatively robust at moderate levels of SNP dropout.

---

## Scientific Significance

Ancestry inference remains an important component of forensic genetics, population genomics, and human genetic diversity research.

This benchmark demonstrates how a highly reduced AISNP panel can still capture substantial population structure while maintaining strong classification performance.

The project also provides a reproducible framework for evaluating future ancestry marker panels and machine-learning approaches using publicly available genomic datasets.

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

## Limitations

Several limitations should be considered:

* The benchmark currently evaluates a minimal panel of five AISNPs.
* Continental ancestry inference is assessed at a broad population level and does not capture fine-scale population structure.
* Admixed populations remain more challenging to classify accurately.
* Additional ancestry-informative markers are required for higher-resolution inference.
* Validation on independent population datasets would further strengthen the findings.

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

## Citation

If you use this benchmark, please cite:

**Gabara, A. (2026).**
*Forensic Ancestry Benchmark: Verified 5-SNP benchmark against 1000 Genomes VCF files.*
Zenodo.
https://doi.org/10.5281/zenodo.20643550

---

## DOI

https://doi.org/10.5281/zenodo.20643550

---

## Author

**Agata Gabara**

Incoming MSc Bioinformatics Student

Research Interests:

* Computational Biology
* Population Genetics
* Cancer Genomics
* Machine Learning for Genomics
* Single-Cell Transcriptomics

GitHub: https://github.com/ag48665

LinkedIn: https://www.linkedin.com/in/agatha-gabara-06494a37/

---

## License

MIT License
