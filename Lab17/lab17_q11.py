numbers=[1,2,3,4,3,5,6,3,7,2,1]
a=len(numbers)
count=0
for i in range(0,a):
    for j in range(i+1,a):
        if numbers[i]==numbers[j]:
            if numbers[i] not in numbers[:i]:
                print(numbers[i])
            break

