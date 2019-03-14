"""
This program prompts the user for a number, and then gives the factorial of the number.
Steps:
Prompt user for a positive number, if it's not positive, print this fact.
Else, set total = 1, and for i in range(1, user number +1), multiply i by the total.
Print the total.
"""


number = int(input("Please enter a positive integer: "))

if number < 0:
    print("You did not enter a positive integer!")

else:
    total = 1
    for i in range(1, number+1):
        total *= i

    print("The factorial of", number, "is:", total)
