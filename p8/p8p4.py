"""
This program asks the user to input numbers, then counts how many of the numbers fall into certain ranges.
Steps:
Create counter variables to count how many times a number falls into a certain range.
Prompt the user for input.
If the number lands within a certain range, then the counter for that range is increased by 1.
If the user enter a negative number, the count for each range is displayed and the program exits.
"""
import sys

number = int(input("Input a number (negative to quit): "))

number0 = 0
number0_20 = 0
number20_40 = 0
number40_60 = 0
number60_80 = 0
number80_100 = 0
number100plus = 0


# Find which range the number is within and print out the range.
while number >= 0:
    if 0 < number <= 20:
        print("Number is greater than 0 and less than or equal to 20")
        number0_20 += 1

    elif 20 < number <= 40:
        print("Number is greater than 20 and less than or equal to 40")
        number20_40 += 1

    elif 40 < number <= 60:
        print("Number is greater than 40 and less than or equal to 60")
        number40_60 += 1

    elif 60 < number <= 80:
        print("Number is greater than 60 and less than or equal to 80")
        number60_80 += 1

    elif 80 < number <= 100:
        print("Number is greater than 80 and less than or equal to 100")
        number80_100 += 1

    elif number > 100:
        print("Number is greater than 100")
        number100plus += 1

    elif number == 0:
        print("Number is equal to 0")
        number0 += 1

    number = int(input("Input a number (negative to quit): "))


print("The amount of numbers equal to 0 =", number0)
print("The amount of numbers in the range 0 - 20 =", number0_20)
print("The amount of numbers in the range 21 - 40 =", number20_40)
print("The amount of numbers in the range 41 - 60 =", number40_60)
print("The amount of numbers in the range 61 - 80 =", number60_80)
print("The amount of numbers in the range 81 - 100 =", number80_100)
print("The amount of numbers greater than 100 =", number100plus)
sys.exit()


