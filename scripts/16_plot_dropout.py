import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "results/tables/dropout_results.tsv",
    sep="\t"
)

plt.figure(figsize=(8,5))
plt.plot(df["dropout"], df["accuracy"], marker="o")

plt.xlabel("SNP dropout rate")
plt.ylabel("Classification accuracy")
plt.title("Effect of SNP dropout on ancestry prediction")

plt.grid(True)
plt.tight_layout()

plt.savefig(
    "results/figures/figure2_dropout_accuracy.png",
    dpi=300
)

print("Saved Figure 2")