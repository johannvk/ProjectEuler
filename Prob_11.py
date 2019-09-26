import numpy as np


#with open('Data_prob_11.txt', 'r') as f:

data_grid = np.loadtxt('Data_prob_11.txt', dtype='int64', ndmin=2)


def find_sum_ndarray_rowwise(ndarray, row, col):
    ret_value = 1
    for i in range(4): ret_value*=ndarray[row, col+i]
    return ret_value


def find_sum_ndarray_colwise(ndarray, row, col):
    ret_value = 1
    for i in range(4): ret_value *= ndarray[row + i, col]
    return ret_value


def sum_ndarray_right_diagonal(data, row, col):
    ret_value = 1
    for i in range(4):
        ret_value *= data[row - i, col + i]
    return ret_value


def sum_ndarray_left_diagonal(data, row, col):
    ret_value = 1
    for i in range(4):
        # print(data[row + i, col + i])
        ret_value *= data[row + i, col + i]
    return ret_value


def find_largest_set_4():
    max_value = 0
    pos_row = (0, 0)
    pos_col = (0, 0)
    pos_ldiag = (0, 0)
    pos_rdiag = (0, 0)

    max_row_value = 0
    max_col_value = 0
    max_rdiag_value = 0
    max_ldiag_value = 0

    # horizontal and vertical directions
    for i in range(0, 20):
        for j in range(0, 17):
            temp_value1 = find_sum_ndarray_rowwise(data_grid, i, j)
            if temp_value1 > max_row_value:
                max_row_value = temp_value1
                pos_row = (i, j)

            temp_value2 = find_sum_ndarray_colwise(data_grid, j, i)
            if temp_value2 > max_col_value:
                pos_col = (i, j)
                max_col_value = temp_value1

    # right-diagonal
    for i in range(3, 20):
        for j in range(0, 17):

            temp_value1 = sum_ndarray_right_diagonal(data_grid, i, j)

            if temp_value1 > max_rdiag_value:
                max_rdiag_value = temp_value1
                pos_rdiag = (i, j)

    # left-diagonal
    for i in range(0, 17):
        for j in range(0, 17):
            temp_value2 = sum_ndarray_left_diagonal(data_grid, i, j)
            if temp_value2 > max_ldiag_value:
                max_ldiag_value = temp_value2
                pos_ldiag = (i, (j+20))

    max_value = max(max_row_value, max_col_value, max_rdiag_value, max_ldiag_value)

    return max_value, [pos_row, pos_col, pos_rdiag, pos_ldiag], [max_row_value, max_col_value, max_rdiag_value, max_ldiag_value]


largest_sum, list_pos, list_max_values = find_largest_set_4()
print("Largest sum:", largest_sum)
print("List of pos: ", list_pos)
print("List of values: ", list_max_values)
