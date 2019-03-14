"""
Define the definition to calculate common divisors, which will return them.
Prompt the user to enter two positive ints. If either isn't positive, print that the number must be positive.
Otherwise call the divisors() function passing in the two ints, and print out the common divisors.
Set total counter to 0, and iterate through divisors with a for loop, adding the common divisors to total to find the
sum of those divisors, and print out total.
"""


def finddivisors(num1, num2):
    """
    :param num1: int
    :param num2: int
    :return: a tuple containing the common divisors of num1 and num2
    """

    divisors = ()
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
                divisors += (i,)
    return divisors


number1 = int(input("Enter a positive int: "))
number2 = int(input("Enter another positive int: "))

if number1 <= 0 or number2 <= 0:
    print("Numbers should be > 0.")
else:
    divisors = finddivisors(number1, number2)
    print("The common divisors of", number1, "and", number2,
          "are:", divisors)

    total = 0
    for d in divisors:
        total += d
    print("Sum of the common divisors is:", total)
print("Finished!")
