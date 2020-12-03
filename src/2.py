# How many passwords are valid according to their policies?
# https://adventofcode.com/2020/day/2

from src.aoc_core import *

c = Core(2)
c.tic()
accepted_passwords = 0

# region Part 1
for line in c.get_str_input():

    split_line = line.split(' ')

    occ = split_line[0].split('-')
    # Minimum allowed occurrences of the given letter
    min_occ = int(occ[0])
    # Maximum allowed occurrences of the given letter
    max_occ = int(occ[1])

    # Letter in question
    letter = split_line[1][0]

    password = split_line[2]
    count = 0

    for char in password:
        if char == letter:
            count += 1

    if count in range(min_occ, max_occ+1):
        accepted_passwords += 1
print("Number of valid passwords for Part 1:", accepted_passwords)

# endregion

# region Part 2
accepted_passwords = 0
for line in c.get_str_input():

    split_line = line.split(' ')

    occ = split_line[0].split('-')

    # Toboggan Corporate Policies have no concept of "index zero"

    # Position of given character
    pos1 = int(occ[0])-1
    # Second position of given character
    pos2 = int(occ[1])-1

    # Letter in question
    letter = split_line[1][0]

    password = split_line[2]

    # XOR
    if (password[pos1] == letter) ^ (password[pos2] == letter):
        accepted_passwords += 1

print("Number of valid passwords for Part 2:", accepted_passwords)

# endregion


c.print_toc()
