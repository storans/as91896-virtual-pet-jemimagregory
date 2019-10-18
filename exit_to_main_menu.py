# including the list items function and welcome screen function for testing
# This function is used after the main explanation of how the program works
def welcome_screen(pet_name):
    # displays an introduction of the pet rabbit to the user
    print("This is your pet, {}!".format(pet_name))
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

def list_items(list_name):
    # sets the number the list begins with to 1
    number = 1

    # uses the 'list' argument to assess what dictionary to take the items from to display.  (eg. if the argument given in the main routine was FOOD_DICTIONARY then the program lists the food.)
    for item in list_name:
        # displays the dictionary of items in an ordered list for the user to choose from. (formats the dictionary)
        print("{}.  {}".format(number, item))

        # makes the number increase as the list items increase
        number += 1


# this is the function this component is centred around
def exit_to_main_menu(back_to_function, leave_function, pet_name, list_name):
    # asks the user if they would like to continue to the main menu
    leave = input("Would you like to return to the main menu? ENTER to exit, or PRESS ANY KEY to return to what you were just doing")

    # (using an if statement to move onto the function listing the main menu items (by entering) if the user chooses to move to the main menu [if leave  == ""]
    if leave == "":
        leave_function(list_name)

    # else, go back to [back_to function])
    else:
        back_to_function(pet_name)


# Main Routine
MAIN_MENU_ITEMS = ["Check Pet's Weight", "Feed Pet", "Exercise Pet", "See Help Information", "Exit Game"]

# calling the function to test it, using the welcome_screen function screen as a test of what the user may have been doing before deciding the wanted to exit
exit_to_main_menu(welcome_screen, "Slip", MAIN_MENU_ITEMS)
