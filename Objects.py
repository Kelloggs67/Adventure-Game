import weakref
from Player import *


class Items():
    _instances = set()

    def __init__(self, name, type, attack, armor, max_health, health, equip, price, level):
        self.name = name
        self.type = type
        self.attack = attack
        self.armor = armor
        self.max_health = max_health
        self.health = health
        self.equip = equip
        self.price = price
        self.level = level
        self._instances.add(weakref.ref(self))
        self.description = None

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


rusty_axe = Items("Rusty Axe", "Axe", 5, 0, 0, 0, "Weapon", 10, 1)
bike_helmet = Items("Bike Helmet", "Helmet", 0, 2, 0, 0, "Head", 5, 1)
cool_sword = Items("Cool Sword", "Sword", 7, 0, 0, 0, "Weapon", 12, 1)
potion = Items("Potion", "Potion", 0, 0, 0, 5, False, 5, 1)
bedroom_key = Items("bedroom key", "key", 0, 0, 0, 0, False, 0, 0)

all_items = []
for obj in Items.getinstances():
    all_items.append(obj)


def list_of_random_items(level):
    complete_list = []
    armor = []
    useable = []
    weapons = []
    list_items_of_level = []
    for item in all_items:
        if item.level == level:
            list_items_of_level.append(item)
    for item in list_items_of_level:
        if not item.equip:
            useable.append(item)
        if item.equip == "Weapon":
            weapons.append(item)
        else:
            armor.append(item)
    armor_choice = random.choice(armor + [None])
    usable_choice = random.choice(useable + [None])
    weapons_choice = random.choice(weapons + [None])
    complete_list.extend([armor_choice, usable_choice, weapons_choice])
    return complete_list


def pick_up_item(item):
    if item in player1.current_room.loot:
        player1.current_room.loot.remove(item)
        player1.pick_up(item)
    elif item in player1.current_room.chest_loot:
        player1.current_room.chest_loot.remove(item)
        player1.pick_up(item)
    else:
        delay_print("There's no item by that name.")


class Static():
    _instances = set()

    def __init__(self, name, description, state):
        self.name = name
        self.description = description
        self.interactions = {}
        self.state = state
        self.loot = []
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


def add_interactions(thing, interaction_list, function):
    for command in interaction_list:
        thing.interactions[command] = function


# BED
bed = Static("bed", "This has been your bed all your life.", "in bed")


def get_out_of_bed():
    if bed.state == "out of bed":
        return delay_print("You're already out of bed.")
    delay_print("You get out of bed.")
    bed.description = "Mom would've wanted you to make the bed."
    bed.state = "out of bed"
    player1.state = None


def make_bed():
    delay_print("You made your bed")
    bed.description = "The bed is nicely made"


def get_in_bed():
    delay_print("You get into your bed.")
    bed.description = "Sometimes it's hard to get out of bed."
    bed.state = "in bed"
    player1.state = "in bed"


bed.interactions["get out"] = get_out_of_bed
bed.interactions["hop out"] = get_out_of_bed
bed.interactions["leave"] = get_out_of_bed
bed.interactions["make"] = make_bed
bed.interactions["tidy up"] = make_bed
bed.interactions["get in"] = get_in_bed
bed.interactions["jump in"] = get_in_bed
bed.interactions["go in"] = get_in_bed
bed.interactions["go to"] = get_in_bed

# BED

# LIGHT
bedroom_lamp = Static("lamp", "the light is off.", "off")
bedroom_light = Static("light", "the light is off.", "off")
light_interactions_on = ["turn on", "open"]
light_interactions_off = ["turn off", "close"]


def turn_on_light():
    if bedroom_lamp.state == "on":
        delay_print("The light is already on.")
    else:
        delay_print("You turned the light on.")
        bedroom_lamp.state = "on"
        bedroom_light.state = "on"
        bedroom_lamp.description = "The light is on."
        bedroom_light.description = "The light is on."


def turn_off_light():
    if bedroom_lamp.state == "off":
        delay_print("The light is already off.")
    else:
        delay_print("You turned the light off.")
        bedroom_lamp.state = "off"
        bedroom_light.state = "off"
        bedroom_lamp.description = "The light is on."
        bedroom_light.description = "The light is on."


add_interactions(bedroom_lamp, light_interactions_on, turn_on_light)
add_interactions(bedroom_light, light_interactions_on, turn_on_light)
add_interactions(bedroom_light, light_interactions_off, turn_off_light)
add_interactions(bedroom_lamp, light_interactions_off, turn_off_light)

# LIGHT

# CHESTS

class Chest(Static):

    def open_chest(self):
        if self.state == "open":
            return delay_print("It's already open.")
        else:
            self.state = "open"
            delay_print("You opened the " + self.name + ".")
            player1.current_room.chest_loot.extend(self.loot)
            if len(self.loot) == 1:
                delay_print("There's a " + self.loot[0].name + " in here!")
                self.loot = []
            if len(self.loot) > 1:
                print(self.name.capitalize() + ":")
                for item in self.loot:
                    print(item.name)
                self.loot = []
            if len(self.loot) < 1:
                return

    def put_in_chest(self, item):
        if self.state == "closed":
            return delay_print("It's closed.")
        else:
            if item in player1.inventory:
                player1.inventory.remove(item)
                player1.current_room.chest_loot.append(item)
                delay_print("You put the " + item.name + " in the " + self.name + ".")
            else:
                delay_print("You don't have this item.")

    def close_chest(self):
        if self.state == "closed":
            return delay_print("It's already closed.")
        else:
            self.state = "closed"
            delay_print("You closed the " + self.name + ".")
            if player1.current_room.chest_loot:
                for item in player1.current_room.chest_loot:
                    player1.current_room.chest_loot.remove(item)
                    self.loot.append(item)


# Dresser
bedroom_dresser = Chest("dresser", "It's a big wooden dresser.", "closed")
bedroom_dresser.loot.append(bedroom_key)
bedroom_dresser.loot.append(rusty_axe)


def open_dresser():
    bedroom_dresser.open_chest()
    if not player1.current_room.chest_loot:
        delay_print("It's full of clothes")


def put_in_dresser(item):
    bedroom_dresser.put_in_chest(item)


def close_dresser():
    bedroom_dresser.close_chest()


bedroom_dresser.interactions["open"] = open_dresser
bedroom_dresser.interactions["go through"] = open_dresser
bedroom_dresser.interactions["search"] = open_dresser
bedroom_dresser.interactions["open drawers"] = open_dresser
bedroom_dresser.interactions["put in"] = put_in_dresser
bedroom_dresser.interactions["place in"] = put_in_dresser
bedroom_dresser.interactions["close"] = close_dresser
bedroom_dresser.interactions["shut"] = close_dresser
bedroom_dresser.interactions["close drawers"] = close_dresser
bedroom_dresser.interactions["close drawer"] = close_dresser
# Dresser


all_statics = []
for obj in Static.getinstances():
    all_statics.append(obj)

all_things = all_items + all_statics
