import random
import time

# Create Game loop
play_again = 'yes'

while play_again == 'yes':

    Question = 1
    Score = 0

# Create Question counter
    while Question <= 10:

        number_1 = random.randint(1, 10)
        number_2 = random.randint(1, 10)

        comp_product = number_1 * number_2

        print('Question {}. {} * {}='.format(Question, number_1, number_2))
        user_product = int(input())

        if comp_product == user_product:
            # Add Score counter
            Score = Score + 1
            print('Correct!')
        else:
            print('Wrong! The answer is {}'.format(comp_product))

        Question = Question + 1
    if Question > 10:
        print('Thank you for playing!\nScore = {} / 10'.format(Score))

        time.sleep(4)

    print()
    print('Do you want to play again? (yes or no)')
    play_again = input().lower()
    if play_again == 'no':
        print('Thank you for playing')
