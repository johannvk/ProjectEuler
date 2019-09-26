# Problem 17
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
# letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115
# (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in
# compliance with British usage.

one_to_twenty_dict = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
                       9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
                       15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
tens_dict = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
hundred = "hundred"
thousand = "thousand"


def integer_to_string(num):
    if num == 1000: return "onethousand"

    if num < 100:
        return integer_under_hundred_to_string(num)

    ret_string = ""
    ret_string += (integer_under_hundred_to_string(num//100) + "hundred")
    if num % 100 != 0: ret_string += "and" + integer_under_hundred_to_string(num % 100)
    return ret_string



def integer_under_hundred_to_string(num):
    ret_string = ""
    if num < 20:
        ret_string = one_to_twenty_dict[num]
        return ret_string
    ret_string = tens_dict[(num//10)]
    if num % 10 != 0: ret_string += one_to_twenty_dict[(num % 10)]
    return ret_string


number_string = ""

for i in range(1, 1001):
    number_string += integer_to_string(i)

print(len(number_string))

