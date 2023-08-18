from warrior import Warrior


class Game:
    def __init__(self, n_warrior = 4, n_monster = 5, n_tree = 5):
        self.n_warrior = n_warrior
        self.n_monster = n_monster
        self.n_tree = n_tree
        self.warrior_lis = self.initiate_warrior()

    def initiate_warrior(self):
        n_warr_lis = []
        for i in range(self.n_warrior):
            n_warr_lis.append(Warrior())

        while True:
            count = 0
            for i in range(self.n_warrior):
                for j in range(self.n_warrior):
                    if i != j:
                        if n_warr_lis[i].current_location == n_warr_lis[j].current_location:
                            n_warr_lis[i].reset_location()
                            count = count + 1
            if count == 0:
                break
        return n_warr_lis

    def initiate_monster(self):
        pass

# game=Game()
# print([game.warrior_lis[i].current_location for i in range(4)])
