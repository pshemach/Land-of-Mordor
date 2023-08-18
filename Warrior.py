import random


class Warrior:
    def __init__(self, grid=10):
        self.grid = grid
        self.i_h = None
        self.i_w = None
        self.command = None
        self.c_loc = self.initiate_location()

    def initiate_location(self):
        self.i_w = random.choice([i for i in range(self.grid)])
        if self.i_w != 0 or 9:
            self.i_h = random.choice([0, 9])
        else:
            self.i_h = random.choice([i for i in range(self.grid)])
        return [self.i_w, self.i_h]

    def reset_location(self):
        self.c_loc = self.initiate_location()
        return self.c_loc

    def walk_to_mount_doom(self, command=None):

        self.command = command
        if self.command == 'UP':
            if self.c_loc[1] != 9:
                self.c_loc[1] = self.c_loc[1] + 1
        elif self.command == 'DOWN':
            if self.c_loc[1] != 0:
                self.c_loc[1] = self.c_loc[1] - 1
        elif self.command == 'RIGHT':
            if self.c_loc[0] != 9:
                self.c_loc[0] = self.c_loc[0] + 1
        elif self.command == 'LEFT':
            if self.c_loc[0] != 0:
                self.c_loc[0] = self.c_loc[0] - 1

        return self.c_loc


# warr = Warrior()
# while True:
#     command = random.choice(['UP', 'DOWN', 'LEFT', "RIGHT"])
#     current_location = warr.walk_to_mount_doom(command)
#     if current_location == [4, 4]:
#         print("WIN!!!")
#         break
