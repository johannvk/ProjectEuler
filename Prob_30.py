

def test_sum_digits_to_power(num, power):
    summed_digit_powers = 0
    string_number = str(num)
    for i in range(len(string_number)):
        summed_digit_powers += int(string_number[i])**power
    return summed_digit_powers == num and len(string_number) > 1


test_end = 1e6
power = 5
power_digits = []
for i in range(int(test_end)):
    if test_sum_digits_to_power(i, power): power_digits.append(i)

print("Numbers that can be written as the sum of the {}-th power of their digits: {}\nSum: {}".format(
    power, power_digits, sum(power_digits)
))

