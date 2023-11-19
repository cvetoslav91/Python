n = int(input())
word = input()
whole_list = []
list_with_word = []
for string in range(n):
    current_string = input()
    whole_list.append(current_string)
    if word in current_string:
        list_with_word.append(current_string)
print(whole_list)
print(list_with_word)