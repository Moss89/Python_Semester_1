"""
For number in range (2, end):
for i in range (2, number):
if number % i is 0:
print number equals i * number//i
break
else:
print that the number is prime
"""

for number in range(2, 20):
    for i in range(2, number):
        if number % i == 0:
            print(number, "equals", i, "*", number//i)
            break

    else:
            print(number, "is a prime number")

print("Finished!")
