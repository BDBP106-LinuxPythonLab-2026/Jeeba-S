inventory = {
"pen": (10.0, 50),
"notebook": (45.0, 20),
"eraser": (5.0, 100),
"marker": (30.0, 15),
}
cart={}

while True:
    i = input("enter items with quantity")
    if i.lower == 'done':
        break
    if i not in inventory:
        print("invalid input")
    if i.split() != 2:
        print("please enter item name and quantity with a space in between")
    else:
        cart.append(i)

