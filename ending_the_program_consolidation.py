def dictionary_to_two_d_list(dictionary):
    two_d_list = list(dictionary.items())

    # returning the list created by the function so it can be used outside of this function
    return two_d_list

def choose_item(question, list_name):
    # asks the user for an input of which item (from the list which will always display above) they would like from the dictionary specified as an argument
    choice = int(input(question))

    # subtracting 1 from the number the user inputted so it conforms to the way lists are numbered starting at 0 rather than 1.
    choice -= 1

    # displaying to the user what they chose by taking the number they picked and using it as the index to access the 2d list of foods.
    print("you chose: {}".format(list_name[choice][0]))

    # assigning the value to choice
    # choice = list_name[choice][0]

    # returning what the user chose so it can be assessed outside of the this function
    return choice

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
    print("your pet weights: {}kg".format(pet_weight))

    # returns the pet's weight so it can be accessed later, outside of the function.
    return weight


def check_if_dead(weight, min_weight, max_weight):

    if weight > max_weight:

        # if the pet_weight exceeds the maximum weight, assigns death to 'overweight'
        death_type = "overweight"

        # returns the death so it can be used to identify that the pet is dead and that the program needs to end, it's also used outside the function (in the death_screen function)
        return death_type

        # this has been moved to the main routine
        # if the pet_weight exceeds the maximum weight, the death_screen function runs.
        # death_screen(weight, death_type, min_weight, max_weight)

    elif weight < min_weight:

        # if the pet_weight doesn't reach the minimum weight, assigns death to 'underweight'
        death_type = "underweight"

        # returns the death so it can be used to identify that the pet is dead and that the program needs to end, it's also used outside the function (in the death_screen function)
        return death_type

        # this has been moved to the main routine
        # if the pet_weight exceeds the maximum weight, the death_screen function runs.
        # death_screen(weight, death_type, min_weight, max_weight)

    # if the pet is still within the minimum and maximum weights the function ends
    else:
        death_type = "alive"
        return death_type


# calls 'death' as an argument so the function knows how the equation for the difference needs to be ordered (death is usually assigned in the check_if_dead function)
def death_screen(weight, death, min_weight, max_weight):
    # if death is 'overweight' then the order for the equation is pet's weight minus the maximum weight
    if death == "overweight":
        # calculates the difference between the pet's weight and the maximum weight
        difference = weight - max_weight

    # if death is 'underweight' then the order for the equation is the maximum weight minus the pet's weight
    else:
        difference = min_weight - weight

    # rounds the difference to 2 decimal places for clarity
    difference = round(difference, 1)

    # tells the user why their pet died
    print("Your pet died because it was {}.".format(death))

    # displays the difference so the user can see how much their pet was over/under weight
    print("At {}kgs, your pet was {}kgs {}.".format(weight, difference, death))

    # pet_dead = exit_program()

    # return pet_dead


def exit_program():
    # the goodbye message is displayed to the user
    print("Thank you for playing the Virtual Pet game! Goodbye!")

    # the 'alive' loop is broken, so the program ends
    pet_alive = False

    # returning the alive variable so it can end the program outside of this function.
    return pet_alive


# Main Routine

# Setting dictionaries/lists
NAMES_DICTIONARY = {"Leaf": 1, "Noodles": 2, "Nofeet": 3, "Pretzel": 4, "Slip": 5, "Slinky": 6, "Slithers": 7,
                    "Sunshine": 8, "Worm": 9, "Zippy": 10, "Fluffy": 11, "Monty the Python": 12,
                    "William Snakespeare": 13}

FOOD_DICTIONARY = {"kale": 0.1, "broccoli": 0.2, "apple": 0.4}

EXERCISE_DICTIONARY = {"walking": -0.1, "running": -0.2, "hopping": -0.4}

PATH_DICTIONARY = {"Write your own name": 1, "chose from a list of super fun names": 2}

MAIN_MENU_ITEMS = ["Check Pet's Weight", "Feed Pet", "Exercise Pet", "See Help Information", "Exit Game"]

FOOD_LIST = dictionary_to_two_d_list(FOOD_DICTIONARY)

EXERCISE_LIST = dictionary_to_two_d_list(EXERCISE_DICTIONARY)

NAMES_LIST = dictionary_to_two_d_list(NAMES_DICTIONARY)

PATH_LIST = dictionary_to_two_d_list(PATH_DICTIONARY)


pet_weight = 2

max_weight = 2.5

min_weight = 1.5


# A variable set to True to check whether the program should continue running.
alive = True

# Start an infinite loop to prompt for a correct option value
while alive:

    path= int(input("enter choice (1) >>"))

    if path == 1:
        choice = choose_item("What would you like to feed your pet?", FOOD_LIST)
        pet_weight = change_weight(pet_weight, choice, FOOD_LIST)
        life = check_if_dead(pet_weight, min_weight, max_weight)
        if life == "overweight" or life == "underweight":
            death_screen(pet_weight, life, min_weight, max_weight)
            alive = exit_program()
    else:
        print("error")
