import pandas as pd

snps = [
    "rs2814778",
    "rs3827760",
    "rs1426654",
    "rs16891982",
    "rs12913832"
]

meta = pd.read_csv(
    "data/processed/test_genotype_matrix.tsv",
    sep="\t"
)

meta = meta[["sample", "super_pop"]]

for snp in snps:
    geno = pd.read_csv(
        f"results/tables/{snp}_genotypes.tsv",
        sep="\t",
        names=["sample", "gt"]
    )

    merged = geno.merge(
        meta,
        on="sample",
        how="inner"
    )

    outfile = f"results/tables/{snp}_by_population.tsv"

    merged.to_csv(
        outfile,
        sep="\t",
        index=False
    )

    print("saved", outfile, len(merged))
