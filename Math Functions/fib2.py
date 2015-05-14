# Returns fibonacci sequence number using a for loop
def fib2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        f0 = 0
        f1 = 1
        f2 = 0
        for i in range (0, n - 1):
            f2 = f1 + f0
            f0 = f1
            f1 = f2
        return f2

