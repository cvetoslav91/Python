from unittest import TestCase, main
from project.mammal import Mammal

class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal('Joe', 'Lion', 'Grr')

    def test_init(self):
        self.assertEqual('Joe', self.mammal.name)
        self.assertEqual('Lion', self.mammal.type)
        self.assertEqual('Grr', self.mammal.sound)
        self.assertEqual('animals', self.mammal.get_kingdom())

    def test_sounds(self):
        result = self.mammal.make_sound()
        self.assertEqual('Joe makes Grr', result)

    def test_info_function(self):
        result = self.mammal.info()
        self.assertEqual('Joe is of type Lion', result)


if __name__ == '__main__':
    main()
