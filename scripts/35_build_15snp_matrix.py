import pandas as pd

snps = pd.read_csv("metadata/aim_panel.tsv", sep="\t")["rsid"].tolist()

frames = []

for snp in snps:
    try:
        df = pd.read_csv(
            f"results/tables/{snp}_genotypes.tsv",
            sep="\t"
        )
        frames.append(df)
    except:
        print("missing:", snp)

merged = frames[0]

for df in frames[1:]:
    merged = merged.merge(
        df,
        on=["sample", "super_pop"],
        how="inner"
    )

merged.to_csv(
    "data/processed/fifteen_snp_matrix.tsv",
    sep="\t",
    index=False
)

print(merged.shape)
