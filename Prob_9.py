

def test_pythagorean_triplet(a, b, c):
    return a**2 + b**2 - c**2 == 0


for a in range(1, 1000):
    for b in range(1, 1000):
        if test_pythagorean_triplet(a, b, 1000-(a+b)):
            print("Product of a*b*c:", a*b*(1000-a-b))
