#!/usr/bin/env python3
# Created By: Abdul
# Date: 10/30/2025
# Program to ask the user for an integer


def main():
    # get user input and handle exceptions
    user_num = input("Please enter a positive integer: ")
    try:
        user_num = int(user_num)
        if user_num < 0:
            print("Please enter a positive integer.")
        else:
            # loop to calculate squares up to user input
            for counter in range(0, user_num + 1):
                square_value = counter**2

                # show the counter and square value
                print(f"{counter}² is {square_value}")

    except ValueError:
        print(user_num, "is not an integer.")

    # display ending message to user no matter the outcome
    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
