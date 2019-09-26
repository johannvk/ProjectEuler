# Number Spiral diagonals


def indexed_odd_number(num):
    counter = 0
    while num != 1:
        num -= 2
        counter += 1
    return counter

spiral_dimension = 1001
sum_diagonals = 1
temp_num = 1

for i in range(indexed_odd_number(spiral_dimension)):
    for j in range(4):
        temp_num += 2*(i+1)
        sum_diagonals += temp_num
        print("Diagonal number: {}".format(temp_num))

print("Sum of diagonals: {}".format(sum_diagonals))


