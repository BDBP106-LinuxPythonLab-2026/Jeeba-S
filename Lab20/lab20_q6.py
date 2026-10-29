students = [("Asha", 88), ("Ravi", 72), ("Meera", 95), ("Karan", 59), ("Divya", 81)]
total=0
max=0
min=students[0][1]
for student in students:
    total = total + student[1]
    if student[1] >=90:
        print("A")
    elif student[1] >=80:
        print("B")
    elif student[1] >=70:
        print("C")
    elif student[1] >=60:
        print("D")
    else:
        print("F")
    if max<student[1]:
        max=student[1]
    if min>student[1]:
        min=student[1]

avg=total/len(students)
print (avg)
print (max)
print (min)