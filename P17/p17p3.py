"""
Prompt the user to enter a string.
Convert the string to lowercase, and set catcount and dogcount to 0.
for i in range(0, len(string))-2, if [i] = c, [i]+1 = a, [i]+2 = t, increment catcount,
or if [i] = d [i+1] = o [i+2] = g, increment dog count.
Print out catcount and dogcount.
"""


stringy = input("Please enter a string: ")

stringylower = stringy.lower()
catcount = 0
dogcount = 0


for i in range(0, len(stringylower)-2):
    if stringylower[i] == "c":
        if stringylower[i+1] == "a":
            if stringy[i+2] == "t":
                    catcount += 1
    if stringylower[i] == "d":
        if stringylower[i+1] == "o":
            if stringy[i+2] == "g":
                dogcount += 1


print("The word dog is in the string", dogcount, "times, and the word cat is in the string", catcount, "times."
                                                                                                     " Is this an equal"
                                                                                                    " amount of times?"
                                                                                            ":", dogcount == catcount)
