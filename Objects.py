import weakref

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

    def __init__(self, description):
        self.description = description
        self.interactions = []
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

bed = Static("Your bed feels comfy")

all_items = []
for obj in Items.getinstances():
    all_items.append(obj)

all_statics = []
for obj in Static.getinstances():
    all_statics.append(obj)