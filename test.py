def next_letter():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    user_letters = input('Input your letters here: ')
    response = []

    for letter in user_letters:
        for char in enumerate(alphabet):
            if letter == char[1]:
                if letter != 'z':
                    new_letter_index = char[0] + 1
                    response.append(alphabet[new_letter_index])
                else:
                    response.append(alphabet[0])
    return print(' '.join(response))


next_letter()
