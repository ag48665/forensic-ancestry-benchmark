import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "results/tables/rs2814778_population_frequencies.tsv",
    sep="\t"
)

plt.figure(figsize=(8,5))
plt.bar(df["super_pop"], df["C_frequency"])

plt.ylabel("Allele C frequency")
plt.xlabel("Superpopulation")
plt.title("rs2814778 allele frequency across 1000 Genomes superpopulations")

plt.tight_layout()

plt.savefig(
    "results/figures/figure1_rs2814778_frequency.png",
    dpi=300
)

print("Saved figure.")