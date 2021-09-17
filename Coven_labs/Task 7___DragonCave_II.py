import random
import time


def display_intro():
    print('You are in a land full of dragons.\nIn front of you, you see two caves.\nIn one cave, the dragon is '
          'friendly and will share his treasure with you.'
          '\nThe other dragon is greedy and hungry, and will eat you on sight')
    print()


def choose_cave():
    cave = ''

    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()

    return cave


def check_cave(chosen_cave):
    print('You approach the cave...')
    time.sleep(1.5)
    print('It is dark and spooky...')
    time.sleep(1.5)
    print('A large dragon jumps out in front of you!')
    time.sleep(1.5)
    print('He opens his jaws and...')
    print()

    time.sleep(2)

    computer_cave = random.randint(1, 2)

    if chosen_cave == str(computer_cave):
        print('Shares his treasures with you')
    else:
        print('Gobbles you down its throat.\nSorry, that is just life')


play_again = 'yes'
while play_again == 'yes':
    display_intro()

    cave_number = choose_cave()

    check_cave(cave_number)

    time.sleep(2)
    print('Do you want to play again? (yes or no)')
    play_again = input().lower()
