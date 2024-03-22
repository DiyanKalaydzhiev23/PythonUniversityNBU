from sys import argv

text = "abcdz"
new_text = []

for letter in text:
    ascii_number = 97 + ((ord(letter) + 3 - 97) % 26)
    new_text.append(chr(ascii_number))

print("".join(new_text))
