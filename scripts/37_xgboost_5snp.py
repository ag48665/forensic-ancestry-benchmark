import pandas as pd

from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder

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

encoder = LabelEncoder()
y = encoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

clf = XGBClassifier(
    n_estimators=300,
    max_depth=4,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    objective="multi:softmax",
    eval_metric="mlogloss",
    random_state=42
)

clf.fit(X_train, y_train)

pred = clf.predict(X_test)

acc = accuracy_score(y_test, pred)

print()
print("Accuracy:", acc)
print()

print(
    classification_report(
        y_test,
        pred,
        target_names=encoder.classes_
    )
)

with open(
    "results/tables/xgboost_5snp_results.txt",
    "w"
) as f:
    f.write(f"Accuracy: {acc}\n\n")
    f.write(
        classification_report(
            y_test,
            pred,
            target_names=encoder.classes_
        )
    )

print(
    "saved results/tables/xgboost_5snp_results.txt"
)
