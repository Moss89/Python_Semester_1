"""
Prompt the user to enter a non negative float and a tolerance.
Define the function to calculate the square root using exhaustive enumeration with the user inputted number and
tolerance.

-
Function:
Take 2 floats as arguments, num and tol which are the number and tolerance.
Initialize step = tol ** 2, root = 0.0
while (num - root ** 2) >= tol and (root ** 2 <= num), root += step
if num - root**2 < tol, return root. Otherwise return -1.
-

If the user entered number is non negative, pass the number and tolerances as arguments to the definition which will
gives an approximation of the square root. Return this value, and print it if it is not -1. If it is, print no root
approximation found.
Otherwise, print that the number must be non negative.

"""

number = float(input("Please enter a non negative number: "))
tolerance = float(input("Please enter a tolerance: "))


def sqroot(num, tol):
    step = tol ** 2
    root = 0.0
    while (num - root ** 2) >= tol and (root**2 <= num):
        root += step

    if (num - root**2) < tol:
        return root
    else:
        return -1


if number >= 0:
    square = sqroot(number, tolerance)
    if square != -1:
        print("The approx square root of", number, "is", sqroot(number, tolerance))
    else:
        print("No approx square root could be found.")

else:
    print("The number must be non negative!")
