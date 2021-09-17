import random
import time

play_again = 'yes'

while play_again == 'yes':

    print('You are in a land full of dragons.\nIn front of you, you see two caves.\nIn one cave, the dragon is '
          'friendly and will share his treasure with you.'
          '\nThe other dragon is greedy and hungry, and will eat you on sight')

    comp_choice = random.randint(1, 2)

    print('Which cave will you go into? (1 or 2)')
    user_choice = int(input())

    while user_choice not in [1, 2]:
        print('Which cave will you go into? (1 or 2)')
        user_choice = int(input())

    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you!')
    time.sleep(2)
    print('He opens his jaws and...')
    time.sleep(2)

    if user_choice == comp_choice:
        print('Shares his treasures with you')
    else:
        print('Gobbles you down its throat.\nSorry, that is just life')

    time.sleep(2)
    print()

    print('Do you want to play again? (yes or no)')
    play_again = input().lower()
    if play_again == 'no':
        print('Dragon will still eat you las las')

    time.sleep(3)
