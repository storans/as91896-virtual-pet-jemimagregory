# including the exit program function for testing
def exit_program():
    # the goodbye message is displayed to the user
    print("Thank you for playing the Virtual Pet game! Goodbye!")

    # the 'alive' loop is broken, so the program ends
    alive = False

    # returning the alive variable so it can end the program outside of this function.
    return alive


# calls 'death' as an argument so the function knows how the equation for the difference needs to be ordered (death is usually assigned in the check_if_dead function)
def death_screen(pet_weight, death, min_weight, max_weight, exit_program_function):
    # if death is 'overweight' then the order for the equation is pet's weight minus the maximum weight
    if death == "overweight":
        # calculates the difference between the pet's weight and the maximum weight
        difference = pet_weight - max_weight

    # if death is 'underweight' then the order for the equation is the maximum weight minus the pet's weight
    else:
        difference = min_weight - pet_weight

    # rounds the difference to 2 decimal places for clarity
    difference = round(difference, 1)

    # tells the user why their pet died
    print("Your pet died because it was {}.".format(death))

    # displays the difference so the user can see how much their pet was over/under weight
    print("At {}kgs, your pet was {}kgs {}.".format(pet_weight, difference, death))

    exit_program_function()


# calling the function for testing using an appropriate (realistic) weight, labeling it correctly as overweight, and including the current min and max weights (which will be set as variables when the program is assembled)
death_screen(2.9, "overweight", 1.5, 2.5, exit_program)
