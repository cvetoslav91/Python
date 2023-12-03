def merge_elements(start_index, final_index, list_of_words: list):
    if start_index < 0:
        start_index = 0
    new_word = list_of_words[start_index: final_index + 1]
    list_of_words_first_half = list_of_words[:start_index]
    list_of_words_second_half = list_of_words[final_index + 1:]
    if start_index == 0:
        return f"{''.join(new_word)} {' '.join(list_of_words_second_half)}"
    return f"{' '.join(list_of_words_first_half)} {''.join(new_word)} {' '.join(list_of_words_second_half)}"


def divide_elements(index, parts, list_of_words):
    divided_word = list(list_of_words[index])
    len_of_new_words = len(divided_word) // parts
    if len_of_new_words == 0:
        len_of_new_words = 1
        parts = len(divided_word)
    final_list = []
    while len(final_list) != parts:
        if len(final_list) + 1 == parts:
            final_list.append(''.join(divided_word))
            break
        else:
            new_word = divided_word[0:len_of_new_words]
            final_list.append(''.join(new_word))
            divided_word = divided_word[len_of_new_words:]
    list_of_words.pop(index)
    final_list = ' '.join(final_list)
    list_of_words.insert(index, final_list)
    divided = ' '.join(list_of_words)
    return divided


words = input().split()
while True:
    command = input().split()
    if command[0] == "3:1":
        break
    elif command[0] == 'merge':
        result = merge_elements(int(command[1]), int(command[2]), words)
    elif command[0] == 'divide':
        result = divide_elements(int(command[1]), int(command[2]), words)
    words = result.split()
print(' '.join(words))
