# Amicable numbers
# Problem 21
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

import time

def d(n):
    divisors = [1]
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            divisors += [i, n // i]
    return sum(divisors)


def amicable_test(a, b):
    if a == b:
        return False
    return (d(a) == b) and (d(b) == a)

t_0 = time.clock()

list_amicable = []
for i in range(10000):
    if i not in list_amicable and amicable_test(i, d(i)):|
        list_amicable += [i]

print("list_amicable:", list_amicable)
print("Sum list:", sum(list_amicable))

dt = time.clock() - t_0
print("Time elapsed:", dt)
