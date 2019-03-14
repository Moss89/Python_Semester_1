'''
    The program sums the integers in the range 1–10,000 that are divisible by 3 or by 5 and
    prints out the total.
    Steps:
    Set variable i to 0.
    Set variable total to store the sum of the numbers, with an initial value of zero.
    While the variable i is less than 10,001, check if i modulus 3 equals 0 or if i modulus 5 equals 0.
    If the above is true, add the value of i to the value of total. Otherwise do nothing.
    Increment the value of i in each loop.
    After the loop has completed, print out the value of the variable total.
'''

i = 1
total = 0

while i < 10001:
    if i % 3 == 0 or i % 5 == 0:
        total += i
    i += 1

print("The sum of the integers between 1 and 10,000 that are divisible by 3 or 5 is:", total)

