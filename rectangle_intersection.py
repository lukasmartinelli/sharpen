class Rectangle:
    def __init__(self, left_x, bottom_y, width, height):
        self.left_x = left_x
        self.bottom_y = bottom_y
        self.width = width
        self.height = height

def intersection(rect1, rect2):
    # Find intersection on x range
    x1 = rect1.left_x
    x2 = rect1.left_x + rect1.width

    _x1 = rect2.left_x
    _x2 = rect2.left_x + rect2.width

    """
    x1---------r1-------x2
       _x1---r2---_x2
    """

    # What do I need to do to get coords from the intersection of x1
    if _x1 <= x1:
        i1 = x1
    if _x1 > x1:
        i1 = _x1
# 
#
#     8-----r1-----12
# 5-----r2---------12

    if _x2 <= x2:
        i2 = _x2
    if _x2 > x2:
        i2 = x2
# 
#
#     8-----r1-----13
# 5-----r2------11
    print('X axis intersection: {}'.format((i1, i2)))

    # Find intersection on x range
    y1 = rect1.bottom_y
    y2 = rect1.bottom_y + rect1.height

    _y1 = rect2.bottom_y
    _y2 = rect2.bottom_y + rect2.height

    # What do I need to do to get coords from the intersection of y1
    if _y1 <= y1:
        j1 = y1
    if _y1 > y1:
        j1 = _y1
# 
#
#     8-----r1-----12
# 5-----r2---------12

    if _y2 <= y2:
        j2 = _y2
    if _y2 > y2:
        j2 = y2

    print('Y axis intersection: {}'.format((j1, j2)))


rect1 = Rectangle(1, 5, width=10, height=4)
rect2 = Rectangle(2, 5, width=10, height=4)
intersection(rect1, rect2)

rect3 = Rectangle(1, 5, width=1, height=1)
rect4 = Rectangle(7, 8, width=1, height=1)
intersection(rect3, rect4)

