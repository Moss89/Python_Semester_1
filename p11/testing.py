number = int(input("Enter a number: "))

if number < 0:
    print("OHHHH")
else:
    if number == 0:
        fact = 1
    elif number == 1:
        fact = 1
    else:
        i = 1
        fact = 1
        while i <= number:
            fact *= i
            i += 1
    print("Fact is", fact)
