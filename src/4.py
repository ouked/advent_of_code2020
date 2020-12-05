# In your batch file, how many passports are valid?
# https://adventofcode.com/2020/day/4

import re
from src.aoc_core import *

c = Core(4)
c.tic()

data = c.get_str_input()


def get_fields(l):
    results = []
    split_line = l.split(" ")
    for field in split_line:
        split_field = field.split(":")
        results.append(split_field)
    return results


def verify_yr(year, minimum, maximum):
    return len(year) == 4 and minimum <= int(year) <= maximum


def verify_hgt(hgt):
    units = hgt[-2:]
    x = int(hgt[:-2])

    if units == "cm":
        return 150 <= x <= 193
    elif units == "in":
        return 59 <= x <= 76

    return False


def verify_hcl(hcl):
    return re.match(r"#(?:[0-9a-f]{6})$", hcl)


def verify_ecl(ecl):
    return ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def verify_pid(pid):
    return len(pid) == 9


def verify_byr(byr):
    return verify_yr(byr, 1920, 2002)


def verify_iyr(iyr):
    return verify_yr(iyr, 2010, 2020)


def verify_eyr(eyr):
    return verify_yr(eyr, 2020, 2030)


def verify_cid(cid):
    return True


def valid_length(doc):
    length = len(doc)
    return (length == 8) or \
           (length == 7 and not any("cid" in sublist for sublist in doc))


document_info = []
valid_documents = 0
valid_documents_valid_data = 0
data.append("")
for line in data:
    # End of document?
    if line == "":
        # (PART 1) Check that all fields are present
        if valid_length(document_info):

            # (PART 2) Check that all fields are valid
            invalid = 0
            for field in document_info:
                if not eval("verify_" + field[0] + "(field[1])"):
                    invalid = 1
                    break

            if invalid == 0:
                valid_documents_valid_data += 1

            valid_documents += 1
        # Reset data
        document_info = []
    else:
        document_info += get_fields(line)

print("1) Valid Documents:", valid_documents)
print("2) Valid Documents with valid data:", valid_documents_valid_data)
c.print_toc()
