import random


def menu():
    print(" _________")
    print("|         |")
    print("|         0")
    print("|        /|\ ")
    print("|        / \ ")
    print("|             ")
    print("|   A H O R C A D O\n\n")
    print('Tema: "Deportes"')
    print('Escribe "jugar" para comenzar el juego, "escape" para salir:')
    return input()


def main_module():
    attempts = 8
    word_list = ['Futbol', 'tenis', 'baloncesto', 'atletismo', 'remo',
                 'natacion', 'esgrima', 'pingpong', 'voleibol', 'ciclismo',
                 'taekwondo', 'pentatlon', 'judo', 'gimnasia', 'boxeo']
    game_word = random.choice(word_list)
    game_word_list = list(game_word)
    tried_letters = set()
    blurred_word = list(len(game_word) * '-')
    while attempts > 0:
        print()
        print("".join(blurred_word))
        letter = input('Ingresa una letra o la palabra:')
        if letter == game_word:
            print(f'Has adivinado la palabra!\nSobreviviste!\nPuntaje:{attempts}/8')
            exit()
        elif len(letter) > 1:
            print('Debes ingresar solo una letra')
            continue
        elif not letter.isalpha() or letter.isupper():
            print('No es una letra ASCII en minúscula')
            continue
        elif letter in tried_letters:
            print('Ya escribiste esta letra')
            continue
        else:
            tried_letters.update(letter)
        if letter in game_word_list:
            for i in range(0, len(game_word_list)):
                if letter == game_word_list[i]:
                    blurred_word[i] = letter
            if "".join(blurred_word) == game_word:
                print(f'''\n{"".join(blurred_word)}''')
                print(f'Has adivinado la palabra!\nSobreviviste!\nPuntaje:{attempts}/8')
                exit()
        else:
            attempts -= 1
            if attempts == 0:
                print('''Esta letra no esta en la palabra\nHas sido ahorcado!''')
                exit()
            print('Esta letra no esta en la palabra')
            print(f'Te quedan {attempts} intentos!')


while menu() == 'jugar':
    main_module()
    if menu() == 'escape':
        exit()
