from itertools import count
def next_prime(n):
    for num in count(n+1):
        factor=0
        for i in range(1,num+1):
            if num%i==0:
                factor+=1
        if factor==2:
            return num
n=int(input("enter a number "))
print(next_prime(n))



