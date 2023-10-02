import random


class Warrior:
    def __init__(self, grid_length, grid):
        self.grid_length = grid_length
        self.grid = grid
        self.move_dic = {'UP': [0, 1], 'DOWN': [0, -1], 'RIGHT': [1, 0], 'LEFT': [-1, 0]}
        self.command = None
        self.current_location = self.initiate_location()

    def initiate_location(self):
        i_w = random.randint(0, self.grid_length - 1)
        if i_w != 0 or i_w != (self.grid_length - 1):
            i_h = random.choice([0, (self.grid_length - 1)])
        else:
            i_h = random.randint(0, self.grid_length - 1)
        return [i_w, i_h]

    def reset_initial_location(self):
        self.current_location = self.initiate_location()
        return self.current_location

    def get_direction(self):
        direction_lis = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        choice = random.choice(direction_lis)
        for i in range(4):
            a, b = self.current_location + self.move_dic[choice]
            if isinstance(self.grid[a, b], Warrior):
                direction_lis.remove(choice)
                choice = random.choice(direction_lis)
                continue
            else:
                break
        return choice

    def take_step(self, command=None):
        self.command = command
        # if self.command == 'UP':
        #     if self.current_location[1] != (self.grid_length - 1):
        #         self.current_location = self.current_location + self.move_dic[command]
        # elif self.command == 'DOWN':
        #     if self.current_location[1] != 0:
        #         self.current_location = self.current_location + self.move_dic[command]
        # elif self.command == 'RIGHT':
        #     if self.current_location[0] != (self.grid_length - 1):
        #         self.current_location = self.current_location + self.move_dic[command]
        # elif self.command == 'LEFT':
        #     if self.current_location[0] != 0:
        #         self.current_location = self.current_location + self.move_dic[command]
        # return self.current_location
        a, b = self.current_location + self.move_dic[self.command]
        if 0 <= a and b <= 9:
            self.current_location = self.current_location + self.move_dic[self.command]
        return self.current_location

    def move_to_mount_doom(self):
        pass
