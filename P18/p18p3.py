"""
Define countcode function to count the number of instances of "co*e" in a string, where
* can be any upper or lower case letter.
Prompt the user to enter a string, and pass it as an argument to the countcode function.
Print out the returned count.
"""


def codecount(stringy):
    chars = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
    count = 0
    for i in range(0, len(stringy)-3):
        if stringy[i] == "c":
            if stringy[i+1] == "o":
                if stringy[i+2] in chars:
                    if stringy[i+3] == "e":
                        count += 1
    return count


stringy = input("Please enter a string: ")
print("The word co(any letter)e is in the string", codecount(stringy), "times.")
