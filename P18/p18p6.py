"""
Import the os module.
Prompt the user to input a file name, and check if it exists.
If it does, open and read the file, and initialise counters.
for line in htmlFile:
        readString = htmlFile.read()
        for i in range(len(readString)):
            if readString[i:i+4] == "<!--":
                increment leftCom
                    ''''
            elif readString[i:i+3] == "-->":
                increment rightCom

Store the number of instances found in a string, and close the file.
Open a file file for writing, called results.txt. Check if it exists.
Write the string to results.txt, and close the file.

"""


import os
file = input("Please input an html file name (index.html to test): ")

if not os.path.isfile(file):
    print("File doesn't exist")
else:
    htmlFile = open(file, 'r')

    leftBr = 0
    rightBr = 0
    newLn = 0
    lowe = 0
    leftCom = 0
    rightCom = 0

    # for line in htmlFile:
    readString = htmlFile.read()
    for i in range(len(readString)):
            if readString[i:i+4] == "<!--":
                leftCom += 1
            elif readString[i] == "<":
                leftBr += 1
            elif readString[i] == ">":
                rightBr += 1
            elif readString[i] == "\n":
                newLn += 1
            elif readString[i] == "e":
                lowe += 1
            elif readString[i:i+3] == "-->":
                rightCom += 1

    outputStr = ("Number of - left angle brackets: " + str(leftBr) + " right angle brackets: " + str(rightBr) + " newlines: " +
            str(newLn) + " lowercase letter e: " + str(lowe) + " the string <!--: " + str(leftCom) + " and the string -->: " + str(rightCom))

    htmlFile.close()

    output = open("results.txt", "w")

    if not os.path.isfile('results.txt'):
        print("Failed to create results file")
    else:
        print("results.txt successfully created")

    output.write(outputStr)
    output.close()
