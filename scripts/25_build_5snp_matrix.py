import pandas as pd

meta = pd.read_csv(
    "metadata/1000g_sample_panel.tsv",
    sep="\t"
)

snps = [
    "rs2814778",
    "rs3827760",
    "rs1426654",
    "rs16891982",
    "rs12913832"
]

merged = meta[["sample", "super_pop"]].copy()

for snp in snps:

    geno = pd.read_csv(
        f"results/tables/{snp}_genotypes.tsv",
        sep="\t",
        names=["sample", snp]
    )

    merged = merged.merge(geno, on="sample")

merged.to_csv(
    "data/processed/five_snp_matrix.tsv",
    sep="\t",
    index=False
)

print(merged.head())
print("Rows:", len(merged))
