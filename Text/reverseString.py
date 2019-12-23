"""
Date: 2019-12-23
Purpose: This code will reverse a given string
Author: Zach Archibald
"""


def reverse_string(string):
    return string[::-1]


def main():
    string_to_reverse = input("Please insert the string you would like to see reversed: ")
    string_reversed = reverse_string(string_to_reverse)
    print(string_reversed)


if __name__ == "__main__":
    main()