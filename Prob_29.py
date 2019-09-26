

number_list = []

start_num = 2
end_num = 100
for a in range(start_num, end_num+1):
    for b in range(start_num, end_num+1):
        temp = a**b
        if temp not in number_list:
            number_list.append(temp)

print("Sequence of distinct power-terms (a={}, b={}): {}".format(start_num, end_num, number_list))
print("Length of sequence = {}".format(len(number_list)))
