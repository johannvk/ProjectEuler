# Problem 16
# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 21000?

power = 100


def sum_digits(num):
    tot_sum = 0
    tot_sum_wrong = 0
    num_wrong = num
    while num > 0:
        tot_sum += int(num % 10)
        num //= 10
        print("num =", num)
        print("tot_sum =", tot_sum, "\n")

        tot_sum_wrong += int(num_wrong % 10)
        num_wrong /= 10
        print("num_wrong =", num_wrong)
        print("tot_sum_wrong =", tot_sum_wrong, "\n")
    return tot_sum, tot_sum_wrong


ans, ans_wrong = sum_digits(2**power)

print("Sum of digits 2^", power, ":", ans, "\nSum of digits_wrong:", ans_wrong)


