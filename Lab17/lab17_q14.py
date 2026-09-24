numbers=[1,2,3,4,3,2,3]
rem=3
a=len(numbers)
while rem in numbers:
    numbers.remove(rem)
print(numbers)