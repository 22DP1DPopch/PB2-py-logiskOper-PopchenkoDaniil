from doctest import testmod

def check_coordinates(punkt_x, punkt_y):

    """
    >>> check_coordinates(0, 0)
    uz robezlinijas
    >>> check_coordinates(1, 0)
    uz robezlinijas
    >>> check_coordinates(2, 0)
    uz robezlinijas
    >>> check_coordinates(1, 1)
    iekša
    """


    if punkt_x >= -1 and punkt_y >= 0 and punkt_y <= -1.5*punkt_x+3:
        if punkt_x == -1 or punkt_y == 0 or punkt_y == -1.5*punkt_x+3:
            print('uz robezlinijas')
        else:
            print('iekša')
    else:
        print('Ārpuss figuras')

testmod()

# check_coordinates(2, 0)
# check_coordinates(1, 0)
# check_coordinates(1, 1)