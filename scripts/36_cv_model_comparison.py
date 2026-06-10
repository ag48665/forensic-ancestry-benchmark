import pandas as pd

from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

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

cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

models = {
    "Random Forest": RandomForestClassifier(
        n_estimators=500,
        random_state=42
    ),
    "Logistic Regression": LogisticRegression(
        max_iter=5000
    ),
    "Decision Tree": DecisionTreeClassifier(
        random_state=42
    )
}

rows = []

for name, model in models.items():
    scores = cross_val_score(
        model,
        X,
        y,
        cv=cv,
        scoring="accuracy"
    )

    rows.append({
        "model": name,
        "mean_accuracy": scores.mean(),
        "std_accuracy": scores.std()
    })

    print(name)
    print("scores:", scores)
    print("mean:", scores.mean())
    print("std:", scores.std())
    print()

out = pd.DataFrame(rows)

out.to_csv(
    "results/tables/cv_model_comparison.tsv",
    sep="\t",
    index=False
)

print("saved results/tables/cv_model_comparison.tsv")
print(out)
