from Subject import Subject


class MountDoom(Subject):
    def __init__(self, grid_length, grid):
        super(MountDoom, self).__init__()
        self.grid_length = grid_length
        self.grid = grid
        a = (self.grid_length // 2) - 1
        self.grid[a][a] = self

    def notify(self, winner):
        for war in self.subscribers:
            war.listen_massage(winner)
