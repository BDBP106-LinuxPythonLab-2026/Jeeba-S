import re

dna = "ACTNGCATRGCTACGTYACGATSCGAWTCG"
result = re.split(r"[^ATGC]", dna)
print(result)