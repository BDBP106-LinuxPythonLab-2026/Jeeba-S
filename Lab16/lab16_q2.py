principle=float(input("enter principle:"))
rate=float(input("enter rate of interest:"))
time=float(input("enter time in years:"))

SI=(principle*rate*time)/100
amount=principle + SI
print("Amount is ",amount)
print("Simple interest is ",SI)
