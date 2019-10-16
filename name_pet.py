def name_pet():

    # the user inputs their name for the pet.
    pet_name = input("What would you like to name your pet?")

    # returns the name the user chooses so it can be used throughout the program.
    return pet_name

# Main Routine

# calling the function fro testing

pet_name = name_pet()
print (pet_name)
