from sys import argv

text = argv[1]
occurrences = {}

for letter in text:
    occurrences[letter] = occurrences.get(letter, 0) + 1

print(occurrences)
