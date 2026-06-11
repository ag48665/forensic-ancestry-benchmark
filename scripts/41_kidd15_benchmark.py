import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

df = pd.read_csv(
    "data/processed/test_genotype_matrix.tsv",
    sep="\t"
)

X = df.drop(columns=["sample", "pop", "super_pop"])
y = df["super_pop"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

models = {
    "RandomForest": RandomForestClassifier(
        n_estimators=500,
        random_state=42
    ),
    "LogisticRegression": LogisticRegression(
        max_iter=5000
    ),
    "DecisionTree": DecisionTreeClassifier(
        random_state=42
    ),
    "SVM": SVC(
        kernel="linear"
    )
}

for name, model in models.items():

    model.fit(X_train, y_train)

    pred = model.predict(X_test)

    acc = accuracy_score(y_test, pred)

    print(f"{name}: {acc:.4f}")
