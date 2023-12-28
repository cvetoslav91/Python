first_char = input()
second_char = input()
text = input()
total_sum = 0
for current_char in text:
    if ord(first_char) < ord(current_char) < ord(second_char):
        total_sum += ord(current_char)
print(total_sum)