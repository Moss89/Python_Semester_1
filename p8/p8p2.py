"""
This program prints out multiplication tables of a size determined by the user.
Steps:
Prompt the user for a number which will be the table size.
Set variables i and j to 1, and while the user inputted number is larger than or equal to i,
print out i*j while j is less than or equal the user inputted number. Increment j after every print.
print a new line when the j while loop has finished, and increment i.
"""


table_size = int(input("Please enter the table size: "))

i = 1

while i <= table_size:
    j = 1
    while j <= table_size:
        print(i*j, sep=" ", end="   ")
        j += 1
    print()
    i += 1
