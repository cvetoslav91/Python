from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    MAX_OXYGEN_LEVEL = 540

    def __init__(self, name):
        super().__init__(name, oxygen_level=540)

    def miss(self, time_to_catch: int):
        used = round(0.3 * time_to_catch)
        if self.oxygen_level < used:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= used

    def renew_oxy(self):
        self.oxygen_level = self.MAX_OXYGEN_LEVEL
