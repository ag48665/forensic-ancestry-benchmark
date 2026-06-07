import pandas as pd

url = (
    "https://bochet.gcc.biostat.washington.edu/"
    "beagle/1000_Genomes_phase3_v5a/sample_info/"
    "integrated_call_samples_v3.20130502.ALL.panel"
)

print("Downloading 1000 Genomes sample panel...")
print(url)

df = pd.read_csv(url, sep="\t")

print(df.head())
print()
print(f"Rows: {len(df)}")
print(f"Columns: {list(df.columns)}")

df.to_csv("metadata/1000g_sample_panel.tsv", sep="\t", index=False)

print("Saved: metadata/1000g_sample_panel.tsv")