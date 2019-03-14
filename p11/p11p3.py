"""
Prompt the user to enter a non-negative int which will be the limit they want to calculate the fibonacci series up to.
This series will start at 1.
If the int is negative, print this out and exit.
While the user's int is greater than or equal to 0:
If the int = 0, print this out and ask for a positive number.
Else, set a = 0, b = 1, print("series is: ")
For i in range(user's int), set b,a = b + a, b and append the print statement above with(b, ", ").
Print "finished" after the loop.
Repeat step 1.
"""

number = int(input("Enter the limit you want to calculate the "
                   "fibonacci series up to (negative to exit): "))

while number >= 0:

    if number == 0:
        print("Please enter a positive integer")

    else:
        a = 0
        b = 1
        print("Series is: ", sep="", end="")

        for i in range(number):
            b, a = b + a, b
            print(b, ", ", sep="", end="")
        print("finished!")
        print()
        
    number = int(input("Enter the limit you want to calculate the "
                           "fibonacci series up to (int > 0): "))


if number < 0:
    print("Limit cannot be a negative number, program exiting")
