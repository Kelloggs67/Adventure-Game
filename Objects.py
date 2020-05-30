import weakref
from Player import *

class Items():

    _instances = set()

    def __init__(self, name, type, attack, armor, max_health, health, equip, price, use=False):
        self.name = name
        self.type = type
        self.attack = attack
        self.armor = armor
        self.max_health = max_health
        self.health = health
        self.equip = equip
        self.price = price
        self._instances.add(weakref.ref(self))
        self.use = use

    def __repr__(self):
        return self.name

    @classmethod
    def getinstances(cls):
        dead = set()
        for ref in cls._instances:
            obj = ref()
            if obj is not None:
                yield obj
            else:
                dead.add(ref)
        cls._instances -= dead

rusty_axe = Items("Rusty Axe", "Axe", 5, 0, 0, 0, "Weapon", 10)
cool_sword = Items("Cool Sword", "Sword", 7, 0, 0, 0, "Weapon", 12)
potion = Items("Potion", "Potion", 0, 0, 0, 5, False, 5, True)


class Static():

    _instances = set()

    def __init__(self, name, description, state):
        self.name = name
        self.description = description
        self.interactions = {}
        self.state = state
        self._instances.add(weakref.ref(self))

    @classmethod
    def getinstances(cls):
        dead = set()
        for ref in cls._instances:
            obj = ref()
            if obj is not None:
                yield obj
            else:
                dead.add(ref)
        cls._instances -= dead

bed = Static("bed", "This has been your bed all your life.", "in bed")
bed.state = "in bed"
def get_out_of_bed():
    bed.state = "out of bed"
    player1.state = None
def make_bed():
    print("You made your bed")
    bed.description = "The bed is nicely made"
bed.interactions["get out"] = get_out_of_bed
bed.interactions["hop out"] = get_out_of_bed
bed.interactions["leave"] = get_out_of_bed
bed.interactions["make"] = make_bed


all_items = []
for obj in Items.getinstances():
    all_items.append(obj)

all_statics = []
for obj in Static.getinstances():
    all_statics.append(obj)

all_things = all_items + all_statics


