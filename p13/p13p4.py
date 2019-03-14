"""
Set x, y, z = 5, 10, 15
print x,y,z
z = f(x) calling function f(x)
print x,y,z
"""


def f(x):
    """
    :param: x
    :return: x
    Take argument x, increment x by 1, y = 1, print values of x, y, z, return x
    """
    print("In function f:")
    x += 1
    y = 1
    print("x is", x)
    print("y is", y)
    print("z is", z)
    return x


x, y, z = 5, 10, 15

print("Before function f:")
print("x is", x)
print("y is", y)
print("z is", z)

z = f(x)

print("After function f:")
print("x is", x)
print("y is", y)
print("z is", z)

