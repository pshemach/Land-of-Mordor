from Warrior import Warrior
from Monster import Monster
from Tree import Tree
import random
import threading

class Game:
    def __init__(self, n_warrior=4, n_monster=5, n_tree=5, grid_length=10):
        self.grid_length = grid_length
        self.n_warrior = n_warrior
        self.n_monster = n_monster
        self.n_tree = n_tree
        self.grid = [[0 for _ in range(self.grid_length)] for _ in range(self.grid_length)]
        self.warrior_lis = self.initiate_warrior()
        self.monster_lis = self.initiate_monster()
        self.tree_lis = self.initiate_tree()
        print(f'Worriers Locations: {[self.warrior_lis[i].warrior_location for i in range(self.n_warrior)]}')
        print(f'Monsters Locations: {[self.monster_lis[i].monster_location for i in range(self.n_monster)]}')
        print(f'Trees Locations: {[self.tree_lis[i].tree_location for i in range(self.n_tree)]}')

    def initiate_warrior(self):
        n_war_lis = []
        for _ in range(self.n_warrior):
            war = Warrior(grid_length=self.grid_length, grid=self.grid)
            n_war_lis.append(war)
            a, b = war.warrior_location
            self.grid[a][b] = war
        return n_war_lis

    def initiate_monster(self):
        n_mons_lis = []
        for _ in range(self.n_monster):
            mons = Monster(grid_length=self.grid_length, grid=self.grid)
            n_mons_lis.append(mons)
            a, b = mons.monster_location
            self.grid[a][b] = mons
        return n_mons_lis

    def initiate_tree(self):
        n_tree_lis = []
        for _ in range(self.n_tree):
            tree = Tree(grid_length=self.grid_length, grid=self.grid)
            n_tree_lis.append(tree)
            a, b = tree.tree_location
            self.grid[a][b] = tree
        return n_tree_lis

    def play_game(self):
        for war in self.warrior_lis:
            war.move_to_mount_doom()


game = Game()
print(game.grid)