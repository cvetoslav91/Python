import re


class NameTooShortError(Exception):
    "Name must be more than 4 characters"

class MustContainAtSymbolError(Exception):
    "Email must contain @"

class InvalidDomainError(Exception):
    "Domain must be one of the following: .com, .bg, .org, .net"

command = input()

while command != 'End':
    result = re.findall(r'[a-zA-Z0-9]{5,}@', command)
    if not result:
        raise NameTooShortError("Name must be more than 4 characters")
    second = re.findall(r'@', command)
    if not second:
        raise MustContainAtSymbolError("Email must contain @")
    third = re.findall(r'\.com|\.bg|\.org|\.net', command)
    if not third:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    command = input()