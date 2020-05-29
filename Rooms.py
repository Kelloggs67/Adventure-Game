from Objects import *

class Room:
    def __init__(self, name):
        self.name = name
        self.connections = {}
        self.objects = {}
        self.characters = []
        self.loot = []
        self.description = None

    def add_connection(self, room, weight="Unlocked"):
        self.connections[room] = weight

    def get_connections(self):
        return list(self.connections.keys())

    def place_object(self, object):
        self.objects[object.name] = object

bedroom = Room("your bedroom")
living_room = Room("The Living Room")
bathroom = Room("The Bathroom")
kitchen = Room("The Kitchen")
front_door = Room("The Front Door")

bedroom.place_object(bed)