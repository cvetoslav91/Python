words = input().split()
palindromes = [word for word in words if word == word[::-1]]
palindrome = input()
result = palindromes.count(palindrome)
print(palindromes)
print(f'Found palindrome {result} times')