from GameObjects import GameObject


class Monster(GameObject):
    def __init__(self, grid_length, grid_keeper):
        super().__init__(grid_length, grid_keeper)
        self.monster_location = self.object_location()