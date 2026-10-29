import string
s=input("enter a sentence")
l=list(s.lower())
count_v=0
count_c=0
count_d=0
count_s=0
for i in l:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        count_v=count_v+1
    elif i=="0" or i=="1" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7" or i=="8" or i=="9":
        count_d=count_d+1
    elif i==" ":
        count_s=count_s+1
    elif i in string.punctuation:
        pass
    else:
        count_c=count_c+1
print("vowels",count_v)
print("consonants",count_c)
print("digits",count_d)
print("spaces",count_s)