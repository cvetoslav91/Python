from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    def calculate_revenue_after_race(self, race_pos: int):
        prizes = {
            'Petronas': {1: 1000000, 3: 500000},
            'TeamViewer': {5: 100000, 7: 50000}
        }
        revenue = 0
        for sponsor, info in prizes.items():
            for place, prize in info.items():
                if race_pos <= place:
                    revenue += prize
                    break
        revenue -= 200000
        self.budget += revenue

        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"