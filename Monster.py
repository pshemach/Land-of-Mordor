import random


class Monster:
    def __init__(self, grid=10):
        self.grid = grid
        self.loc_mons = self.locate_monster()
        while self.loc_mons==[4,4]:
            self.loc_mons = self.locate_monster()

    def locate_monster(self):
        w_i = random.choice([i for i in range(self.grid)])
        h_i = random.choice([i for i in range(self.grid)])

        return [w_i, h_i]

    def get_monster_location(self):
        return self.loc_mons

mons=Monster()
print(mons.get_monster_location())