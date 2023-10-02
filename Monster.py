import random


class Monster:
    def __init__(self, grid_length, grid):
        self.grid_length = grid_length
        self.grid = grid
        self.monster_location = self.locate_monster()

    def locate_monster(self):
        while True:
            i_w = random.randint(0, self.grid_length - 1)
            i_h = random.randint(0, self.grid_length - 1)
            if self.grid[i_w][i_h] == 0 and (i_w, i_h) != ((self.grid_length/2)-1, (self.grid_length/2)-1):
                break
        return [i_w, i_h]

    def reset_location(self):
        self.monster_location = self.locate_monster()
        return self.monster_location

