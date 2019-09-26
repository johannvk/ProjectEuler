

# Champernowne's constant
# Problem 40
# An irrational decimal fraction is created by concatenating the positive integers:
#
# 0.123456789101112131415161718192021...
#
# It can be seen that the 12th digit of the fractional part is 1.
#
# If dn represents the nth digit of the fractional part, find the value of the following expression.
#
# d1 × d10 × d100 × d1000 × d10000 × d100000 ×

digit_product = 1
digit = 0
frac_dig_counter = 0
upper_digit_limit = 1e6
power = 0

while frac_dig_counter < int(upper_digit_limit):
    digit += 1
    for i in range(len(str(digit))):
        frac_dig_counter += 1
        if frac_dig_counter == 10**power:
            digit_product *= int(str(digit)[i])
            power += 1

print("The product og the 10th-power digits up to {} is: {}".format(upper_digit_limit, digit_product))
