"""
Prompt the user to enter an int.
If the number is negative, print this fact and exit.
Set root to 0. While root * 2 is less than or equal to the user inputted number, check if the root * 2
equals to the number. If it does, print out that root is a perfect square root of the number, then exit.
Otherwise, increment root by 1.
If no perfect square is found, then print this fact out and exit.
"""

import sys

number = int(input("Please enter an int to find the square root of. Enter a negative number to exit. "))
root = 0


if number < 0:
    print("Negative number entered, now exiting the program.")
    sys.exit()

else:
    while (root ** 2) <= number:
        if (root ** 2) == number:
            print("The perfect square root of", number, "is", root)
            sys.exit()
        root += 1
print("No perfect square root of the number exists")
sys.exit()



