#Environments will capture the map, characters, items, furniture, etc. at certain moments defined by events.
from Map import *
from Events import *
from Objects import *


class Environment:
    def __init__(self, map):
        self.map = map
        self.characters = {}
        self.loot = {}
        self.objects = {}


    def put_loot_in_room(self, room, loot):
        self.loot[room] = loot

    def remove_loot(self, room, loot_name=None):
        if loot_name:
            self.loot[room].pop(loot_name)
        else:
            self.loot[room] = []

    def put_characters_in_room(self, room, characters):
        self.characters[room] = characters
        pass

    def remove_characters(self, room, character_name=None):
        if character_name:
            self.characters[room].pop(character_name)
        else:
            self.characters[room] = []

    def put_objects_in_room(self, room, objects):
        self.objects[room] = objects

    def remove_loot(self, room, object_name=None):
        if object_name:
            self.objects[room].pop(object_name)
        else:
            self.objects[room] = []


env_house = Environment(build_house())

