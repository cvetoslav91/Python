from collections import deque
from unittest import TestCase, main

from project.railway_station import RailwayStation


class TestRailway(TestCase):
    def setUp(self):
        self.railway = RailwayStation('Mezdra')
        self.railway_with_trains = RailwayStation('Vratsa')
        self.railway_with_trains.arrival_trains.append('1')
        self.railway_with_trains.arrival_trains.append('2')
        self.railway_with_trains.departure_trains.append('3')

    def test_station_name(self):
        self.assertEqual('Mezdra', self.railway.name)

    def test_name_expect_error(self):

        with self.assertRaises(ValueError) as ve:
            self.railway.name = ''

        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_arrival_on_board_method(self):
        self.railway.new_arrival_on_board('1')
        self.railway.new_arrival_on_board('2')
        self.assertEqual(deque(['1', '2']), self.railway.arrival_trains)

    def test_arrival_of_train_expect_error(self):
        result = self.railway_with_trains.train_has_arrived('3')
        self.assertEqual("There are other trains to arrive before 3.", result)

    def test_arrival_happy_case(self):
        result = self.railway_with_trains.train_has_arrived('1')
        self.assertEqual("1 is on the platform and will leave in 5 minutes.", result)
        self.assertEqual(deque(['3', '1']), self.railway_with_trains.departure_trains)
        self.assertEqual(deque(['2']), self.railway_with_trains.arrival_trains)

    def test_train_has_left_method_if_true(self):
        result = self.railway_with_trains.train_has_left('3')
        self.assertEqual(deque([]), self.railway_with_trains.departure_trains)
        self.assertEqual(True, result)

    def test_train_has_left_method_if_false(self):
        result = self.railway_with_trains.train_has_left('2')
        self.assertEqual(False, result)

if __name__ == '__main__':
    main()
