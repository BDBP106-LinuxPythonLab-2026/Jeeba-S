import re
pattern=r'GC[ATGC]GC'
txt=("”ATCGCGAATTCAC”")
if re.search(pattern,txt):
    print("BisI restriction site found")
else:
    print("BisI restriction site not found")