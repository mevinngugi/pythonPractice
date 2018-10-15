# The Collatz Sequence


def collatz(number):

    # Check if number is even or odd
    # Even number
    if number % 2 == 0:
        new_number = number // 2

        if new_number > 1:
            print(new_number)

            # Resursive function
            return collatz(new_number)
        else:
            return 1

    # Odd number
    elif number % 2 == 1:
        new_number = 3 * number + 1

        if new_number > 1:
            print(new_number)
            # Resursive function
            return collatz(new_number)
        else:
            return 1


def theCollatzProblem():

    while True:

        print("The Collatz Problem.")

        # Get user input that is of type integer.
        try:
            user_input = int(input("Enter a number:\n"))
            return collatz(user_input)

        # Return an error if a string iskeyed in.
        except ValueError:
            print("Error: Invalid input\n")


print(theCollatzProblem())
