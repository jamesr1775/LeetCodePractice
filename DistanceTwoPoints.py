from math import sqrt

x1, y1 = (3, 4)
x2, y2 = (4, 3)


def distance_two_coords(x1, y1, x2, y2):
    return sqrt(square_num(x2 - x1) + square_num(y2-y1))


def square_num(num):
    return num*num


print "Distance %.4f" % distance_two_coords(x1, y1, x2, y2)
