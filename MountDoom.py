class MountDoom:
    def __init__(self, grid_length, grid):
        self.grid_length = grid_length
        self.grid = grid
        a = (self.grid_length // 2) - 1
        self.grid[a][a] = self
