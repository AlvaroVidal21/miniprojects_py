import random
import data
import math

def hangman_word(data):
    index_random = random.randint(0, len(data) - 1)
    hangman_word = data[index_random].lower()
    return hangman_word # hangman_word = "python"


def letter_in_hyphen(hangman_word):
    letters = len(hangman_word)
    hyphen = "-" * letters
    return hyphen # hyphen = "-----"

def letter_deleter(word, letter_to_delete):
    word = word.replace(letter_to_delete, '')
    return word









