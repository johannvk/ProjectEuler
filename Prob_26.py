from decimal import *
# Reciprocal cycles

getcontext().prec = 2000

def find_recurring_cycle(flp_num):
    try:
        assert(flp_num < 1), "The number was not smaller than one."
    except AssertionError as e:
        print(e)
        return None

    str_number = str(flp_num)[2:]
    str_number = str_number.lstrip('0')

    counter = 0
    print("str_number: {}".format(str_number))
    while counter <= len(str_number):
        recurring_digits = ''
        for j, dig in enumerate(str_number[counter:]):
            recurring_digits += dig
            # print("recurring_dig: {}, str_number[1+counter+j:1+counter+j+len(recurring_digits)]: {}"
            #       .format(recurring_digits, str_number[1+counter+j:1+counter+j+len(recurring_digits)]))
            if recurring_digits == str_number[1+counter+j:1+counter+j+len(recurring_digits)]:
                length_recurring_cycle = len(recurring_digits)
                print("The length of recurring cycle is: {}\n".format(length_recurring_cycle))
                return length_recurring_cycle
        counter += 1
    return 0


longest_recurring_denominator = 0
longest_recurring_cycle = 0

for denom in range(2, 1000):
    print("The number sent in is: 1/{}:".format(denom))
    temp_length = find_recurring_cycle(Decimal(1)/Decimal(denom))
    if temp_length > longest_recurring_cycle:
        longest_recurring_denominator = denom
        longest_recurring_cycle = temp_length


print("The longest length of recurring cycle occurs with the denominator {}, and the length is: {}"
      .format(longest_recurring_denominator, longest_recurring_cycle))

# Wrong solution! Need unending accuracy to get the right answer with this method.
# Even with super high accuracy, no correct answer...
# Needed to remove leading zeros to get the algorithm to work


