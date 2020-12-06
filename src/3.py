# Starting at the top-left corner of your map and following a slope of right 3 and down 1,
#       how many trees would you encounter?
# https://adventofcode.com/2020/day/3

from src.aoc_core import *

c = Core(3)
c.tic()

slope = c.get_str_input()

# Tree character
tree = '#'

# Width and Height of given slope
slope_width = len(slope[0])
slope_height = len(slope)


# Function to get the number of trees hit, travelling in the given pattern (d_y down, d_x right)
def get_trees_hit(d_y, d_x):
    # Toboggan coordinates
    x, y = 0, 0

    # Number of trees hit
    tree_count = 0

    while y < slope_height:
        # Increase tree_count if toboggan hit a tree
        tree_count += int(slope[y][x] == tree)

        # Increase toboggan coordinates. X wraps around (equivalent to slope repeating)
        y += d_y
        x = (x + d_x) % slope_width

    return tree_count


print("1) Number of trees:", get_trees_hit(1, 3))
print("2) Result:",
      get_trees_hit(1, 1) * get_trees_hit(1, 3) * get_trees_hit(1, 5) * get_trees_hit(1, 7) * get_trees_hit(2, 1))
c.print_toc()
