def name_pet():
    # asks the user if they would like to enter their own name or choose from a list
    path = input("How would you like to name your pet? EITHER: write OR choose")

    if path == 'write':
        # the user inputs their name for the pet.
        pet_name = input("What would you like to name your pet?")
        print(pet_name)

    else:
        print("1. John\n"
              "2. Aimee\n"
              "3. Olivia\n"
              "4. George\n"
              "5. Madelynn")

        pet_name = int(input("Choose from the list:"))
        if pet_name == 1:
            pet_name = "John"
        if pet_name == 2:
            pet_name = "Aimee"
        if pet_name == 3:
            pet_name = "Olivia"
        if pet_name == 4:
            pet_name = "George"
        print(pet_name)


# Main Routine

# calling the function fro testing

name_pet()
