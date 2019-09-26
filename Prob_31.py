

desired_value = 200  # 2£ in pennies
currency_dict = {"1p": 1, "2p": 2, "5p": 5, "10p": 10, "20p": 20, "50p": 50,  "1£": 100, "2£": 200}
currency_list = ["1p", "2p", "5p", "10p", "20p", "50p", "1£", "2£"]
coin_combinations = []


def value_coins(coins_list):
    return sum([currency_dict[coin]*coefficient for coin, coefficient in coins_list])


def compare_coin_combination(coins_list1, coins_list2):
    if len(coins_list1) != len(coins_list2): return False
    for i in range(len(coins_list1)):
        if coins_list1[i] in coins_list2:
            continue
        else:
            return False
    else:
        return True


def generate_coin_combination(currency_value, coin_index):
    temp_coins_list = [["1p", 0], ["2p", 0], ["5p", 0], ["10p", 0], ["20p", 0], ["50p", 0], ["1£", 0], ["2£", 0]]
    while value_coins(temp_coins_list) < 200:
        temp_coins_list[coin_index][1] = temp_coins_list[0][1] + 1
    coin_combinations.append(temp_coins_list)


# test_list = [["1p", 15], ["10p", 1], ["2£", 4], ["20p", 1]]
# test_list2 = [["1p", 15], ["2£", 4], ["10p", 1], ["20p", 1]]
# print("Value of test_list: {}".format(value_coins(test_list)))
# print("Comparison test: {}".format(compare_coin_combination(test_list, test_list2)))

# generate_coin_combination(desired_value)
# print("Coin bombinations: {}".format(coin_combinations))

combinations = 0

for a in range(desired_value, -1, -200):
    for b in range(a, -1, -100):
        for c in range(b, -1, -50):
            for d in range(c, -1, -20):
                for e in range(d, -1, -10):
                    for f in range(e, -1, -5):
                        for g in range(f, -1, -2):
                            print("a: {}, b: {}, c: {}, d: {}, e: {}, f: {}, g: {}\n".format(a,b,c,d,e,f,g))
                            combinations += 1

print("Number of combinations is: {}".format(combinations))
