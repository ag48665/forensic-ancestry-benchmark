import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

snps = [
    "rs2814778",
    "rs3827760",
    "rs1426654",
    "rs16891982",
    "rs12913832"
]

outdir = Path("results/plots")
outdir.mkdir(parents=True, exist_ok=True)

for snp in snps:

    df = pd.read_csv(
        f"results/tables/{snp}_by_population.tsv",
        sep="\t"
    )

    counts = (
        df.groupby(["super_pop", "gt"])
        .size()
        .reset_index(name="count")
    )

    pivot = counts.pivot(
        index="super_pop",
        columns="gt",
        values="count"
    ).fillna(0)

    pivot.plot(kind="bar")

    plt.title(snp)
    plt.ylabel("Individuals")
    plt.tight_layout()

    plt.savefig(
        outdir / f"{snp}.png",
        dpi=300
    )

    plt.close()

    print("saved", snp)
