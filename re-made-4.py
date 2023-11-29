import math
import doctest

def check_cordinates(punkts_x : float, punkts_y : float) -> bool:
# (0.5, 0.8660254037844386); - Point is inside
# (-0.5, -0.8660254037844386); - Point is inside
# (0.3, 0.9539392014169456); - Point is inside
# (-0.3, 0.9539392014169456); - Point is inside
# (-0.3, -0.9539392014169456) - Point is inside

    l, k = 0, 0  
    radius = 1   

    # ! calculates the distance
    distance = math.sqrt((punkts_x - l)**2 + (punkts_y - k)**2)

    # ! where
    if distance == radius:
        print("Point is on the border")
    elif distance < radius:
        print("Point is inside")
    else:
        print("Point is not inside")
    
doctest.testmod(verbose=True)

x = float(input("Enter x point:"))
y = float(input("Enter y point:"))
check_cordinates(x, y)

