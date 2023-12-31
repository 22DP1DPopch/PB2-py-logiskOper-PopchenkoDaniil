user_input = float(input('Enter coordinate: '))


def define_insert():
    if user_input <= -2.1:
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
    return x <= -2.1

if __name__ == "__main__":
    import doctest
    doctest.testmod() #test the whole module.


# ! Добавить везде доктест и закинуть в репозиторий рвт 