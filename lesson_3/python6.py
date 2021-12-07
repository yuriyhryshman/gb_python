def to_up_word(word):
    word = list(word)
    word[0] = word[0].upper()
    word = ''.join(word)
    return word


def to_up_str(string):
    string = string.lower()
    string = string.split()
    for i in range(0, len(string)):
        string[i] = to_up_word(string[i])
    string = ' '.join(string)
    return string


print(to_up_str(input('Введите пожалуйста строку: ')))
