class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)

class Game:
    def __init__(self):
        self.property_changed = Event()


class Rat:
    _rat_instances = []
    def __init__(self, game):
        self.game = game
        self.attack = 1
        _rat_instances.append(self)
        self.game.property_changed.append(increment_attack)
        
    def increment_attack(self):
        for rat in _rat_instances:
            rat.attack =+ 1
            
    def decrement_attack(self):
        for rat in _rat_instances:
            rat.attack =- 1
            
    def __exit__(self):
        self.game.property_changed.append(decrement_attack)