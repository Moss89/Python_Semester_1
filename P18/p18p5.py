"""
Define function isxyz, which checks if there is an instance of xyz in
a string which isn't preceded with a ".".
Prompt the user for a string. Pass the string to the isxyz,
and print out the return statement; either true or false.
"""


def isxyz(stringy):
    """
    :param stringy: string
    :return:
    If index of xyz = 0, or [i]-1 != ".", return true.
    Else, return false.
    """
    if stringy.find("xyz") != -1:
        indexofstr = stringy.find("xyz")
        if indexofstr == 0:
            return True
        elif stringy[indexofstr-1] != ".":
            return True
        else:
            return False
    else:
        return False


stringy = input("Please enter a string: ")

print("Does the string contain an instance of xyz that isn't preceded by a '.'?:", isxyz(stringy))


