"""
Date: 2019-11-16
Purpose: This code will calculate Pi using the Chudnovsky method to a specified number of decimal places
Author: Zach Archibald
"""

import math


def sqrt(n, digits):
    """
    Return the square root of n as a fixed point number with the one
    passed in.  It uses a second order Newton-Raphson convergence.  This
    doubles the number of significant figures on each iteration.
    :param n: value to find square root of
    :param digits: one million
    :return: square root value
    """

    float_point = 10 ** 16
    n_float = float((n * float_point) // digits) / float_point
    x = (int(float_point * math.sqrt(n_float)) * digits) // float_point
    n_one = n * digits
    while True:
        x_old = x
        x = (x + n_one // x) // 2
        if x == x_old:
            break
    return x


def calculatePi(digits):
    """
    This function will calculate pi using the Chudnovsky method
    :param digits: number of digits to show in Pi value
    :return: float(pi)
    """

    k = 1
    a_k = digits
    a_sum = digits
    b_sum = 0
    c = 640320
    c3_over_24 = c ** 3 // 24
    while True:
        a_k *= -(6 * k - 5) * (2 * k - 1) * (6 * k - 1)
        a_k //= k ** 3 * c3_over_24
        a_sum += a_k
        b_sum += k * a_k
        k += 1
        if a_k == 0:
            break
    total = 13591409 * a_sum + 545140134 * b_sum
    pi = (426880 * sqrt(10005 * digits, digits) * digits) // total
    return pi


def validate_user_input():
    """
    Take in a user input for number of digits between 0 and 10000
    :return: int number of digits
    """
    while True:
        num = input("How many digits of Pi would you like to see? ")
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
    pi = str(calculatePi(10 ** (digits * 10)))[:digits]
    print("Complex: " + pi[0] + "." + pi[1:])
    pi_str = str(math.pi)
    print("Simple: " + pi_str[:digits + 1])


if __name__ == "__main__":
    main()
