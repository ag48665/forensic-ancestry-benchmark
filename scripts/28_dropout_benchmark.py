import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
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
    if gt in ["0|0", "0/0"]:
        return 0
    if gt in ["0|1", "1|0", "0/1", "1/0"]:
        return 1
    if gt in ["1|1", "1/1"]:
        return 2
    return None

for snp in snps:
    df[snp] = df[snp].apply(gt_to_num)

y = df["super_pop"]

results = []

for n in [5, 4, 3, 2, 1]:
    features = snps[:n]

    X = df[features]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    clf = RandomForestClassifier(
        n_estimators=200,
        random_state=42
    )

    clf.fit(X_train, y_train)

    pred = clf.predict(X_test)

    acc = accuracy_score(y_test, pred)

    print(n, round(acc, 4))

    results.append({
        "num_snps": n,
        "accuracy": acc
    })

pd.DataFrame(results).to_csv(
    "results/tables/dropout_benchmark.tsv",
    sep="\t",
    index=False
)

print("saved results/tables/dropout_benchmark.tsv")
