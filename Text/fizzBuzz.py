"""
Date: 2019-12-23
Purpose: This code will print the results of a fizz buzz game
Author: Zach Archibald
"""

for i in range(100):
    if i % 3 == 0 and i % 5 == 0:
        print ("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)