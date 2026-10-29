l=[]
while True:
    print("MENU")
    print("1 - add items")
    print("2 - remove items")
    print("3 - view list")
    print("4 - sort list")
    print("5 - exit")
    choice =input("Enter your choice: ")
    if choice == "1":
        s=input("enter an item")
        itm=s.capitalize()
        if itm in l:
            print("the item is already present")
        else:
            l.append(itm)
    elif choice == "2":
        f=input("enter a item")
        rm=f.capitalize()
        if rm in l:
            l.remove(rm)
        else:
            print("the item is not in the list")
    elif choice == "3":
        print(l)
    elif choice == "4":
        l.sort()
        print(l)
    else:
        break
