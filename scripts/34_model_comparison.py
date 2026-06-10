import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "model": [
        "Logistic Regression",
        "Random Forest",
        "Decision Tree"
    ],
    "accuracy": [
        0.9082,
        0.9062,
        0.9022
    ]
})

df.to_csv(
    "results/tables/model_comparison.tsv",
    sep="\t",
    index=False
)

plt.figure(figsize=(7,4))

plt.bar(
    df["model"],
    df["accuracy"]
)

plt.ylabel("Accuracy")
plt.ylim(0.85, 0.95)

plt.title(
    "Classification Accuracy of Three Models\nUsing Five AISNPs"
)

plt.tight_layout()

plt.savefig(
    "results/plots/model_comparison.png",
    dpi=300
)

print(df)
