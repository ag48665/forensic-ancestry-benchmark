#!/bin/bash

bcftools query -r 1:159174683-159174683 -f '[%SAMPLE\t%GT\n]' data/raw/chr1.vcf.gz > results/tables/rs2814778_genotypes.tsv

bcftools query -i 'ID="rs1426654"' -f '[%SAMPLE\t%GT\n]' data/raw/chr15.vcf.gz > results/tables/rs1426654_genotypes.tsv

bcftools query -i 'ID="rs16891982"' -f '[%SAMPLE\t%GT\n]' data/raw/chr5.vcf.gz > results/tables/rs16891982_genotypes.tsv

bcftools query -i 'ID="rs12913832"' -f '[%SAMPLE\t%GT\n]' data/raw/chr15.vcf.gz > results/tables/rs12913832_genotypes.tsv

bcftools query -i 'ID="rs3827760"' -f '[%SAMPLE\t%GT\n]' data/raw/chr2.vcf.gz > results/tables/rs3827760_genotypes.tsv

wc -l results/tables/rs*_genotypes.tsv