import math

# Digit cancelling fractions


class RationalNumber(object):
    def __init__(self, numerator, denominator):
        self.numerator = int(numerator)
        self.denominator = int(denominator)
        self.str_numerator = str(int(numerator))
        self.str_denominator = str(int(denominator))

    def __call__(self, *args, **kwargs):
        try:
            return self.numerator/self.denominator
        except ZeroDivisionError:
            return False

    def bad_division(self):
        for digit in self.str_numerator:
            if digit in self.str_denominator and digit != '0':
                if self.str_numerator[0] == self.str_numerator[1]:
                    temp_numerator = int(self.str_numerator[0])
                else:
                    temp_numerator = int(str(self.numerator).replace(digit, ''))

                if self.str_denominator[0] == self.str_denominator[1]:
                    temp_denominator = int(self.str_denominator[0])
                else:
                    temp_denominator = int(str(self.denominator).replace(digit, ''))
                try:
                    return temp_numerator/temp_denominator
                except ZeroDivisionError:
                    return False
        else:
            return False

    def __str__(self):
        return "{}/{}".format(self.numerator, self.denominator)

    def simplify(self):
        greatest_common_den = math.gcd(self.numerator, self.denominator)
        while greatest_common_den > 1:
            print("GCD: {}".format(greatest_common_den))
            self.numerator = int(self.numerator / greatest_common_den)
            self.denominator = int(self.denominator / greatest_common_den)
            greatest_common_den = math.gcd(self.numerator, self.denominator)


# ratNum = RationalNumber(10, 20)
# print("The value of ratNum = {}\n"
#       "And the value of ratNum with bad_division is {}".format(ratNum(), ratNum.bad_division()))
correct_bad_divisions = []
for denom in range(11, 100):
    for enum in range(10, denom):
        temp_ratnum = RationalNumber(enum, denom)
        # print("The number is {}/{}".format(temp_ratnum.numerator, temp_ratnum.denominator))
        if temp_ratnum() == temp_ratnum.bad_division():
            correct_bad_divisions.append((temp_ratnum.numerator, temp_ratnum.denominator))

print(correct_bad_divisions)

product_num = 1
product_den = 1

for e, d in correct_bad_divisions:
    product_num *= e
    product_den *= d

final_num = RationalNumber(product_num, product_den)
print(final_num)
final_num.simplify()
print(final_num)
