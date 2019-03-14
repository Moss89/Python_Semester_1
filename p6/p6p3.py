'''
    Steps:
    Prompt the user to enter their name.
    Compare the inputted string against the programmer's name, printing "That is a
    cool name!" if they are equal.
    Else, if they the string equals "Mickey Mouse" or "Spongebob Squarepants", then "I'm not sure that's your
    name" is printed.
    Otherwise, "You have a nice name" is printed.
'''

name = input("Please enter your name: ")

if name == "Tomas":
    print("That is a cool name!")
elif name == "Mickey Mouse" or name == "Spongebob Squarepants":
    print("I'm not sure that's your name")
else:
    print("You have a nice name")



