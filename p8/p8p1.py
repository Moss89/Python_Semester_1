"""
This program prints out whether a number is divisible by 2,3,5 and/or 7.
Steps:
Prompt user for number, negative number to quit.
While the number isn't negative check:
If the number = 0, print that the result is always 0 after being divided.
If the number isn't divisible by 2,3,5, and/or 7, print out this fact.
If the number is divisible by 2,3,5, and/or 7, then print this out.
Print it all as a single line, by changing the print "end" property to "".
"""


number = float(input("Please enter a number (negative number to quit): "))

while number >= 0:
    print("The number is:", number, sep=" ", end="")
    if number % 2 == 0 and number != 0:
        print(", which is divisible by: 2", sep=" ", end="")
    if number % 3 == 0 and number != 0:
        print(", which is divisible by: 3", sep=" ", end="")
    if number % 5 == 0 and number != 0:
        print(", which is divisible by: 5", sep=" ", end="")
    if number % 7 == 0 and number != 0:
        print(", which is divisible by: 7", sep=" ", end="")
    if number % 2 != 0 and number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
        print(", this number is not divisible by 2, 3, 5, or 7.")
    elif number == 0:
        print(", which when divided by anything is 0.")

    number = float(input("\nPlease enter another number (negative number to quit): "))




