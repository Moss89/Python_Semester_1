"""
This program prompts the user for a number, and then gives the sum of all the numbers up to and including that number.
This continues until the user enters a non-positive number.
Steps:
Prompt user for a positive number, if it's not positive, then exit.
While the number is positive, set total = 0, and for i in range(1, user number +1), add i to the total.
Print the total.
Return to the first step.
"""


number = int(input("Please enter a positive integer (non-positive number to stop): "))

while number > 0:
        total = 0
        for i in range(1, number+1):
            total += i
        print("The sum of the numbers up to and including", number, "is:", total)
        number = int(input("Please enter a positive integer (non-positive number to stop) : "))

