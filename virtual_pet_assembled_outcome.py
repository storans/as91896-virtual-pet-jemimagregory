import time


# using generalised arguments so I can use this function in lots of places
def check_int(question, low, high):
    valid = False
    error = "Please enter an number (whole number) between {} and {} -a" \
            " number from the list above." \
        .format(low, high)

    # The try and except is ensuring the value can be converted to an integer.
    # If it can, the infinite loop is broken so the program can continue
    while not valid:
        try:

            # asks for the user's input, checks the input is an integer
            # for questions that have a numerical input from the user
            number = int(input("{} >> ".format(question)))
            # checks that the user's input is between the lowest acceptable
            # number and the highest acceptable number.
            if low <= number <= high:

                # returns the user's input if it meets all the criteria
                return number

            # if the user's input doesn't meet all the criteria
            # then the error message is printed
            else:
                print(error)
                print()

        # the except branch of the try and except prints the error message
        # if there is a value error.
        except ValueError:
            print(error)


def list_items(dictionary_name):
    # sets the number the list begins with to 1
    number = 1

    # uses the 'list' argument to assess what dictionary
    # to take the items from to display.
    # (eg. if the argument given in the main routine was FOOD_DICTIONARY
    # then the program lists the food.)
    for item in dictionary_name:
        # displays the dictionary of items in an ordered list for the user
        # to choose from. (formats the dictionary)
        print("{}.  {}".format(number, item))

        # makes the number increase as the list items increase
        number += 1
    print()


def choose_item(question, list_name, low, high):
    # asks the user for an input of which item
    # (from the list which will always display above)
    # they would like from the dictionary specified as an argument
    pick = check_int(question, low, high)

    # subtracting 1 from the number the user inputted
    # so it conforms to the way lists are numbered starting at 0 rather than 1
    pick -= 1

    print()

    # displaying to the user what they chose
    # by taking the number they picked
    # and using it as the index to access the 2d list of foods.
    print("You chose: {}".format(list_name[pick][0]))

    # assigning the value to choice
    # choice = list_name[choice][0]

    # returning what the user chose
    # so it can be assessed outside of the this function
    return pick


def dictionary_to_two_d_list(dictionary):
    two_d_list = list(dictionary.items())

    # returning the list created by the function
    # so it can be used outside of this function
    return two_d_list


def opening_screen():
    # giving the component a header so the user can easily see what's going on
    header_ = "Welcome to Virtual Pet Snake Game"
    header_character_ = "*"
    format_header(header_character_, header_)
    print("Virtual Pets are great for proving to your parents that you are "
          "responsible enough to own a real pet. \n"
          "To keep your virtual pet snake alive you will need to balance "
          "feeding the pet and exercising it,"
          " so it stays a good weight.")


def name_pet(path_dictionary, path_list, names_dictionary, names_list,
             path_low, path_high, list_low, list_high):
    # giving the component a header so the user can easily see what's going on
    header_ = "Naming Your Pet"
    header_character_ = "-"
    format_header(header_character_, header_)
    # create a list of the two options
    # either 'write your own name' or 'chose from a list of super fun names'
    # (using the list_items function).
    list_items(path_dictionary)
    # asks the user to choose from the list (which path they want to take)
    # using the choose_item function.
    user_choice = choose_item("How would you like to name your pet? ",
                              path_list, path_low, path_high)

    # if the user chooses the path of writing their own name
    if user_choice == 0:
        # asks the user to input their name for the pet. -using the .title
        # to capitalise the name the user writes.
        name = input("What would you like to name your pet? >> ").title()

        # inform the user of what they wrote
        print("You chose: {}, what a lovely name.".format(name))

        # returns the name the user chooses
        # so it can be used throughout the program.
        return name

    # if the user the chooses the path of picking a name from a list
    else:
        # prints a list of names using the list_item function
        list_items(names_dictionary)

        # uses the choose_item function to ask the user to choose
        # from the list of names
        name_index = choose_item("Which name would you like to pick?",
                                 names_list, list_low, list_high)
        # print(name_index)
        chosen_name = names_list[name_index][0]
        # print(chosen_name)
        return chosen_name


