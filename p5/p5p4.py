# Take user input and convert to int
number = int(input("Input a number: "))

# Find which range the number is within and print out the range.

if 0 < number <= 20:
    print("Number is greater than 0 and less than or equal to 20")

elif 20 < number <= 40:
    print("Number is greater than 20 and less than or equal to 40")

elif 40 < number <= 60:
    print("Number is greater than 40 and less than or equal to 60")

elif 60 < number <= 80:
    print("Number is greater than 60 and less than or equal to 80")

elif 80 < number <= 100:
    print("Number is greater than 80 and less than or equal to 100")

elif number > 100:
    print("Number is greater than 100")

# If the number is less than zero, print this fact out
elif number < 0:
    print("Number is less than 0")

# If the number isn't positive or negative, it must be zero.
else:
    print("Number is equal to 0")



