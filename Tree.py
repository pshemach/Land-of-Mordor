import random


class Tree:
    def __init__(self, grid_length = 10):
        self.grid_length = grid_length
        self.tree_location = self.locate_tree()
        while self.tree_location == [4,4]:
            self.tree_location = self.locate_tree()

    def locate_tree(self):
        w_i = random.choice([i for i in range(self.grid_length)])
        h_i = random.choice([i for i in range(self.grid_length)])

        return [w_i, h_i]

# tree= Tree()