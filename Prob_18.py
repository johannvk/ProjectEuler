
# Maximum path sum 1
# Brute force method, not smart enough for problem 67, with the exact same problem with 100 rows,
#  versus 15 now

filename = "data_prob_18.txt"

with open(filename, "r") as f:
    lines = f.readlines()
    data_list = [line.split() for line in lines]
    data_list = [[int(num) for num in data_list[i]] for i in range(len(data_list))]


routes = [[data_list[0][0], 0]]
triangle_rows = len(data_list) - 1
# print(data_list)

for row in range(triangle_rows):
    len_routes = len(routes)
    for k in range(len_routes):
        route = routes[k]
        val = route[0]
        route[0] += data_list[row + 1][route[1]]
        routes.append([val+data_list[row+1][routes[k][1] + 1], routes[k][1]+1])

max_path_value = 0

for path in routes:
    if path[0] > max_path_value:
        max_path_value = path[0]

print("The maximum path value through the triangle is: {}".format(max_path_value))