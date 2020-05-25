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
        print(self.name + " picked up " + item.name)
        self.inventory.append(item)



    def update_stats(self):
        equipped = self.equipped.values()
        for item in equipped:
            if item:
                self.stats["attack"] += item.attack
                self.stats["armor"] += item.armor
            else:
                continue



    def unequip(self, item):
        equipped = self.equipped.values()
        if item not in equipped:
            print("You don't have this item equipped.")
        else:
            print(self.name + " unequiped " + item.name)
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



class Equippables:
    def __init__(self, name, type, attack, armor, equip, price):
        self.name = name
        self.type = type
        self.attack = attack
        self.armor = armor
        self.equip = equip
        self.price = price


    def __repr__(self):
        return self.name




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

def check(input, player=None, items=None):
    mod_input = input.lower().strip()
    actions = {"pick up": ["take", "pick up", "put"]}
    if mod_input == "inventory":
        return print(player.inventory)
    if mod_input == "stats":
        return print(player)
    for action in actions["pick up"]:
        if action in mod_input:
            for item in items:
                if item.name or item.type in mod_input:
                    player.pick_up(item)
                else:
                    return print("Huh?")
        else:
            return print("Huh?")

    else:
        return print("Command not found")

def create_character():
    name_input = input("What is your name?").strip().capitalize()
    player1 = Player(name_input)
    print("Hello " + player1.name)
    return player1


def play_game():
    player1 = create_character()
    print("You wake up and there is an Axe and a Sword next to you.")
    loot = [cool_sword, rusty_axe]
    action = input("What would you like to do?")
    check(action, player1, loot)
play_game()
