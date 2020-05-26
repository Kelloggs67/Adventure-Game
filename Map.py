from Rooms import *

class Map:
    def __init__(self, directed=False):
        self.directed = directed
        self.map_dict = {}

    def add_room(self, room):
        self.map_dict[room.name] = room

bedroom = Room("Bedroom")
living_room = Room("Living Room")
