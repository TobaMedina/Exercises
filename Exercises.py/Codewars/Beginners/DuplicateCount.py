# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

def duplicate_count(text):
    char_count = {}

    for char in text:
        char_lower = char.lower()
        if char_lower.isalnum():
            char_count[char_lower] = char_count.get(char_lower, 0) + 1

    count = 0
    for value in char_count.values():
        if value > 1:
            count += 1

    return count
# return len([c for c in set(text.lower()) if text.lower().count(c)>1])


print(duplicate_count("1AbcdEfGb12345"))
