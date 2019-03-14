"""
Prompt the user to enter a non negative int.
Define the function to calculate the factorial recursively.
If the user entered number is non negative, pass the number as an argument to the definition, return the factorial,
and print it.
Otherwise, print that the number must be non negative.
"""

from datetime import datetime

number = int(input("Please enter a non negative number: "))
startTime = datetime.now()
def fact(x):
    """
    :param x:
    :return:

    if x == 0, return 1
    if x is greater than 0, return x * fact(x-1)
    """

    if x == 0:
        print("X is currently 0!")
        return 1

    else:
        print("x is currently", x)
        return x * fact(x - 1)


if number >= 0:
    print("The factorial of", number, "is", fact(number))
    print(datetime.now() - startTime)

else:
    print("The number must be non negative!")
