import math
def wall_paint(height, width, coverage):
    area_of_wall = height * width
    num_0f_can = area_of_wall / coverage
    print(math.ceil(num_0f_can))


wall_paint(2, 5, 4)