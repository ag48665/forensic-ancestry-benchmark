import pandas as pd

df = pd.read_csv("metadata/1000g_sample_panel.tsv", sep="\t")

print(df.head())
print()
print("Rows:", len(df))
print("Columns:", list(df.columns))
print()
print(df["super_pop"].value_counts())
print()
print(df["pop"].value_counts())