"""
Define endofstring function, which checks to see if either of 2 strings appears at the end of the other, ignoring case.
Prompt the user for 2 strings.
Pass the strings to the endofstring function, and return and print
true if a string appears at the end of another. Otherwise return and
print false.
"""


def endofstring(stringy, stringy2):
    """
    :param stringy: string
    :param stringy2: string
    :return: True, False
    Strings are converted to lower case.
    Check if a string exists in another, and if true, find the index of the
     last occurrence of the string.
    If the index + length of the string equals the length of the other string,
    return true, otherwise false.

    """
    stringy, stringy2 = stringy.lower(), stringy2.lower()

    if stringy.rfind(stringy2) != -1:
        indexofstr = stringy.rfind(stringy2)
        if len(stringy) == indexofstr + len(stringy2):
            return True
        else:
            return False

    if stringy2.rfind(stringy) != -1:
        indexofstr = stringy2.rfind(stringy)
        if len(stringy2) == indexofstr + len(stringy):
            return True
        else:
            return False

    else:
        return False


stringy = input("Please enter a string: ")
stringy2 = input("Please enter another string: ")

print("Is either string at the end of the other string? :", endofstring(stringy, stringy2))





