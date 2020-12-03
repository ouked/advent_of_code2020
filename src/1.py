# Find the two entries that sum to 2020; what do you get if you multiply them together?
# https://adventofcode.com/2020/day/1


from src.aoc_core import *

c = Core(1)

c.tic()
entries = c.get_int_input()


# Part 1
def find_two_entries():
    for i in entries:
        for j in entries:
            if i + j == 2020:
                return [i, j]
    return [0, 0]


# Part 2
def find_three_entries():
    for i in entries:
        for j in entries:
            for k in entries:
                if i + j + k == 2020:
                    return [i, j, k]
    return [0, 0, 0]


x = find_two_entries()
print("Part 1: " + str(x[0] * x[1]))

y = find_three_entries()
print("Part 2: " + str(y[0] * y[1] * y[2]))

c.print_toc()
