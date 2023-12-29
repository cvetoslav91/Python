title = input()
print('<h1>')
print(f'\t{title}')
print('</h1>')
content = input()
print('<article>')
print(f'\t{content}')
print('</article>')
while True:
    comment = input()
    if comment == 'end of comments':
        break
    print('<div>')
    print(f'\t{comment}')
    print('</div>')