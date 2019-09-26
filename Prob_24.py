import numpy as np


def permutation_value(num_list, max_num):
    return sum([num_list[i]*max_num**(len(num_list)-1-i) for i in range(len(num_list))])


def permutation_update(in_list):
    pass


init_array = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
init_array.astype('int64')

#ULØST!
