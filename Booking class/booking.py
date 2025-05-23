from utils import validate_id

class Booking:
    # booking_id, user_id, car_id = 0, 0, 0
    def __init__(self, booking_id, user_id, car_id):
        self.booking_id = validate_id(booking_id, "Booking ID")
        self.user_id = validate_id(user_id, "User ID")
        self.car_id = validate_id(car_id, "Car ID")
        self.valid = all([self.booking_id, self.user_id, self.car_id])

    def display(self):
        if self.valid:
            print(f"Booking: {self.booking_id}, User: {self.user_id}, Car: {self.car_id}")
        else:
            print("Invalid booking")

class ConfirmeBooking(Booking):
    def __init__(self, booking_id, user_id, car_id, status):
        super().__init__(booking_id, user_id, car_id)
        self.status = status if self.valid else "Invalid"

    def display(self):
        if self.valid:
            print(f"Confirmed Booking ID: {self.booking_id}, User ID: {self.user_id}, Car ID: {self.car_id}, Status: {self.status}")
        else:
            print("Invalid confirmed booking: Cannot display details.")