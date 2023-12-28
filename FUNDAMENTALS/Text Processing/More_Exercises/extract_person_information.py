n = int(input())
for i in range(n):
    current_text = input()
    index_at = current_text.index('@')
    index_line = current_text.index('|')
    index_hashtag = current_text.index('#')
    index_star = current_text.index('*')
    name = current_text[index_at + 1: index_line]
    age = current_text[index_hashtag + 1: index_star]
    print(f'{name} is {age} years old.')