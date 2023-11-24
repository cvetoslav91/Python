def characters(first_char, second_char):
    start = ord(first_char)
    final = ord(second_char)
    for character in range(start + 1, final):
        print(chr(character), end=' ')

first_char = input()
second_char = input()
characters(first_char, second_char)