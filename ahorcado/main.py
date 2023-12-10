import data
# Modules
import hangman_word
import game_process


data = data.DATA
input_letters = []

def run():
    # 1- Obtener la palabra a adivinar
    word_to_guess = hangman_word.hangman_word(data)
    # 2- Obtener la variante en guiones de la palabra
    hyphen_word_to_guess = hangman_word.letter_in_hyphen(word_to_guess)

    # 3- Mostrar la variante en guiones de la palabra
    print(hyphen_word_to_guess)

    # 4- Iniciar el juego
    # intentos
    attempts = (len(word_to_guess) / 2) + 2
    counter = 0

    while counter < attempts:

        letter_input = input('Ingrese una letra o la palabra a adivinar: ')
        
        if letter_input.lower() == word_to_guess.lower():
            print('Ganaste')
            break

        # 5- Procesar la letra ingresada
          
        input_letters.append(letter_input)
        word_to_analyze = game_process.reveal_matching_letters(word_to_guess, input_letters)
        word_to_see = game_process.process_guess(word_to_analyze, word_to_guess)

        print(word_to_see)


if __name__ == '__main__':
    run()
