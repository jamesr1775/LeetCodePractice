

screen = [
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 2, 1, 1, 1, 0, 0],
            [1, 0, 0, 1, 1, 0, 1, 1],
            [1, 2, 2, 2, 2, 0, 1, 0],
            [1, 1, 1, 2, 2, 0, 1, 0],
            [1, 1, 1, 2, 2, 2, 2, 0],
            [1, 1, 1, 1, 1, 2, 1, 1],
            [1, 1, 1, 1, 1, 2, 2, 1]
         ]


def flood_fill_algo(two_dim_screen, new_colour, prev_colour, x_coord, y_coord):
    if x_coord in range(0, len(two_dim_screen)):
        if y_coord in range(0, len(two_dim_screen[x_coord])):
            if not prev_colour:
                prev_colour = two_dim_screen[x_coord][y_coord]
            if two_dim_screen[x_coord][y_coord] == prev_colour:
                two_dim_screen[x_coord][y_coord] = new_colour
                flood_fill_algo(two_dim_screen, new_colour, prev_colour, x_coord+1, y_coord)
                flood_fill_algo(two_dim_screen, new_colour, prev_colour, x_coord-1, y_coord)
                flood_fill_algo(two_dim_screen, new_colour, prev_colour, x_coord, y_coord+1)
                flood_fill_algo(two_dim_screen, new_colour, prev_colour, x_coord, y_coord-1)
    return


flood_fill_algo(screen, new_colour=3, prev_colour=None, x_coord=4, y_coord=4)

for row in screen:
    print row
