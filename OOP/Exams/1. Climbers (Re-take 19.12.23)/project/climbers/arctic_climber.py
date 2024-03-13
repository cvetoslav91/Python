from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):
    def __init__(self, name: str):
        super().__init__(name, strength=200)

    def can_climb(self) -> bool:
        if self.strength >= 100:
            return True

    def climb(self, peak: BasePeak):
        diff = 2 if peak.difficulty_level == 'Extreme' else 1.5
        self.strength -= 20 * diff

        self.conquered_peaks.append(peak.name)