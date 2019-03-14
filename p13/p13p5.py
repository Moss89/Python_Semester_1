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
    a = 5
    print("a is", a)
    print("x is", x)
    print("y is", y)
    print("z is", z)
    return x


a, x, y, z = 1, 5, 10, 15

print("Before function f:")
print("a is", a)
print("x is", x)
print("y is", y)
print("z is", z)

z = f(x)
a = f(z)

print("After function f:")
print("a is", a)
print("x is", x)
print("y is", y)
print("z is", z)

