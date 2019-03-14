"""
Define perfectnum function, which finds whether the sum of a number's factors equals the number.
Prompt the user for a positive int, and pass it as an argument to the perfectnum function.
Print out whether the number is a perfect number or not.
"""


def perfectnum(num):
    """
    :param num:
    :return:
    True if the sum of the factors of num equals num
    False if the sum of the factors does not equal num
    """
    total = 0
    for i in range(1, (num//2)+1):
        if num % i == 0:
            total += i
            print("Factor is :", i)
    if total == num:
        return True
    else:
        return False


number = int(input("Please enter a positive int: "))
if number > 0:
    print("Is", number, "a perfect number? :", perfectnum(number))

