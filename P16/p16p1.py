"""
Define function funkyfunction, which will give the specified sequence (2 to the power of entered number).
Prompt the user for an int equal to or greater than 1.
While the number is >= 1, set counter i = 1, and while i <= number,
print funkyfunction(i), and increment i.
Prompt the user for another >= 1 int.
"""


def funkyfunction(num):
    """
    :param num:
    :return:
    if num == 1, return 2
    if num > 1, 2*(funkyfunction(num - 1))
    """
    if num == 1:
        print("num now at:", num)
        return 2
    else:
        print("num now at:", num)
        return 2*(funkyfunction(num - 1))


number = int(input("Please enter an int >= 1: "))

while number >= 1:
    i = 1
    while i <= number:
        print("Term number:", i, " = ", funkyfunction(i))
        i += 1
    number = int(input("Please enter an int >= 1: "))




