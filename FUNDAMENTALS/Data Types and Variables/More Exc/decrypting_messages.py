forward_characters = int(input())
number_of_characters = int(input())
for i in range(number_of_characters):
    character = input()
    new_character = ord(character) + forward_characters
    new_character = chr(new_character)
    print(new_character, end='')