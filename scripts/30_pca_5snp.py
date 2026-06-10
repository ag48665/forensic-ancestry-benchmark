import pandas as pd
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA

df = pd.read_csv(
    "data/processed/five_snp_matrix.tsv",
    sep="\t"
)

snps = [
    "rs2814778",
    "rs3827760",
    "rs1426654",
    "rs16891982",
    "rs12913832"
]

def gt_to_num(gt):
    if gt in ["0|0", "0/0"]:
        return 0
    if gt in ["0|1", "1|0", "0/1", "1/0"]:
        return 1
    if gt in ["1|1", "1/1"]:
        return 2
    return None

X = df[snps].copy()

for snp in snps:
    X[snp] = X[snp].apply(gt_to_num)

pca = PCA(n_components=2)
coords = pca.fit_transform(X)

plot_df = pd.DataFrame({
    "PC1": coords[:, 0],
    "PC2": coords[:, 1],
    "super_pop": df["super_pop"]
})

plt.figure(figsize=(8, 6))

for pop in sorted(plot_df["super_pop"].unique()):
    subset = plot_df[plot_df["super_pop"] == pop]
    plt.scatter(
        subset["PC1"],
        subset["PC2"],
        label=pop,
        alpha=0.7,
        s=25
    )

plt.xlabel(f"PC1 ({pca.explained_variance_ratio_[0] * 100:.1f}%)")
plt.ylabel(f"PC2 ({pca.explained_variance_ratio_[1] * 100:.1f}%)")
plt.title("PCA of Five Ancestry-Informative SNPs")
plt.legend()
plt.tight_layout()

plt.savefig(
    "results/plots/pca_5snp.png",
    dpi=300
)

print("saved results/plots/pca_5snp.png")
print("Explained variance:", pca.explained_variance_ratio_)
