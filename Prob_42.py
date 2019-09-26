import numpy as np

# Triangle numbers: t_n = (1/2)*n*(n+1)
# In the text file, how many of the words are "Triangle numbers" with their
# value being assigned by their position in the alphabet?

# First triangle nums: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55


# Only non-capital letters
def word_value(lower_case_string):
    return sum((ord(letter) - 65 + 1) for letter in lower_case_string)


def check_triangle_num_value(value):
    # print("Value: {}".format(value))
    test_n = (-1 + (8*value + 1)**(1/2)) / 2
    # print("Test n: {}".format(test_n))
    return int(test_n) == test_n


def tri_num(n):
    return (1/2)*n*(n+1)


def find_triangle_words():
    with open('p042_words.txt', 'r') as f:
        all_words = f.read()
        all_words = all_words.replace('"', '')
        word_list = all_words.split(',')

        # print("Word list: ", word_list)

    counter_tri_words = 0
    for word in word_list:
        word_val = word_value(word)
        # print("Word: {}, word value: {}".format(word, word_val))
        if check_triangle_num_value(word_val):
            counter_tri_words += 1

    return counter_tri_words


# print(word_value("'ABILITY'"))
num_tri_words = find_triangle_words()
print("The number of Triangle words are: {}".format(num_tri_words))
