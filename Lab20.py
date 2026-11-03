# q1
n = int(input("enter a number"))
if n > 0:
    print("its a positive integer", n)
elif n < 0:
    print("it is a negative integer", n)
else:
    print("it is zero")

if n != 0:
    if n % 2 == 0:
        print("even")
    else:
        print("odd")
    if n % 3 == 0 and n % 5 == 0:
        print("fizzbuzz")
# q2
import string

s = input("enter a sentence")
l = list(s.lower())
count_v = 0
count_c = 0
count_d = 0
count_s = 0
for i in l:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        count_v = count_v + 1
    elif i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9":
        count_d = count_d + 1
    elif i == " ":
        count_s = count_s + 1
    elif i in string.punctuation:
        pass
    else:
        count_c = count_c + 1
print("vowels", count_v)
print("consonants", count_c)
print("digits", count_d)
print("spaces", count_s)
# q3
n = int(input("enter a number"))
s = 43
attempt = 1
for attempt in range(1, 7):
    if s > n:
        attempt = attempt + 1
        print("too low")
        n = int(input("enter a number"))
    elif s < n:
        attempt = attempt + 1
        print("too high")
        n = int(input("enter a number"))
    else:
        print("correct guess")
        print("total attempts made", attempt)
        break
else:
    print("the secret no is", s)
#q4
n = int(input("Enter a number n: "))

# Set column width based on the largest value in the table.
width = len(str(n * n))

print(" " * (width + 1), end="")
for col in range(1, n + 1):
    print(f"{col:>{width}}", end=" ")
print()

for row in range(1, n + 1):
    print(f"{row:>{width}}", end=" ")
    for col in range(1, n + 1):
        print(f"{row * col:>{width}}", end=" ")
    print()
# q5
items=[]
while True:
    print("\n MENU")
    print("1. add item")
    print("2. remove item")
    print("3. view items")
    print("4. sort items")
    print("5. quit")

    choice = input("Enter your choice: ")
    if choice == "1":
        add_item = input("Enter a item to add: ").strip()
        found=False
        for word in items:
            if word.lower() == add_item.lower():
                found=True
        if found:
            print("Item already present in the list")
        else:
            items.append(add_item)
            print(add_item, "was added")
    elif choice == "2":
        remove_item = input("Enter a item to remove: ").strip()
        removed = False
        for word in items:
            if word.lower() == remove_item.lower():
                items.remove(word)
                print(remove_item, "was removed")
                removed = True
        if not removed:
                print("Item not found")
    elif choice == "3":
        if len(items) == 0:
            print("The list is empty")
        else:
            n = 1
            for word in items:
                print(f"{n}. {word}")
                n += 1
    elif choice == "4":
        items.sort(key=str.lower)
        print("the list is sorted")
        print(items)
    elif choice == "5":
        print("quit")
        break
    else:
        print("invalid choice")

#q6
students=[("Asha", 88), ("Ravi", 72), ("Meera", 95), ("Karan", 59), ("Divya", 81)]
for name,marks in students:
    if marks >= 90:
        print(f"{name} has a grade A")
    elif marks >= 80:
        print(f"{name} has a grade B")
    elif marks >= 70:
        print(f"{name} has a grade C")
    elif marks >= 60:
        print(f"{name} has a grade D")
    else:
        print(f"{name} has failed")
m=[]
n=[]
for marks in students:
    m.append(marks[1])
    n.append(marks[0])

print(m)
print(n)
avg=0
for i in m:
    avg=avg+i
    avg /= len(m)
print("the average of the class is",avg)
highest=students[0][1]
top_name=students[0][0]
for name,marks in students:
    if marks > highest:
        highest = marks
        top_name=name
print(f"The highest grade is {highest} by {top_name}.")

lowest=students[0][1]
lowest_name=students[0][0]
for name,marks in students:
    if marks < lowest:
        lowest = marks
        lowest_name=name
print(f"The lowest grade is {lowest} by {lowest_name}.")


#q7
import string

para = (
    "Cats love to play! Dogs love to run. Fast dogs and fast cats are both fun, but cats and dogs both love to sleep.")
p = para.lower()
l = list(p.split())
unwanted = ".,!?:;"
newl = []
for i in l:
    x = i.strip(unwanted)
    newl.append(x)
newl.sort()
print(newl)
c = []
w = []
count = 1
for i in range(0, len(newl) - 1):
    if newl[i] == newl[i + 1]:
        count += 1


    else:
        print(newl[i], "is repeated", count, "times")
        w.append(newl[i])
        c.append(count)
        count = 1
print(newl[-1], "is repeated", count, "times")
w.append(newl[-1])
c.append(count)
print(c)
print(w)

max_count = c[0]
for count in c:
    if count > max_count:
        max_count = count
for index, count in enumerate(c):
    if count == max_count:
        print(w[index])

# q9
p = input("enter password")
while True:
    l = list(p)
    e = []
    if len(p) < 8:
        e.append("Password is short")
    if p.lower() == "password":
        e.append("password is not allowed")
    if not any('A' <= char <= 'Z' for char in l):
        e.append("atleast one uppercase letter needed")
    if not any('a' <= char <= 'z' for char in l):
        e.append("atleast one lowercase letter needed")
    if not any('0' <= char <= '9' for char in l):
        e.append("atleast one digit needed")
    if not any(char == '!' or char == '@' or char == '#' or char == '$' or char == '%' or char == '&' or char == '*' for
               char in l):
        e.append("atleast one special character needed")
    if any(char == ' ' for char in l):
        e.append("no space allowed")
    if len(e) > 0:
        print(e)
        p = input("enter password")
    else:
        print("password is correct")
        break

# q8
python_class = ["Anil", "Bina", "Chetan", "Deepa", "Esha"]
java_class = ["Chetan", "Farhan", "Deepa", "Gita", "Bina"]
l1 = []
l2 = []
l3 = []
l4 = []
for i in range(0, len(python_class)):
    for j in range(0, len(java_class)):
        if python_class[i] == java_class[j]:
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
l4 = list(set(python_class))
l4.sort()

print("students enrolled in both classes", l1)
print("students only in python class", l2)
print("students only taking one course", l3)
print("sorted list of students", l4)

user = input("enter student name")
i = user.capitalize()
if i in l4:
    if i in l1:
        print("student in both class")
    elif i in l2:
        print("student in python class")
    elif i not in l1 and i not in l2 and i in l4:
        print("student in java class")
else:
    print("invalid name")

#q10
inventory = {
"pen": (10.0, 50),
"notebook": (45.0, 20),
"eraser": (5.0, 100),

"marker": (30.0, 15),
}
cart={}
while True:
    x = input("Enter item with quantity (or 'done'): ").strip().lower()
    if x == "done":
        break

    parts = x.split()
    if len(parts) != 2:
        print("wrong input")
        continue

    item, qty_text = parts

    if item not in inventory:
        print("unknown item")
        continue

    qty = int(qty_text)
    if qty <= 0:
        print("please enter a positive whole number")
        continue

    price, stock = inventory[item]
    if qty > stock:
        print("stock not available")
        continue

    cart[item] = cart.get(item, 0) + qty  # merges repeated items
    inventory[item] = (price, stock - qty)  # replace the tuple
    print(f"Added {qty} x {item}")

