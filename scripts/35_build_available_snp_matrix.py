import pandas as pd
from pathlib import Path

meta = pd.read_csv(
    "metadata/1000g_sample_panel.tsv",
    sep="\t"
)

meta = meta[["sample", "super_pop"]]

files = sorted(Path("results/tables").glob("*_genotypes.tsv"))

merged = meta.copy()
used = []

for f in files:
    snp = f.name.replace("_genotypes.tsv", "")

    geno = pd.read_csv(
        f,
        sep="\t",
        names=["sample", snp]
    )

    merged = merged.merge(
        geno,
        on="sample",
        how="inner"
    )

    used.append(snp)

print("Used SNPs:")
for snp in used:
    print(snp)

print("Shape:", merged.shape)

merged.to_csv(
    "data/processed/available_snp_matrix.tsv",
    sep="\t",
    index=False
)
