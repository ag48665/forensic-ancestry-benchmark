import urllib.request

url = (
    "https://hgdownload.cse.ucsc.edu/gbdb/hg19/1000Genomes/phase3/"
    "ALL.chr1.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz"
)

out = "data/raw/chr1.vcf.gz"

print("Downloading chr1 VCF...")
print(url)

urllib.request.urlretrieve(url, out)

print("Saved:", out)