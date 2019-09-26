
def number_to_base(integer, base=2):
    try:
        assert (0 < base < 10), "The new base for {} was not between 1 and 9".format(integer)
    except AssertionError as e:
        print(e)
        return None

    if integer == 1: return "1"  # Fringe case for integer == 1

    power = 0
    while integer > base**power:
        power += 1

    new_base_number = ""

    while power >= 1:
        power -= 1
        if integer >= base**power:
            new_base_number += "{}".format(integer // base**power)
            integer -= int(new_base_number[-1])*base**power
            # print("The power of {} is: {}, the reduced integer is: {}".format(base, power, integer))
        else:
            new_base_number += "0"
    return new_base_number


def check_palindrome(integer):
    if str(integer) != str(integer)[::-1]:
        return False
    return True


# print(number_to_base(1200, 8))
# print(check_palindrome(585))

palindrome_10_2_numbers = []
roof = int(1e6 + 10)
base = 2

for i in range(1, roof, 2):
    if check_palindrome(i) and check_palindrome(number_to_base(i)):
        palindrome_10_2_numbers.append((i, number_to_base(i)))

print("All the numbers that are palindrome under {} in base-10 and base-2 are: {}\n"
      "The sum of all the numbers is: {}"
      .format(roof, palindrome_10_2_numbers, sum(p[0] for p in palindrome_10_2_numbers)))
