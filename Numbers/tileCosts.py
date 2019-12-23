"""
Date: 2019-11-16
Purpose: This code will find cost of tiling a room given the price, W, and H by the user
Author: Zach Archibald
"""


def validate_input(question):
    # All inputs must be able to be cast as a double
    while True:
        user_in = input(question)
        try:
            num = float(user_in)
            return num
        except ValueError:
            print("Error: please enter a float type variable.")


def main():
    price = validate_input("What is the price of the tile per square foot? ")
    width = validate_input("What is the width of your floor in feet? ")
    height = validate_input("What is the height of your floor in feet? ")

    cost = price * width * height
    print("The total cost of your tile will be: $" + "{:.2f}".format(cost))


if __name__ == "__main__":
    main()