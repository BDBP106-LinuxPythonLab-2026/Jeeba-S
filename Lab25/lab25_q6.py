line = input("Enter a line of CSV: ")
fields = line.split(",")

if len(fields) <= 3:
    print("Error: there must be more than 3 fields.")
else:
    third = fields[2].strip()

    # a very basic email check
    if (
        " " not in third
        and third.count("@") == 1
        and not third.startswith("@")
        and "." in third.split("@")[1]
        and not third.endswith(".")
        and not third.split("@")[1].startswith(".")
    ):
        print("The 3rd field is a valid email address.")
    else:
        print("The 3rd field is NOT an email address.")