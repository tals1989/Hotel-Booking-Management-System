class Booking:
    def __init__(self, cust_id, room_id, arrival_date, departure_date, total_price):
        self.cust_id = cust_id
        self.room_id = room_id
        self.arrival_date = arrival_date
        self.departure_date = departure_date
        self.total_price = total_price

    def to_dict(self):
        return {
            "cust_id": self.cust_id,
            "room_id": self.room_id,
            "arrival_date": self.arrival_date,
            "departure_date": self.departure_date,
            "total_price": self.total_price
        }

class BookingManager:
    def __init__(self):
        self.bookings = []

    def load_bookings(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split('|')
                booking = Booking(*data)
                self.bookings.append(booking)

    def book_room(self, booking):
        self.bookings.append(booking)

    def cancel_booking(self, cust_id, room_id):
        self.bookings = [booking for booking in self.bookings if booking.cust_id != cust_id or booking.room_id != room_id]

    def display_all_bookings(self):
        for booking in self.bookings:
            print(booking.to_dict())

    def find_bookings_by_date(self, date):
        return [booking for booking in self.bookings if booking.arrival_date <= date <= booking.departure_date]

    def find_bookings_by_customer(self, cust_id):
        return [booking for booking in self.bookings if booking.cust_id == cust_id]
