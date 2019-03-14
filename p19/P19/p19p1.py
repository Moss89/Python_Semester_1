"""
Define function convertdec, which takes a number in base 10 and a base
(2-16), and returns the number in the base supplied.
Prompt the user for 2 positives int, one the number, one the base (2-16)
If the number isn't positive or the base isn't 2-16, print the error and exit.
Otherwise, pass the number and base to the convertdec function, which will print
out the result.
"""


def convertdec(num, base):
    """
    :param num: int
    :param base: int (2 - 16)
    If num > 0, recursively call convertdec(num//base, base)
    remainder = num % base, If base > 10, remainder 10 = A,......15 = F.
    Print out remainder.
    """
    if num > 0:
        convertdec(num//base, base)
        remainder = num % base
        if base > 10:
            if remainder == 10:
                remainder = "A"
            elif remainder == 11:
                remainder = "B"
            elif remainder == 12:
                remainder = "C"
            elif remainder == 13:
                remainder = "D"
            elif remainder == 14:
                remainder = "E"
            elif remainder == 15:
                remainder = "F"
        print(remainder, sep=",", end="")


number = int(input("Please enter a positive int which you want converted: "))
base = int(input("Please enter a positive int which you want to be the base (2 to 16): "))

if number > 0 and 1 < base < 17:
    convertdec(number, base)
else:
    print("Number must be positive, and the base must be between 2 and 16")
