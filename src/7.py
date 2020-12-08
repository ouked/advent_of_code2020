# How many bag colors can eventually contain at least one shiny gold bag?
# https://adventofcode.com/2020/day/7

from src.aoc_core import *

c = Core(7)
c.tic()

data = c.get_str_input()


class Bag:
    # List of all bags
    all = []

    # Gets or makes new bag
    @staticmethod
    def get(color):
        for b in Bag.all:
            if b.color == color.strip():
                return b

        # Make new bag
        n = Bag(color)
        Bag.all.append(n)
        return n

    def __init__(self, color):
        self.color = color
        self.children = dict()
        self.parents = set()
        self.ancestors = set()

    def __str__(self):
        return self.color + " | " + str([child.color for child in self.children])

    def add_child(self, color, quantity):
        child = Bag.get(color)
        self.children[child] = quantity
        child.add_parent(self)

    def add_parent(self, parent):
        if type(parent) is str:
            parent = Bag.get(parent)
        self.parents.add(parent)

    def get_all_ancestors(self):
        for p in self.parents:
            self.ancestors = self.ancestors.union(p.get_all_ancestors())

        self.ancestors = self.ancestors.union(self.parents)
        return self.ancestors

    def get_size(self):
        count = 0
        for child in self.children.keys():
            quantity = int(self.children.get(child))
            count += quantity + (quantity * child.get_size())
        return count


# Make Bag objects
for line in data:
    split_line = line.split(" bags contain")
    if split_line[1].strip() != "no other bags.":
        for rule in split_line[1].split(","):
            split_rule = rule.replace("bags", "").replace(".", "").replace("bag", "").strip().split(" ", 1)

            # Make new bag
            Bag.get(split_line[0]).add_child(split_rule[1], split_rule[0])

print("1)", len(Bag.get("shiny gold").get_all_ancestors()))
print("2)", Bag.get("shiny gold").get_size())

c.print_toc()
