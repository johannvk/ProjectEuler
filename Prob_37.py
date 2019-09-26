
# Truncatable primes


def prime_test_list(numbers):
    return all(prime_test(elem) for elem in numbers)


def prime_test(num):
    try:
        if num == 2:
            return True
        if num == 0 or num == 1 or num % 2 == 0:
            return False
        for i in range(3, int(num**(1/2))+1, 2):
            if num % i == 0:
                return False
        else:
            return True

    except TypeError:
        return all(prime_test(elem) for elem in num)


def make_truncated_list(integer):
    len_str_int = len(str(integer))
    return [int(integer/(10**i)) for i in range(len_str_int)] + [integer % (10**i) for i in range(1, len_str_int)]


counter = 11
truncatable_prime_numbers = []
while len(truncatable_prime_numbers) < 11:
    if prime_test_list(make_truncated_list(counter)):
        print("The number {} is prime_truncatable both ways.".format(counter))
        truncatable_prime_numbers.append(counter)
    counter += 2

print(truncatable_prime_numbers)
