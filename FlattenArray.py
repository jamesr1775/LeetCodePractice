
x1 = [3]
i = 0
sum_array = [[1, [2, [3]]], 4]
new_array_1 = sum_array
no_more_arrays = False
new_array_2 = []

while not no_more_arrays:
    new_array_2 = []
    for x in new_array_1:
        if type(x) is list:
            for y in x:
                new_array_2.append(y)
        else:
            new_array_2.append(x)

    new_array_1 = new_array_2

    for y in new_array_1:
        if type(y) is list:
            no_more_arrays = False
            break
        else:
            no_more_arrays = True
print new_array_1

#

# sum_array = [[1, [2, [3]]], 4]


def flatten(test_list):
    t = []
    for i in test_list:
        if isinstance(i, list):
            t.extend(flatten(i))
        else:
            t.append(i)
    else:
        return t


def flatten1(test_list):
    if isinstance(test_list, list):
        if len(test_list) == 0:
            return []
        first = test_list[0]
        rest = test_list[1:]
        a1 = flatten(first)
        a2 = flatten(rest)
        return a1 + a2
    else:
        return [test_list]



a = flatten(sum_array)
print a

# def fibonacci(n):
#     print "hi"
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     elif n > 2:
#         return fibonacci(n-1) + fibonacci(n-2)

