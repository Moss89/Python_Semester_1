"""
Define the fibonacci recursive function fib.
Prompt the user for a non negative int.
While the number is greater than or equal to 0,
for i in range number, print fib(i).
Prompt user for another non negative int.
Exit on negative int.
"""

def fib(n):
    """
    :param n:
    :return:
    if n <= 1 return n,
    else return fib(n-2) + fib(n-1)
    """
    if n <= 1:
        print("n now at:", n)
        return n
    else:
        print("n now at:", n)
        return fib(n-1) + fib(n-2)


number = int(input("Please enter how many terms of the Fibonacci sequence you wish to see (negative number to stop): "))

while number >= 0:
    print("Fibonacci sequence:")
    for i in range(number):
        print("Fibonacci series term", i+1, "=", fib(i))
    number = int(input("Please enter how many terms of the Fibonacci sequence you wish to see(negative number to stop)"
                       ": "))

