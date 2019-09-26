
# Pandigital multiplies
# Only need to check numbers whose length when concatenated is equal to 9.
# Set (1, 2, 3, ..., n), n > 1
# Len(Num):     n:
#   1           7, 8
#   2           3, 4
#   3           2, 3
#   4           2


def concatenated_tuple_product(integer, multiplier_tuple):
    return int(''.join(str(integer * multiplier) for multiplier in multiplier_tuple))


def check_pandigital(integer):
    if ''.join(sorted(str(integer))) == "123456789":
        return True
    return False


# print(check_pandigital(concatenated_tuple_product(192, (1, 2, 3))))

maximum_value_pandigital_num = 0
for i in range(1, 5):
    for n in range(2, 10-i):
        for integer in range(int(10**(i-1)), int(10**i)):
            temp_conc_prod = concatenated_tuple_product(integer, tuple(range(1, n)))
            if len(str(temp_conc_prod)) != 9: continue
            if temp_conc_prod > maximum_value_pandigital_num and check_pandigital(temp_conc_prod):
                maximum_value_pandigital_num = temp_conc_prod
                print("Found new maximum pandigital number: {}".format(temp_conc_prod))

print("The maximum pandigital multiple found was: {}".format(maximum_value_pandigital_num))

# test_num = 6328
# n = 2
# conc_num = concatenated_tuple_product(test_num, tuple(range(1, n+1)))
#
# print("The concatenated tuple product with {} and n = {} is: {}\nLen: {}"
#       .format(test_num, n, conc_num, len(str(conc_num))))
