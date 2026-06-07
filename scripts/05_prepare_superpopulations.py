import pandas as pd

df = pd.read_csv(
    "metadata/1000g_sample_panel.tsv",
    sep="\t"
)

print(df.columns)

summary = (
    df.groupby("super_pop")
      .size()
      .reset_index(name="count")
)

print(summary)

summary.to_csv(
    "results/tables/superpopulation_counts.tsv",
    sep="\t",
    index=False
)

print("Saved results/tables/superpopulation_counts.tsv")