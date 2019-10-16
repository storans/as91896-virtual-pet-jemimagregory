# Using the weight boundaries as arguments so they can be easily changed when the program is put together
def help_information(min_weight, max_weight):

    # displays the information to help the user understand how the program works.
    print("This game about your pet is super fun when you know how it works!\n"
          "How your virtual pet works:\n"
          "1. Your pet has to stay healthy by being a good weight (between {}kg and {}kg)\n"
          "2. You need to feed and exercise your pet so it stays a healthy weight.".format(min_weight, max_weight))


# Main Routine

# current min and max weights for testing
help_information(1.5, 2.5)
