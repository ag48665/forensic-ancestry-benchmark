import pandas as pd

df = pd.read_csv(
    "results/tables/rs2814778_by_population.tsv",
    sep="\t"
)

def count_c(gt):
    a, b = gt.split("|")
    return int(a) + int(b)

df["C_count"] = df["gt"].apply(count_c)

summary = (
    df.groupby("super_pop")
      .agg(
          samples=("sample", "count"),
          mean_C=("C_count", "mean")
      )
      .reset_index()
)

summary["C_frequency"] = summary["mean_C"] / 2

print(summary)

summary.to_csv(
    "results/tables/rs2814778_population_frequencies.tsv",
    sep="\t",
    index=False
)

print("\nSaved.")