def format_header(character, output):
    print()
    # Printing the character accounting for the length of the output
    # and two spaces between the character and the output
    print(character * (len(output) + 6))
    print("{} {} {}".format(character, output, character))
    print(character * (len(output) + 6))
    print()


words = "This is the output"

format_header('#', words)
