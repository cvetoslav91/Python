from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    MAX_OXYGEN_LEVEL = 120

    def __init__(self, name):
        super().__init__(name, oxygen_level=FreeDiver.MAX_OXYGEN_LEVEL)

    def renew_oxy(self):
        self.oxygen_level = self.MAX_OXYGEN_LEVEL

    def miss(self, time_to_catch: int):
        used = round(0.6 * time_to_catch)
        if self.oxygen_level < used:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= used
