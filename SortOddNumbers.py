

num_array = [x for x in range(20, 0, -1)]


def sort_odd_numbers(array_of_nums):
    array_of_odd = []
    for num in array_of_nums:
        if num % 2 != 0:
            array_of_odd.append(num)
    return sorted(array_of_odd)


sorted_odd_array = sort_odd_numbers(num_array)
print sorted_odd_array
