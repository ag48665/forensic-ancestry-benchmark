import pandas as pd

geno = pd.read_csv(
    "results/tables/rs2814778_genotypes.tsv",
    sep="\t",
    names=["sample", "gt"]
)

meta = pd.read_csv(
    "data/processed/test_genotype_matrix.tsv",
    sep="\t"
)

merged = geno.merge(
    meta[["sample", "super_pop"]],
    on="sample",
    how="inner"
)

print(merged.head())
print()
print("Rows:", len(merged))

merged.to_csv(
    "results/tables/rs2814778_by_population.tsv",
    sep="\t",
    index=False
)

print("Saved.")