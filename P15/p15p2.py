"""
Define function funkyfunction, which will give the Eulerian numbers sequence.
Prompt the user for an int equal to or greater than 1.
While the number is >= 1, for i in range 1, number +1, print funkyfunction(i).
Prompt the user for another int.
"""


def funkyfunction(num):
    """
    :param num:
    :return:
    if num == 1, return 1
    if num > 1, funkyfunction(num-1) + 2 ** num-1
    """
    if num == 1:
        print("num now at:", num)
        return 1
    else:
        print("num now at:", num)
        return funkyfunction(num-1) + 2 ** num-1


number = int(input("Please enter an int >= 1: "))

while number >= 1:
    print("The series is: ")
    for i in range(1, number + 1):
        print("Term number:", i, " = ", funkyfunction(i))
    number = int(input("Please enter an int >= 1: "))




