class Room:
    def __init__(self, name):
        self.name = name
        self.connections = {}
        self.loot = []
        self.characters = []
        self.things = []

    def add_connection(self, room):
        self.connections[room] = True

    def get_connections(self):
        return list(self.connections.keys())