# What is the highest seat ID on a boarding pass?
# https://adventofcode.com/2020/day/5

from src.aoc_core import *

c = Core(5)
c.tic()

data = c.get_str_input()

# Plane info
rows = 128
seats = 8


# Returns number specified by boarding pass.
def binary_partition(boarding_pass, lo_char, hi_char, upper, lower=0):
    lo = lower
    hi = upper

    for char in boarding_pass:
        if char == hi_char:
            lo = int((lo + hi) / 2)
        elif char == lo_char:
            hi = int((lo + hi) / 2)
        else:
            raise Exception("Invalid format for boarding pass:", boarding_pass, "/nAccepted characters: {", lo_char,
                            hi_char, "}")

    return hi


# Calculates seat_id from row and column of seat
def get_seat_id(boarding_pass):
    row = binary_partition(boarding_pass[:-3], "F", "B", rows - 1)
    seat = binary_partition(boarding_pass[-3:], "L", "R", seats - 1)

    return (row * seats) + seat

# List of all seat_ids
seat_ids = [get_seat_id(line.rstrip()) for line in data]

# Find maximum seat_id
# This can be done by sharing the for loop used to collect all seat_ids, but this reads better
max_seat_id = max(seat_ids)

print("1) Maximum seat ID:", max_seat_id)

seat_ids.sort()

# "Your seat wasn't at the very front or back"
for i in range(1, len(seat_ids) - 2):
    # check if seat_ids are contiguous
    if seat_ids[i + 1] != seat_ids[i] + 1:
        print("2) Your seat is:", seat_ids[i] + 1)
        break

c.print_toc()
