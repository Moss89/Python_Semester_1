"""
Define countcode function to count the number of instances of "code" in a string.
Prompt the user to enter a string, and pass it as an argument to the countcode function.
Print out the returned count.
"""


def countcode(stringy):
    """

    :param stringy: String
    :return: count (int), which is the number of times "code" appears.
    """
    count = 0
    for i in range(0, len(stringy)-3):
        if stringy[i] == "c":
            if stringy[i+1] == "o":
                if stringy[i+2] == "d":
                    if stringy[i+3] == "e":
                        count += 1
    return count


stringy = input("Please enter a string: ")
print("The word code is in the string", countcode(stringy), "times.")
