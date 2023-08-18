from Warrior import Warrior


class Game:
    def __init__(self,n_warr=4,n_mons=5,n_tree=5):
        self.n_warr =n_warr
        self.n_mons=n_mons
        self.n_tree=n_tree
        self.initiate_war_lis = self.initiate_warrior()

    def initiate_warrior(self):
        self.n_warr_lis =[]
        for i in range(self.n_warr):
            self.n_warr_lis.append(Warrior())

        while True:
            c=0
            for i in range(self.n_warr):
                for j in range(self.n_warr):
                    if i!=j:
                        if self.n_warr_lis[i].c_loc==self.n_warr_lis[j].c_loc:
                            self.n_warr_lis[i].reset_location()
                            c=c+1

            if c==0:
                break
        return self.n_warr_lis


    def initiate_monster(self):
        pass

game=Game()
print([game.initiate_war_lis[i].c_loc for i in range(4)])