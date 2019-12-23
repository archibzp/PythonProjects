"""
Date: 2019-11-16
Purpose: This code will display E to a specified number of decimal places
Author: Zach Archibald
"""

import math

def validate_user_input():
    """
    Take in a user input for number of digits between 0 and 10000
    :return: int number of digits
    """
    while True:
        num = input("How many digits of E would you like to see? ")
        try:
            digits = int(num)
            if digits >= 10000:
                print("Error: Please use a number less than 10000")
            elif digits < 0:
                print("Error: Please enter a positive integer")
            else:
                return digits
        except ValueError:
            print("Error: Please enter a valid integer.")


def main():
    digits = validate_user_input()
    e = str(math.e)
    print(e[:digits + 1])


if __name__ == "__main__":
    main()
