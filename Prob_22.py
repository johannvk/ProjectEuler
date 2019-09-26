

def sort_list_alphabetically(i_list):
    new_list = []
    while len(i_list) > 0:
        min_string = i_list[0]
        for i in range(len(i_list)):
            if i_list[i] < min_string:
                min_string = i_list[i]
        leading_name = i_list.pop(i_list.index(min_string))
        new_list.append(leading_name)
    return new_list


def name_value(name):
    ret_value = 0
    for char in name:
        ret_value += alphabetic_value_dict[char]
    return ret_value


alphabetic_value_dict = {}
for i, code in enumerate(range(ord('A'), ord('Z') +1)):
    alphabetic_value_dict[chr(code)] = (i+1)

name_list = []
with open("p022_names.txt", "r") as f:
    read_string = f.read()
    read_string = read_string.replace('"', '')
    # print(read_string)
    name_list += (read_string.split(","))


alphabetic_sorted_list = sort_list_alphabetically(name_list)

tot_value = 0
for i, name in enumerate(alphabetic_sorted_list):
    tot_value += (i+1)*name_value(name)

print("Total Value of names:", tot_value)
