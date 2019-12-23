"""
Date: 2019-12-23
Purpose: This code will print the monthly payment for a loan given the amount, rate, and term information by the user
Author: Zach Archibald
"""


def validate_rate():
    while True:
        try:
            rate = float(input("What is the yearly rate (x%)? ").rstrip("%"))
            return rate
        except ValueError:
            print("Error: Please insert a validate percentage amount (i.e. 3.5")

def validate_integer_input(question):
    while True:
        try:
            amount = int(input(question))
            return amount
        except ValueError:
            print("Error: please input an integer amount.")


def main():
    print("Welcome to the mortgage calculator.")
    amount = validate_integer_input("What is the mortgage amount? ")
    rate = validate_rate() / 100
    terms = validate_integer_input("How many year terms? ")
    monthly_rate = rate / 12
    n = terms * 12

    payment = (amount * (monthly_rate * ((1 + monthly_rate) ** n))) / (((1 + monthly_rate) ** n) - 1)
    total_mortgage = payment * n
    total_interest = total_mortgage - amount

    print("Your monthly payment is: $" + "{:.2f}".format(payment))
    print("Total mortgage amount: $" + "{:.2f}".format(total_mortgage))
    print("Total interest paid: $" + "{:.2f}".format(total_interest))


if __name__ == "__main__":
    main()
