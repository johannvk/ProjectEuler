

def sum_digits(num):
    tot_sum = 0
    while num > 0:
        tot_sum += int(num % 10)
        num //= 10
    return tot_sum

def fact(num):
    if num == 0: return 1
    else:
        return num*fact(num-1)

print(sum_digits(fact(100)))