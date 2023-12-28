words = input()
current_word = ''
final_word = ''
current_number = ''
end_of_word = False
for char in range(len(words)):
    current_char = words[char]
    if not current_char.isnumeric():
        if end_of_word:
            final_word += current_word * int(current_number)
            current_number = ''
            current_word = ''
            end_of_word = False
        current_word += current_char.upper()
    else:
        current_number += current_char
        end_of_word = True
final_word += current_word * int(current_number)

print(f'Unique symbols used: {len(set(final_word))}')
print(final_word)