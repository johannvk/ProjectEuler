
def generate_triangle_numbers(n):
    return n*(n+1)//2


def find_num_divisors(x): # Gir feil antall divisorer
    divisors = 1
    if x % 2 == 0:
        divisors += 1
        x = x / 2
    while x % 2 == 0:
        x = x / 2

    p = 3
    while x != 1:
        if x % p == 0:
            print(p)
            divisors += 1
            x = x / p
            while x % p == 0: x = x / p
        p += 2

    return divisors


divisors_wanted = 500
n = 1

# while find_num_divisors(generate_triangle_numbers(n)) <= divisors_wanted:
#     n += 1
#     if n % 50 == 0: print("n: =", n)
#
# print(generate_triangle_numbers(n))

print(generate_triangle_numbers(15000))
print("Number of divisors: n = 288450, num_divisors =", find_num_divisors(generate_triangle_numbers(15000)))
