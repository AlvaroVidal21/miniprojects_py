

def reveal_matching_letters(word_to_guess, input_letters):
    """
    Reemplaza letras coincidentes en una palabra con guiones.

    Args:
    word_to_guess (str): La palabra en la que se reemplazarán las letras.
    input_letters (list): Una lista de letras para buscar en la palabra.

    Returns:
    str: Una versión modificada de la palabra con las letras coincidentes reemplazadas por guiones.

    Example:
    >>> reveal_matching_letters('juego', ['e', 'o'])
    'j--g-o'
    """
    for i in input_letters:
        if i in word_to_guess:
            word_to_guess = word_to_guess.replace(i, '❓')
    
    word_to_analyze = word_to_guess

    return word_to_analyze 


def process_guess(word_to_analyze, word_to_guess):
    word_to_guess_list = list(word_to_guess) 
    word_to_analyze_list = list(word_to_analyze) 

    word_to_see = word_to_analyze_list.copy()

    index = 0

    for i in word_to_analyze_list:
        if word_to_analyze_list[index] != '❓':
            word_to_see[index] = '❓'
            index += 1

        else:
            word_to_see[index] = word_to_guess_list[index]
            index += 1

    word_to_see = ''.join(word_to_see)

    return word_to_see


