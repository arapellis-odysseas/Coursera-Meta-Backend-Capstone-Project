from django.test import TestCase
from restaurant.models import Menu, Booking


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")

class BookingItemTest(TestCase):
    def test_get_item(self):
        item = Booking.objects.create(name="John", no_of_guests=2, bookingDate="2022-01-01")
        self.assertEqual(str(item), "John - 2022-01-01")