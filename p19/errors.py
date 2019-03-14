finished = False
total = 0
number = 0
count = 0
while not finished:
    total = total + number
    if total == 0 or number == 0:
        print("Current average is 0")
    else:
        print("Current average is ", total // count)
    if total < 40:
        number = number + 3
        print(number)
        count = count + 1
    else:
        finished = True
print("The total was", total)
print("There were", count, "numbers.")