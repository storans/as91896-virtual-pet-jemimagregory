SUPER_AGE = 65
keep_going = ""
while keep_going == "":
    age = int(input("How old are you?"))
    if age >= SUPER_AGE:
        print("You can have super")
    else:
        print("You cannot have super")

    keep_going = input("Do you want to continue?, enter to continue, any other key to exit")
