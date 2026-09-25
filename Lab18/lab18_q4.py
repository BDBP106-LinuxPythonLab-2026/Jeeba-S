test_dict= {"Gfg":[5,7,7,7,7], "is":[6,7,7,7], "Best":[9,9,6,5,5]}
max=0
count=0
for k in test_dict:

    for v in test_dict[k]:
        if test_dict[k].count(v)==1:
            count=count+1
        if count>max:
            max=count
        result=k
print(result)