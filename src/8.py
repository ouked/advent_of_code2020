# Immediately before any instruction is executed a second time, what value is in the accumulator?
# https://adventofcode.com/2020/day/8

from src.aoc_core import *

c = Core(8)
c.tic()

data = c.get_str_input()


# Run code
# Returns [(bool) successfully run?, (int)accumulator value]
def run():
    # Accumulator
    run.acc = 0

    # Program Counter
    run.pc = 0

    # Execute acc instruction
    def x_acc(x):
        run.acc += eval(str(x))

    # Execute jmp instruction
    def x_jmp(x):
        run.pc += eval(str(x)) - 1

    # Execute nop instruction
    def x_nop(x):
        return

    # Set of executed instructions (used instead of list due to quicker look-up times)
    executed = set()

    while run.pc < len(data):
        # Split line into operation and operand
        [inst, operand] = data[run.pc].split(" ")

        # Save pc value to executed list
        executed.add(run.pc)

        # Execute instruction
        eval("x_" + inst + "(" + operand + ")")

        # Increment program counter
        run.pc += 1

        # Check if next instruction has been executed before
        if run.pc in executed:
            return [False, run.acc]

    # Program got to end successfully
    return [True, run.acc]


print("1)", run()[1])

# Part 2 takes a while, so tell user it's working on it
print("\nFinding answer for part 2...\n")
for i in range(len(data)):

    # Replace jmp with nop (and vice-versa), after saving original line
    if "jmp" in data[i]:
        original_line = data[i]
        data[i] = data[i].replace("jmp", "nop")
    elif "nop" in data[i]:
        original_line = data[i]
        data[i] = data[i].replace("nop", "jmp")

    # Skip acc instructions
    else:
        continue

    # Run code with changes made
    result = run()

    # Did program run successfully?
    if result[0]:
        print("2)", result[1])
        break

    # Revert line back to original
    data[i] = original_line

c.print_toc()
