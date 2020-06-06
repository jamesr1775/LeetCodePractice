

array_of_ints = [4, 2, 1, 2, 2, 3, 3, 6, 7, 6, 3, 4, 4]


def count_vals_array(numbers_array):
    integer_occurence = {}
    for i in range(0, len(numbers_array)):
        count_val = 1
        if numbers_array[i] not in integer_occurence:
            for j in range(i+1, len(numbers_array)):
                if numbers_array[i] == numbers_array[j] and i != j:
                    count_val += 1
            integer_occurence[numbers_array[i]] = count_val
    return integer_occurence


int_count_dict = count_vals_array(array_of_ints)

for int_val in int_count_dict:
    print "Int Value: %d" % int_val + "  Count: %d" % int_count_dict[int_val]