import csv
import os


def parse_bookings(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            bookings = []
            for row in reader:
                bookings.append(row)
            return bookings
    except FileNotFoundError:
        print("Error: file not found")
    except csv.Error:
        print("Error: Failed to parse CSV file.")
        return []

def main():
    bookings = parse_bookings('boking.csv')
    if bookings:
        for booking in bookings:
            print(f"Booking ID: {booking['booking_id']}, User: {booking['user_id']}, Car: {booking['car_id']}, Date: {booking['date']}")

# if __name__ == "__main__":
main()