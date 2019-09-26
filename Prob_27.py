import time

# Quadratic Primes


def customizable_prime_quadratic(n, a, b):
    return n**2 + a * n + b


def check_prime(num):
    if num == 1: return False
    if num == 2: return True
    if num % 2 == 0: return False
    for i in range(3, int(abs(num)**(1/2)+1), 2):
        if num % i == 0: return False
    else: return True


def check_prime_tree(a, b):
    primes = 0
    n = 0
    while check_prime(customizable_prime_quadratic(n, a, b)):
        n += 1
        primes += 1
    return primes


def prime_generating_quadratic_function_checker():
    max_primes = 0
    a_max = 0
    b_max = 0
    for a in range(-999, 999):
        for b in range(-1000, 1000):
            num_primes = check_prime_tree(a, b)
            if num_primes > max_primes:
                max_primes = num_primes
                a_max = a
                b_max = b
    return max_primes, a_max, b_max


max_primes, a_max, b_max = prime_generating_quadratic_function_checker()
print("The coefficients which produce the largest amount of primes are a = {1}, b = {2}. Generating {0} primes.\n".format(max_primes, a_max, b_max))


#print("Num of primes for a = 1, b = 41: {}".format(check_prime_tree(2, 41)))

# Checking Time_efficiency of the prime_checking function
# times = []
# for i in range(10):
#     t = time.clock()
#     for i in range(int(1e7)):
#         testnum = i
#         #print("Checking primeness of {}, {}".format(testnum, check_prime(testnum)))
#     dt = time.clock()-t
#     times.append(dt)
#
# print("The process averaged over 10 times took {} seconds".format(round(sum(times)/len(times), 8)))
