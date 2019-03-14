"""
Define the definition to calculate the divisors of a number, which will return them in a tuple.
Prompt the user to enter a positive int. If it isn't positive, print that the number must be positive.
Otherwise call the divisors() function passing in the int, and print out the common divisors.
Set total counter to 0, and iterate through divisors with a for loop, adding the common divisors to total to find the
sum of those divisors, and print out total.
"""


def finddivisors(num1):
    """
    :param num1: int
    :return: a tuple containing the divisors of num1
    """

    divisors = (1,)
    for i in range(2, num1//2 + 1):
        if num1 % i == 0:
            divisors += (i,)
    return divisors


number1 = int(input("Enter a positive int: "))


if number1 <= 0:
    print("Number should be > 0.")
else:
    divisors = finddivisors(number1)
    print("The divisors of", number1,
          "are:", divisors)

    total = 0
    for d in divisors:
        total += d
    print("Sum of the divisors is:", total)
print("Finished!")


