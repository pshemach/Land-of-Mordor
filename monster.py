import random


class Monster:
    def __init__(self, grid_length=10):
        self.grid_length = grid_length
        self.monster_location = self.locate_monster()
        while self.monster_location == [(self.grid_length/2)-1, (self.grid_length/2)-1]:
            self.monster_location = self.locate_monster()

    def locate_monster(self):
        w_i = random.choice([i for i in range(1,self.grid_length-1)])
        h_i = random.choice([i for i in range(1,self.grid_length-1)])
        return [w_i, h_i]

    def reset_location(self):
        self.monster_location = self.locate_monster()
        return self.monster_location

