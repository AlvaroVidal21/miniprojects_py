word = 'java'


word_list_see = list(word)
word_list_hangman = list(word)

index = 0
counter = 0

while counter < 3:
    letter = input('Enter a letter: ') # 'j'
    iterator = 0
    index = 0
    for l in word_list_hangman: # ['j', 'a', 'v', 'a']
    # 'j'
        print(f'iteration #{iterator}')
        print(f'list_see: {word_list_see}')
        print(f'list_hangman: {word_list_hangman}')
        # see
        if letter != l: # if 'j' != 'j' -> False
            word_list_see[index] = '-'
            word_list_hangman[index] = l

        else:
            word_list_see[index] = l
            word_list_hangman[index] = '-'
           
            

        index += 1 

        iterator += 1
            
 
    
    
    
    print(f'see: {word_list_see}')
    print(f'hangman: {word_list_hangman}')
    print(f'valor de index: {index}')
    counter += 1













