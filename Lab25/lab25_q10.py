import re
pattern=r'GGACC|GGTCC'
txt=("”ATCGCGAATTCAC”")
if re.search(pattern,txt):
    print("AvaII restriction site found")
else:
    print("AvaII restriction site not found")