#q1

t=int(input("enter temperature in celcius"))
def f(x):
    return (x*1.8)+32

farenheit=list(map(f,[t]))
print(farenheit)

#q2

far=list(map (lambda x:x*1.8+32,[t]))
print(far)

