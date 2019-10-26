def check_pet_weight(pet_weight, min_weight, max_weight):

    # Displays the maximum and minimum weights the pet has to between
    print("Your pet has to be between {}kg and {}kg to stay alive and happy.".format(min_weight, max_weight))

    # Displays the pets current weight for the user.
    print("Currently your pet weighs {}kg, so your pet is alive and happy!".format(pet_weight))


# Main Routine

# calling the function to test with general inputs
check_pet_weight(2.9, 1.5, 2.5)
