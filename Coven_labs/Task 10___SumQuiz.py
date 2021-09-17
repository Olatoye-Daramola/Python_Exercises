import random
import time


def display_intro():
    name = input(print('What is your name?'))

    print('Hello {}! \nWelcome to the maths quiz game...'.format(name))
    print()


def add():
    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)

    comp_answer = num_1 + num_2
    user_answer = int(input('{} + {} = '.format(num_1, num_2)))

    while comp_answer != user_answer:
        print('Try again')
        user_answer = int(input('{} + {} = '.format(num_1, num_2)))

        if user_answer == comp_answer:
            print('Good Job!')

    return user_answer, comp_answer


display_intro()


def replay():
    play_again = 'yes'
    while play_again == 'yes':
        add()

        time.sleep(1)
        print('Do you want to play again? (yes or no)')
        play_again = input().lower()

    if play_again != 'yes':
        time.sleep(1)
        print('Thanks for playing')


replay()
