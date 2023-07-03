# Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed. Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

def reverse_long_words(sentence):
    words = sentence.split()
    reversed_words = []

    for word in words:
        if len(word) >= 5:
            reversed_words.append(word[::-1])
        else:
            reversed_words.append(word)

    return ' '.join(reversed_words)


print(reverse_long_words("Hello world"))
