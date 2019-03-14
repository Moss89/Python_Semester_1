"""
For number in range (2, end):
set isPrime flag to true
for i in range (2, number):
if number % i is 0:
print number equals i * number//i for all pairs of factors
set isPrime flag to false.

if isPrime = true after the previous for loop, then print number is prime.

"""


for number in range(2, 20):
    isPrime = True
    for i in range(2, number):
        if number % i == 0:
            print(number, "equals", i, "*", number//i)
            isPrime = False

    if isPrime:
        print(number, "is a prime number")

print("Finished!")
