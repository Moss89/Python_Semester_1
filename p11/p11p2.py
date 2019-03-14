"""
Prompt the user to enter a positive int which will be the limit they want to calculate the fibonacci series up to.
This series will start at 1.
If the int isn't a positive number, print this out and exit.
Otherwise, set a = 0, b = 1, i = 0. Print "Series is:"
While i < the user inputted int, set b,a = b + a, b and append the print statement above with(b, ", ").Increment i by 1.
Print "finished" after the loop.
"""
number = int(input("Enter the limit you want to calculate the "
                   "fibonacci series up to (int > 0): "))


if number > 0:
    a = 0
    b = 1
    i = 0
    print("Series is: ", sep="", end="")
    while i < number:
        b, a = b + a, b
        print(b, ", ", sep="", end="")
        i += 1
    print("finished!")

else:
    print("Must be a positive integer!")
