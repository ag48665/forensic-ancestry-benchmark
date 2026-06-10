
# Benchmarking Forensic Ancestry Inference Using Five Ancestry-Informative SNPs from the 1000 Genomes Project

DOI: https://doi.org/10.5281/zenodo.20634314


## Abstract

Forensic ancestry inference is increasingly used to generate investigative leads from biological evidence when conventional DNA profiling cannot identify an individual.

This study evaluates the utility of five ancestry-informative single nucleotide polymorphisms (AISNPs) extracted from the 1000 Genomes Project Phase 3 reference dataset comprising 2,504 individuals from five continental superpopulations (AFR, AMR, EAS, EUR and SAS).

Population-genetic analyses demonstrated substantial genotype frequency differences among continental groups. Principal Component Analysis revealed clear population clustering based on only five AISNPs.

Four machine-learning classifiers were evaluated for ancestry prediction. Support Vector Machine achieved the highest classification accuracy (91.2%), followed by Logistic Regression (90.8%), Random Forest (90.6%) and Decision Tree (90.2%).

Feature importance analysis identified rs2814778 as the most informative marker. SNP dropout benchmarking demonstrated a gradual decline in classification performance as markers were removed, with accuracy decreasing from 89.6% using five SNPs to 46.3% using a single SNP.

Five-fold cross-validation confirmed the robustness of the classification models, with Logistic Regression and SVM showing the most stable performance across validation folds.

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

Five ancestry-informative SNPs were selected based on their established forensic relevance and documented continental allele-frequency differences.

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


### Dataset

Genotype and population metadata were obtained from the 1000 Genomes Project Phase 3 dataset. A total of 2504 individuals were included in the analysis.

Individuals were grouped into five continental superpopulations:

- AFR (African)
- AMR (Admixed American)
- EAS (East Asian)
- EUR (European)
- SAS (South Asian)

### SNP Selection

Five ancestry-informative SNPs were selected based on their established forensic relevance:

| SNP | Gene |
|------|------|
| rs2814778 | ACKR1 |
| rs3827760 | EDAR |
| rs1426654 | SLC24A5 |
| rs16891982 | SLC45A2 |
| rs12913832 | HERC2/OCA2 |

These markers have previously been associated with continental population differentiation and externally visible characteristics.


### Genotype Extraction

Genotypes were extracted directly from chromosome-specific VCF files obtained from the 1000 Genomes Project. For each SNP, genotype tables were generated and merged with superpopulation metadata.

Population-specific genotype counts were calculated and visualized using bar plots.


### Machine Learning Classification

A five-SNP genotype matrix was constructed using all 2504 individuals.

A Random Forest classifier was trained to predict continental superpopulation membership from genotype information. Model evaluation was performed using a train-test split approach and classification performance was assessed using accuracy, precision, recall and F1-score metrics.


## Results
### Comparison of Machine Learning Models

Three supervised machine-learning algorithms were evaluated using five ancestry-informative SNPs extracted from the 1000 Genomes reference panel.

Logistic Regression achieved the highest classification accuracy (90.8%), followed by Random Forest (90.6%) and Decision Tree (90.2%).

The relatively small performance differences suggest that the selected AISNP panel contains highly informative ancestry signals that can be captured even by simple linear classifiers.

These findings indicate that carefully selected forensic AISNP markers provide substantial ancestry prediction power without requiring highly complex machine-learning architectures.


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


### Population Structure

All five ancestry-informative SNPs demonstrated substantial population differentiation across the 1000 Genomes reference populations.

The rs2814778 variant showed strong enrichment in African populations, whereas rs3827760 was highly enriched in East Asian populations.

European populations were characterized by elevated frequencies of rs16891982 and rs12913832 alternative alleles.

These observations were consistent with previously reported population genetics studies and confirm the ancestry informativeness of the selected markers.


### Machine Learning Benchmark

A Random Forest classifier was trained using five ancestry-informative SNPs.

The model achieved an overall classification accuracy of 90.6%.

Performance was highest for African populations (F1 = 0.98), followed by European (0.95), East Asian (0.93), and South Asian populations (0.91).

The lowest performance was observed for Admixed American populations (F1 = 0.63), reflecting their complex ancestry composition.


### SNP Dropout Experiment

To evaluate robustness under degraded forensic DNA conditions, ancestry classification was repeated after progressively reducing the number of available SNPs.

Classification accuracy decreased from 89.6% with five SNPs to 46.3% with a single marker.

A substantial reduction in performance was observed when fewer than three markers were available, indicating that a minimum panel of several ancestry-informative SNPs is required for reliable continental ancestry prediction.


### Population Stratification

All five AISNPs demonstrated substantial differences in genotype frequencies across continental populations.

The rs2814778 marker exhibited strong African enrichment. Homozygous alternative genotypes were highly prevalent in AFR individuals and rare in non-African populations.

The rs3827760 marker showed strong East Asian enrichment, with the highest frequency of alternative genotypes observed among EAS individuals.

The rs1426654 and rs16891982 markers displayed marked differences between European and non-European populations.

The rs12913832 variant also demonstrated substantial population differentiation and contributed additional ancestry information.

Together, these findings confirm that a small panel of ancestry-informative SNPs captures substantial continental population structure.


### ### Feature Importance Analysis

