import pandas as pd

from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

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

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

clf = SVC(
    kernel="linear",
    random_state=42
)

clf.fit(X_train, y_train)

pred = clf.predict(X_test)

acc = accuracy_score(y_test, pred)

print()
print("Accuracy:", acc)
print()

report = classification_report(y_test, pred)

print(report)

with open(
    "results/tables/svm_5snp_results.txt",
    "w"
) as f:
    f.write(f"Accuracy: {acc}\n\n")
    f.write(report)

print("saved results/tables/svm_5snp_results.txt")
