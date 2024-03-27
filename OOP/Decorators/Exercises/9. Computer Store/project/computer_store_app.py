from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    valid_computers = {
        'Desktop Computer': DesktopComputer,
        'Laptop': Laptop
    }

    def __init__(self):
        self.warehouse = []
        self.profits = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        try:
            computer = self.valid_computers[type_computer](manufacturer, model)
        except KeyError:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        result = computer.configure_computer(processor, ram)
        self.warehouse.append(computer)

        return result

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        for computer in self.warehouse:
            if computer.price <= client_budget:
                if computer.processor == wanted_processor and computer.ram >= wanted_ram:
                    self.profits += client_budget - computer.price
                    self.warehouse.remove(computer)
                    return f"{computer} sold for {client_budget}$."
        raise Exception("Sorry, we don't have a computer for you.")

csa = ComputerStoreApp()
csa.build_computer('Desktop Computer', 'Apple', 'MacBook Pro', 'Intel Core i5-12600K', 128)
csa.build_computer('Laptop', 'Apple', 'MacBook Pro', 'Apple M1 Pro', 64)
csa.sell_computer(1810, 'Apple M1 Pro', 64)
print(csa.warehouse)
print(csa.profits)