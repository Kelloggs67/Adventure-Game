class Player:
    def __init__(self, name):
        self.name = name
        self.stats = {"max_health": 10,
                      "attack": 5,
                      "armor": 0}
        self.health = self.stats["max_health"]
        self.equipped = {"Head": None,
                         "Chest": None,
                         "Legs": None,
                         "Feet": None,
                         "Weapon": None}
        self.inventory = []

    def __repr__(self):
        return "{0}\nHealth: {1}\nAttack: {2}\nArmor: {3}\n".format(self.name, self.stats["max_health"], self.stats["attack"], self.stats["armor"])

    def pick_up(self, item):
        if item.name[0] in [a, e, i, o, u]:
            print(self.name + "picked up an " + item.name)
        else:
            print(self.name + "Picked up a " + item.name)
        self.inventory.append(item)

    def update_stats(self):
        self.equipped.values()

    def equip(self, item):
        if item not in self.inventory:
            print("You do not have that item.")
        else:
            print(self.name + "equipped a " + item.name)
            self.inventory.pop(item)
            self.equipped[item.equip] = item


class Items:
    def __init__(self, price):
        self.price = price

class Equippables:
    def __init__(self, name, type, attack, armor, equip, price, buffs):
        self.name = name
        self.type = type
        self.attack = attack
        self.armor = armor
        self.equip = equip
        self.price = price
        self.buffs = {}

    def __repr__(self):
        return self.name





player1 = Player("Tim")
Rusty_Axe = Equippables("Rusty Axe","Axe", 5, 0, "Weapon", 10)


def create_character():
    name_input = input("What is your name?")
    player1 = Player(name_input)
    print("Hello " + player1.name)
    print("These are your stats")
    print(player1)


