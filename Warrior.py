import random


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
            a, b = self.warrior_location + self.move_dic[choice]
            if isinstance(self.grid[a, b], Warrior):
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
            self.warrior_location = self.warrior_location + self.move_dic[self.command]
            a, b = self.warrior_location
            self.grid[a][b] = self
        return self.warrior_location

    def move_to_mount_doom(self):
        while True:
            command = self.get_direction()
            a, b = self.take_step(command=command)
            print(self.grid)
            if (a, b) == (4, 4):
                print('WIN...')
                break
