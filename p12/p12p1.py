"""
Prompt the user to enter a non negative int.
Define the function to calculate the factorial.

-
Function:
Take an int as an argument, initialize the counter to 1.
For i in range 1 to int +1, counter *= i.
return counter.
-

If the user entered number is non negative, pass the number as an argument to the definition, return the factorial,
and print it.
Otherwise, print that the number must be non negative.

"""
from datetime import datetime

number = int(input("Please enter a non negative number: "))
startTime = datetime.now()


def fact(num):
    factorial = 1
    for i in range(1, num+1):
        factorial *= i
    return factorial


if number >= 0:
    print("The factorial of", number, "is", fact(number))
    print(datetime.now() - startTime)

else:
    print("The number must be non negative!")







