from string import ascii_lowercase, ascii_uppercase
import itertools
import random

class User():
    def rand_password(self, alph_lower, alph_upper, special_chars, numbers):
        password = []
        length = random.randint(10, 15)  # Choosing random password length.
        for i in range(1, length):
            randomizer = random.randint(1, 4)  # var randomizer decides whether next char will be alph_lower, alph_upper, special or number
            if randomizer == 1:
                password.append(alph_lower[random.randint(1, len(alph_lower) - 1)])
            elif randomizer == 2:
                password.append(alph_upper[random.randint(1, len(alph_upper) - 1)])
            elif randomizer == 3:
                password.append(special_chars[random.randint(1, len(special_chars) - 1)])
            else:
                password.append(numbers[random.randint(1, len(numbers) - 1)])
        return ''.join(char for char in password)

    def rand_username(self, word_list, numbers, min_words, max_words):
        amt_of_words = random.randint(min_words, max_words)
        word1 = word_list[random.randint(1, len(word_list) - 1)]
        word2 = word_list[random.randint(1, len(word_list) - 1)]
        word3 = word_list[random.randint(1, len(word_list) - 1)]
        if amt_of_words == 1:
            username = [word1]
        elif amt_of_words == 2:
            username = [word1, word2]
        else:
            username = [word1, word2, word3]

        def randomized_word(username):
            username = [[char for char in word] for word in username]
            for i, word in enumerate(username):
                for j, char in enumerate(word):
                    is_upper = random.randint(1, 8)
                    is_number = random.randint(1, 10)
                    if is_upper == 1:
                        username[i][j] = char.upper()
                    elif is_number == 1:
                        username[i][j] = numbers[random.randint(1, len(numbers) - 1)]
            return username

        randomized_word_joined = list(itertools.chain.from_iterable(randomized_word(username)))
        return ''.join(char for char in randomized_word_joined)

    def rand_name(self, name_list):
        return name_list[random.randint(1,len(name_list)-1)]

    def rand_surname(self, name_list):
        return name_list[random.randint(1,len(name_list)-1)]


def main():
    with open('words.txt', 'r') as words:
        word_list = [word.strip() for word in words]
    with open('namex.txt', 'r') as names:
        name_list = [name.strip() for name in names]
    alph_lower, alph_upper = ascii_lowercase, ascii_uppercase
    special_chars = '!"#$%&\/\()*+,-./:;?@[]^_`{|}~'
    numbers = '0123456789'

    user = User()
    with open('users.txt', 'w') as users:
        for i in range(1,501):
            username = user.rand_username(word_list, numbers, 2, 3)
            password = user.rand_password(alph_lower, alph_upper, special_chars, numbers)
            name = user.rand_name(name_list)
            surname = user.rand_surname(name_list)
            users.write(f'{i}.  username: {username}\n    password:  {password}\n    name:  {name}\n    surname:  {surname}')
            users.write('\n\n')

main()


