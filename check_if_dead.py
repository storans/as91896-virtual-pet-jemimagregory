def check_if_dead(pet_weight, min, max):

    if pet_weight > max:

        # if the pet_weight exceeds the maximum weight, the death_end function runs.
        death_end()

        # if the pet_weight exceeds the maximum weight, assigns death to 'overweight'
        death = "overweight"

        # returns the death so it can be used outside the function (in the death_screen function)
        return death

    elif pet_weight < min:

        # if the pet_weight doesn't reach the minimum weight, the death_end function runs.
        death_end()

        # if the pet_weight doesn't reach the minimum weight, assigns death to 'underweight'
        death = "underweight"

        # returns the death so it can be used outside the function (in the death_screen function)
        return death

    # if the pet is still within the minimum and maximum weights the function ends
    else:
        return

# death_end function for testing purposes
def death_end():
    print("death end function, will eventually be in this place")
