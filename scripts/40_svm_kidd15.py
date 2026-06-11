import pandas as pd

from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv("data/processed/test_genotype_matrix.tsv", sep="\t")

X = df.drop(columns=["sample", "pop", "super_pop"])
y = df["super_pop"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

clf = SVC(kernel="linear", random_state=42)
clf.fit(X_train, y_train)

pred = clf.predict(X_test)
acc = accuracy_score(y_test, pred)

print("Accuracy:", acc)
print()
print(classification_report(y_test, pred))

with open("results/tables/svm_kidd15_results.txt", "w") as f:
    f.write(f"Accuracy: {acc}\n\n")
    f.write(classification_report(y_test, pred))
