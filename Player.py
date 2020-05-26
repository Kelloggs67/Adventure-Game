class Player:
    def __init__(self, name=None):
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
        print(self.name + " picked up " + item.name)
        self.inventory.append(item)



    def update_stats_equip(self):
        equipped = self.equipped.values()
        for item in equipped:
            if item:
                self.stats["attack"] += item.attack
                self.stats["armor"] += item.armor
            else:
                continue

    def update_stats_unequip(self):
        equipped = self.equipped.values()
        for item in equipped:
            if item:
                self.stats["attack"] -= item.attack
                self.stats["armor"] -= item.armor
            else:
                continue

    def unequip(self, item):
        equipped = self.equipped.values()
        if item not in equipped:
            print("You don't have this item equipped.")
        else:
            print(self.name + " unequiped " + item.name)
            self.update_stats_equip()
            self.equipped[item.equip] = None
            self.inventory.append(item)



    def equip(self, item):
        if item not in self.inventory:
            print("You do not have that item.")
        else:
            if self.equipped[item.equip] != None:
                self.unequip(self.equipped[item.equip])
            print(self.name + " equipped " + item.name)
            self.inventory.pop(self.inventory.index(item))
            self.equipped[item.equip] = item
            self.update_stats()



class Items:
    def __init__(self, price):
        self.price = price



class Equippables(Items):
    def __init__(self, name, type, attack, armor, equip, price):
        self.name = name
        self.type = type
        self.attack = attack
        self.armor = armor
        self.equip = equip
        self.price = price


    def __repr__(self):
        return self.name





player1 = Player()
rusty_axe = Equippables("Rusty Axe","Axe", 5, 0, "Weapon", 10)
cool_sword = Equippables("Cool Sword", "Sword", 7, 0, "Weapon", 12)

'''''''''
print(player1)
player1.pick_up(rusty_axe)
player1.equip(rusty_axe)
print(player1)
player1.pick_up(cool_sword)
player1.equip(cool_sword)
print(player1)
'''''''''