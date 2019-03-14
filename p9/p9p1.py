"""
This program prompts the user for a number, and then gives the sum of all the numbers up to and including that number.
Steps:
Prompt user for a positive number, if it's not positive, print this fact.
Else, set total = 0, i = 1, and while i is less than or equal to the user number, add i to total.
Print the total.
"""


number = int(input("Please enter a positive integer: "))

if number < 1:
    print("You did not enter a positive integer!")

else:
    total = 0
    i = 1
    while i <= number:
        total += i
        i += 1
    print("The sum of the numbers up to and including", number, "is: ", total)
