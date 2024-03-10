from project.next_id_mixin import NextIdMixin


class Customer(NextIdMixin):
    id = 0
    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.id = self.get_next_id()

    def __repr__(self):
        return f"Customer <{Customer.id}> {self.name}; Address: {self.address}; Email: {self.email}"