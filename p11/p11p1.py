"""
Prompt the user for an int. If the int is less than 0, print this out and exit.
Otherwise, set fact = 1 and i =1.
While i <= number, fact = fact * i. Increment i by 1.
After the loop, print the value of fact.
"""

number = int(input("Please enter a number which you want the factorial of: "))

if number < 0:
    print("The number must not be less than zero!")

else:
    fact = 1
    i = 1
    while i <= number:
        fact *= i
        i += 1
    print("The factorial of", number, "=", fact)
