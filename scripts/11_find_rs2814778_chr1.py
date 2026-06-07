import gzip

vcf_path = "data/raw/chr1.vcf.gz"
target = "rs2814778"

print(f"Searching for {target}...")

with gzip.open(vcf_path, "rt") as f:
    for line in f:
        if line.startswith("#"):
            continue

        parts = line.strip().split("\t")
        rsid = parts[2]

        if rsid == target:
            print("FOUND")
            print("CHROM:", parts[0])
            print("POS:", parts[1])
            print("ID:", parts[2])
            print("REF:", parts[3])
            print("ALT:", parts[4])
            break
    else:
        print("NOT FOUND")