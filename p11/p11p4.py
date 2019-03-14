"""
Prompt the user for a non-negative int (n). If it is negative, print this and exit.
Else, find the factorial of 2*n. Set variable first_factorial = 1, i = 1, and while i<= 2*n, first_factorial *= i. i+=1.
Next, find the factorial of n+1. Set variable second_factorial = 1, 1 = 1, and while i<=n+1, second_factorial *=i. i+=1.
Next, find the factorial of n. Set variable third_factorial = 1, 1 = 1, and while i<=n, third_factorial *=i. i+=1.
Next, multiply second_factorial by third_factorial, and then divide the first factorial by the result of this
multiplication.
This is the Catalan number, therefore, print it out.
"""

number = int(input("Please enter a non-negative int: "))

if number >= 0:
    numberby2 = number * 2
    first_factorial = 1
    i = 1
    while i <= numberby2:
        first_factorial *= i
        i += 1

    numberplus1 = number + 1
    second_factorial = 1
    i = 1
    while i <= numberplus1:
        second_factorial *= i
        i += 1

    third_factorial = 1
    i = 1
    while i <= number:
        third_factorial *= i
        i += 1

    second_by_third = second_factorial * third_factorial

    catalan_number = first_factorial // second_by_third

    print("The catalan number of", number, "is:", catalan_number)

else:
    print("You need to enter a non-negative number!")












