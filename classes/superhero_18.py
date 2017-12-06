from classes.hero_17 import *


class SuperHero(Hero):
    def __init__(self, name, level, race, magic):
        super().__init__(name, level, race)
        self.magic = magic
        self.mana = 100

    def use_magic(self):
        self.mana -= 10

    def show_hero(self):
        discription = (self.name + " " + str(self.level) + " " + self.race + " " + str(self.health) + " " + str(
            self.mana)).title()
        print(discription)
