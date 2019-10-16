# for testing the name pet function
def list_items(list):
    # sets the number the list begins with to 1
    number = 1

    # uses the 'list' argument to assess what dictionary to take the items from to display.  (eg. if the argument given in the main routine was FOOD_DICTIONARY then the program lists the food.)
    for item in list:
        # displays the dictionary of items in an ordered list for the user to choose from. (formats the dictionary)
        print("{}.  {}".format(number, item))

        # makes the number increase as the list items increase
        number += 1


# this is the function This component is based around
def name_pet(path_list):

    # create a list of the two options, either 'write your own name' or 'chose from a list of super fun names' (using the list_items function).
    list_items(path_list)



# Main Routine
PATH = {"Write your own name": 1, "chose from a list of super fun names": 2}

# calling the function for testing
name_pet(PATH)

