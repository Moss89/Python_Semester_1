# Using slices to extract one or more values from a string

animals = 'herd of elephants'
seg = animals[:]
print('Segment is: ', seg)


#x and y are the same:

animals = 'herd of elephants'
seg = animals[3:3]
print('Segment is: ', seg)
#Result is blank: from the 3rd index position, print from 3, up to 3 but not including 3


# x is greater than y
animals = 'herd of elephants'
seg = animals[3:2]
print('Segment is: ', seg)
#Result is blank: from the 3rd index position, print from 3, up to 2 but not including 2. So there's nothing
#to print. Y needs to be greater than x.

# y is greater than x
animals = 'herd of elephants'
seg = animals[3:6]
print('Segment is: ', seg)
#Result is 'd o'. from the 3rd index position, print from 3 up to, but not including position 6. So we get
#the values at index position 3, 4, 5.

# x is omitted
animals = 'herd of elephants'
seg = animals[:2]
print('Segment is: ', seg)
#Result is 'he'. When x is omitted, the slice starts from the beginning, as in index 0. So here we have print
#from index 0 to 2, not including 2.

# y is omitted
animals = 'herd of elephants'
seg = animals[8:]
print('Segment is: ', seg)
#Result is 'elephants'. When y is omitted, the slice ends at the end of the string, as in the last index
#position. So here we have print from index position 8 to the end of the string.

