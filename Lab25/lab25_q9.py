import re
pattern=r'GAATTC'
txt=("ATCGCGAATTCAC")
if re.search(pattern,txt):
    print("EcoRI restriction site found")
else:
    print("EcoRI restriction site not found")
