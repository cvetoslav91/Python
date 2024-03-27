from unittest import TestCase, main
# from Test_Cat import Cat

class CatTests(TestCase):

    def setUp(self):
        self.cat = Cat('Murcho')

    def test_init(self):
        self.assertEqual('Murcho', self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_if_eat_func_raises_exception(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as exception:
            self.cat.eat()

        self.assertEqual('Already fed.', str(exception.exception))

    def test_eat_func_when_goes_ok(self):
        self.cat.eat()

        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(1, self.cat.size)

    def test_sleep_if_not_fed(self):
        self.cat.fed = False

        with self.assertRaises(Exception) as exception:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(exception.exception))

    def test_sleep_if_goes_well(self):
        self.cat.sleepy = True
        self.cat.fed = True

        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)

if __name__ == '__main__':
    main()