# calls 'death' as an argument so the function knows how the equation for the difference needs to be ordered (death is usually assigned in the check_if_dead function)
def death_screen(pet_weight, death, min_weight, max_weight):
    # if death is 'overweight' then the order for the equation is pet's weight minus the maximum weight
    if death == "overweight":
        # calculates the difference between the pet's weight and the maximum weight
        difference = pet_weight - max_weight

    # if death is 'underweight' then the order for the equation is the maximum weight minus the pet's weight
    else:
        difference = min_weight - pet_weight

    # tells the user why their pet died
    print("Your pet died because it was {}.".format(death))

    # displays the difference so the user can see how much their pet was over/under weight
    print("At {}, your pet was {}kgs {}.".format(pet_weight, difference, death))

    # sets alive to false, which ends the loop running the program and the program ends.
    alive = False

    # returns alive so it can be known outside of the function
    return alive


# Main Routine

# setting alive to true to test if the function will change it to false
alive = True
print(alive)

# calling the function for testing using an appropriate (realistic) weight, labeling it correctly as overweight, and including the current min and max weights (which will be set as variables when the program is assembled)
alive = death_screen(2.9, "overweight", 1.5, 2.5)

print(alive)
