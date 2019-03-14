'''
The program will take 3 ints from the user, and display the larger odd number of the three.
If none are odd, a message to that effect will be displayed.
Steps:

Take 3 ints from the user
Check if none are odd; if true, then print this fact

In case only one number is odd, assign any odd numbers to the largest odd number variable.

Then we check if both number 1 and 2 are odd. If true, see which number is bigger.
Assign this value as the largest odd value variable. Then we check if number 3 is odd too. If it is, compare it to the
largest odd value variable. If number 3 is larger, it's value is given to the largest odd number variable.

In case number 1 isn't odd, we compare numbers 2 and 3 like above, assigning the largest value to the
largest odd number variable.

In case number 2 isn't odd, we compare numbers 1 and 3 like above, assigning the largest value to the
largest odd number variable.

Print out the largest odd number variable. If no numbers are odd, this is printed.
'''

number1 = int(input("Input the first number: "))
number2 = int(input("Input the second number: "))
number3 = int(input("Input the third number: "))
largest_odd_no = 0


if number1 % 2 != 0 or number2 % 2 != 0 or number3 % 2 != 0:

    if number1 % 2 != 0:
        largest_odd_no = number1
    elif number2 % 2 != 0:
        largest_odd_no = number2
    elif number3 % 2 != 0:
        largest_odd_no = number3

    if number1 % 2 != 0 and number2 % 2 != 0:
        if number1 > number2:
            largest_odd_no = number1
        else:
            largest_odd_no = number2
        if number3 % 2 != 0:
            if number3 > largest_odd_no:
                largest_odd_no = number3

    elif number2 % 2 != 0 and number3 % 2 != 0:
        if number2 > number3:
            largest_odd_no = number2
        else:
            largest_odd_no = number3

    elif number1 % 2 != 0 and number3 % 2 != 0:
        if number1 > number3:
            largest_odd_no = number1
        else:
            largest_odd_no = number3

    print(largest_odd_no)

else:
    print("None of these numbers are odd!")
