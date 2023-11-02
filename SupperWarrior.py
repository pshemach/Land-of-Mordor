from Tree import Tree
from Warrior import Warrior
import random


class SupperWarrior(Warrior):
    def __init__(self, grid_length, grid_keeper):
        super().__init__(grid_length, grid_keeper)

    def get_direction(self):
        direction_lis = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        choice = random.choice(direction_lis)
        for i in range(4):
            a = self.warrior_location[0] + self.move_dic[choice][0]
            b = self.warrior_location[1] + self.move_dic[choice][1]
            try:
                if isinstance(self.grid[a][b], Warrior) or isinstance(self.grid[a][b], Tree):
                    direction_lis.remove(choice)
                    choice = random.choice(direction_lis)
                    continue
                else:
                    break
            except:
                continue
        return choice
