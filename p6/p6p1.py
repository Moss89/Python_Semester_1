'''
The program will add two numbers and determine if the result is larger than 100. If it is, a message will
be displayed
Steps:
Get the first number from the user
Get the second number from the user
If the first number plus the second number is larger than 100, print out "That is a big number!"
Otherwise print nothing and terminate
'''

number1 = float(input("Enter a number: "))
number2 = float(input("Which number do you want to add to your previous number?:"))

if number1 + number2 > 100:
    print("That is a big number!")
