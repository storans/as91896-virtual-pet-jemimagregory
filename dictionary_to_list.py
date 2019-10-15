# Copying dictionary of food choices to a list -so they can be accessed using an index, rather than a key
def dictionary_to_two_d_list(dictionary):
    two_d_list = list(dictionary.items())

    # printing the new list craeted for testing purposes
    print (two_d_list)
    # returning the list created by the function so it can be used outside of this function
    return two_d_list


# Main Routine

# for testing the return statement
two_d_list = ("Error")

# an example list for testing purposes
FOOD_DICT = {"kale": 0.1, "broccoli": 0.2, "apple": 0.4}

dictionary_to_two_d_list(FOOD_DICT)

# printing the list to test for the return
print(two_d_list)

#TO FIX THE RETURN ISSUE, REMOVE THE RETURN (PROBABLY) AND MAKE THE CALLING THE DICT TO LIST FUNCTION EQUAL TO "LEW_LIST", THEN JUST PRINT LEW LIST TP TEST IT
