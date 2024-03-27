from unittest import TestCase, main
# from List import IntegerList


class TestIntegerList(TestCase):

    def setUp(self):
        self.list = IntegerList(1, 2, 3, 4.5, 'a')

    def test_init(self):
        self.assertEqual(self.list.get_data(), [1, 2, 3])

    def test_add_func_if_raises_error(self):

        with self.assertRaises(ValueError) as error:
            self.list.add('a')

        self.assertEqual("Element is not Integer", str(error.exception))

    def test_add_func_if_goes_ok(self):
        self.list.add(5)

        self.assertEqual(self.list.get_data(), [1, 2, 3, 5])

    def test_remove_index_func_if_invalid_index(self):
        with self.assertRaises(IndexError) as error:
            self.list.remove_index(5)

        self.assertEqual("Index is out of range", str(error.exception))

    def test_remove_index_func_if_goes_well(self):
        self.list.remove_index(1)

        self.assertEqual(self.list.get_data(), [1, 3])

    def test_get_func_if_invalid_index(self):
        with self.assertRaises(IndexError) as error:
            self.list.get(5)

        self.assertEqual("Index is out of range", str(error.exception))

    def test_get_func_if_goes_well(self):
        self.assertEqual(self.list.get(1), 2)

    def test_insert_func_if_invalid_index(self):
        with self.assertRaises(IndexError) as error:
            self.list.insert(5, 'a')

        self.assertEqual("Index is out of range", str(error.exception))

    def test_insert_func_if_el_is_not_int(self):
        with self.assertRaises(ValueError) as error:
            self.list.insert(1, 'a')

        self.assertEqual("Element is not Integer", str(error.exception))

    def test_insert_if_goes_well(self):
        self.list.insert(2, 10)

        self.assertEqual(self.list.get_data(), [1, 2, 10, 3])

    def test_get_biggest_func(self):
        self.assertEqual(self.list.get_biggest(), 3)

    def test_get_index_func(self):
        result = self.list.get_index(1)
        self.assertEqual(0, result)

if __name__ == '__main__':
    main()