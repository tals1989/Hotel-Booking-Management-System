from rooms import Room, RoomManager
from customers import Customer, CustomerManager
from bookings import Booking, BookingManager

def display_menu():
    print("=== Menu ===")
    print("1. Load rooms from file")
    print("2. Add a new room")
    print("3. Add a new customer")
    print("4. Book a room")
    print("5. Cancel booking")
    print("6. Display all rooms")
    print("7. Display all customers")
    print("8. Display all bookings")
    print("9. Display booked rooms for a specific date")
    print("10. Display available rooms for a specific date")
    print("11. Find room by type")
    print("12. Find room by number")
    print("13. Find customer by name")
    print("14. Remove room")
    print("15. Remove customer")
    print("0. Exit")

def add_new_room(room_manager):
    print("Enter room details:")
    id = input("ID: ")
    size = input("Size: ")
    capacity = input("Capacity: ")
    num_beds = input("Number of beds: ")
    type = input("Type (Basic/Deluxe/Suite): ")
    price = input("Price: ")
    room = Room(id, size, capacity, num_beds, type, price)
    room_manager.add_room(room)
    print("Room added successfully!")

def main():
    room_manager = RoomManager()
    customer_manager = CustomerManager()
    booking_manager = BookingManager()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            room_manager.load_rooms("Rooms.txt")
            room_manager.display_all_rooms()
        elif choice == '2':
            add_new_room(room_manager)
        elif choice == '3':
            # Implement add new customer functionality
            pass
        elif choice == '4':
            # Implement book a room functionality
            pass
        elif choice == '5':
            # Implement cancel booking functionality
            pass
        elif choice == '6':
            room_manager.display_all_rooms()
        elif choice == '7':
            customer_manager.display_all_customers()
        elif choice == '8':
            booking_manager.display_all_bookings()
        elif choice == '9':
            # Implement display booked rooms for a specific date functionality
            pass
        elif choice == '10':
            # Implement display available rooms for a specific date functionality
            pass
        elif choice == '11':
            # Implement find room by type functionality
            pass
        elif choice == '12':
            # Implement find room by number functionality
            pass
        elif choice == '13':
            # Implement find customer by name functionality
            pass
        elif choice == '14':
            # Implement remove room functionality
            pass
        elif choice == '15':
            # Implement remove customer functionality
            pass
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
