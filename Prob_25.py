import time


def fib(n):
    if n == 1: return 1
    if n == 2: return 1
    return fib(n-1) + fib(n-2)


def fib2():
    a = 1
    b = 0
    n = 1
    while len(str(a)) < 1000:
        a, b = a+b, a
        n = n + 1
    return a, n

t_0 = time.clock()

a_1,  n_1 = fib2()
print("The first fibonacci number with a thousand digits is\n the {0}th: ({1})".format(n_1, a_1))

dt = time.clock() - t_0
print("Time elapsed:", dt)