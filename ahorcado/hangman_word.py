import random


def hangman_word(data):
    index_random = random.randint(0, len(data) - 1)
    hangman_word = data[index_random].lower()
    return hangman_word # hangman_word = "python"


def letter_in_hyphen(hangman_word):
    letters = len(hangman_word)
    hyphen = "❓" * letters
    return hyphen # hyphen = "-----"




# Aquí obtenemos la palabra a adivinar y su variante en guiones (que solo se usará la primera vez para mostrar la longitud de la palabra)





