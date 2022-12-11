#! /usr/bin/python
"""
how to check if a number is even or odd

"""

input_number1 = input("Enter value to check if number is even or not:")
input_number2 = input("Enter value to check if number is even or not:")

a = int(input_number1)
b = int(input_number2)
if a % 2 == 0:
    print(a, " is an even number")

else:
    print(a, " is an odd number")
    print(b, "is od")
if b % 2 == 0:
    print(b, "is even")
else:
    print(b, "is odd")