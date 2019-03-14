

table_size = int(input("Enter a table size: "))

i = 0

while i <= table_size:
    j = 0
    while j <= i:
        print(i*j, " ", end='')
        j += 1
    print()
    i += 1
