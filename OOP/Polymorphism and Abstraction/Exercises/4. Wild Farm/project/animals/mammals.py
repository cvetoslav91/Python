from project.animals.animal import Mammal

from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal):
    @staticmethod
    def make_sound():
        return 'Squeak'

    @property
    def eaten_foods(self):
        return [Vegetable, Fruit]

    @property
    def increase_of_weight(self):
        return 0.1


class Dog(Mammal):
    @staticmethod
    def make_sound():
        return "Woof!"

    @property
    def eaten_foods(self):
        return [Meat]

    @property
    def increase_of_weight(self):
        return 0.4


class Cat(Mammal):
    @staticmethod
    def make_sound():
        return "Meow"

    @property
    def eaten_foods(self):
        return [Meat, Vegetable]

    @property
    def increase_of_weight(self):
        return 0.3


class Tiger(Mammal):
    @staticmethod
    def make_sound():
        return "ROAR!!!"

    @property
    def eaten_foods(self):
        return [Meat]

    @property
    def increase_of_weight(self):
        return 1
