import random

from Monster import Monster
from Tree import Tree


class Warrior:
    def __init__(self, grid_length, grid):
        self.grid_length = grid_length
        self.grid = grid
        self.move_dic = {'UP': [0, 1], 'DOWN': [0, -1], 'RIGHT': [1, 0], 'LEFT': [-1, 0]}
        self.command = None
        self.warrior_location = self.initiate_location()

    def initiate_location(self):
        while True:
            i_w = random.randint(0, self.grid_length - 1)
            if i_w != 0 or i_w != (self.grid_length - 1):
                i_h = random.choice([0, (self.grid_length - 1)])
            else:
                i_h = random.randint(0, self.grid_length - 1)
            if self.grid[i_w][i_h] == 0:
                break
        return [i_w, i_h]

    def reset_initial_location(self):
        self.warrior_location = self.initiate_location()
        return self.warrior_location

    def get_direction(self):
        direction_lis = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        choice = random.choice(direction_lis)
        for i in range(4):
            a = self.warrior_location[0] + self.move_dic[choice][0]
            b = self.warrior_location[1] + self.move_dic[choice][1]
            if isinstance(self.grid[a][b], Warrior):
                direction_lis.remove(choice)
                choice = random.choice(direction_lis)
                continue
            else:
                break
        return choice

    def take_step(self, command=None):
        self.command = command
        a, b = self.warrior_location
        if 0 <= a and b <= self.grid_length - 1:
            self.grid[a][b] = 0
            self.warrior_location[0] = self.warrior_location[0] + self.move_dic[self.command][0]
            self.warrior_location[1] = self.warrior_location[1] + self.move_dic[self.command][1]
        return self.warrior_location

    def move_to_mount_doom(self):
        while True:
            self.command = self.get_direction()
            a, b = self.take_step(command=self.command)
            print(a,b)
            if [a, b] == [(self.grid_length / 2) - 1, (self.grid_length / 2) - 1]:
                print('WIN', self)
                break
            elif isinstance(self.grid[a][b],Monster):
                print('Monster',self)
                break
            elif isinstance(self.grid[a][b],Tree):
                self.warrior_location[0] = self.warrior_location[0] - self.move_dic[self.command][0]
                self.warrior_location[1] = self.warrior_location[1] - self.move_dic[self.command][1]
            else:
                self.grid[a][b] = self





