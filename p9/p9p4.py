"""
This program prompts the user for a number, and then gives the factorial of that number.
Steps:
Prompt user for a number; if it's negative, stop the program.
Else, set total = 0, i = 1, and while i is less than or equal to the user number, add i to total.
Print the total.
Repeat step 1.
"""


number = int(input("Please enter a positive integer (negative to quit): "))

while number >= 0:
    total = 1
    i = 1
    while i <= number:
        total *= i
        i += 1
    print("The factorial of", number, "is:", total)
    number = int(input("Please enter a positive integer: (negative to quit) "))
