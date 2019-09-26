

def prime_test_list(number_list):
    return all(prime_test(elem) for elem in number_list)


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


def find_rotations(integer):
    rotations = [integer]
    string_integer = str(integer)
    for i in range(len(string_integer)-1):
        string_integer = string_integer[-1]+string_integer[:-1]
        rotations.append(int(string_integer))
    return rotations


# test_prime_array = [2, 3, 5]
#
# for i in range(19):
#     print("The number {} is {} prime".format(i, "a" if prime_test(i) else "not a"))
#
#
# print(prime_test(test_prime_array))
# print(prime_test_list(find_rotations(197)))

test_limit = int(1e6)
circular_primes = []
for i in range(test_limit):
    if prime_test_list(find_rotations(i)):
        circular_primes.append(i)

print("The circular primes under {} are: {}\nThere are a total of {} such primes"
      .format(test_limit, circular_primes, len(circular_primes)))

