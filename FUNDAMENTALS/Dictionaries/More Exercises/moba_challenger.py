import copy
def sort(item):
    name, points = item
    return -points, name

players = {}
total_pts_dictionary = {}
while True:
    info = input()
    if info == 'Season end':
        break
    if ' -> ' in info:
        name, position, skill = info.split(" -> ")
        skill = int(skill)
        if name not in players:
            players[name] = {position: skill}
            total_pts_dictionary[name] = skill
        else:
            if position not in players[name]:
                players[name][position] = skill
                total_pts_dictionary[name] += skill
            else:
                if players[name][position] < skill:
                    diff = skill - players[name][position]
                    players[name][position] = skill
                    total_pts_dictionary[name] += diff


    elif ' vs ' in info:
        flag = False
        player1, player2 = info.split(' vs ')
        players_copy = copy.deepcopy(players)
        total_pts_dictionary_copy = copy.deepcopy(total_pts_dictionary)
        if player1 in players and player2 in players:
            for pos in players_copy[player1].keys():
                if flag:
                    flag = False
                    break
                for pos2 in players_copy[player2].keys():
                    if pos == pos2:
                        if total_pts_dictionary[player1] > total_pts_dictionary[player2]:
                            del total_pts_dictionary[player2]
                            del players[player2]
                            flag = True
                            break
                        elif total_pts_dictionary[player1] < total_pts_dictionary[player2]:
                            del total_pts_dictionary[player1]
                            del players[player1]
                            flag = True
                            break

for name, info in players.items():
    sorted_dict = dict(sorted(info.items(), key=sort))
    players[name] = sorted_dict

sorted_total = dict(sorted(total_pts_dictionary.items(), key=sort))

for name, info in sorted_total.items():
    print(f'{name}: {info} skill')
    for new_name, new_info in players.items():
        if new_name == name:
            for position, skill_pts in new_info.items():
                print(f'- {position} <::> {skill_pts}')