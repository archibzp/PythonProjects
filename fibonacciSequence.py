"""
Date: 2019-11-16
Purpose: This code will print the fibonacci sequence to a specified number of values
Author: Zach Archibald
"""


def build_sequence(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


def validate_user_input():
    """
    Take in a user input for number of sequence items between 0 and 10000
    :return: int number of digits
    """
    while True:
        num = input("How many sequence items would you like to see? ")
        try:
            seq_size = int(num)
            if seq_size >= 10000:
                print("Error: Please use a number less than 10000")
            elif seq_size < 0:
                print("Error: Please enter a positive integer")
            else:
                return seq_size
        except ValueError:
            print("Error: Please enter a valid integer.")


def main():
    seq_size = validate_user_input()
    for num in build_sequence(seq_size):
        print(num)


if __name__ == "__main__":
    main()
