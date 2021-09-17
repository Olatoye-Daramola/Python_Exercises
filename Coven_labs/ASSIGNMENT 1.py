print('Hello! What is your name?')
name = input()

response = 'Y'

print('Well, {}, \nKindly follow the instructions if you do not want a knock \nNow press '
          'Y if you would like to continue, else press N'.format(name))
response = input()

while response == 'Y':
    print('Enter the value of a')
    a = int(input())

    print('Enter the value of b')
    b = int(input())

    print('Enter the value of c')
    c = int(input())

    d = (b ** 2 - (4 * a * c)) ** (1 / 2)
    e = -b + d
    f = -b - d

    x1 = e / (2 * a)
    x2 = f / (2 * a)

    print('The value of x is {} or {}'.format(x1, x2))

    print()

    print('Do you want to calculate again? (Y/N)')
    response = input()
