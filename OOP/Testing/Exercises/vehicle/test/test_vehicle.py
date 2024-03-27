from unittest import TestCase, main
from project.vehicle import Vehicle

class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(5.5, 100)

    def test_init(self):
        self.assertEqual(5.5, self.vehicle.fuel)
        self.assertEqual(5.5, self.vehicle.capacity)
        self.assertEqual(100, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_function_expect_error(self):
        with self.assertRaises(Exception) as exception:
            self.vehicle.drive(1000)

        self.assertEqual("Not enough fuel", str(exception.exception))

    def test_drive_function_if_ok(self):
        self.vehicle.drive(2)

        self.assertEqual(3, self.vehicle.fuel)

    def test_refuel_function_expect_error(self):
        with self.assertRaises(Exception) as exception:
            self.vehicle.refuel(1)

        self.assertEqual("Too much fuel", str(exception.exception))

    def test_refuel_function_if_goes_ok(self):
        self.vehicle.fuel = 0
        self.vehicle.refuel(2)

        self.assertEqual(2, self.vehicle.fuel)

    def test_str_func(self):
        result = f"The vehicle has 100 " \
               f"horse power with 5.5 fuel left and 1.25 fuel consumption"

        self.assertEqual(result, str(self.vehicle))

if __name__ == "__main__":
    main()