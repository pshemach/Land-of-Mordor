import random


class Tree:
    def __init__(self, grid=10):
        self.grid = grid
        self.loc_tree = self.locate_tree()
        while self.loc_tree==[4,4]:
            self.loc_tree = self.locate_tree()

    def locate_tree(self):
        w_i = random.choice([i for i in range(self.grid)])
        h_i = random.choice([i for i in range(self.grid)])

        return [w_i, h_i]

    def get_tree_location(self):
        return self.loc_tree

tree= Tree()