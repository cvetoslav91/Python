from project.next_id_mixin import NextIdMixin


class Subscription(NextIdMixin):
    id = 0
    def __init__(self, date: str, customer_id: str, trainer_id: str, exercise_id: str):
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id
        self.id = self.get_next_id()

    def __repr__(self):
        return f"Subscription <{Subscription.id}> on {self.date}"