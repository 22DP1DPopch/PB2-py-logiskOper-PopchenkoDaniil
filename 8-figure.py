import doctest


# x1 = -5 
# x2 = 2
# y1 = 3
# y2 = -1


def check_coordinates(punkt_x, punkt_y):
    """
    >>> check_coordinates(1, 1)
    'inside'
    >>> check_coordinates(3, 1) 
    'outside'
    >>> check_coordinates(2, 0)
    'on the border'
    """

    if(punkt_x >= -5 and punkt_x <= 2 and punkt_y >= -1 and punkt_y <= 3):
        if(punkt_x == -5 or punkt_x == 2 or punkt_y == -1 or punkt_y == 3):
           return 'on the border'
        else:
            return 'inside'
    else:
        return 'outside'


doctest.testmod(verbose=True)

# check_coordinates(1, 1) # inside
# check_coordinates(3, 1) # outside
# check_coordinates(2, 0) # on the border

