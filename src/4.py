# In your batch file, how many passports are valid?
# https://adventofcode.com/2020/day/4

import re
from src.aoc_core import *

c = Core(4)
c.tic()

data = c.get_str_input()
# Append "" so that last document gets processed
data.append("")


# Return key value pairs
def get_fields(l):
    return [f.split(":") for f in l.split(" ")]


# Verify year
def verify_yr(year, minimum, maximum):
    try:
        return len(year) == 4 and minimum <= int(year) <= maximum
    except ValueError:
        return False


# Verify Height
def verify_hgt(hgt):
    units = hgt[-2:]
    try:
        x = int(hgt[:-2])
    except ValueError:
        return False

    # Check bounds for value, based on whether the given unit is cm or in
    if units == "cm":
        return 150 <= x <= 193
    elif units == "in":
        return 59 <= x <= 76

    return False


# Verify Hair Colour
def verify_hcl(hcl):
    # Regex matches hex colours
    return re.match(r"#(?:[0-9a-f]{6})$", hcl)


# Verify Eye colour
def verify_ecl(ecl):
    return ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


# Verify Passport ID
def verify_pid(pid):
    try:
        return len(pid) == 9
    except ValueError:
        return False


# Verify Birth year
def verify_byr(byr):
    return verify_yr(byr, 1920, 2002)


# Verify Issue Year
def verify_iyr(iyr):
    return verify_yr(iyr, 2010, 2020)


# Verify Expiry year
def verify_eyr(eyr):
    return verify_yr(eyr, 2020, 2030)


# Verify Country ID (ignored)
def verify_cid(cid):
    return True


def valid_length(doc):
    length = len(doc)
    # All fields are present, or only one missing is cid (country  id)
    return (length == 8) or \
           (length == 7 and not any("cid" in sublist for sublist in doc))


document_info = []
valid_documents = 0
valid_documents_valid_data = 0

for line in data:
    # End of document?
    if line == "":
        # (PART 1) Check that all fields are present
        if valid_length(document_info):

            # (PART 2) Check that all fields are valid
            valid = True
            for field in document_info:

                # Runs appropriate verify function

                # EXAMPLE:
                #       field[0] = ecl -> verify_ecl(field[1])

                if eval("verify_" + field[0] + "(field[1])"):
                    continue

                valid = False
                break

            if valid:
                valid_documents_valid_data += 1

            valid_documents += 1
        # Reset data
        document_info = []
    else:
        document_info += get_fields(line)

print("1) Valid Documents:", valid_documents)
print("2) Valid Documents with valid data:", valid_documents_valid_data)
c.print_toc()
