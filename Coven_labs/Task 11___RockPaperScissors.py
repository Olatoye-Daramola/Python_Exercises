import random


def display_intro():
    name = input(print('What is your name? '))

    print('Hello {}! \nWelcome to the Rock-Paper-Scissors game...'
          '\nR = Rock, P = Paper, S = Scissors'.format(name))
    print()


def play():
    score = 0

    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    comp_choice = beats[random.choice(['rock', 'paper', 'scissors'])]
    user_choice = input('Choose \'Rock\', \'Paper\', \'Scissors\': ').lower()

    if beats[user_choice] == comp_choice:
        print('Computer played: {}.'.format(comp_choice))

        score = score + 1

        return print('Player Wins')

    elif beats[comp_choice] == user_choice:
        print('Computer played: {}.'.format(comp_choice))

        return print('Computer wins')

    else:
        print('Computer played: {}.'.format(comp_choice))
    return print('Draw!')


def loop():
    again = 0
    while again < 5:
        play()

        again = again + 1
        print(f"Score= {score}")


loop()
