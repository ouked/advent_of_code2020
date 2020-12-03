# Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?
# https://adventofcode.com/2020/day/3

from src.aoc_core import *

c = Core(3)
c.tic()

slope = c.get_str_input()

tree = '#'

slope_width = len(slope[0])
slope_height = len(slope)


def get_trees_hit(dY, dX):
    x = 0
    y = 0
    tree_count = 0
    while y < slope_height:
        if slope[y][x] == tree:
            tree_count += 1
        y += dY
        x = (x + dX) % slope_width
    return tree_count


print("1) Number of trees:", get_trees_hit(1, 3))
print("2) Result:", get_trees_hit(1, 1) * get_trees_hit(1, 3) * get_trees_hit(1, 5) * get_trees_hit(1, 7) * get_trees_hit(2, 1))
c.print_toc()
