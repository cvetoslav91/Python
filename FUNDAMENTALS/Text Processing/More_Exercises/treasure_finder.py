numbers = [int(x) for x in input().split()]
message = ''
while True:
    text = input()
    if text == 'find':
        break
    message = ''
    for i in range(len(text)):
        current_char = text[i]
        while i > len(numbers) - 1:
            i -= len(numbers)
        added_char = chr(ord(current_char) - numbers[i])
        message += added_char
    start_index = message.find('&')
    final_index = message.find('&', start_index + 1)
    type_of_good = message[start_index + 1: final_index]
    start_index_of_coordinates = message.find('<')
    final_index_of_coordinates = message.find('>')
    coordinates = message[start_index_of_coordinates + 1: final_index_of_coordinates]
    print(f'Found {type_of_good} at {coordinates}')