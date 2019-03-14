'''
The program finds whether a year is a leap year or not.
Steps:
Prompt the user to input a year, and cast it to an int. Print the year entered.
If the year modulus 4 is not equal to zero, print the year is a common year.
else if the year modulus 100 is not equal to zero, print the year is a leap year.
else if the year modulus 400 is not equal to zero, print it is a common year.
else, print it is a leap year.
'''


year = int(input("Please input a year: "))

print("Year entered", year)

if year % 4 != 0:
    #you can't divide it by 4 so it's not a leap year
    print(year, "is a common year")
elif year % 100 != 0:
    #you can divide it by 4, and you can't divide it by 100, so it's a leap year.
    print(year, "is a leap year")
elif year % 400 != 0:
    #you can divide it by 4, you can divide it by 100, you can't divide it by 400, so it's a common year
    print(year, "is a common year")
    #you can divide it by 4, you can divide it by 100, you can divide it by 400, so it's a leap year
else:
    print(year, "is a leap year")
