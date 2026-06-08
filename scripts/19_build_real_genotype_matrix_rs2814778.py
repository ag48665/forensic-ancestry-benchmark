import pandas as pd

meta = pd.read_csv(
    "metadata/1000g_sample_panel.tsv",
    sep="\t"
)

geno = pd.read_csv(
    "results/tables/rs2814778_genotypes.tsv",
    sep="\t",
    names=["sample", "rs2814778_gt"]
)

def gt_to_dosage(gt):
    gt = gt.replace("|", "/")
    a, b = gt.split("/")
    return int(a) + int(b)

geno["rs2814778"] = geno["rs2814778_gt"].apply(gt_to_dosage)

out = meta[["sample", "pop", "super_pop"]].merge(
    geno[["sample", "rs2814778"]],
    on="sample",
    how="inner"
)

print(out.head())
print("Shape:", out.shape)

out.to_csv(
    "data/processed/real_genotype_matrix_rs2814778.tsv",
    sep="\t",
    index=False
)

print("Saved: data/processed/real_genotype_matrix_rs2814778.tsv")