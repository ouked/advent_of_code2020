import time


class Core:
    puzzle_input_dir = "../puzzle_input/"

    def __init__(self, day):
        self.day = day
        self.start_time = 0

    def get_input_filename(self, extension=".txt"):
        return self.puzzle_input_dir + str(self.day) + extension

    def get_invalid_input_filename(self, extension=".txt"):
        return self.puzzle_input_dir + str(self.day) + "_invalid" + extension

    def get_sample_input_filename(self, extension=".txt"):
        return self.puzzle_input_dir + str(self.day) + "_example" + extension

    def tic(self):
        self.start_time = time.time()
        return self.start_time

    def toc(self):
        end_time = time.time()
        return end_time - self.start_time

    def print_toc(self):
        duration = self.toc()
        print("\nElapsed time:", duration)

    def get_int_input(self):
        with open(self.get_input_filename(), 'r') as f:
            return [int(line.rstrip()) for line in f.readlines()]

    def get_str_input(self):
        with open(self.get_input_filename(), 'r') as f:
            return [line.rstrip() for line in f.readlines()]

    def get_str_invalid_input(self):
        with open(self.get_invalid_input_filename(), 'r') as f:
            return [line.rstrip() for line in f.readlines()]

    def get_str_sample_input(self):
        with open(self.get_sample_input_filename(), 'r') as f:
            return [line.rstrip() for line in f.readlines()]