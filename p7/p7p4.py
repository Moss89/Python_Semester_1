'''
    The program finds the sum of the first 5000 integers (0 - 4999)
    Steps:
    Set variable i to 0.
    Variable total will store the sum of the numbers. Set an initial value of 0.
    While the variable i is less than 5000, add the value of i to the value of total, and increment the
    value of i in each loop.
    After the loop has completed, print out the value of the variable total.
'''

i = 0
total = 0

while i < 5000:
    total = i + total
    i += 1

print("The sum of the first 5000 integers is:", total)
