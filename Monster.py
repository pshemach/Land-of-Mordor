import random


class Monster:
    def __init__(self, grid_length = 10):
        self.grid_length = grid_length
        self.monster_location = self.locate_monster()
        while self.monster_location == [4,4]:
            self.monster_location = self.locate_monster()

    def locate_monster(self):
        w_i = random.choice([i for i in range(self.grid_length)])
        h_i = random.choice([i for i in range(self.grid_length)])

        return [w_i, h_i]


# mons=Monster()
