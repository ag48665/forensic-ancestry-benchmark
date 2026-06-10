import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

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
    if gt == "0|0":
        return 0
    if gt in ["0|1", "1|0"]:
        return 1
    if gt == "1|1":
        return 2
    return 0

X = df[snps].copy()

for snp in snps:
    X[snp] = X[snp].apply(gt_to_num)

y = df["super_pop"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

clf = LogisticRegression(
    max_iter=5000
)

clf.fit(X_train, y_train)

pred = clf.predict(X_test)

acc = accuracy_score(y_test, pred)

print()
print("Accuracy:", acc)
print()
print(classification_report(y_test, pred))
