d={"a":10,"b":2,"c":50,"d":25}
max=0
for k,v in d.items():
    if v>max:
        max=v
min = max
for k, v in d.items():
     if v<min:
        min=v

print("the minimum is: ",min)
print("the maximum is: ",max)