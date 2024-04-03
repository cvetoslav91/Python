from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    valid_divers = {
        'FreeDiver': FreeDiver,
        'ScubaDiver': ScubaDiver,
    }

    valid_fishes = {
        'PredatoryFish': PredatoryFish,
        'DeepSeaFish': DeepSeaFish,
    }

    def __init__(self):
        self.divers = []
        self.fish_list = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in NauticalCatchChallengeApp.valid_divers:
            return f"{diver_type} is not allowed in our competition."
        if diver_name in [d.name for d in self.divers]:
            return f"{diver_name} is already a participant."

        new_diver = NauticalCatchChallengeApp.valid_divers[diver_type](diver_name)
        self.divers.append(new_diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in NauticalCatchChallengeApp.valid_fishes:
            return f"{fish_type} is forbidden for chasing in our competition."
        if fish_name in [f.name for f in self.fish_list]:
            return f"{fish_name} is already permitted."

        new_fish = NauticalCatchChallengeApp.valid_fishes[fish_type](fish_name, points)
        self.fish_list.append(new_fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        try:
            diver = [d for d in self.divers if d.name == diver_name][0]
        except IndexError:
            return f"{diver_name} is not registered for the competition."

        try:
            fish = [f for f in self.fish_list if f.name == fish_name][0]
        except IndexError:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver.name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            if diver.oxygen_level == 0:
                diver.update_health_status()
            return f"{diver.name} missed a good {fish.name}."

        elif diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                if diver.oxygen_level == 0:
                    diver.update_health_status()
                return f"{diver.name} hits a {fish.points}pt. {fish.name}."
            else:
                diver.miss(fish.time_to_catch)
                if diver.oxygen_level == 0:
                    diver.update_health_status()
                return f"{diver.name} missed a good {fish.name}."

        elif diver.oxygen_level > fish.time_to_catch:
            diver.hit(fish)
            if diver.oxygen_level == 0:
                diver.update_health_status()
            return f"{diver.name} hits a {fish.points}pt. {fish.name}."

    def health_recovery(self):
        diver_with_issues = [d for d in self.divers if d.has_health_issue]
        counter = 0
        for diver in diver_with_issues:
            diver.renew_oxy()
            diver.has_health_issue = False
            counter += 1
        return f"Divers recovered: {counter}"

    def diver_catch_report(self, diver_name: str):
        try:
            diver = [d for d in self.divers if d.name == diver_name][0]
        except KeyError:
            return f"{diver_name} is not registered for the competition."

        return f"**{diver_name} Catch Report**\n" + '\n'.join([f.fish_details() for f in diver.catch])

    def competition_statistics(self):
        divers_ranked = [d for d in self.divers if not d.has_health_issue]
        sorted_divers = sorted(divers_ranked, key=lambda x: (-x.competition_points, -len(x.catch), x.name))
        return f'**Nautical Catch Challenge Statistics**\n' + '\n'.join(str(d) for d in sorted_divers)
