n=int(input("enter a number"))
if n>0:
    print("its a positive integer",n)
elif n<0:
    print("it is a negative integer",n)
else:
    print("it is zero")

if n != 0:
    if n%2==0:
        print("even")
    else:
        print("odd")
    if n%3==0 and n%5==0:
        print("fizzbuzz")