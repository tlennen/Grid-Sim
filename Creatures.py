import pygame


class Creatures:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (0,255,0)
        self.alive = False

    def print_critter(self):
        pass

class Plant(Creatures):
    def __init__(self, x, y):
        Creatures.__init__(self, x, y)
        self.color = (0,255,0)
        self.alive = True

    def print_critter(self, pos_x, pos_y, size):
        pass

class Herbivore(Creatures):
    def __init__(self, x, y):
        Creatures.__init__(self, x, y)
        self.color = (255,0,0)
        self.alive = True

    def print_critter(self, pos_x, pos_y, size):
        pass

class Carnivore(Creatures):
    def __init__(self, x, y):
        Creatures.__init__(self, x, y)
        self.color = (0,0,255)
        self.alive = True

    def print_critter(self, pos_x, pos_y, size):
        pass