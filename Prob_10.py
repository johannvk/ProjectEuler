import numpy as np

sum_primes = 2


def check_prime(integer):
    for i in range(3, int(integer**(1/2))+1, 2):
        if integer % i == 0:
            return False
    else:
        return True


for i in range(3, 2*1000000, 2):
    if check_prime(i):
        sum_primes += i

print("Sum of primes under 2 million:", sum_primes)
