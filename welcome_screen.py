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

# Main Routine

welcome_screen("Rodney")
