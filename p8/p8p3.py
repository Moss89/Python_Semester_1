"""
This program prints out the times tables of a user inputted number. The values of 0 to 20, multiplied
by the user inputted number is shown.
Steps:
Prompt the user to enter a number.
Set variable i to 0.
Print the number that the user provided to show what number will be used for multiplication.
While i is less than 21, print the value of i, and the value of i multiplied by the user number.
Increment i after every loop.
"""


number = int(input("Please enter a number: "))

i = 0

print(number, "times table")
while i < 21:
    print(i, "         ", i*number)
    i += 1
