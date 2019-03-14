"""
This program shows the total number of combinations possible using input from the user.
Steps:
Prompt the user to enter the number of possibilities, and the actual number being used.
If they are both positive (the manager wouldn't be interesting in learning how many possibilities there are if they
don't have any possibilities or offer nothing), then add 1 to number of possibilities, and subtract the number offered.
While the number (stored in variable i) calculated above is less than the number possible,
multiply i by total_possible, which has an initial value of 1. Increment the i variable.

Set j = 1, while j is less than the amount offered, multiply total_offered (initialized as 1) by j then increment j.

Total combinations = total_possible divided by total offered. Print total combinations.
"""

number_possible = int(input("Please enter the number of toppings that are possible to have: "))
number_offered = int(input("Please enter the number of toppings offered on a standard pizza: "))

if number_possible > 0 and number_offered > 0:

    i = (number_possible+1)-number_offered
    total_possible = 1

    while i <= number_possible:
        total_possible *= i
        i += 1

    j = 1
    total_offered = 1
    while j <= number_offered:
        total_offered *= j
        j += 1

    total_combinations = total_possible//total_offered

    print("With", number_possible, "possible toppings, and", number_offered, "toppings offered per standard pizza, "
                                                                             "there are", total_combinations,
          "possible combinations")
