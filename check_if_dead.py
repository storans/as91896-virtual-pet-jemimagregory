def check_if_dead(weight, min_weight, max_weight):

    if weight > max_weight:

        # if the pet_weight exceeds the maximum weight, the death_end function runs.
        death_end()

        # if the pet_weight exceeds the maximum weight, assigns death to 'overweight'
        death_type = "overweight"

        # returns the death so it can be used outside the function (in the death_screen function)
        return death

    elif weight < min_weight:

        # if the pet_weight doesn't reach the minimum weight, the death_end function runs.
        death_end()

        # if the pet_weight doesn't reach the minimum weight, assigns death to 'underweight'
        death_type = "underweight"

        # returns the death so it can be used outside the function (in the death_screen function)
        return death_type

    # if the pet is still within the minimum and maximum weights the function ends
    else:
        return


# death_end function for testing purposes
def death_end():
    print("death end function, will eventually be in this place")


# Main Routine

# setting pet_weight for testing
pet_weight = float(input("enter the pet's weight: "))

# setting minimum_weight for testing
minimum_weight = 1.5

# setting maximum_weight for testing
maximum_weight = 2.5

death = check_if_dead(pet_weight, minimum_weight, maximum_weight)

# print 'death' for testing if it can now be used outside of the function and that the function gets the output i expect
print(death)
