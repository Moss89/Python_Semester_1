def fib(n):
    f_0 = 0
    f_1 = 1

    if n<=0:
        print("error")
    elif n == 1:
        print("series is", f_0)
    elif n ==2:
        print("series is", f_0,",", f_1)

    else:
        print("series is", f_0,",", f_1, sep="", end="")
        a = f_0
        b = f_1
        i = 2
        while i<n:
            fibon = b+a
            print(",", fibon, end="")
            a = b
            b = fibon
            i += 1



n = int(input("enter a number"))
fib(n)