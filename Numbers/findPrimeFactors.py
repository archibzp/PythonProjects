"""
Date: 2019-11-16
Purpose: This code will print all prime factors of a provided number
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


def find_prime_factors(number):
    prime_factors = []
    for i in range(2, number + 1):
        if number % i == 0:
            # Add check for if factor is prime
            if is_prime(i):
                prime_factors.append(i)
    return prime_factors


def validate_user_input():
    """
    Take in a user input for number between 0 and 10000
    :return: int number to find prime factors of
    """
    while True:
        num = input("Enter a number to find its prime factors? ")
        try:
            number = int(num)
            if number >= 10000:
                print("Error: Please use a number less than 10000")
            elif number < 0:
                print("Error: Please enter a positive integer")
            else:
                return number
        except ValueError:
            print("Error: Please enter a valid integer.")


def main():
    number = validate_user_input()
    factors = find_prime_factors(number)
    print(factors)


if __name__ == "__main__":
    main()
