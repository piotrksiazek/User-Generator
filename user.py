class user():
    def rand_password(alph_lower, alph_upper, special_chars, numbers):
        password = []
        length = random.randint(10, 15)
        for i in range(1, length):
            randomizer = random.randint(1, 4)
            if randomizer == 1:
                password.append(alph_lower[random.randint(1, len(alph_lower) - 1)])
            elif randomizer == 2:
                password.append(alph_upper[random.randint(1, len(alph_upper) - 1)])
            elif randomizer == 3:
                password.append(special_chars[random.randint(1, len(special_chars) - 1)])
            else:
                password.append(numbers[random.randint(1, len(numbers) - 1)])
        return ''.join(char for char in password)

    def rand_username(word_list, len_word_list, alph_lower, alph_upper, special_chars, numbers):
        amt_of_words = random.randint(2, 3)
        word1 = word_list[random.randint(1, len(word_list) - 1)]
        word2 = word_list[random.randint(1, len(word_list) - 1)]
        word3 = word_list[random.randint(1, len(word_list) - 1)]
        username = []
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
                    # is_special = random.randint(1,8)
                    is_number = random.randint(1, 10)
                    if is_upper == 1:
                        username[i][j] = char.upper()
                    # elif is_special == 1:
                    #     username[i][j] = special_chars[random.randint(1,len(special_chars))-1]
                    elif is_number == 1:
                        username[i][j] = numbers[random.randint(1, len(numbers) - 1)]
            return username

        randomized_word_joined = list(itertools.chain.from_iterable(randomized_word(username)))
        return ''.join(char for char in randomized_word_joined)