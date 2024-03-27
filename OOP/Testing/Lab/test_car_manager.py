from unittest import TestCase, main
# from Car_Manager import Car


class TestCar(TestCase):
    def setUp(self):
        self.car = Car("VW", "Golf", 5, 50)

    def test_init_car(self):
        self.assertEqual('VW', self.car.make)
        self.assertEqual('Golf', self.car.model)
        self.assertEqual(5, self.car.fuel_consumption)
        self.assertEqual(50, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_if_empty_string(self):
        with self.assertRaises(Exception) as error:
            self.car.make = ''

        self.assertEqual("Make cannot be null or empty!", str(error.exception))

    def test_model_if_empty_string(self):
        with self.assertRaises(Exception) as error:
            self.car.model = ''

        self.assertEqual("Model cannot be null or empty!", str(error.exception))

    def test_fuel_consumption_if_negative(self):
        with self.assertRaises(Exception) as error:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(error.exception))

    def test_fuel_capacity_if_negative(self):
        with self.assertRaises(Exception) as error:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(error.exception))

    def test_fuel_amount_if_negative(self):
        with self.assertRaises(Exception) as error:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(error.exception))

    def test_refuel_if_fuel_is_negative_or_zero(self):
        with self.assertRaises(Exception) as error:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(error.exception))

    def test_fuel_amount_if_positive_fuel(self):
        self.car.refuel(60)
        self.assertEqual(50, self.car.fuel_amount)

    def test_drive_if_not_enough_fuel(self):
        with self.assertRaises(Exception) as exception:
            self.car.drive(100)

        self.assertEqual("You don't have enough fuel to drive!", str(exception.exception))

    def test_drive_if_ok(self):
        self.car.fuel_amount = 50
        self.car.drive(100)
        self.assertEqual(45, self.car.fuel_amount)


if __name__ == "__main__":
    main()
