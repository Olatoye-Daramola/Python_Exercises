import random

# Sum of Random numbers

number_1 = random.randint(1, 10)
number_2 = random.randint(1, 10)

total = number_1 + number_2

print('{} + {}='.format(number_1, number_2))

answer = int(input())

if total == answer:
    print('Correct!')
else:
    print('Wrong!')
