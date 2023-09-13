user_input = int(input('Enter coordinate: '))


def define_insert(x):
    if x >= -2 and x <= 1:
        print('Coordinate intersects')
    else:
        print('Coordinate does not intersect')

define_insert(user_input)