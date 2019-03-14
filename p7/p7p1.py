'''
The program finds whether a year is a leap year or not.
Steps:
Prompt the user to input a year, and cast it to an int. Print the year entered.
If the input is not greater than or equal to 0, print a message stating this is a requirement.
If the year is greater than or equal to zero, then check both that the year modulus 4 is equal to zero AND
the year modulus 100 is not equal to zero,
OR that the year modulus 400 equals 0.
If the expression is true, print that the year is a leap year.
Otherwise, print that it is not a leap year.
Print out that the program has finished.
'''

year = int(input("Please input a year: "))

print("Year entered", year)

if year >= 0:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")

else:
    print("Year must be greater than or equal to zero")

print("Finished!")

