class Room:
    def __init__(self, id, size, capacity, num_beds, type, price):
        self.id = id
        self.size = size
        self.capacity = capacity
        self.num_beds = num_beds
        self.type = type
        self.price = price

    def to_dict(self):
        return {
            "id": self.id,
            "size": self.size,
            "capacity": self.capacity,
            "num_beds": self.num_beds,
            "type": self.type,
            "price": self.price
        }

class RoomManager:
    def __init__(self):
        self.rooms = []

    def load_rooms(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split('|')
                room = Room(*data)
                self.rooms.append(room)

    def add_room(self, room):
        self.rooms.append(room)

    def remove_room(self, room_id):
        self.rooms = [room for room in self.rooms if room.id != room_id]

    def find_room_by_type(self, room_type):
        return [room for room in self.rooms if room.type == room_type]

    def find_room_by_id(self, room_id):
        for room in self.rooms:
            if room.id == room_id:
                return room

    def display_all_rooms(self):
        for room in self.rooms:
            print(room.to_dict())
