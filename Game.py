from warrior import Warrior
from monster import Monster
from tree import Tree


class Game:
    def __init__(self, n_warrior=4, n_monster=5, n_tree=5):
        self.n_warrior = n_warrior
        self.n_monster = n_monster
        self.n_tree = n_tree
        self.warrior_lis = self.initiate_warrior()
        self.monster_lis = self.initiate_monster()
        self.tree_lis = self.initiate_tree()

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
        n_mons_lis = []
        for i in range(self.n_monster):
            n_mons_lis.append(Monster())

        while True:
            count = 0
            for i in range(self.n_monster):
                for j in range(self.n_monster):
                    if i != j:
                        if n_mons_lis[i].monster_location == n_mons_lis[j].monster_location:
                            n_mons_lis[i].reset_location()
                            count += 1
            if count == 0:
                break
        return n_mons_lis

    def initiate_tree(self):
        n_tree_lis = []
        for i in range(self.n_tree):
            n_tree_lis.append(Tree())

        while True:
            count = 0
            for i in range(self.n_tree):
                for j in range(self.n_tree):
                    if i != j:
                        if n_tree_lis[i].tree_location == n_tree_lis[j].tree_location:
                            n_tree_lis[i].reset_location()
                            count += 1
            for i in range(self.n_tree):
                for k in range(self.n_monster):
                    if n_tree_lis[i].tree_location == self.monster_lis[k].monster_location:
                        n_tree_lis[i].reset_location()
                        count += 1
            if count == 0:
                break
        return n_tree_lis


game = Game()
print([game.warrior_lis[i].current_location for i in range(4)])
print([game.monster_lis[i].monster_location for i in range(5)])
print([game.tree_lis[i].tree_location for i in range(5)])