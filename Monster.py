from GameObjects import GameObject
from GameObjects import GameObject


class Monster(GameObject):
    def __init__(self, grid_length, grid):
        super().__init__(grid_length, grid)
        self.monster_location = self.object_location()