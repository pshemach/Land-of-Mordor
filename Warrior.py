import random


class Warrior:
    def __init__(self, grid_length=10):
        self.grid_length = grid_length
        self.command = None
        self.current_location = self.initiate_location()

    def initiate_location(self):
        i_w = random.choice([i for i in range(self.grid_length)])
        if i_w != 0 or i_w != (self.grid_length - 1):
            i_h = random.choice([0, (self.grid_length - 1)])
        else:
            i_h = random.randint(0,self.grid_length-1)
        return [i_w, i_h]

    def reset_location(self):
        self.current_location = self.initiate_location()
        return self.current_location

    def walk_to_mount_doom(self, command=None):

        self.command = command
        if self.command == 'UP':
            if self.current_location[1] != (self.grid_length - 1):
                self.current_location[1] = self.current_location[1] + 1
        elif self.command == 'DOWN':
            if self.current_location[1] != 0:
                self.current_location[1] = self.current_location[1] - 1
        elif self.command == 'RIGHT':
            if self.current_location[0] != (self.grid_length - 1):
                self.current_location[0] = self.current_location[0] + 1
        elif self.command == 'LEFT':
            if self.current_location[0] != 0:
                self.current_location[0] = self.current_location[0] - 1
        return self.current_location

