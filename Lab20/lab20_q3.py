n=int(input("enter a number"))
s=43
attempt=1
for attempt in range (1,7):
    if s>n:
        attempt = attempt + 1
        print("too low")
        n=int(input("enter a number"))
    elif s<n:
        attempt=attempt+1
        print ("too high")
        n = int(input("enter a number"))
    else:
        print("correct guess")
        print("total attempts made", attempt)
        break
else:
    print("the secret no is",s)





