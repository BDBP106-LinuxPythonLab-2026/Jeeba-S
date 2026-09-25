#s=input("enter a sentence")
s=("hi im jeeba im studying in ibab")
print("the sentence before removing the duplicates:-",s)
words=s.split()
d=dict([])
for word in words:
    d[word]=1
print("the sentence after removing the duplicates:-"," " .join(d.keys()))
