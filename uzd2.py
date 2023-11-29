from doctest import testmod

def check_cordinates(punkts_x : float, punkts_y : float) -> bool:
    """
    Checks if the point is inside the figure
    >>> check_cordinates(2, 1)
    Point is on the border
    >>> check_cordinates(1, 0)
    Point in inside the figure
    >>> check_cordinates(4, 0)
    Point is not inside the figure 
    """
# parbauda kur ir punkti 
    if (punkts_y >= -1 and punkts_y <= 3  and (punkts_x == -5 or punkts_x == 2)) or (punkts_x >= -5 and punkts_x <= 2 and (punkts_y == -1 or punkts_y == 3)):
        print("Point is on the border")

    elif punkts_x > -5 and punkts_x < 2 and punkts_y > -1 and punkts_y < 3:
        print("Point in inside the figure")

    else:
        print("Point is not inside the figure")
testmod(verbose=True)

x = float(input("Enter x point: "))
y = float(input("Enter y point: "))

check_cordinates(x,y)
