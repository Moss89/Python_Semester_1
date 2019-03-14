def print_max():
    """
    :return:
    Calls max function
    """

    def max(a, b):
        """
        :param a:
        :param b:
        :return: a or b
        Prompt user for 2 floats, which will be bound to a and b
        Call function max, which takes a and b as arguments and return the larger value:
        if a > b return a, otherwise return b
        Print the largest number
        """
        if a > b:
            return a
        else:
            return b

    number1 = float(input("Please enter a number: "))
    number2 = float(input("Please enter a number: "))

    print("The largest number between", number1, "and", number2, "is", max(number1, number2))


print_max()
help(max)