# This function is used after the main explanation of how the program works
def welcome_screen(name):
    # displays an introduction of the pet rabbit to the user
    print("This is your pet snake, {}!".format(name))
    print("   _________         ________ \n"
          "  /         \       /         \  \n"
          " /  /~~~~~\  \     /  /~~~~~\  \ \n"
          " |  |     |  |     |  |     |  | \n"
          " |  |     |  |     |  |     |  | \n"
          " |  |     |  |     |  |     |  |         / \n"
          " |  |     |  |     |  |     |  |       // \n"
          "(O  O)    \  \_____/  /     \  \_____/ / \n"
          " \__/      \         /       \        / \n"
          "  |         ~~~~~~~~~         ~~~~~~~~ \n"
          "  ^")


def choose_item(question, two_d_list, int_low, int_high):
    # asks the user for an input of which item
    # (from the list which will always display above)
    # they would like from the dictionary specified as an argument
    pick = check_int(question, int_low, int_high)

    # subtracting 1 from the number the user inputted
    # so it conforms to the way lists are numbered starting at 0 rather than 1
    pick -= 1

    # displaying to the user what they chose by taking the number they picked
    # and using it as the index to access the 2d list of foods.
    print("You chose: {}".format(two_d_list[pick][0]))

    # returning what the user chose
    # so it can be assessed outside of the this function
    return pick


def check_pet_weight(weight, minimum, maximum):
    # Displays the maximum and minimum weights the pet has to between
    print("Your pet has to be between {}kg and {}kg to stay alive and happy.".
          format(minimum, maximum))

    # Displays the pets current weight for the user.
    print("Currently your pet weighs {}kg, so your pet is alive and happy!".
          format(weight))


# uses the pet_weight argument to add/subtract the weight from
# uses the pick argument to know what to select from the list
# uses the two_d_list argument to assess what list the function
# needs to find the amount of weight to add.
def change_weight(weight, pick, two_d_list):
    # adds the weight linked to the option chosen
    # (by accessing the list they came from)
    if pick == 0:
        weight += two_d_list[0][1]

    elif pick == 1:
        weight += two_d_list[1][1]

    else:
        weight += two_d_list[2][1]

    # rounds the difference to 2 decimal places for clarity
    weight = round(weight, 2)

    # displays the weight of the pet after the weight was added
    print("Your pet now weighs: {}kg".format(weight))

    # returns the pet's weight so it can be accessed later,
    # outside of the function.
    return weight


def check_if_dead(weight, minimum, maximum):
    if weight > maximum:

        # if the pet_weight exceeds the maximum weight,
        # assigns death to 'overweight'
        death_type = "overweight"

        # returns the death so it can be used to identify that the pet is dead
        # and that the program needs to end
        # it's also used outside the function (in the death_screen function)
        return death_type

        # this has been moved to the main routine
        # if the pet_weight exceeds the maximum weight,
        # the death_screen function runs.
        # death_screen(weight, death_type, min_weight, max_weight)

    elif weight < minimum:

        # if the pet_weight doesn't reach the minimum weight,
        # assigns death to 'underweight'
        death_type = "underweight"

        # returns the death so it can be used to identify that
        # the pet is dead and that the program needs to end,
        # it's also used outside the function (in the death_screen function)
        return death_type

    elif weight == 1.5 or weight == 2.5:
        death_type = "close"
        return death_type

    # if the pet_weight exceeds the maximum weight,
    # the death_screen function runs.
    # death_screen(weight, death_type, min_weight, max_weight)
    # if the pet is still within the minimum and maximum weights
    # the function ends
    else:
        death_type = "alive"
        return death_type


