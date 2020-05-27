class Room:
    def __init__(self, name):
        self.name = name
        self.connections = {}
        self.loot = []
        self.characters = []
        self.things = []

    def add_connection(self, room, weight="Unlocked"):
        self.connections[room] = weight

    def get_connections(self):
        return list(self.connections.keys())

bedroom = Room("Bedroom")
living_room = Room("Living Room")
bathroom = Room("Bathroom")
kitchen = Room("Kitchen")
front_door = Room("Front Door")