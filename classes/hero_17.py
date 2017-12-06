class Hero(object):
    def __init__(self, name, level, race):
        self.name = name
        self.level = level
        self.race = race
        self.health = 100

    def show_hero(self):
        disc = (self.name + " " + str(self.level) + " " + self.race + " " + str(self.health)).title()
        print(disc)

    def level_p(self):
        self.level += 1