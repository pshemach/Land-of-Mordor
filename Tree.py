from GameObjects import GameObject


class Tree(GameObject):
    def __init__(self, grid_length, grid):
        super().__init__(grid_length, grid)
        self.tree_location = self.object_location()