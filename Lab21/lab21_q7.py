def analyze_dna(seq):
    l=len(seq)
    count_at=0
    count_gc=0
    for i in range(l):
        if seq[i]=="A" or seq[i]=="T":
            count_at+=1
        else:
            count_gc+=1
    if count_at>count_gc:
        print("the squence is AT rich")
    else:
        print("the squence is GC rich")
    def gc_content():
        r=(count_gc/l)*100
        f=round(r,2)
        return f
    return gc_content()
user=input("enter a sequence:")
print(analyze_dna(user))




