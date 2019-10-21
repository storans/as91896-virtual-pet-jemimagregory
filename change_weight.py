# uses the pet_weight argument to add/subtract the weight from
# uses the choice argument to know what to select from the list
# uses the two_d_list argument to assess what list the function needs to find the amount of weight to add.
def change_weight(weight, choice, two_d_list):
    # adds the weight linked to the option chosen (by accessing the list they came from)
    if choice == 0:
        weight += two_d_list[0][1]

    elif choice == 1:
        weight += two_d_list[1][1]
        # weight += 1

    else:
        weight += two_d_list[2][1]

    # displays the weight of the pet after the weight was added
    # print("your pet weights: {}kg".format(pet_weight))

    # returns the pet's weight so it can be accessed later, outside of the function.
    return weight


# Main Routine

# Lists for testing the function
FOOD_LIST = [['kale', 0.1], ['broccoli', 0.2], ['apple', 0.4]]
# using negative numbers so the function effectively takes weight away for exercise
EXERCISE_LIST = [['walking', -0.1], ['running', -0.2], ['hopping', -0.4]]

# Setting pet's default weight (this will change later)
pet_weight = 2

# for testing
print("this is the pet's weight before the function: {}".format(pet_weight))

# Setting 'running' as a choice for testing -should subtract 0.2 from the weight (this will become user input later on)
choice = int(input("input which exercise (between 0 and 2)"))

pet_weight = change_weight(pet_weight, choice, FOOD_LIST)

# for testing
print("this is the pet's weight after the function: {}".format(pet_weight))
