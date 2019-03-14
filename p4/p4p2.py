# Taking user input,then using mathematical expressions within print statements

# import math module for pi

import math

length = float(input("Please input a length: "))
# Square = length^2
print('Area of square with a side length of', length, ' = ', length**2)
# Cube = length^3
print('Area of cube with a side length of', length, ' = ', length**3)
# circle = 2r^2*pi
print('Area of a circle with a radius of', length, ' = ', (length**2)*math.pi)
# Sphere = 4r^2*pi
print('Area of a sphere with radius of', length, ' = ', 4*(length**2)*math.pi)
# Cylinder = 2*pi*r*length + 2*pi*radius^2
print('Area of a cylinder with a radius of', length, 'and side of', length, ' = ',
      ((2*math.pi*length*length) + (2*math.pi*(length**2))))



