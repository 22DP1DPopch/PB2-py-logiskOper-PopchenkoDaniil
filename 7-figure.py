from doctest import testmod

def parbaudit_koordinati(punkts_x : float, punkts_y : float) -> bool:
    """
    Funkcija pārbauda vai x ir laukumā
    >>> parbaudit_koordinati(2, 1)
    Punkts is inside the figure
    >>> parbaudit_koordinati(1, 0)
    Punkts is inside the figure
    >>> parbaudit_koordinati(4, 0)
    Punkts is not inside the figure
    """

    if punkts_x > -1 and punkts_x < 3 and punkts_y > -2 and punkts_y < 2:
        print("Punkts is inside the figure")

    elif (punkts_x == -1 and punkts_y >= -2 and punkts_y <= 1) or \
            (punkts_x == 3 and punkts_y >= -2 and punkts_y <= 1) or \
            (punkts_y == -2 and punkts_x >= -1 and punkts_x <= 3) or \
            (punkts_y == 2 and punkts_x == -1 and punkts_x <= 3):
        print("Punkts is on the border")

    else:
        print("Punkts is not inside the figure")


# doctest with testmod() and printing the results of the test to the console
testmod()

parbaudit_koordinati(float(input("Enter x: ")), float(input("Enter y: ")))