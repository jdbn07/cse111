import random

def choose_word():
    """Selecciona una palabra aleatoria de una lista predefinida."""
    words = ["python", "programacion", "desarrollo", "computadora", "inteligencia"]
    return random.choice(words)

def display_word(word, guessed_letters):
    """Muestra la palabra oculta con las letras adivinadas reveladas."""
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    """Función principal para el juego del ahorcado."""
    print("¡Bienvenido al juego del ahorcado!")
    print("Tienes que adivinar la palabra. ¡Buena suerte!")

    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6

    while attempts > 0:
        print("\nPalabra a adivinar:", display_word(word_to_guess, guessed_letters))
        guess = input("Ingresa una letra: ").lower()

        if guess in guessed_letters:
            print("Ya has intentado con esa letra. ¡Intenta con otra!")
            continue
        elif guess in word_to_guess:
            guessed_letters.append(guess)
            print("¡Bien hecho! La letra está en la palabra.")
        else:
            attempts -= 1
            print("¡Incorrecto! Te quedan {} intentos.".format(attempts))

        if "_" not in display_word(word_to_guess, guessed_letters):
            print("\n¡Felicidades! Has adivinado la palabra:", word_to_guess)
            break

    if attempts == 0:
        print("\n¡Oh no! Te has quedado sin intentos. La palabra era:", word_to_guess)

if __name__ == "__main__":
    hangman()