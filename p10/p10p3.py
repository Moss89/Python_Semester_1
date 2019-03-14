"""
Prompt the user for a string; empty string exits the program.
While the string isn't empty, set variable counter = 0.
For each character in the string, check if it's a vowel.
If it is a vowel, increment the counter by 1.
After the for loop, print the number of vowels found in the string.
Repeat step 1.

"""

string = input("Please enter a string. Empty string to exit: ")

while string != "":
    counter = 0
    for char in string:
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u" or char == "A" or char == "E" or char\
                == "I" or char == "O" or char == "U":
            counter += 1
    print("The number of vowels in", string, "=", counter)
    string = input("Please enter a string. Empty string to exit ")