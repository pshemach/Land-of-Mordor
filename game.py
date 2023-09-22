from Warrior import Warrior
from Monster import Monster
from Tree import Tree
import random


class Game:
    def __init__(self, n_warrior=4, n_monster=5, n_tree=5, grid_length=10):
        self.grid_length = grid_length
        self.n_warrior = n_warrior
        self.n_monster = n_monster
        self.n_tree = n_tree
        self.warrior_lis = self.initiate_warrior()
        self.monster_lis = self.initiate_monster()
        self.tree_lis = self.initiate_tree()
        print(f'Worriers Locations: {[self.warrior_lis[i].current_location for i in range(self.n_warrior)]}')
        print(f'Monsters Locations: {[self.monster_lis[i].monster_location for i in range(self.n_monster)]}')
        print(f'Trees Locations: {[self.tree_lis[i].tree_location for i in range(self.n_tree)]}')
        for worrier in self.warrior_lis:
            self.play_game(worrier)

    def initiate_warrior(self):
        n_war_lis = []
        for i in range(self.n_warrior):
            n_war_lis.append(Warrior())

        while True:
            count = 0
            for i in range(self.n_warrior):
                for j in range(self.n_warrior):
                    if i != j:
                        if n_war_lis[i].current_location == n_war_lis[j].current_location:
                            n_war_lis[i].reset_location()
                            count = count + 1
            if count == 0:
                break
        return n_war_lis

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

    def move_choice(self, warrior):
        move_dic = {'UP': [0, 1], 'DOWN': [0, -1], 'RIGHT': [1, 0], 'LEFT': [-1, 0]}
        choice_lis = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        choice = random.choice(choice_lis)
        for wor in self.warrior_lis:
            if wor != warrior and wor.current_location == warrior.current_location + move_dic[choice]:
                choice_lis.remove(choice)
                choice = random.choice(choice_lis)
        return choice

    def play_game(self, warrior):
        while True:
            choice = self.move_choice(warrior)
            warrior.walk_to_mount_doom(choice)
            for mons in self.monster_lis:
                if mons.monster_location == warrior.current_location:
                    print(f'Worrier {self.warrior_lis.index(warrior)} Out AT Monster Location: {mons.monster_location}')
                    return False
                elif warrior.current_location == [(self.grid_length / 2) - 1, (self.grid_length / 2) - 1]:
                    print(f'Worrier {self.warrior_lis.index(warrior)} WIN!!!')
                    return False


game = Game()
