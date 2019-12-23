"""
Date: 2019-12-18
Purpose: This code will print the next highest prime number from a user input until the user says to stop
Author: Zach Archibald
"""

def is_prime(number):
    if number == 2:
        return True

    if number % 2 == 0:
        return False

    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True


def get_next_prime(num):
    next_num = num + 1
    prime_bool = is_prime(next_num)
    if prime_bool:
        return next_num
    else:
        return get_next_prime(next_num)


def validate_user_input():
    while True:
        num = input("Please enter the integer for which you would like to see the next prime number for: ")
        try:
            num = int(num)
            if num >= 10000:
                print("Error: please enter a number less than 10000")
            elif num < 0:
                print("Error: please enter a positive integer")
            else:
                return num
        except ValueError:
            print("Error: please enter an integer value")


def validate_find_next_input():
    while True:
        bool = input("Would you like to find the next highest prime (y/n)? ")
        if bool != "y" and bool != "n":
            print("Error: please submit a 'y' or an 'n'")
        elif bool == "y":
            return True
        else:
            return False

def keep_finding(num):
    next_prime = get_next_prime(num)
    print("The next prime number is " + str(next_prime))
    find_next = validate_find_next_input()
    if find_next:
        keep_finding(next_prime)
    else:
        print("Ending program.")

def main():
    num = validate_user_input()
    keep_finding(num)


if __name__ == "__main__":
    main()