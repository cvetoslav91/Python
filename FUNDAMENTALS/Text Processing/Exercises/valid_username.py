usernames = input().split(', ')
for current_username in usernames:
    if 3 <= len(current_username) <= 16:
        for char in current_username:
            if not char.isalnum() and char != '-' and char != '_':
                break
        else:
            print(current_username, end='\n')