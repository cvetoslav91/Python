def age_assignment(*names, **info):
    dictionary = {}
    for first_letter, age in info.items():
        for full_name in names:
            if first_letter == full_name[0]:
                dictionary[full_name] = age
    result = dict(sorted(dictionary.items(), key=lambda x: x[0]))
    to_print = ""
    for key, value in result.items():
        to_print += f"{key} is {value} years old.\n"
    return to_print


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))