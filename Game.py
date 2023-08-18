from warrior import Warrior


class Game:
    def __init__(self, n_warr = 4, n_mons = 5, n_tree = 5):
        self.n_warr = n_warr
        self.n_mons = n_mons
        self.n_tree = n_tree
        self.warior_lis = self.initiate_warrior()

    def initiate_warrior(self):
        n_warr_lis = []
        for i in range(self.n_warr):
            n_warr_lis.append(Warrior())

        while True:
            count = 0
            for i in range(self.n_warr):
                for j in range(self.n_warr):
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
# print([game.initiate_war_lis[i].c_loc for i in range(4)])