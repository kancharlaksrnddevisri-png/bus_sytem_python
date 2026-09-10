from datetime import datetime

buses = []
bookings = []
booking_counter = 1001


# ==========================================
# 1. ADD BUS
# ==========================================

def add_buses():
    print("\n========== ADD BUS ==========")

    bus_number = input("Enter Bus Number: ")
    bus_name = input("Enter Bus Name: ")
    from_address = input("From: ")
    to_address = input("To: ")
    departure = input("Departure Time: ")
    arrival = input("Arrival Time: ")
    price = float(input("Ticket Price: "))
    total_seats = int(input("Total Seats: "))

    bus = {
        "bus_number": bus_number,
        "bus_name": bus_name,
        "from_address": from_address,
        "to_address": to_address,
        "departure_time": departure,
        "arrival_time": arrival,
        "ticket_price": price,
        "total_seats": total_seats,
        "available_seats": list(range(1, total_seats + 1))
    }

    buses.append(bus)

    print("\nBus added successfully!")


# ==========================================
# 2. VIEW BUSES
# ==========================================

def view_buses():
    print("\n========== ALL BUSES ==========")

    if len(buses) == 0:
        print("No buses available.")
        return

    for bus in buses:
        print("\nBus Number :", bus["bus_number"])
        print("Bus Name   :", bus["bus_name"])
        print("From       :", bus["from_address"])
        print("To         :", bus["to_address"])
        print("Departure  :", bus["departure_time"])
        print("Arrival    :", bus["arrival_time"])
        print("Price      : ₹", bus["ticket_price"])
        print("Total Seats:", bus["total_seats"])
        print("Available  :", len(bus["available_seats"]))


# ==========================================
# 3. SEARCH BUS
# ==========================================

def search_buses():
    print("\n============== SEARCH BUS ===============")

    from_addr = input("From: ")
    to_addr = input("To: ")

    found = False

    for bus in buses:
        if (bus["from_address"].lower() == from_addr.lower()
                and bus["to_address"].lower() == to_addr.lower()):

            found = True

            print("\nBus No          :", bus["bus_number"])
            print("Bus Name        :", bus["bus_name"])
            print("Departure       :", bus["departure_time"])
            print("Arrival         :", bus["arrival_time"])
            print("Price           : ₹", bus["ticket_price"])
            print("Available Seats :", len(bus["available_seats"]))

    if not found:
        print("\nThere are no available buses.")


# ==========================================
# 4. VIEW AVAILABLE SEATS
# ==========================================

def available_seats():
    print("\n=============== VIEW AVAILABLE SEATS ============")

    bus_number = input("Enter bus number to view the available seats: ")

    bus = None

    for b in buses:
        if b["bus_number"].lower() == bus_number.lower():
            bus = b
            break

    if bus is None:
        print("Bus not found.")
        return

    if len(bus["available_seats"]) == 0:
        print("No seats available.")
        return

    print("\nAvailable Seats:")

    count = 0

    for seat in bus["available_seats"]:
        print(f"{seat:02}", end="   ")

        count += 1

        if count % 5 == 0:
            print()

    print()


# ==========================================
# 5. BOOK TICKET
# ==========================================

def book_ticket():
    global booking_counter

    print("\n========== BOOK TICKET ==========")

    passenger_name = input("Passenger Name: ")
    age = int(input("Age: "))
    phone = input("Phone Number: ")
    bus_number = input("Bus Number: ")

    bus = None

    for b in buses:
        if b["bus_number"].lower() == bus_number.lower():
            bus = b
            break

    if bus is None:
        print("Bus not found.")
        return

    if len(bus["available_seats"]) == 0:
        print("Sorry, no seats available.")
        return

    print("\nAvailable Seats:")

    count = 0

    for seat in bus["available_seats"]:
        print(f"{seat:02}", end="   ")

        count += 1

        if count % 5 == 0:
            print()

    print()

    try:
        seat_number = int(input("\nSeat Number: "))
    except ValueError:
        print("Invalid seat number.")
        return

    if seat_number not in bus["available_seats"]:
        print("Seat is not available.")
        return

    # Remove seat from available seats
    bus["available_seats"].remove(seat_number)

    booking_id = "B" + str(booking_counter)
    booking_counter += 1

    booking = {
        "booking_id": booking_id,
        "passenger": passenger_name,
        "age": age,
        "phone": phone,
        "bus_number": bus["bus_number"],
        "from": bus["from_address"],
        "to": bus["to_address"],
        "seat": seat_number,
        "amount": bus["ticket_price"],
        "status": "Confirmed",
        "date": datetime.now().strftime("%d-%m-%Y")
    }

    bookings.append(booking)

    # ==========================================
    # TICKET
    # ==========================================

    print("\n")
    print("========== BUS TICKET ==========")
    print()
    print("Booking ID :", booking["booking_id"])
    print("Passenger  :", booking["passenger"])
    print("Bus No     :", booking["bus_number"])
    print("From       :", booking["from"])
    print("To         :", booking["to"])
    print("Date       :", booking["date"])
    print(f"Seat No    : {booking['seat']:02}")
    print("Amount     : ₹", booking["amount"])
    print()
    print("================================")

    print("\nTicket booked successfully!")


# ==========================================
# 6. CANCEL TICKET
# ==========================================

def cancel_tickets():

    print("\n========== CANCEL TICKET ==========")

    booking_id = input("Enter Booking ID: ")

    booking = None

    for b in bookings:
        if b["booking_id"].lower() == booking_id.lower():
            booking = b
            break

    if booking is None:
        print("Booking ID not found.")
        return

    if booking["status"] == "Cancelled":
        print("Ticket is already cancelled.")
        return

    # Find bus
    bus = None

    for b in buses:
        if b["bus_number"].lower() == booking["bus_number"].lower():
            bus = b
            break

    # Return seat to available seats
    if bus is not None:
        bus["available_seats"].append(booking["seat"])
        bus["available_seats"].sort()

    booking["status"] = "Cancelled"

    print("\nTicket cancelled successfully.")
    print(f"Seat {booking['seat']:02} is now available.")


# ==========================================
# 7. VIEW BOOKINGS
# ==========================================

def view_bookings():

    print("\n========== BOOKINGS ==========")

    if len(bookings) == 0:
        print("No bookings available.")
        return

    for booking in bookings:

        print("\nBooking ID :", booking["booking_id"])
        print("Passenger  :", booking["passenger"])
        print("Bus No     :", booking["bus_number"])
        print(f"Seat       : {booking['seat']:02}")
        print("Status     :", booking["status"])

    print("\n==============================")


# ==========================================
# MAIN MENU
# ==========================================

while True:

    print("\n")
    print("================================")
    print("      BUS RESERVATION SYSTEM")
    print("================================")

    print("1. Add Bus")
    print("2. View Buses")
    print("3. Search Bus")
    print("4. View Available Seats")
    print("5. Book Ticket")
    print("6. Cancel Ticket")
    print("7. View Bookings")
    print("8. Exit")

    print("================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_buses()

    elif choice == "2":
        view_buses()

    elif choice == "3":
        search_buses()

    elif choice == "4":
        available_seats()

    elif choice == "5":
        book_ticket()

    elif choice == "6":
        cancel_tickets()

    elif choice == "7":
        view_bookings()

    elif choice == "8":
        print("\nThank you for using Bus Reservation System!")
        break

    else:
        print("\nInvalid choice. Please try again.")
