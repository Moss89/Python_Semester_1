"""
Prompt the user to enter a non negative int.
Define the function to calculate the fibonacci sequence.

-
Function:
Take an int as an argument, initialize a = 0, b = 1.
if num == 0, print 0 produces no output.
if num == 1, print a.
if num == 2, print a and b.
else, print a and b, and for i in range 2, int, b,a = b+a, b, then append the print with b
print new line
-

If the user entered number is non negative, pass the number as an argument to the definition which will print
the fibonacci series out from within the function. If the number == 0, print there is no output.
Otherwise, print that the number must be non negative.

"""
number = int(input("Please enter a non negative number: "))


def fib(num):
    a = 0
    b = 1
    if num == 0:
        print("0 produces no output!")
    elif num == 1:
        print("The series is ", a)
    elif num == 2:
        print("The series is ", a, ", ", b, sep="")

    else:
        print("The series is ", a, ", ", b, sep="", end="")

    for i in range(2, num):
        b, a = b+a, b
        print(",", b, end="")
    print()


if number >= 0:
    fib(number)

else:
    print("The number must be non negative!")