def team_lineup(*args):
    dictionary = {}
    for name, country in args:
       if country not in dictionary:
          dictionary[country] = []
       dictionary[country].append(name)
    sorted_dict = dict(sorted(dictionary.items(), key=lambda x: (-len(x[1]), x[0])))
    result = ''
    for key, value in sorted_dict.items():
       result += f"{key}:\n"
       for name in value:
          result += f'  -{name}\n'
    return result


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))