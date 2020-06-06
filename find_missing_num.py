
my_list = []

for i in range(0, 1000):
    my_list.append(i)

my_list.pop(400)


for i in range(0, len(my_list)):
    num_in_list = False
    count = 0
    for j in range(0, len(my_list)):
        if i == my_list[j]:
            count = count + 1
    if count == 0:
        print i
