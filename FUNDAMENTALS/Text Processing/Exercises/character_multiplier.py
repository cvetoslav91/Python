word = input().split()
first_word = word[0]
second_word = word[1]
minimum_chars = min(len(first_word), len(second_word))
max_word = max(word, key=len)
left_chars = max_word[minimum_chars:]
total_sum = 0
for i in range(minimum_chars):
    first_number = first_word[i]
    second_number = second_word[i]
    result = ord(first_number) * ord(second_number)
    total_sum += result
for current_char in left_chars:
    total_sum += ord(current_char)

print(total_sum)