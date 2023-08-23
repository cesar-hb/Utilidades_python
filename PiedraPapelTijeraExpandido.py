##Piedra papel y tijera con 15 opciones

import random


def get_options():
    options = input().split(',')
    if options == ['']:
        options = ['rock', 'paper', 'scissors']
    return options


def outcome(gesture, random_gesture):
    gestures = ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge',
                'wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock']
    start = gestures.index(gesture)
    if gesture == random_gesture:
        return 'draw'
    else:
        for counter in range(1, 8):
            if gestures[start - counter] == random_gesture:
                return 'win'
        else:
            return 'lost'


def game():
    print(f'Hello, {name}')
    options = get_options()
    print('Okay, let\'s start')
    while True:
        global score
        gesture = input()
        random_gesture = random.choice(options)
        if gesture == '!exit':
            print('Bye!')
            #update_score()
            exit()
        elif gesture == '!rating':
            print(f'Your rating: {int(score)}')
        elif gesture not in options:
            print('Invalid input')
            continue
        else:
            result = outcome(gesture, random_gesture)
            if result == 'lost':
                print(f'Sorry, but computer chose {random_gesture}')
            elif result == 'draw':
                print(f'There is a draw ({gesture})')
                score += 50
            else:
                print(f'Well done. Computer chose {random_gesture} and failed')
                score += 100


def get_score():
    ratings = open('rating.txt')
    for line in ratings:
        line = line.split()
        if name in line[0]:
            global score
            score = int(line[1].strip('\n'))
            ratings.close()
            break
    else:
        ratings_append = open('rating.txt', 'a')
        ratings_append.write(f'{name} 0\n')
        ratings_append.close()

## Pedazo de codigo que servia para actualizar
## el texto con los score de cada jugador, no lo hize bien, y no funciona.
#def update_score():
#    update = open('rating.txt', mode='a+')
#    for line in update:
#        line_split = line.split()
#        if name in line_split[0]:
#            print(f'{name} {score}')
#            update.close()


name = input('Enter your name:')
score = 0
get_score()
game()
