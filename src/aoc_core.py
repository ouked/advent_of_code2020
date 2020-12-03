import time


class Core:
    puzzle_input_dir = "../puzzle_input/"
    start_time = 0

    def __init__(self, day):
        self.day = day

    def get_input_filename(self, extension=".txt"):
        return self.puzzle_input_dir + str(self.day) + extension

    def tic(self):
        self.start_time = time.time()
        return self.start_time

    def toc(self):
        end_time = time.time()
        return end_time - self.start_time

    def print_toc(self):
        duration = str(self.toc())
        print("Elapsed time: " + duration)

    def get_int_input(self):
        with open(self.get_input_filename(), 'r') as f:
            return [int(line.rstrip()) for line in f.readlines()]

    def get_str_input(self):
        with open(self.get_input_filename(), 'r') as f:
            return [line.rstrip() for line in f.readlines()]