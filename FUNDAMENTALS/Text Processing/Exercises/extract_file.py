path = input().split("\\")
file_info = path[-1]
file_name, file_extension = file_info.split('.')
print(f'File name: {file_name}')
print(f'File extension: {file_extension}')