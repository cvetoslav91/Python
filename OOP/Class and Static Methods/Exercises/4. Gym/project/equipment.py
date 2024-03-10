from project.customer import Customer
from project.next_id_mixin import NextIdMixin


class Equipment(NextIdMixin):
    id = 0
    def __init__(self, name: str):
        self.name = name
        self.id = self.get_next_id()


    def __repr__(self):
        return f"Equipment <{Equipment.id}> {self.name}"

