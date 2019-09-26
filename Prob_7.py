

def check_prime(integer):
    if integer == 1: return False
    if integer == 2: return True

    if integer % 2 == 0: return False

    for i in range(3, int(integer**(1/2))+1, 2):
        if integer % i == 0:
            return False
    else:
        return True


num_primes = 0
n = 0

while num_primes < 10001:
    n += 1
    # print("n:", n)
    if check_prime(n):
        num_primes += 1
        # print("num_primes:", num_primes)

print("Prime number", num_primes, "is: \n", n)
