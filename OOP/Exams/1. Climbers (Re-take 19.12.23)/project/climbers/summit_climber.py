from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):
    def __init__(self, name: str):
        super().__init__(name, strength=150)

    def can_climb(self) -> bool:
        if self.strength >= 75:
            return True

    def climb(self, peak: BasePeak):
        diff = 2.5 if peak.difficulty_level == 'Extreme' else 1.3
        self.strength -= 30 * diff

        self.conquered_peaks.append(peak.name)

