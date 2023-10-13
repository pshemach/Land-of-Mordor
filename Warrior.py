import random
from Monster import Monster
from Tree import Tree
from MountDoom import MountDoom
from GameObjects import GameObject


class Warrior(GameObject):
    def __init__(self, grid_length, grid_keeper):
        super().__init__(grid_length, grid_keeper)
        self.grid_keeper = grid_keeper
        self.move_dic = {'UP': [0, 1], 'DOWN': [0, -1], 'RIGHT': [1, 0], 'LEFT': [-1, 0]}
        self.command = None
        self.warrior_location = self.object_location()

    def object_location(self):
        while True:
            i_w = random.randint(0, self.grid_length - 1)
            if i_w != 0 or i_w != (self.grid_length - 1):
                i_h = random.choice([0, (self.grid_length - 1)])
            else:
                i_h = random.randint(0, self.grid_length - 1)
            if self.grid[i_w][i_h] == 0:
                break
        return [i_w, i_h]

    def get_direction(self):
        direction_lis = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        choice = random.choice(direction_lis)
        for i in range(4):
            a = self.warrior_location[0] + self.move_dic[choice][0]
            b = self.warrior_location[1] + self.move_dic[choice][1]
            try:
                if isinstance(self.grid[a][b], Warrior):
                    direction_lis.remove(choice)
                    choice = random.choice(direction_lis)
                    continue
                else:
                    break
            except:
                continue
        return choice

    def take_step(self, command=None):
        self.command = command
        a, b = self.warrior_location
        if self.command == 'UP':
            if self.warrior_location[1] != (self.grid_length - 1):
                self.grid[a][b] = 0
                self.warrior_location[1] = self.warrior_location[1] + 1
        elif self.command == 'DOWN':
            if self.warrior_location[1] != 0:
                self.grid[a][b] = 0
                self.warrior_location[1] = self.warrior_location[1] - 1
        elif self.command == 'RIGHT':
            if self.warrior_location[0] != (self.grid_length - 1):
                self.grid[a][b] = 0
                self.warrior_location[0] = self.warrior_location[0] + 1
        elif self.command == 'LEFT':
            if self.warrior_location[0] != 0:
                self.grid[a][b] = 0
                self.warrior_location[0] = self.warrior_location[0] - 1
        return self.warrior_location

    def move_to_mount_doom(self):
        while True:
            self.grid_keeper.acquire_lock()
            self.command = self.get_direction()
            a, b = self.take_step(command=self.command)
            if isinstance(self.grid[a][b], MountDoom):
                print('WIN', self)
                self.grid_keeper.release_lock()
                break
            elif isinstance(self.grid[a][b], Monster):
                print('Meet Monster', self)
                self.grid_keeper.release_lock()
                break
            elif isinstance(self.grid[a][b], Tree):
                self.warrior_location[0] = self.warrior_location[0] - self.move_dic[self.command][0]
                self.warrior_location[1] = self.warrior_location[1] - self.move_dic[self.command][1]
                a, b = self.warrior_location
                self.grid_keeper.place_in_grid(a, b, self)
                self.grid_keeper.release_lock()
            else:
                self.grid_keeper.place_in_grid(a, b, self)
                self.grid_keeper.release_lock()

