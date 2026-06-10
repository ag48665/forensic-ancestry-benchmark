# Benchmarking Forensic Ancestry Inference Using Five Ancestry-Informed SNPs from the 1000 Genomes Project

DOI: https://doi.org/10.5281/zenodo.20634314

## Abstract

Forensic ancestry inference is increasingly used to generate investigative leads from biological evidence when conventional DNA profiling cannot identify an individual.

This study evaluates the utility of five ancestry-informative single nucleotide polymorphisms (AISNPs) extracted from the 1000 Genomes Project Phase 3 reference dataset comprising 2,504 individuals from five continental superpopulations (AFR, AMR, EAS, EUR and SAS).

Population-genetic analyses demonstrated substantial genotype frequency differences among continental groups. Principal Component Analysis revealed clear population clustering based on only five AISNPs.

Four machine-learning classifiers were evaluated for ancestry prediction. Support Vector Machine achieved the highest classification accuracy (91.2%), followed by Logistic Regression (90.8%), Random Forest (90.6%) and Decision Tree (90.2%).

Feature importance analysis identified rs2814778 as the most informative marker. SNP dropout benchmarking demonstrated a gradual decline in classification performance as markers were removed, with accuracy decreasing from 89.6% using five SNPs to 46.3% using a single SNP.

Five-fold cross-validation confirmed the robustness of the classification models.

These findings demonstrate that a compact panel of carefully selected AISNPs captures substantial continental population structure and supports robust forensic ancestry inference under simulated degraded DNA conditions.

## Materials and Methods

### Dataset

Genotype and population metadata were obtained from the 1000 Genomes Project Phase 3 reference dataset. A total of 2,504 individuals were included in the analysis.

Individuals were grouped into five continental superpopulations:

- AFR (African)
- AMR (Admixed American)
- EAS (East Asian)
- EUR (European)
- SAS (South Asian)

### SNP Selection

Five ancestry-informative SNPs were selected:

| SNP | Gene |
|------|------|
| rs2814778 | ACKR1 |
| rs3827760 | EDAR |
| rs1426654 | SLC24A5 |
| rs16891982 | SLC45A2 |
| rs12913832 | HERC2/OCA2 |

### Statistical Analysis

Population-specific genotype frequencies were calculated for each AISNP. Principal Component Analysis (PCA) was performed to visualize continental population structure.

### Machine Learning

Four supervised machine-learning algorithms were evaluated:

- Random Forest
- Logistic Regression
- Decision Tree
- Support Vector Machine (SVM)

Classification performance was assessed using overall accuracy and five-fold cross-validation.

### SNP Dropout Analysis

To simulate degraded forensic DNA samples, SNP dropout experiments were performed by progressively removing ancestry-informative markers and evaluating the effect on classification accuracy.

## Results

### Population Structure

All five ancestry-informative SNPs demonstrated substantial population differentiation across the 1000 Genomes reference populations.

### Machine Learning Benchmark

Support Vector Machine achieved the highest classification accuracy (91.2%), followed by Logistic Regression (90.8%), Random Forest (90.6%) and Decision Tree (90.2%).

### Feature Importance Analysis

Random Forest feature importance analysis identified rs2814778 as the most informative marker.

### SNP Dropout Benchmark

Classification accuracy decreased from 89.6% with five SNPs to 46.3% with a single marker.

### Figures

Figure 1. Genotype distribution of rs2814778.

Figure 2. Genotype distribution of rs3827760.

Figure 3. Genotype distribution of rs1426654.

Figure 4. Genotype distribution of rs16891982.

Figure 5. Genotype distribution of rs12913832.

Figure 6. Principal Component Analysis of five AISNPs.

Figure 7. Random Forest confusion matrix.

Figure 8. SNP dropout benchmark.

Figure 9. Random Forest feature importance.

Figure 10. Comparison of machine-learning models.

## Discussion

The results demonstrate that a small panel of only five ancestry-informative SNPs can provide substantial information regarding continental ancestry.

Support Vector Machine achieved the highest overall classification accuracy, suggesting that ancestry differentiation captured by the selected markers is highly separable within the feature space.

Future studies should expand the marker set to include the complete Kidd 55 AISNP panel.

## Conclusions

Five ancestry-informative SNPs successfully reproduced known continental population structure within the 1000 Genomes Project Phase 3 reference dataset.

Support Vector Machine achieved the highest classification accuracy (91.2%).

These findings provide a benchmark framework for future forensic ancestry inference studies using larger AISNP panels and machine-learning approaches.

## Data Availability

Source code, processed datasets and results are publicly available at:

https://github.com/ag48665/forensic-ancestry-benchmark

DOI:

https://doi.org/10.5281/zenodo.20634314

## Code Availability

The complete analysis pipeline is available at:

https://github.com/ag48665/forensic-ancestry-benchmark

## Citation

Gabara A. Benchmarking Forensic Ancestry Inference Using Five Ancestry-Informed SNPs from the 1000 Genomes Project. Zenodo. 2026.

DOI: https://doi.org/10.5281/zenodo.20634314

## References

1000 Genomes Project Consortium. Nature. 2015.

Kidd KK et al. Forensic Science International: Genetics. 2014.

Phillips C. Forensic Science International: Genetics. 2015.

Kayser M. Nature Reviews Genetics. 2015.

## Author

Agata Gabara

Independent Research Project

## License

MIT License
