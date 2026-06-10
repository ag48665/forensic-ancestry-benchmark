import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "results/tables/dropout_benchmark.tsv",
    sep="\t"
)

plt.figure(figsize=(7, 5))
plt.plot(df["num_snps"], df["accuracy"], marker="o")
plt.xlabel("Number of available SNPs")
plt.ylabel("Accuracy")
plt.title("Random Forest Accuracy Under SNP Dropout")
plt.ylim(0, 1)
plt.grid(True)
plt.tight_layout()

plt.savefig(
    "results/plots/dropout_benchmark_5snp.png",
    dpi=300
)

print("saved results/plots/dropout_benchmark_5snp.png")
