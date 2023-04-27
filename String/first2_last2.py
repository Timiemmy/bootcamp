def first_last_characters(word):
    letter = word
    if len(letter) < 4:
        return ''
    else:
        return letter[:2]+letter[-2:]


word1 = input('Enter a word ')
print(first_last_characters(word1))