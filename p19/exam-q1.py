"""
Import sys to allow for exit functionality.
Prompt the user to enter a year > 0
if year > 0:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 900 != and year % 900 != 600:
                print not a Revised Julian leap year and exit
            else: print it is a Revised Julian leap year and exit
        else: print it is a Revised Julian leap year and exit
    else: print not a Revised Julian leap year and exit
else: print error and exit

"""


import sys

inputYear = int(input("Please enter a year (>0) to check if it is a leap year in the Revised Julian calendar: "))
if inputYear > 0:
    if inputYear % 4 == 0:
        if inputYear % 100 == 0:
            if inputYear % 900 != 200 and inputYear % 900 != 600:
                print("This isn't a Revised Julian Leap year!")
                sys.exit()
            else:
                print("This is a Revised Julian Leap year!")
                sys.exit()
        else:
            print("This is a Revised Julian Leap year!")
            sys.exit()
    else:
        print("This isn't a Revised Julian Leap year!")
        sys.exit()
else:
    print("Please input a year number greater than 0!")
    sys.exit()


