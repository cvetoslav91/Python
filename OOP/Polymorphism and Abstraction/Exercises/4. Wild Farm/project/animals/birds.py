from project.animals.animal import Bird

from project.food import Vegetable, Fruit, Meat, Seed


class Owl(Bird):
    @staticmethod
    def make_sound():
        return 'Hoot Hoot'

    @property
    def eaten_foods(self):
        return [Meat]

    @property
    def increase_of_weight(self):
        return 0.25




class Hen(Bird):
    @staticmethod
    def make_sound():
        return 'Cluck'

    @property
    def eaten_foods(self):
        return [Vegetable, Fruit, Meat, Seed]

    @property
    def increase_of_weight(self):
        return 0.35
