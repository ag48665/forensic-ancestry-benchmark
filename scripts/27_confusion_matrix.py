import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay

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

labels = ["AFR", "AMR", "EAS", "EUR", "SAS"]

cm = confusion_matrix(
    y_test,
    pred,
    labels=labels
)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=labels
)

fig, ax = plt.subplots(figsize=(8, 6))

disp.plot(ax=ax)

plt.title("Random Forest Ancestry Classification (5 SNPs)")

plt.tight_layout()

plt.savefig(
    "results/plots/confusion_matrix_5snp.png",
    dpi=300
)

print("saved results/plots/confusion_matrix_5snp.png")
