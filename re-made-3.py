import doctest

def check_cordinates(punkts_x : float, punkts_y : float) -> bool:
    '''
    Checks points
    >>> check_cordinates(0.7, 1.95)
    Point is on the border
    '''

    if ((punkts_x == -1 and 0 <= punkts_y <= 4.5) or (punkts_y == 0 and -1 <= punkts_x <= 2) or (punkts_y + 1.5 * punkts_x - 3 == 0)):
         print("Point is on the border")
    elif -1 < punkts_x < 2 and 0 < punkts_y < 4.5 and (punkts_y + 1.5 * punkts_x - 3) < 0:
        print("Point is inside")
    else:
        print("Point is not inside")


doctest.testmod(verbose=True)

x = float(input("Enter x point: "))
y = float(input("Enter y point: "))
check_cordinates(x, y)
