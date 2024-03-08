def check_if_anagram(text1: str, text2: str):
    count_letters_text1 = {}
    count_letters_text2 = {}

    if len(text1) != len(text2):
        return "Is not anagram!"

    for i in range(len(text1)):
        count_letters_text1[text1[i]] = count_letters_text1.get(text1[i], 0) + 1
        count_letters_text2[text2[i]] = count_letters_text2.get(text2[i], 0) + 1

    for letter, count_times in count_letters_text1.items():
        try:
            if count_letters_text2[letter] != count_times:
                return "Is not anagram!"
        except KeyError:
            return "Is not anagram!"

    return "Is anagram!"


print(check_if_anagram("nbu", "ubn"))
