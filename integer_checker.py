def check_int(question, low, high, error):  # using generalised arguments so I can use this function in lots of places
    valid = False

    # The try and except is ensuring the value can be converted to an integer. If it can, the infinite loop is broken so the program can continue
    while not valid:
        try:

            # asks for the user's input, checks the input is an integer -for questions that have a numerical input from the user
            number = int(input("{}".format(question)))

            # checks that the user's input is between the lowest acceptable number and the highest acceptable number.
            if low <= number <= high:

                # returns the user's input if it meets all the criteria
                return number

            # if the user's input doesn't meet all the criteria then the error message is printed
            else:
                print(error)
                print()

        # the except branch of the try and except prints the error message if there is a value error.
        except ValueError:
            print(error)


# Main routine

# testing the function (5 times to make testing easier)
for i in range(5):
    choice = check_int("Enter a number between 1 and 5: ", 1, 5, "Just the number (integer) between 1 and 5, please")

    print(choice)
