import re
txt=("ATCGCGYAATTCAC")
unambigous=re.findall(r"[ATGC]",txt)
ambigous=re.findall(r"[^ATGC]",txt)
print("the unambigous bases are: ",unambigous)
print("the ambigous bases are: ",ambigous)
