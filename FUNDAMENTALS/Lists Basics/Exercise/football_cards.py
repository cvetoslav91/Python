team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
game_was_terminated = False
booked_player = input()
current_list = booked_player.split(' ')
for i in current_list:
    new_list = i.split('-')
    removed_player = new_list[1]
    if 'A' in new_list:
        if int(removed_player) not in team_a:
            continue
        team_a.remove(int(removed_player))
    elif 'B' in new_list:
        if int(removed_player) not in team_b:
            continue
        team_b.remove(int(removed_player))
    if len(team_a) < 7 or len(team_b) < 7:
        game_was_terminated = True
        break
print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if game_was_terminated:
    print('Game was terminated')