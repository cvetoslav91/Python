from unittest import TestCase, main
# from Test_Worker import Worker


class WorkerTests(TestCase):
    def setUp(self):
        self.worker = Worker('John', 100, 10)

    def test_init_worker(self):
        self.assertEqual('John', self.worker.name)
        self.assertEqual(100, self.worker.salary)
        self.assertEqual(10, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_work_func_if_returns_exception(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as exception:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(exception.exception))

    def test_money_and_energy_after_work(self):
        self.worker.work()

        self.assertEqual(self.worker.money, 100)
        self.assertEqual(self.worker.energy, 9)

    def test_rest_func(self):
        self.worker.rest()

        self.assertEqual(11, self.worker.energy)

    def test_get_info_func(self):
        result = self.worker.get_info()
        self.assertEqual(f'{self.worker.name} has saved {self.worker.money} money.', result)


if __name__ == '__main__':
    main()
