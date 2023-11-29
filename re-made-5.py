import doctest

def check_cordinates(punkts_x: float, punkts_y: float) -> bool:

# (-3.4, 5); - Point is inside
# (4, 5); - Point is inside
# (6, 4); - Point is on the border
# (3, 8); - Point is on the border
# (-2, 8); - Point is on the border
# (4, 8); - Point is on the border
# (-4, 7); - Point is not inside
# (-3.45, 5); - Point is on the border
# (5, 6.6046511627907005); - Point is on the border
# (4.5, 7.302325581395352); - Point is on the border
# (6, 5.209302325581399); - Point is on the border
# (5.433333333333335, 6.0) - Point is on the border

    if (punkts_y == 4 and punkts_x >= -4 and punkts_x < 8.3 or 
        punkts_y == 8 and punkts_x >= -2.9 and punkts_x <= 4) or\
        round(punkts_y,4) == round(6/1.1*punkts_x + 26.2/1.1,4 ) or\
        round(punkts_y,4) == round(-6/4.3*punkts_x + 58.4/4.3 ,4):
        print ('Point is on the border')
    elif punkts_x > -4 and punkts_x < 8.3 and punkts_y > 4 and punkts_y < 8 and round(punkts_y,4) < round(6/1.1*punkts_x + 26.2/1.1 ,4) and round(punkts_y,4) < round(-6/4.3*punkts_x + 58.4/4.3 ,4):
        print('Point is inside')
    else:
        print('Point is not inside')


# doctest.testmod(verbose=True)

x = float(input("Enter x point: "))

y = float(input("Enter y point:"))

check_cordinates(x, y)



