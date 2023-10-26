import doctest


def check_coordinates(punkt_x, punkt_y):
    """
    >>> check_coordinates(1, 0)
    uz 'robezlinijas'
    >>> check_coordinates(0, 0)
    uz 'robezlinijas'
    >>> check_coordinates(-1.2, 0)
    'Ārpuss figuras'
    >>> check_coordinates(0.1, 2.8)
    'iekša'
    >>> check_coordinates(-0.5, 3.2)
   'iekša'
    >>> check_coordinates(-0.9, 4.4)
    'Ārpuss figuras'
    >>> check_coordinates(1.7, 0.3)
    'iekša'
    >>> check_coordinates(0, 1.5)
    'iekša'
    >>> check_coordinates(-1, 2)
    'uz robezlinijas'
    >>> check_coordinates(-1, 4.5)
    'uz robezlinijas'
    >>> check_coordinates(-1, 0)
    'uz robezlinijas'
    >>> check_coordinates(2, 0)
    'uz robezlinijas'
    >>> check_coordinates(2, 1)
    'Ārpuss figuras'
    >>> check_coordinates(3, -1.2)
    'Ārpuss figuras'
    >>> check_coordinates(1, -2)
    'Ārpuss figuras'
    >>> check_coordinates(-0.4, -0.3)
    'Ārpuss figuras'
    >>> check_coordinates(-1, -3)
    'Ārpuss figuras'
    >>> check_coordinates(-3, 6)
    'Ārpuss figuras'
    >>> check_coordinates(-0.3, 5)
    'Ārpuss figuras'

    """

    if punkt_x >= -1 and punkt_y >= 0 and punkt_y <= -1.5*punkt_x+3:
        if punkt_x == -1 or punkt_y == 0 or punkt_y == -1.5*punkt_x+3:
            return 'uz robezlinijas'
        else:
            return 'iekša'
    else:
        return 'Ārpuss figuras'

doctest.testmod(verbose=True)

# print('1')
# check_coordinates(1, 0)
# print('2')
# check_coordinates(0, 0)
# print('3')
# check_coordinates(-1.2, 0)

# print('4')
# check_coordinates(0.1, 2.8)
# print('5')
# check_coordinates(-0.5, 3.2)
# print('6')
# check_coordinates(-0.9, 4.4)

# print('7')
# check_coordinates(1.7, 0.3)
# print('8')
# check_coordinates(0, 1.5)
# print('9')
# check_coordinates(-1, 2)

# print('10')
# check_coordinates(-1, 4.5)
# print('11')
# check_coordinates(-1, 0)
# print('12')
# check_coordinates(2, 0)

# print('13')
# check_coordinates(2, 1)
# print('14')
# check_coordinates(3, -1.2)
# print('15')
# check_coordinates(1, -2)

# print('16')
# check_coordinates(-0.4, -0.3)
# print('17')
# check_coordinates(-1, -3)
# print('18')
# check_coordinates(-3, 6)

# print('19')
# check_coordinates(-0.3, 5)
# print('20')
# check_coordinates(0.5, 2.25)
# print('21')
# check_coordinates(1.7, 0.45)

# print('21')
# check_coordinates(1, 1.5)
# print('22')
# check_coordinates(0, 3)
# print('23')
# check_coordinates(-0.1, 3.15)

# print('24')
# check_coordinates(-0.8, 4.2)



