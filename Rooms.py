from Objects import *


class Room:
    def __init__(self, name):
        self.name = name
        self.connections = {}
        self.objects = {}
        self.key = {}
        self.characters = []
        self.chest_loot = []
        self.loot = []
        self.description = None

    def add_connection(self, room, weight="Unlocked", key=None):
        self.connections[room] = weight
        self.key[room] = key

    def get_connections(self):
        return list(self.connections.keys())

    def place_object(self, object):
        self.objects[object.name] = object


bedroom = Room("your bedroom")
living_room = Room("the living room")
bathroom = Room("the bathroom")
kitchen = Room("the kitchen")
front_door = Room("the front door")

bedroom.place_object(bed)
bedroom.place_object(bedroom_dresser)
bedroom.place_object(bedroom_lamp)
bedroom.place_object(bedroom_light)
bedroom.description = "All that is left in your room is the lamp next to your bed and your dresser. "


class Building:
    def __init__(self, name, rooms, doors):
        self.name = name
        self.rooms = rooms
        self.connections = {}
        self.doors = doors

    def add_connection(self, building, weight=0):
        self.connections[building] = weight

    def get_connections(self):
        return list(self.connections.keys())


house = Building("your house", [bedroom, living_room, bathroom, kitchen], [front_door])
