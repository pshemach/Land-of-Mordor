import random


class Tree:
    def __init__(self, grid_length = 10):
        self.grid_length = grid_length
        self.tree_location = self.locate_tree()
        while self.tree_location == [(self.grid_length/2)-1, (self.grid_length/2)-1]:
            self.tree_location = self.locate_tree()

    def locate_tree(self):
        w_i = random.choice([i for i in range(1,self.grid_length-1)])
        h_i = random.choice([i for i in range(1,self.grid_length-1)])
        return [w_i, h_i]

    def reset_location(self):
        self.tree_location = self.locate_tree()
        return self.tree_location
