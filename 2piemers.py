user_input = float(input('Enter coordinate: '))


def define_insert(x):
    if x >= 1:
        print('Coordinate intersects')
    else:
        print('Coordinate does not intersect')

# define_insert(user_input)

def check(x):
    """
        Given a number
        x can be int or float

        >>> check(1)
        Coordinate does not intersect
        >>> check(-3)
        Coordinate intersects
    """
    return x >= 1

if __name__ == "__main__":
    import doctest
    doctest.testmod() #test the whole module.

