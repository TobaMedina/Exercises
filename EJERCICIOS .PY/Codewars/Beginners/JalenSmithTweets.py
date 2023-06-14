# Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.

def to_jaden_case(string):
    words = string.split()
    capitalized = [word[0].upper() + word[1:].lower() for word in words]
    return ' '.join(capitalized)


check = to_jaden_case("raNvkIjNo Y vcwTr")
print(check)
