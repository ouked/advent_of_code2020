# For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?
# https://adventofcode.com/2020/day/6

from src.aoc_core import *

c = Core(6)
c.tic()

# Append "" so last block is processed
data = c.get_str_input()
data.append("")

# Part 1
part1 = 0
positive_answers = []

# Part 2
part2 = 0
mutual_positive_answers = []

# Flag to know when to refill mutual_positive_answers
# Fixes bug where the array would be pre-maturely filled
is_new_group = 1

for line in data:

    # Reset arrays
    if is_new_group:
        mutual_positive_answers = [char for char in line]
        positive_answers = []
        is_new_group = 0

    # End of block
    if line == "":
        part1 += len(positive_answers)
        part2 += len(mutual_positive_answers)
        is_new_group = 1
        continue

    positive_answers += [char for char in line if char not in positive_answers]

    mutual_positive_answers = [char for char in mutual_positive_answers if char in line]


print("1)", part1)
print("2)", part2)

c.print_toc()

# 1) 6259
# 2) 3178
