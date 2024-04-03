from unittest import TestCase, main

from project.climbing_robot import ClimbingRobot


class RobotTest(TestCase):
    ALLOWED_CATEGORIES = ['Mountain', 'Alpine', 'Indoor', 'Bouldering']

    def setUp(self):
        self.robot = ClimbingRobot('Mountain', 'Indoor', 100, 200)

        self.robot_with_software = ClimbingRobot('Mountain', 'Indoor', 100, 200)
        self.robot_with_software.installed_software = [
            {'name': 'JS', 'capacity_consumption': 50, 'memory_consumption': 49},
            {'name': 'HTML', 'capacity_consumption': 49, 'memory_consumption': 51},
        ]

    def test_correct_init(self):
        self.assertEqual('Mountain', self.robot.category)
        self.assertEqual('Indoor', self.robot.part_type)
        self.assertEqual(100, self.robot.capacity)
        self.assertEqual(200, self.robot.memory)
        self.assertEqual([], self.robot.installed_software)

    def test_wrong_category_init(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = 'category'

        self.assertEqual(f"Category should be one of {self.ALLOWED_CATEGORIES}", str(ve.exception))

    def test_get_used_capacity_expect_success(self):
        expected_result = sum(s['capacity_consumption'] for s in self.robot_with_software.installed_software)
        result = self.robot_with_software.get_used_capacity()

        self.assertEqual(expected_result, result)

    def test_get_available_capacity_expect_success(self):
        expected_result = self.robot.capacity - sum(s['capacity_consumption'] for s in self.robot_with_software.installed_software)
        result = self.robot_with_software.get_available_capacity()

        self.assertEqual(result, expected_result)

    def test_get_used_memory_expect_success(self):
        expected_result = sum(s['memory_consumption'] for s in self.robot_with_software.installed_software)
        result = self.robot_with_software.get_used_memory()

        self.assertEqual(expected_result, result)

    def test_get_available_memory_expect_success(self):
        expected_result = self.robot.memory - sum(s['memory_consumption'] for s in self.robot_with_software.installed_software)
        result = self.robot_with_software.get_available_memory()

        self.assertEqual(result, expected_result)

    def test_install_software_if_installed_successfully(self):
        result = self.robot.install_software({'name': 'JS', 'capacity_consumption': 100, 'memory_consumption': 200})
        self.assertEqual("Software 'JS' successfully installed on Mountain part.", result)
        self.assertEqual([{'name': 'JS', 'capacity_consumption': 100, 'memory_consumption': 200}], self.robot.installed_software)

    def test_install_software_if_not_installed_successfully_because_of_not_enough_capacity(self):
        result = self.robot.install_software({'name': 'JS', 'capacity_consumption': 110, 'memory_consumption': 100})
        self.assertEqual("Software 'JS' cannot be installed on Mountain part.", result)
        self.assertEqual([], self.robot.installed_software)

    def test_install_software_not_successfully_because_of_no_memory(self):
        result = self.robot.install_software({'name': 'JS', 'capacity_consumption': 100, 'memory_consumption': 210})
        self.assertEqual("Software 'JS' cannot be installed on Mountain part.", result)
        self.assertEqual(self.robot.installed_software, [])

    def test_if_installed_successfully_with_less_values(self):
        result = self.robot.install_software({'name': 'JS', 'capacity_consumption': 10, 'memory_consumption': 10})
        self.assertEqual("Software 'JS' successfully installed on Mountain part.", result)
        self.assertEqual([{'name': 'JS', 'capacity_consumption': 10, 'memory_consumption': 10}],
                         self.robot.installed_software)

    def test_failed_software_install_both_values_greater(self):
        result = self.robot_with_software.install_software({'name': 'JS', 'capacity_consumption': 110, 'memory_consumption': 220})
        self.assertEqual("Software 'JS' cannot be installed on Mountain part.", result)
        self.assertEqual(self.robot.installed_software, [])


if __name__ == '__main__':
    main()
