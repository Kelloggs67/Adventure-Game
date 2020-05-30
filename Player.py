import sys,time,random

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
        self.current_room = None
        self.state = None
        self.change_state = []

    def __repr__(self):
        return "{0}\nHealth: {1}\nAttack: {2}\nArmor: {3}\n".format(self.name, self.stats["max_health"], self.stats["attack"], self.stats["armor"])



    def pick_up(self, item):
        print(self.name + " picked up " + item.name)
        self.inventory.append(item)

    def use_potion(self, item):
        if item in self.inventory:
            self.health += item.health
        else:
            print("You don't have that item")

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
            self.update_stats_unequip()
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
            self.update_stats_equip()


typing_speed = 120

def delay_print(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print('')



def create_character():
    delay_print("What is your name?")
    name_input = input("> ").strip().capitalize()
    player1.name = name_input
    delay_print("Hello " + player1.name + "")
    time.sleep(2)
    return player1



player1 = Player()
player1.change_state.append("get_out_of_bed")

