import random

keywords = ["MURCIELAGO", "SERPIENTE", "DINOSAURIO", "ELEFANTE"]

# Función para elegir una palabra al azar
def select_word():
    return random.choice(keywords)

# Función para inicializar el tablero con guiones bajos
def initialize_board(word):
    return ["_" if letra.isalpha() else letra for letra in word]

# Función para mostrar el estado actual del tablero
def display_board(board):
    return " ".join(board)

# Función principal del juego
def game():
    word = select_word()
    trys = 5
    win = False
    board = initialize_board(word)

    print("Bienvenido al juego del ahorcado")

    while not win and trys > 0:
        print(f"Tienes {trys} intentos restantes")
        print(display_board(board))

        letter = input("Ingresa una letra: ").upper()

        if len(letter) != 1 or not letter.isalpha():
            print("Ingresa una letra válida.")
            continue

        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    board[i] = letter
            if "".join(board) == word:
                win = True
        else:
            trys -= 1
            print("Letra incorrecta. Intenta nuevamente.")

    if win:
        print(f"Felicitaciones, ganaste. La palabra era '{word}'.")
    else:
        print(f"Lo siento, perdiste. La palabra era '{word}'. Intenta nuevamente más tarde. :(")

# Llamar a la función principal del juego
if __name__ == "__main__":
    game()