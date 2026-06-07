import pandas as pd

panel = pd.read_csv(
    "metadata/aim_panel.tsv",
    sep="\t"
)

print(panel.head())
print()
print(f"Number of SNPs: {len(panel)}")
print(f"Unique chromosomes: {panel['chr'].nunique()}")