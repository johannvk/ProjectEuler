import operator

# Integer Right Triangles

# Implementing stupid brute force trials:


def brute_force_triangle_check(max_perim):
    for p in range(3, max_perim + 1):
        for a in range(1, p - 2):
            b = 0.5*(p - a)
            c = 0.5*(p - a)
            




def is_perfect_square(num):
    return (int(num**(1/2)))**2 == num


# perimeter_length_solutions = {}
#
#
# def len_hyp(a, b):
#     return (a**2 + b**2)**(1/2)
#
#
# def check_right_triangle(kat1, kat2, hyp):
#     return kat1**2 + kat2**2 - hyp**2 == 0
#
#
# base_pairs = []
# triangle_perimeter = 125
#
# # Real part of the imaginary number
# a = 2
#
#
# while a**2 + a < triangle_perimeter - 2:
#     # Complex part of the imaginary number
#     b = 1
#     while b < a:
#         if (a, b) not in base_pairs and (b, a) not in base_pairs:
#             base_pairs.append((a, b))
#             base_pairs.append((b, a))
#             perim = (a**2 - b**2) + 2*a*b + (len_hyp(a, b))
#             if perim in perimeter_length_solutions.keys():
#                 perimeter_length_solutions[perim] += 1
#             else:
#                 perimeter_length_solutions[perim] = 1
#
#         b += 1
#
#         # Ønsker å implementere skalering av triplettene som dannes ved multiplisere (a + ib) med seg selv.
#
#     a += 1
#
#
# max_key = max(perimeter_length_solutions.keys(), key=lambda k: perimeter_length_solutions[k])
#
# print("The perimeter value with the most amount of solutions was: {}\nWith {} solutions"
#       .format(max_key, perimeter_length_solutions[max_key]))

