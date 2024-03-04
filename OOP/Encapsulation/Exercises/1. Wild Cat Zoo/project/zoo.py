class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        free_space = self.__animal_capacity > len(self.animals)
        enough_budget = self.__budget >= price
        if not free_space:
            return "Not enough space for animal"
        if not enough_budget:
            return "Not enough budget"
        self.animals.append(animal)
        self.__budget -= price
        type = animal.__class__.__name__
        return f"{animal.name} the {type} added to the zoo"

    def hire_worker(self, worker):
        free_space = self.__workers_capacity > len(self.workers)
        if not free_space:
            return "Not enough space for worker"
        self.workers.append(worker)
        type = worker.__class__.__name__
        return f"{worker.name} the {type} hired successfully"

    def fire_worker(self, worker_name: str):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker.name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salary = sum([worker.salary for worker in self.workers])
        if self.__budget >= total_salary:
            self.__budget -= total_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_sum = sum([animal.money_for_care for animal in self.animals])
        if self.__budget >= total_sum:
            self.__budget -= total_sum
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [animal for animal in self.animals if animal.__class__.__name__ == 'Lion']
        tigers = [animal for animal in self.animals if animal.__class__.__name__ == 'Tiger']
        cheetahs = [animal for animal in self.animals if animal.__class__.__name__ == 'Cheetah']
        return f"You have {len(self.animals)} animals\n" + f"----- {len(lions)} Lions:\n" + \
            '\n'.join([lion.__repr__() for lion in lions]) + \
            f"\n----- {len(tigers)} Tigers:\n" + \
            '\n'.join([tiger.__repr__() for tiger in tigers]) + \
            f"\n----- {len(cheetahs)} Cheetahs:\n" + \
            '\n'.join([cheetah.__repr__() for cheetah in cheetahs])

    def workers_status(self):
        keepers = [worker for worker in self.workers if worker.__class__.__name__ == 'Keeper']
        caretakers = [worker for worker in self.workers if worker.__class__.__name__ == 'Caretaker']
        vets = [worker for worker in self.workers if worker.__class__.__name__ == 'Vet']
        return f"You have {len(self.workers)} workers\n" + f"----- {len(keepers)} Keepers:\n" + \
            '\n'.join([keeper.__repr__() for keeper in keepers]) + \
            f"\n----- {len(caretakers)} Caretakers:\n" + \
            '\n'.join([caretaker.__repr__() for caretaker in caretakers]) + \
            f"\n----- {len(vets)} Vets:\n" + \
            '\n'.join([vet.__repr__() for vet in vets])




