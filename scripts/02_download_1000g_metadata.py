import pandas as pd

url = (
    "https://raw.githubusercontent.com/"
    "igsr/1000Genomes_data_indexes/master/"
    "20130606_sample_info.xlsx"
)

print("Downloading 1000 Genomes metadata...")
print(url)

df = pd.read_excel(url)

print(df.head())
print()
print(f"Rows: {len(df)}")
print(f"Columns: {list(df.columns)}")

df.to_csv("metadata/1000g_sample_info_raw.tsv", sep="\t", index=False)

print("Saved: metadata/1000g_sample_info_raw.tsv")