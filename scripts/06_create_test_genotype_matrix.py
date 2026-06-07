import numpy as np
import pandas as pd

np.random.seed(42)

samples = pd.read_csv("metadata/1000g_sample_panel.tsv", sep="\t")
snps = pd.read_csv("metadata/aim_panel.tsv", sep="\t")

genotypes = pd.DataFrame({
    "sample": samples["sample"],
    "pop": samples["pop"],
    "super_pop": samples["super_pop"],
})

for rsid in snps["rsid"]:
    genotypes[rsid] = np.random.choice([0, 1, 2], size=len(samples), p=[0.45, 0.40, 0.15])

genotypes.to_csv("data/processed/test_genotype_matrix.tsv", sep="\t", index=False)

print(genotypes.head())
print()
print("Shape:", genotypes.shape)
print("Saved: data/processed/test_genotype_matrix.tsv")