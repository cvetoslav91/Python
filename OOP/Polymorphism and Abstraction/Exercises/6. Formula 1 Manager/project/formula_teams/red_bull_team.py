from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    def calculate_revenue_after_race(self, race_pos: int):
        prizes = {
            'Oracle': {1: 1500000, 2: 800000},
            'Honda': {8: 20000, 10: 10000}
        }
        revenue = 0
        for sponsor, info in prizes.items():
            for place, prize in info.items():
                if race_pos <= place:
                    revenue += prize
                    break
        revenue -= 250000
        self.budget += revenue

        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"