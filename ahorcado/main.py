import random
import data
import hangman
import math

# dependencies functions = hangman_word, letter_in_hyphen, letter_deleter from hangman.py
def hangman_game(hangman_word, hyphhen):
    hangman_word_in_game = hangman_word
    attempts = math.ceil(len(hangman_word) / 1.8)
    counter = 0
    print(f'You have {attempts} attempts to guess the word')
    print(f'{hyphhen} the word have {len(hangman_word)} letters')


    while counter < attempts and hangman_word_in_game != '':
        input_letter = input("Guess the letter or put the word: ").lower()

        # if the input is the word so the game is over and the player win
        if input_letter == hangman_word:
            print('you win')
            break
        
        # function to delete the letter 
        hangman_word_in_game = hangman.letter_deleter(hangman_word_in_game, input_letter)
        if input_letter in hangman_word:
            print('okidoki')
        else:
            print('nope')

        counter += 1

    # 
    if hangman_word_in_game != '':
        print("-" * 20)
        print('give me the hangman word: ')

        input_hangman_word = input().lower()
        if input_hangman_word == hangman_word:
            print('you win')
        else:
            print('you lose')

    print(hangman_word)





def run():
    hangman_word = hangman.hangman_word(data.DATA)
    hyphhen = hangman.letter_in_hyphen(hangman_word)
    hangman_game(hangman_word, hyphhen)


if __name__ == '__main__':
    run()