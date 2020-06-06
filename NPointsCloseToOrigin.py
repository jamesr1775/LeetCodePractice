from math import sqrt

points2 = [[3, 3], [5, -1], [-2, 4], [-2, 1], [0, 0]]
gen_points2 = (point for point in points2)


def gen_of_points():
    points = [[3, 3], [5, -1], [-2, 4], [-2, 1], [0, 0]]
    for point in points:
        yield point


def square_num(num):
    return num*num


def distance_to_origin(x1, y1):
    return sqrt(square_num(x1) + square_num(y1))


def n_points_to_origin(num_of_points):
    point_with_dist_dict = {}
    gen_points = gen_of_points()

    gen_not_exhausted = True
    i=0
    while gen_not_exhausted:
        next_gen_point = get_next(gen_points)
        if next_gen_point:
            distance = distance_to_origin(next_gen_point[0], next_gen_point[1])
            point_with_dist_dict["p" + str(i)] = [next_gen_point, distance]
            i +=1
            print next_gen_point
        else:
            gen_not_exhausted = False
    j = 0
    for k, v in sorted(point_with_dist_dict.items(), key=lambda item: item[1][1]):
        if j >= num_of_points:
            break
        print "point: " + str(point_with_dist_dict[k][0]) + " distance: " + str(point_with_dist_dict[k][1])
        j += 1

def get_next(gen_object):
    return has_next(gen_object)


def has_next(gen):
    try:
        gen_value = gen.next()
        return gen_value
    except StopIteration:
        return None


n_points_to_origin(3)
