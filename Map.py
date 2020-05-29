from Rooms import *

class Map:
    def __init__(self, name, directed=False):
        self.name = name
        self.directed = directed
        self.map_dict = {}
        self.starting_room = None
        self.current_room = None

    def add_room(self, room):
        self.map_dict[room.name] = room

    def add_connection(self, from_room, to_room, weight="Unlocked"):
        self.map_dict[from_room.name].add_connection(to_room.name, weight)
        if not self.directed:
            self.map_dict[to_room.name].add_connection(from_room.name, weight)

    def remove_connection(self, from_room, to_room):
        pass


    def find_path(self, start_room, end_room):
        start = [start_room.name]
        seen = {}
        count = 1
        while len(start) > 0:
            current_room = start.pop(0)
            seen[current_room] = True
            print(str(count) + ": " + current_room)
            if current_room == end_room.name:
                return True
            else:
                rooms_to_visit = set(self.map_dict[current_room].connections.keys())
                start += [room for room in rooms_to_visit if room not in seen]
                count += 1
        return False

    def print_map(self):
        print("    " + self.name.upper() + " LAYOUT")
        for room_key in self.map_dict:
            print("{0} connected to ".format(room_key))
            room = self.map_dict[room_key]
            for adjacent_room in room.connections:
                if room.connections[adjacent_room] == "Unlocked":
                    print("=>{0}".format(adjacent_room))
                else:
                    print("=>" + adjacent_room + " [X]")
            print("")
        print("")

    def peek_next_rooms(self, current_room):
        print(current_room.name + " connected to")
        for adjacent_room in current_room.get_connections():
            if current_room.connections[adjacent_room] == "Unlocked":
                print("=>" + adjacent_room)
            else:
                print("=>" + adjacent_room + " [X]")
        print("")

    def set_starting_room(self, room):
        self.starting_room = room
        self.current_room = room

    def change_rooms(self, room):
        if self.current_room.connections[room] == "Unlocked":
            self.current_room = room
        else:
            print(room.name + "is locked")


class WorldMap(Map):
    pass


house = Map("House")
house.add_room(bedroom)
house.add_room(bathroom)
house.add_room(kitchen)
house.add_room(living_room)
house.add_room(front_door)
house.add_connection(bedroom, living_room)
house.add_connection(living_room, bathroom)
house.add_connection(living_room, kitchen)
house.add_connection(living_room, front_door, "Locked")
