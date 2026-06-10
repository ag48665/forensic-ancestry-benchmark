
import pandas as pd
from pathlib import Path

snps = ["rs2814778", "rs3827760", "rs1426654", "rs16891982", "rs12913832"]

rows = []

for snp in snps:
    df = pd.read_csv(f"results/tables/{snp}_by_population.tsv", sep="\t")
    counts = df.groupby(["super_pop", "gt"]).size().reset_index(name="count")
    for _, r in counts.iterrows():
        rows.append({
            "snp": snp,
            "super_pop": r["super_pop"],
            "gt": r["gt"],
            "count": r["count"]
        })

out = pd.DataFrame(rows)
Path("results/tables").mkdir(parents=True, exist_ok=True)
out.to_csv("results/tables/all_snp_population_genotype_counts.tsv", sep="\t", index=False)

print("saved results/tables/all_snp_population_genotype_counts.tsv")
