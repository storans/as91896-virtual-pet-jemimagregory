def list_items(list_name):
    # sets the number the list begins with to 1
    number = 1

    # uses the 'list' argument to assess what dictionary to take the items from to display.  (eg. if the argument given in the main routine was FOOD_DICTIONARY then the program lists the food.)
    for item in list_name:
        # displays the dictionary of items in an ordered list for the user to choose from. (formats the dictionary)
        print("{}.  {}".format(number, item))

        # makes the number increase as the list items increase
        number += 1


# Main Routine

# a list for testing the function with
FOOD_DICT = {"kale": 0.1, "broccoli": 0.2, "apple": 0.4}

# calling the function for testing
list_items(FOOD_DICT)
