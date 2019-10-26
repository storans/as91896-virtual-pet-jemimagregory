# for testing the name pet function
def list_items(list_name):
    # sets the number the list begins with to 1
    number = 1

    # uses the 'list' argument to assess what dictionary to take the items from to display.  (eg. if the argument given in the main routine was FOOD_DICTIONARY then the program lists the food.)
    for item in list_name:
        # displays the dictionary of items in an ordered list for the user to choose from. (formats the dictionary)
        print("{}.  {}".format(number, item))

        # makes the number increase as the list items increase
        number += 1


def choose_item(question, list_name):
    # asks the user for an input of which item (from the list which will always display above) they would like from the dictionary specified as an argument
    choice = int(input(question))

    # subtracting 1 from the number the user inputted so it conforms to the way lists are numbered starting at 0 rather than 1.
    choice -= 1

    # displaying to the user what they chose by taking the number they picked and using it as the index to access the 2d list of foods.
    print("you chose: {}".format(list_name[choice][0]))

    # returning what the user chose so it can be assessed outside of the this function
    return choice


# this is the function This component is based around
def name_pet(path_dictionary, path_list, names_dictionary, names_list):
    # create a list of the two options, either 'write your own name' or 'chose from a list of super fun names' (using the list_items function).
    list_items(path_dictionary)

    # asks the user to choose from the list (which path they want to take), using the choose_item function.
    choice = choose_item("Choose how you would like to name your pet: >>", path_list)

    # for testing
    # print(choice)

    # if the user chooses the path of writing their own name
    if choice == 0:

        # asks the user to input their name for the pet.
        pet_name = input("What would you like to name your pet? >>")

        # inform the user of what they wrote
        print("You chose: Herb, what a lovely name.")

        # returns the name the user chooses so it can be used throughout the program.
        return pet_name

    # if the user the chooses the path of picking a name from a list
    else:
        # prints a list of names using the list_item function
        list_items(names_dictionary)

        # uses the choose_item function to ask the user to choose from the list of names
        name_index = choose_item("Which name would you like to pick?", names_list)
        # print(name_index)
        chosen_name = names_list[name_index][0]
        # print(chosen_name)
        return chosen_name


# Main Routine
PATH_DICTIONARY = {"Write your own name": 1, "chose from a list of super fun names": 2}
PATH_LIST = [["Write your own name", 1], ["chose from a list of super fun names", 2]]
NAMES_DICTIONARY = {"Leaf": 1, "Noodles": 2, "Nofeet": 3, "Pretzel": 4, "Slip": 5, "Slinky": 6, "Slithers": 7,
                    "Sunshine": 8, "Worm": 9, "Zippy": 10, "Fluffy": 11, "Monty the Python": 12,
                    "William Snakespeare": 13}

NAMES_LIST = [["Leaf", 1], ["Noodles", 2], ["Nofeet", 3], ["Pretzel", 4], ["Slip", 5], ["Slinky", 6], ["Slithers", 7],
              ["Sunshine", 8], ["Worm", 9], ["Zippy", 10], ["Fluffy", 11], ["Monty the Python", 12],
              ["William Snakespeare", 13]]

# calling the function for testing
name = name_pet(PATH_DICTIONARY, PATH_LIST, NAMES_DICTIONARY, NAMES_LIST)

# for testing
# print("returned:{}".format(name))
