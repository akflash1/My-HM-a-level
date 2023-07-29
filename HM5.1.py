def to_lower(string):
    return string.lower()

def to_upper(string):
    return string.upper()

strings = input("Enter strings: ")
lower_case = list(map(to_lower, strings.split()))
upper_case = list(map(to_upper, strings.split()))
print("Strings in lowercase:", lower_case)
print("Strings in uppercase:", upper_case)