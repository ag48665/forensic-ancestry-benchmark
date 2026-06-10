import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

df = pd.read_csv(
    "data/processed/five_snp_matrix.tsv",
    sep="\t"
)

X = df.drop(columns=["sample", "super_pop"])

for col in X.columns:
    X[col] = X[col].astype("category").cat.codes

y = df["super_pop"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

rf = RandomForestClassifier(
    n_estimators=500,
    random_state=42
)

rf.fit(X_train, y_train)

pred = rf.predict(X_test)

acc = accuracy_score(y_test, pred)

print()
print("Accuracy:", round(acc, 4))
print()
print(classification_report(y_test, pred))
