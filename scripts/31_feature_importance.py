import pandas as pd
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestClassifier

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
    return 0

X = df[snps].copy()

for snp in snps:
    X[snp] = X[snp].apply(gt_to_num)

y = df["super_pop"]

clf = RandomForestClassifier(
    n_estimators=500,
    random_state=42
)

clf.fit(X, y)

importance = pd.DataFrame({
    "snp": snps,
    "importance": clf.feature_importances_
})

importance = importance.sort_values(
    "importance",
    ascending=False
)

print(importance)

importance.to_csv(
    "results/tables/feature_importance.tsv",
    sep="\t",
    index=False
)

plt.figure(figsize=(8,5))

plt.bar(
    importance["snp"],
    importance["importance"]
)

plt.ylabel("Feature Importance")
plt.xlabel("SNP")
plt.title("Random Forest Feature Importance")

plt.tight_layout()

plt.savefig(
    "results/plots/feature_importance_5snp.png",
    dpi=300
)

print("saved results/plots/feature_importance_5snp.png")
