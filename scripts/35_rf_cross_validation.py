import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score

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

cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

scores = cross_val_score(
    clf,
    X,
    y,
    cv=cv,
    scoring="accuracy"
)

out = pd.DataFrame({
    "fold": range(1, 6),
    "accuracy": scores
})

out.to_csv(
    "results/tables/rf_5fold_cross_validation.tsv",
    sep="\t",
    index=False
)

print(out)
print()
print("Mean accuracy:", scores.mean())
print("Std accuracy:", scores.std())
