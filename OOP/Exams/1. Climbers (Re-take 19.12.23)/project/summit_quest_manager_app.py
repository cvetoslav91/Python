from typing import List

from project.climbers.arctic_climber import ArcticClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    def __init__(self):
        self.climbers = []
        self.peaks = []

    def register_climber(self, climber_type: str, climber_name: str):
        all_climbers = [cl.name for cl in self.climbers]
        if climber_name in all_climbers:
            return f"{climber_name} has been already registered."

        if climber_type == 'SummitClimber':
            self.climbers.append(SummitClimber(climber_name))

        elif climber_type == 'ArcticClimber':
            self.climbers.append(ArcticClimber(climber_name))

        else:
            return f"{climber_type} doesn't exist in our register."

        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):

        if peak_type == 'SummitPeak':
            self.peaks.append(SummitPeak(peak_name, peak_elevation))

        elif peak_type == 'ArcticPeak':
            self.peaks.append(ArcticPeak(peak_name, peak_elevation))

        else:
            return f"{peak_type} is an unknown type of peak."

        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]):
        peak = [peak for peak in self.peaks if peak_name == peak.name][0]
        climber = [clmbr for clmbr in self.climbers if climber_name == clmbr.name][0]

        if set(peak.get_recommended_gear()).issubset(gear):
            climber.is_prepared = True
            return f"{climber_name} is prepared to climb {peak_name}."

        else:
            missing_gear = set(peak.get_recommended_gear()).difference(gear)
            climber.is_prepared = False
            return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {', '.join(sorted(missing_gear))}."

    def perform_climbing(self, climber_name: str, peak_name: str):
        try:
            peak = [peak for peak in self.peaks if peak_name == peak.name][0]
        except IndexError:
            return f"Peak {peak_name} is not part of the wish list."

        try:
            climber = [clmbr for clmbr in self.climbers if climber_name == clmbr.name][0]
        except IndexError:
            return f"Climber {climber_name} is not registered yet."

        if climber.can_climb() and climber.is_prepared:
            climber.climb(peak)
            return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."

        elif climber.is_prepared == False:
            return f"{climber_name} will need to be better prepared next time."

        else:
            climber.rest()
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

    def get_statistics(self):
        climbers_with_at_least_one_peak = [c for c in self.climbers if len(c.conquered_peaks) > 0]
        sorted_people_lambda = sorted(climbers_with_at_least_one_peak, key=lambda x: (-len(x.conquered_peaks), x.name))

        return f"Total climbed peaks: {len(self.peaks)}\n" + "**Climber's statistics:**\n" + '\n'.join([cl.__str__() for cl in sorted_people_lambda])
