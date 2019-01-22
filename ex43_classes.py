#Basic Object-Oriented Analysis and Design
class Scence(object):
    
    def enter(self):
        pass

class Engine(object):

    def __init__(self, scence_map):
        pass

    def play(self):
        pass

class CentralCorridor(Scence):

    def enter(self):
        pass

class LaserWeaponArmory(Scence):

    def enter(self):
        pass

class EscapePod(Scence):

    def enter(self):
        pass


class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scence_name):
        pass

    def opening_scene(self):
        pass

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()



