def factor(number):
    factors = []

    for num in range(1, number + 1):

        remainder = number % num

        if remainder == 0:
            factors.append(num)

    return factors


user_number = int(input('Enter your number: '))


list_of_factors = factor(user_number)
print('Here is the list of factors of {}= {}'.format(user_number, list_of_factors))