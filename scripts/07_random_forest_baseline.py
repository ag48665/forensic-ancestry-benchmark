import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = pd.read_csv(
    "data/processed/test_genotype_matrix.tsv",
    sep="\t"
)

X = df.drop(
    columns=["sample", "pop", "super_pop"]
)

y = df["super_pop"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

rf = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

rf.fit(X_train, y_train)

pred = rf.predict(X_test)

acc = accuracy_score(y_test, pred)

print()
print("Random Forest Accuracy")
print(acc)