"""
Prompt the user to enter an int, and 0 to exit.
While the int is not 0, set variable cube to 0. While cube**3 < abs(int), increment cube.
If cube**3 == abs(int), check if int is negative, then set cube to negative.
Print cube is the perfect cube root of the int.
If cube**3 != abs(int), print no perfect cube root of the int was found.
Repeat step 1.
"""

import sys

number = int(input("Please enter an int to find the cube root of. Enter 0 to exit. "))

if number == 0:
    print("0 entered, now exiting the program.")
    sys.exit()

while number != 0:
    cube = 0
    while cube ** 3 < abs(number):
            cube += 1
    if cube ** 3 == abs(number):
        if number < 0:
            cube = -cube
        print("The perfect cube root of", number, "is", cube)
    if cube ** 3 != abs(number):
        print("No perfect cube root of the number exists")

    number = int(input("Please enter an int to find the cube root of. Enter 0 to exit. "))
