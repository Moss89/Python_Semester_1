"""
Import the os module.
Prompt the user to input a file name, and check if it exists.
If it does, open and read the file, and initialise counters.
for line in testFile:
        readString = testFile.read()
        for i in range(len(readString)):
             if readString[i] == "[":
                sqbrackets += 1
            elif readString[i] == "]":
                sqbrackets -= 1
            elif readString[i] == ")":
                brackets -= 1
            elif readString[i] == "(":
                brackets += 1
                        ''''''
If there is a left bracket type, increment the counter. If there is a right bracket type, decrement it.
If the counter = -1, it means there is a right bracket type with no preceding left bracket type. Therefore there is
an imbalance. Print this fact, and exit.

Otherwise,
Print out the number of extra left brackets, and if the bracket type is balanced.
If there is any imbalance, print this out.
Close the file.

"""

import os
import sys


file = input("Please input an html file name (brackettest.txt to test): ")

if not os.path.isfile(file):
    print("File doesn't exist")
else:
    testFile = open(file, 'r')

    brackets = 0
    sqbrackets = 0
    curlbrackets = 0
    angbrackets = 0

    for line in testFile:
        readString = testFile.read()
        for i in range(len(readString)):
            if readString[i] == "[":
                sqbrackets += 1
            elif readString[i] == "]":
                sqbrackets -= 1
            elif readString[i] == ")":
                brackets -= 1
            elif readString[i] == "(":
                brackets += 1
            elif readString[i] == "<":
                angbrackets += 1
            elif readString[i] == ">":
                angbrackets -= 1
            elif readString[i] == "{":
                curlbrackets += 1
            elif readString[i] == "}":
                curlbrackets -= 1

            if brackets == -1 or sqbrackets == -1 or angbrackets == -1 or curlbrackets == -1:
                print("The brackets are imbalanced!")
                print("-1 value shows a right bracket type with no preceding left bracket type: () brackets:", brackets,
                      "[] brackets:", sqbrackets, "{} brackets:", curlbrackets, "<> brackets:", angbrackets)
                sys.exit()

    print("Number of extra left normal () brackets:", brackets)
    print("Number of extra left square [] brackets:", sqbrackets)
    print("Number of extra left angled <> brackets:", angbrackets)
    print("Number of extra left curly {} brackets:", curlbrackets)
    print("---------------------------------------------------------")

    if not (brackets == 0 and sqbrackets == 0 and angbrackets == 0 and curlbrackets == 0):
        print("There is a bracket imbalance!")
    else:
        print("The brackets are balanced!")

    testFile.close()
