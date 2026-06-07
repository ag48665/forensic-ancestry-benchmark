import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

np.random.seed(42)

df = pd.read_csv(
    "data/processed/test_genotype_matrix.tsv",
    sep="\t"
)

X = df.drop(
    columns=["sample", "pop", "super_pop"]
)

y = df["super_pop"]

dropout_levels = [0, 0.10, 0.25, 0.50, 0.75]

results = []

for dropout in dropout_levels:

    X_drop = X.copy()

    if dropout > 0:

        mask = np.random.rand(*X_drop.shape) < dropout

        X_drop = X_drop.mask(mask, 0)

    X_train, X_test, y_train, y_test = train_test_split(
        X_drop,
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

    results.append(
        {
            "dropout": dropout,
            "accuracy": acc
        }
    )

results_df = pd.DataFrame(results)

print(results_df)

results_df.to_csv(
    "results/tables/dropout_results.tsv",
    sep="\t",
    index=False
)

print()
print("Saved: results/tables/dropout_results.tsv")