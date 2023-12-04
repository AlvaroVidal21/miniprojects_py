word_to_guess = 'java'

input_list = ['a', 'j']

# input = 'a'

# input_list.append(input)



def reveal_matching_letters(word, input_list):
    for i in input_list:
        if i in word:
            word = word.replace(i, '-')

    return word # 'j-v-'
 


def process_guess(word, word_analyze): # 'j-v-'
    word_analyze = list(word_analyze) # ['j', 'a', 'v', 'a']
    word = list(word) # ['j', '-', 'v', '-']
    word_see = word.copy()
    index = 0
    # print('iniciando el ciclo for------')
    for i in word: # 'j'
        # print(f'index: {index}')
        # print(f'i: {i}')

        if word[index] != '-':
            word_see[index] = '-'
            # print('es una letra')
            # print(f'word_see: {word_see}')
            index += 1
        
        else:
            word_see[index] = word_analyze[index] # 'j'
            # print('no es una letra')
            # print(f'word_see: {word_see}')
            index += 1
    
    # print(f'see: {word_see}') # I wante word see to be ['-', 'a', '-', 'a']
    # print(f'word: {word}')

    return word_see


words_to_match = reveal_matching_letters(word_to_guess, input_list)

word_to_see = process_guess(words_to_match, word_to_guess)

print(word_to_see)
