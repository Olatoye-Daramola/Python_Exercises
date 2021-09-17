import random

# Guess the number

print('Hello! What is your name?')
name = input()

print('Well, {}, \nI am thinking of a number between 1 and 20'.format(name))

number = random.randint(1, 20)

number_of_guesses = 1

while number_of_guesses <= 6:
    print('Take a guess')
    guess = int(input())

    if guess > number:
        print('Guess is too high')
    elif guess < number:
        print('Guess is too low')
    elif guess == number:
        print('Good Job! {}. \nYou guessed my number in {} guesses;) !'.format(name, number_of_guesses))
        break

    number_of_guesses = number_of_guesses + 1
if number_of_guesses > 6:
    print('Game Over! The number is {}'.format(number))
