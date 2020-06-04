from Rooms import *

class Map:
    def __init__(self, name, directed=False):
        self.name = name
        self.directed = directed
        self.map_dict = {}
        self.starting_room = None
        self.current_room = None
        self.connections = {}
        self.functions = {}


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
        player1.current_room = room

    def change_rooms(self, room, action=None):
        if self.current_room.connections[room.name] == "Unlocked":
            self.current_room = room
            player1.current_room = room
            delay_print("You " + action + " " + room.name + ".")
        else:
            print(room.name + " is locked")

    def leave_room(self):
        self.peek_next_rooms(self.current_room)


#WORLD MAP
world_map = Map("World Map")
#HOUSE
world_map.add_room(bedroom)
world_map.add_room(bathroom)
world_map.add_room(kitchen)
world_map.add_room(living_room)
world_map.add_room(front_door)
world_map.add_connection(bedroom, living_room)
world_map.add_connection(living_room, bathroom)
world_map.add_connection(living_room, kitchen)
world_map.add_connection(living_room, front_door, "Locked")




#FUNCTIONS
def change_rooms(room, action):
    if world_map.current_room == room:
        return delay_print("You're already in that room.")
    if room.name not in world_map.current_room.get_connections():
        if room in world_map.map_dict.values():
            return delay_print("You can't get there from here")
        else:
            return print("HUH?")
    else:
        world_map.change_rooms(room, action)

def leave_room():
    delay_print("Where would you like to go?")
    world_map.peek_next_rooms(world_map.current_room)
    room = input("> ")
    change_rooms(room)


change_room_commands = ("move to", "go to", "enter", "walk to", "jump to", "waddle to", "fly to", "go into", "move into", "walk into", "fly into")
world_map.functions[change_room_commands] = change_rooms
leave_room_commands = ("leave", "exit", "change rooms")
world_map.functions[leave_room_commands] = leave_room
room_commands = [change_room_commands, leave_room_commands]