# calls 'death' as an argument
# so the function knows how the difference equation needs to be ordered
# (death is usually assigned in the check_if_dead function)
def death_screen(weight, death, minimum, maximum):
    # giving the component a header so the user can easily see what's going on
    header_ = "Your Pet Has Died"
    header_character_ = "^"
    format_header(header_character_, header_)

    # displays a picture of the dead pet snake to the user
    print("   _________         ________ \n"
          "  /         \       /         \  \n"
          " /  /~~~~~\  \     /  /~~~~~\  \ \n"
          " |  |     |  |     |  |     |  | \n"
          " |  |     |  |     |  |     |  | \n"
          " |  |     |  |     |  |     |  |         / \n"
          " |  |     |  |     |  |     |  |       // \n"
          "(x  x)    \  \_____/  /     \  \_____/ / \n"
          " \__/      \         /       \        / \n"
          "  |         ~~~~~~~~~         ~~~~~~~~ \n"
          "  ^")
    # if death is 'overweight'
    # then the order for the equation is pet's weight minus the maximum weight
    if death == "overweight":
        # calculates the difference between
        # the pet's weight and the maximum weight
        difference = weight - maximum

    # if death is 'underweight' then the order for the equation
    # is the maximum weight minus the pet's weight
    else:
        difference = minimum - weight

    # rounds the difference to 2 decimal places for clarity
    difference = round(difference, 1)

    # tells the user why their pet died
    print("Your pet died because it was {}.".format(death))

    # displays the difference so the user can see
    # how much their pet was over/under weight
    print("At {}kgs, your pet was {}kgs {}."
          .format(weight, difference, death))


def exit_program():
    # giving the component a header so the user can easily see what's going on
    header_ = "Goodbye!"
    header_character_ = "="
    format_header(header_character_, header_)

    # the goodbye message is displayed to the user
    print("Thank you for playing the Virtual Pet game! Goodbye!")

    # the 'alive' loop is broken, so the program ends
    pet_alive = False

    # returning the alive variable so it can
    # end the program outside of this function.
    return pet_alive


# Using the weight boundaries as arguments so they can be
# easily changed when the program is put together
def help_information(minimum, maximum):
    # displays the information
    # to help the user understand how the program works.
    print("This game about your pet is super fun when you know how it works!"
          "\n"
          "How your virtual pet works:\n"
          "1. Your pet has to stay healthy by being a good weight "
          "(between {}kg and {}kg)\n"
          "2. You need to feed and exercise your pet so it stays a healthy"
          " weight.".format(minimum, maximum))
    print()
    print("It is important to not spend too much time looking at screens be"
          "cause looking at screens for too long can cause health problems\n"
          "It is recommended that you spend a maximum of 2 hours looking"
          " at a screen each day.\n"
          "Enjoy playing this game, but don't play"
          " for too long!")


def format_header(character, output):
    print()
    # Printing the character accounting for the length of the output
    # and two spaces between the character and the output
    print(character * (len(output) + 6))
    print("{} {} {}".format(character, output, character))
    print(character * (len(output) + 6))
    print()


def goodbye_snake():
    print("                  _________         ________ \n"
          "                 /         \       /         \  \n"
          "                /  /~~~~~\  \     /  /~~~~~\  \ \n"
          "                |  |     |  |     |  |     |  | \n"
          "                |  |     |  |     |  |     |  | \n"
          "                |  |     |  |     |  |     |  |         / \n"
          "   ________     |  |     |  |     |  |     |  |       // \n"
          "  /        \   (O  O)    \  \_____/  /     \  \_____/ / \n"
          " | Goodbye! - - \__/      \         /       \        / \n"
          "  \________/     |         ~~~~~~~~~         ~~~~~~~~ \n"
          "                 ^")


# Main Routine

# Setting dictionaries/lists
NAMES_DICTIONARY = {"Leaf": 1, "Noodles": 2, "Nofeet": 3, "Pretzel": 4,
                    "Slip": 5, "Slinky": 6, "Slithers": 7, "Sunshine": 8,
                    "Worm": 9, "Zippy": 10, "Fluffy": 11,
                    "Monty the Python": 12, "William Snakespeare": 13}

FOOD_DICTIONARY = {"spiders": 0.1, "rat": 0.2, "chicken": 0.3,
                   "small dog": 0.4, "rabbit": 0.3, "bird": 0.2, "fish": 0.1}

EXERCISE_DICTIONARY = {"slither": -0.1, "slip around": -0.2,
                       "climb a tree": -0.3, "swim": -0.3, "chase prey": -0.4}

