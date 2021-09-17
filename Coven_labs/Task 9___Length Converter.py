RATES = [12, 0.33, 0.000189, 304.8, 30.48, 0.3048, 0.0003048]


def get_user_number():
    user_value = int(input('Enter value in feet: '))

    print()
    print('1. Convert to Inches.\n2. Convert to Yards. \n3. Convert to Miles. \n4. Convert to Millimeter.'
          '\n5. Convert to Centimeters. \n6. Convert to Meters. \n7. Convert to Kilometers')

    print()
    conversion_choice = int(input('Enter conversion number'))

    return user_value, conversion_choice


def conversion(value, rate):
    new_value = value * RATES[rate - 1]

    return new_value


def main():
    value, rate = get_user_number()

    new_value = conversion(value, rate)

    print('Your conversion is: {}'.format(new_value))


main()