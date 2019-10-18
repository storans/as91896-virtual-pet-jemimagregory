def exit_program():
    # the goodbye message is displayed to the user
    print("Thank you for playing the Virtual Pet game! Goodbye!")

    # the 'alive' loop is broken, so the program ends
    alive = False

    # returning the alive variable so it can end the program outside of this function.
    return alive

# Main Routine

# setting alive to true to test if the function will change it to false
alive = True

#printing for testing purposes
print(alive)

# calling the function to test it
alive = exit_program()

#printing for testing purposes
print(alive)
