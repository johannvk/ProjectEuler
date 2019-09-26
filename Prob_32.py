# Pandigital products


def check_pandigital_product(x, y):
    if ''.join(sorted(str(x*y)+str(x)+str(y))) == '123456789':
        return True
    return False


pandig_products = []
for x in range(int(10), int(1e4)):
    for y in range(int(10), int(1e4)):
        if len(str(x)+str(y)+str(x*y)) != 9:
            continue
        if check_pandigital_product(x, y) and x*y not in pandig_products:
            pandig_products.append(x*y)

print(pandig_products)
print("Sum of pandigital products: {}".format(sum(pandig_products)))
