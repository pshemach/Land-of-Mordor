import random


class Tree:
    def __init__(self, grid_length, grid):
        self.grid_length = grid_length
        self.grid = grid
        self.tree_location = self.locate_tree()

    def locate_tree(self):
        while True:
            i_w = random.randint(0, self.grid_length - 1)
            i_h = random.randint(0, self.grid_length - 1)
            if self.grid[i_w][i_h] == 0 and (i_w, i_h) != ((self.grid_length/2)-1, (self.grid_length/2)-1):
                break
        return [i_w, i_h]

    def reset_location(self):
        self.tree_location = self.locate_tree()
        return self.tree_location
