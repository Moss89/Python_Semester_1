"""
Define function convertdec, takes a string of digits, representing a number, and a base (an int) as
arguments, and returns the number in decimal (Base 10).
Prompt the user for a string of numbers, and an int for the base (2-16)
If the number isn't positive or the base isn't 2-16, print the error and exit.
Otherwise, pass the number and base to the convertdec function, which will print
out the result, if the inputted number is a valid number in that base.
"""
import sys


def convertdec(num, base):
    """
    :param num: string
    :param base: int (2-16)
    Initialize total = 0, and power = len(num)-1.
    Convert num to uppercase.
    For char in num, if char = A, char = 10......F = 15
    Test if the char is valid input and that the number is valid for the base, if not, exit.
    Convert char to int. Total += converted int * base * power.
    power -=1
    print total.
    """
    num = num.upper()
    validstring = "0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F,10,11,12,13,14,15"
    total = 0
    power = len(num)-1
    for char in num:
        if char == "A":
            char = "10"
        elif char == "B":
            char = "11"
        elif char == "C":
            char = "12"
        elif char == "D":
            char = "13"
        elif char == "E":
            char = "14"
        elif char == "F":
            char = "15"
        if char not in validstring:
            print("Numbers must contain only 0-9, a-f, A-F!")
            sys.exit()
        if int(char) >= base:
            print("This is not a valid number for this base!")
            sys.exit()
        convert = int(char)
        total += convert * base ** power
        power -= 1

    print(total)


number = (input("Please enter a positive int which you want converted (A to F also allowed): "))
base = int(input("Please enter a positive int which represents the number's base (2 to 16): "))


if len(number) == 1 and number[0] == "0":
    print("Number must be positive!")
    sys.exit()
elif len(number) == 0 or not 1 < base < 17:
    print("Number string can't be blank, and/or base must be between 2 and 16")
    sys.exit()

convertdec(number, base)
