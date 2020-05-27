class Room:
    def __init__(self, name):
        self.name = name
        self.connections = {}

    def add_connection(self, room, weight="Unlocked"):
        self.connections[room] = weight

    def get_connections(self):
        return list(self.connections.keys())

bedroom = Room("Your Bedroom")
living_room = Room("The Living Room")
bathroom = Room("The Bathroom")
kitchen = Room("The Kitchen")
front_door = Room("The Front Door")