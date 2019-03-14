"""
Read line from file
line.lower
myGuesses = 6
create list length of string -1, fill with -
prompt user for guess
if guess in line, replace - in string with the guess
else, decrease remaining guesses
if guesses = 0, lose, exit
else, if all list revealed, win
"""
import sys
import os

myFile = "exam-q2.txt"
myGuesses = 6


if not os.path.isfile(myFile):
    print("File doesn't exist")
else:
    myWords = open(myFile, 'r')

    myLine = myWords.readline()
    myLine = myLine.lower()

    stringLength = len(myLine)-1
    print(stringLength)

    myList = ["-"] * stringLength

    alreadyGuessed = ""

    while myGuesses > 0:
        print("The word to guess is:", myList)
        userGuess = input("Please guess a letter! ")
        userGuess.lower()
        if userGuess not in "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z":
            continue

        if userGuess in alreadyGuessed:
            continue
        if myLine.count(userGuess) > 1:
            count = myLine.count(userGuess)
            # for i in range(count):
            #     newIndex = myLine.index(userGuess)

            #     Ran out of time, needed to find indices of all instances of the letter, then
            #       find the position i, then in the list, replace the "-" at position i with the user guess

            myList.insert(i, userGuess)
            print("You guessed correctly!")
            print("You have", myGuesses, "left!")
            print("Word now: ", myList)
        else:
            myGuesses -= 1
            print("You guessed incorrectly!")
            print("You have", myGuesses, "left!")
            print("Word now: ", myList)

        alreadyGuessed += userGuess
        numDashes = 0
        for i in range(len(myList)):
            if myList[i] == "-":
                numDashes += 1
                if numDashes == 0:
                    print("Congratulations, you won!")
                    sys.exit()
        numDashes = 0

    print("Sorry, you ran out of guesses!")

# Wrap in function, and call for new if user wants a new game, reading the next line.