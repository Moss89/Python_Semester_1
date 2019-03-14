"""
Define function funkyfunction, which will give the specified sequence.
Prompt the user for an int equal to or greater than 0.
While the number is >= 0, print funkyfunction(0), and if number > 0, then set counter i = 1, and while i <= number,
print funkyfunction(i), and increment i.
Prompt the user for another >= 0 int.
"""


def funkyfunction(num):
    """
    :param num:
    :return:
    if num == 0, return 13
    if num == 1, return 8
    if num > 1, funkyfunction(num-2) + 13 * funkyfunction(num-1)
    """
    if num == 0:
        print("num now at:", num)
        return 13
    elif num == 1:
        print("num now at:", num)
        return 8
    else:
        print("num now at:", num)
        return funkyfunction(num-2) + 13 * funkyfunction(num-1)


number = int(input("Please enter an int >= 0: "))

while number >= 0:
    # print("The series at term number: 0 = ", funkyfunction(0))
    # if number > 0:
    i = 0
    while i <= number:
        print("Term number:", i, " = ", funkyfunction(i))
        i += 1
    number = int(input("Please enter an int >= 0: "))




