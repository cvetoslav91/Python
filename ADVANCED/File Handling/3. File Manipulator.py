import os.path

command = input().split('-')

while command[0] != 'End':
    if command[0] == 'Create':
        with open(f'files/{command[1]}', 'w') as file: pass

    elif command[0] == 'Add':
        with open(f'files/{command[1]}', 'a') as file:
            file.write(f'{command[2]}\n')
    elif command[0] == 'Replace':
        try:
            with open(f'files/{command[1]}', "r+") as file:
                text = file.read()
                text = text.replace(f'{command[2]}', f'{command[3]}')

                file.seek(0)
                file.write(text)
                file.truncate()

        except FileNotFoundError:
            print('An error occurred')
    elif command[0] == 'Delete':
        try:
            os.remove(f'files/{command[1]}')
        except FileNotFoundError:
            print('An error occurred')



    command = input().split('-')