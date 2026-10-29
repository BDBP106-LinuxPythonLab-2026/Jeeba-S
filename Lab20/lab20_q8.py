python_class = ["Anil", "Bina", "Chetan", "Deepa", "Esha"]
java_class = ["Chetan", "Farhan", "Deepa", "Gita", "Bina"]
l1=[]
l2=[]
l3=[]
l4=[]
for i in range(0,len(python_class)):
    for j in range(0,len(java_class)):
        if python_class[i]==java_class[j]:
            l1.append(java_class[j])
        else:
            pass
for i in python_class:
    if i not in l1:
        l2.append(i)
    else:
        pass
for i in java_class:
    if i not in l1:
        l3.append(i)
    else:
        pass
l3.extend(l2)
python_class.extend(java_class)
l4=list(set(python_class))
l4.sort()

print("students enrolled in both classes",l1)
print("students only in python class",l2)
print("students only taking one course",l3)
print("sorted list of students",l4)

user=input("enter student name")
i=user.capitalize()
if i in l4:
    if i in l1:
        print("student in both class")
    elif i in l2:
        print("student in python class")
    elif i not in l1 and i not in l2 and i in l4:
        print("student in java class")
else:
    print("invalid name")

