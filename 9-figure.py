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