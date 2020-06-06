
def reverse_list(input_string, start, end):
    if start >= end:
        return
    temp = input_string[start]
    input_string[start] = input_string[end]
    input_string[end] = temp
    reverse_list(input_string, start + 1, end - 1)


mylist = [1, 2, 3, 4, 5, 6, 7]
reverse_list(mylist, 0, len(mylist)-1)
print mylist


def reverse_string(input_string):
    if len(input_string) == 0:
        return input_string
    else:
        return reverse_string(input_string[1:]) + input_string[0]


mystring = "edcba"
mystring2 = reverse_string(mystring)
print mystring2