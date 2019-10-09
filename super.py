#Check that a person is eligible for superannuation

SUPER_AGE = 65
#Loop to allow testing of different values
keep_going = ""
while keep_going == "":
    age = int(input("How old are you?"))

    #Must be greater than OR equal to 65 (in order to catch 65 year olds)
    if age >= SUPER_AGE:
        print("You can have super")
    else:
        print("You cannot have super")

    keep_going = input("Do you want to continue?, enter to continue, any other key to exit")
