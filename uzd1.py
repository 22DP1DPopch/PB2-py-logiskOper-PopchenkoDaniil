from doctest import testmod

def check_cordinates(punkts_x: float, punkts_y: float) -> bool:


# (1, 1); - Point is on the border
#  (2, 1); - Point is on the border
#  (2.5, 1.5); - Point is not inside the figure
#  (-1, 2) - Point is not inside the figure

    """
    Checks if the point inside, outside or on the border of the figure
    >>> check_cordinates(1, 1)
    Point is on the border
    >>> check_cordinates(2, 1)
    Point is on the border
    >>> check_cordinates(2.5, 1.5)
    Point is not inside the figure
    >>> check_cordinates(-1, 2)
    Point is not inside the figure
    """
    #   ? checks where the point is
    if (punkts_y >= -2 and punkts_y <= 1 and (punkts_x == -1 or punkts_x == 3)) or (punkts_x >= -1 and punkts_x <= 3 and (punkts_y == -2 or punkts_y == 1)):
        print("Point is on the border")

    elif punkts_x > -1 and punkts_x < 3 and punkts_y > -2 and punkts_y < 1:
        print("Point is inside the figure")

    else:
        print("Point is not inside the figure")

testmod(verbose=True)

x = float(input("Enter x point: "))
y = float(input("Enter y point: "))

check_cordinates(x,y)
