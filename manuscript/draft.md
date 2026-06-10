
# Benchmarking Forensic Ancestry Inference Using Five Ancestry-Informative SNPs from the 1000 Genomes Project

## Abstract

Forensic ancestry inference is increasingly used to generate investigative leads from biological evidence when conventional DNA profiling is insufficient. Ancestry-informative single nucleotide polymorphisms (AISNPs) provide information about continental population structure and can support forensic intelligence applications. In this study, five well-characterized AISNPs (rs2814778, rs3827760, rs1426654, rs16891982 and rs12913832) were extracted from the 1000 Genomes Project Phase 3 reference dataset comprising 2504 individuals from five continental superpopulations: African (AFR), Admixed American (AMR), East Asian (EAS), European (EUR) and South Asian (SAS). Population-specific genotype distributions were evaluated and a Random Forest classifier was trained using the five-marker panel. The classifier achieved an overall accuracy of 90.6% for superpopulation assignment. Strong population differentiation was observed for all five markers, confirming their utility as ancestry-informative loci. These findings demonstrate that even a small AISNP panel captures substantial continental population structure and provides a useful benchmark for forensic ancestry inference research.

## Introduction

Forensic ancestry inference aims to estimate the biogeographical ancestry of an unknown DNA sample using population-specific genetic variation. Unlike conventional forensic DNA profiling, which focuses on individual identification, ancestry inference seeks to identify the population origins of a biological sample and may provide valuable investigative intelligence.

Ancestry-informative markers (AIMs) are genetic variants that exhibit substantial allele frequency differences between populations. Panels of ancestry-informative SNPs (AISNPs) have become widely used in forensic genetics because they are suitable for massively parallel sequencing workflows and often remain detectable in degraded DNA samples.

Several AISNP panels have been proposed for forensic applications, including the Kidd 55 AISNP panel and other population-informative marker sets. However, the discriminatory power of individual markers and small marker panels remains an important topic for forensic validation studies.

The objective of this study was to evaluate the population differentiation of five well-established AISNPs using the 1000 Genomes Project reference dataset and to assess the performance of a machine-learning classifier trained on these markers.

## Materials and Methods

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

### Population Stratification

All five AISNPs demonstrated substantial differences in genotype frequencies across continental populations.

The rs2814778 marker exhibited strong African enrichment. Homozygous alternative genotypes were highly prevalent in AFR individuals and rare in non-African populations.

The rs3827760 marker showed strong East Asian enrichment, with the highest frequency of alternative genotypes observed among EAS individuals.

The rs1426654 and rs16891982 markers displayed marked differences between European and non-European populations.

The rs12913832 variant also demonstrated substantial population differentiation and contributed additional ancestry information.

Together, these findings confirm that a small panel of ancestry-informative SNPs captures substantial continental population structure.

### Random Forest Classification

The Random Forest classifier achieved an overall classification accuracy of 90.6%.

Performance metrics demonstrated strong classification performance for African, European and East Asian populations. Classification performance for Admixed American populations was lower, reflecting the complex ancestry composition of AMR samples.

The confusion matrix indicated that most classification errors occurred between populations with partially overlapping ancestry profiles.

## Discussion

The results demonstrate that a small panel of only five ancestry-informative SNPs can provide substantial information regarding continental ancestry.

The observed genotype distributions were consistent with previously reported population genetics studies. In particular, rs2814778 showed strong African specificity, whereas rs3827760 exhibited strong East Asian enrichment. European populations were characterized by elevated frequencies of rs16891982 and rs12913832 alternative alleles.

Although five markers are insufficient for high-resolution ancestry assignment, the achieved classification accuracy of 90.6% indicates that a carefully selected AISNP panel can capture a large proportion of continental population structure.

The reduced classification performance observed for Admixed American populations is expected because these individuals frequently possess ancestry components originating from multiple continental populations.

Future studies should expand the marker set to include the complete Kidd 55 AISNP panel and evaluate classifier performance under simulated SNP dropout conditions representative of degraded forensic DNA samples.

## Conclusions

Five ancestry-informative SNPs successfully reproduced known continental population structure within the 1000 Genomes Project reference dataset.

Population-specific genotype distributions were consistent with established forensic genetics literature and a Random Forest classifier achieved 90.6% classification accuracy using only five markers.

These findings validate the analytical workflow and provide a benchmark framework for future forensic ancestry inference studies using larger AISNP panels and machine-learning approaches.

## Author

Agata Gabara

Independent Research Project

## License

MIT License
