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



rusty_axe = Equippables("Rusty Axe","Axe", 5, 0, "Weapon", 10)
cool_sword = Equippables("Cool Sword", "Sword", 7, 0, "Weapon", 12)


class Static():
    def __init__(self, description, key_words):
        self.description = description
        self.interactions = []

bed = Static("")