PATH_DICTIONARY = {"Write your own name": 1, "Chose from a list of super fun "
                                             "names": 2}

MAIN_MENU_ITEMS_DICTIONARY = {"Check Pet's Weight": 1, "Feed Pet": 2,
                              "Exercise Pet": 3, "See Help Information": 4,
                              "Exit Game": 5}

FOOD_LIST = dictionary_to_two_d_list(FOOD_DICTIONARY)

EXERCISE_LIST = dictionary_to_two_d_list(EXERCISE_DICTIONARY)

NAMES_LIST = dictionary_to_two_d_list(NAMES_DICTIONARY)

PATH_LIST = dictionary_to_two_d_list(PATH_DICTIONARY)

MAIN_MENU_ITEMS_LIST = dictionary_to_two_d_list(MAIN_MENU_ITEMS_DICTIONARY)

pet_weight = 2

max_weight = 2.5

min_weight = 1.5

opening_screen()

pet_name = name_pet(PATH_DICTIONARY, PATH_LIST, NAMES_DICTIONARY, NAMES_LIST,
                    1, 2, 1, 13)

welcome_screen(pet_name)
# adds a pause after the pet is named
time.sleep(3)

# A variable set to True to check whether the program should continue running.
alive = True

# Start an infinite loop to prompt for a correct option value
while alive:

    # giving the component a header so the user can easily see what's going on
    header = "Main Menu"
    header_character = "="
    format_header(header_character, header)
    list_items(MAIN_MENU_ITEMS_DICTIONARY)

    path = choose_item("What would you like to do?", MAIN_MENU_ITEMS_LIST,
                       1, 5)

    if path == 0:
        # giving the component a header so the user can easily see what's
        # going on
        header = "Check {}'s Weight".format(pet_name)
        header_character = "-"
        format_header(header_character, header)
        check_pet_weight(pet_weight, min_weight, max_weight)
        # adds a pause after the pet's weight is displayed
        time.sleep(3)

    elif path == 1:
        # giving the component a header so the user can easily see what's
        # going on
        header = "Feed {}".format(pet_name)
        header_character = "-"
        format_header(header_character, header)
        list_items(FOOD_DICTIONARY)
        choice = choose_item("What would you like to feed your pet?",
                             FOOD_LIST, 1, 7)
        pet_weight = change_weight(pet_weight, choice, FOOD_LIST)
        # adds a pause after the pet is fed
        time.sleep(3)
        life = check_if_dead(pet_weight, min_weight, max_weight)
        if life == "overweight" or life == "underweight":
            death_screen(pet_weight, life, min_weight, max_weight)
            alive = exit_program()
        elif life == "close":
            print("{} is very close to being overweight, and dying. "
                  "You should exercise them very soon.".format(pet_name))

    elif path == 2:
        # giving the component a header so the user can easily see what's
        # going on
        header = "Exercise {}".format(pet_name)
        header_character = "-"
        format_header(header_character, header)
        list_items(EXERCISE_DICTIONARY)
        choice = choose_item("How would you like to exercise your pet?",
                             EXERCISE_LIST, 1, 5)
        pet_weight = change_weight(pet_weight, choice, EXERCISE_LIST)
        # adds a pause after the pet is exercised
        time.sleep(3)
        life = check_if_dead(pet_weight, min_weight, max_weight)
        if life == "overweight" or life == "underweight":
            death_screen(pet_weight, life, min_weight, max_weight)
            alive = exit_program()
        elif life == "close":
            print("{} is very close to being underweight, and dying. "
                  "You should feed them very soon.".format(pet_name))

    elif path == 3:
        # giving the component a header so the user can easily see what's
        # going on
        header = "Help Information"
        header_character = "-"
        format_header(header_character, header)
        help_information(min_weight, max_weight)
        # adds a pause after the help information is displayed
        time.sleep(3)

    else:
        # giving the component a header so the user can easily see what's
        # going on
        header = "Exit Game"
        header_character = "-"
        format_header(header_character, header)
        goodbye_snake()
        alive = exit_program()
