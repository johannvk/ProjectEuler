# Digit factorials


def factorial(n):
    if n == 0: return 1
    return n*factorial(n-1)


def digitized_factorial_sum(num):
    if num == 1 or num == 2: return False
    return sum([factorial(int(digit)) for digit in str(num)]) == num


# Need bounds on the numbers to be checked if their sum of factorial of digits is equal
# to the original number.

for i in range(int(1e6)):
    if digitized_factorial_sum(i):
        print("The number {} is equal to the sum of the factorial of its digits.\n".format(i))