Random Forest feature importance analysis identified rs2814778 as the most informative marker for ancestry prediction.

The ranking of marker importance was:

1. rs2814778
2. rs16891982
3. rs3827760
4. rs1426654
5. rs12913832


The results are consistent with known population-genetic differentiation patterns and confirm the strong ancestry-informative value of the Duffy-null variant rs2814778.


### Machine Learning Model Comparison

Four supervised machine-learning algorithms were evaluated using five ancestry-informative SNPs extracted from the 1000 Genomes reference panel.

Support Vector Machine achieved the highest classification accuracy (91.2%), followed by Logistic Regression (90.8%), Random Forest (90.6%), and Decision Tree (90.2%).

Five-fold cross-validation demonstrated stable performance across all models. Mean cross-validation accuracies ranged from approximately 89.8% to 90.1%, indicating robust and reproducible ancestry prediction performance.

The relatively small differences between classifiers suggest that the selected AISNP panel contains highly informative ancestry signals that can be captured even by relatively simple classification algorithms.

These findings indicate that carefully selected forensic AISNP markers provide substantial ancestry prediction power without requiring highly complex machine-learning architectures.


### SNP Dropout Benchmark

Classification performance was evaluated under progressive marker loss conditions to simulate degraded forensic DNA samples.

Accuracy decreased from 89.6% with five SNPs to 46.3% when only a single marker remained available.

Despite the reduction in available information, ancestry prediction remained relatively robust until the number of markers decreased below three SNPs.

These findings support the utility of compact AISNP panels for forensic applications involving degraded DNA samples and demonstrate the resilience of ancestry inference methods under partial genotype loss.


### Random Forest Classification

The Random Forest classifier achieved an overall classification accuracy of 90.6%.

Performance metrics demonstrated strong classification performance for African, European and East Asian populations. Classification performance for Admixed American populations was lower, reflecting the complex ancestry composition of AMR samples.

The confusion matrix indicated that most classification errors occurred between populations with partially overlapping ancestry profiles.


## Data Availability

All source code, benchmark scripts, processed datasets, and analysis results are publicly available at:

https://github.com/ag48665/forensic-ancestry-benchmark

Archived version:

https://doi.org/10.5281/zenodo.20634314


## Code Availability

All analyses were performed using open-source Python software including pandas, numpy, scikit-learn, matplotlib, and seaborn.

The complete analysis pipeline is available at:

https://github.com/ag48665/forensic-ancestry-benchmark


## Citation

Gabara A. Benchmarking Forensic Ancestry Inference Using Five Ancestry-Informative SNPs from the 1000 Genomes Project. Zenodo. 2026.

DOI: https://doi.org/10.5281/zenodo.20634314


## References

1000 Genomes Project Consortium. A global reference for human genetic variation. Nature. 2015.

Kidd KK, Speed WC, Pakstis AJ, et al. Progress toward an efficient panel of SNPs for ancestry inference. Forensic Science International: Genetics. 2014.

Phillips C. Forensic genetic analysis of bio-geographical ancestry. Forensic Science International: Genetics. 2015.

Kayser M. Forensic DNA Phenotyping: Predicting human appearance from crime scene material. Nature Reviews Genetics. 2015.


## Discussion

The results demonstrate that a small panel of only five ancestry-informative SNPs can provide substantial information regarding continental ancestry.

The observed genotype distributions were consistent with previously reported population genetics studies. In particular, rs2814778 showed strong African specificity, whereas rs3827760 exhibited strong East Asian enrichment. European populations were characterized by elevated frequencies of rs16891982 and rs12913832 alternative alleles.

Although five markers are insufficient for high-resolution ancestry assignment, the achieved classification accuracy exceeding 90% indicates that a carefully selected AISNP panel can capture a large proportion of continental population structure.

The reduced classification performance observed for Admixed American populations is expected because these individuals frequently possess ancestry components originating from multiple continental populations.

Support Vector Machine achieved the highest overall classification accuracy, suggesting that ancestry differentiation captured by the selected markers is highly separable within the feature space.

Future studies should expand the marker set to include the complete Kidd 55 AISNP panel and evaluate classifier performance under simulated SNP dropout conditions representative of degraded forensic DNA samples.


## Machine Learning Model Comparison

Four machine-learning classifiers were evaluated on the five-SNP AISNP panel.

Support Vector Machine achieved the highest classification accuracy (91.2%), followed by Logistic Regression (90.8%), Random Forest (90.6%) and Decision Tree (90.2%).

Five-fold cross-validation demonstrated stable performance across models, with mean accuracies ranging from approximately 89.8% to 90.1%.

The small differences between classifiers suggest that the ancestry signal captured by the selected AISNP panel is strong and largely linearly separable.


## Conclusions

Five ancestry-informative SNPs successfully reproduced known continental population structure within the 1000 Genomes Project Phase 3 reference dataset.

Support Vector Machine achieved the highest classification accuracy (91.2%), followed by Logistic Regression (90.8%), Random Forest (90.6%), and Decision Tree (90.2%).

Population-specific genotype distributions were consistent with established forensic genetics literature and confirmed the ancestry-informative value of the selected markers.

These findings validate the analytical workflow and provide a benchmark framework for future forensic ancestry inference studies using larger AISNP panels and machine-learning approaches.



## Author

Agata Gabara

Independent Research Project


## License

MIT License
