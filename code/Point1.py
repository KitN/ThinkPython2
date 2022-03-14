"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division


class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return('(%g, %g)' % (self.x, self.y))

    def __add__(self, other):
        if isinstance(other, Point):
            return self.add_point(other)
        else:
            return self.add_tuple(other)

    def __radd__(self, other): # Make point addition commutative
        return self.__add__(other)
            
    def add_point(self, other):
        sumpoint = Point()
        x3 = self.x + other.x
        y3 = self.y + other.y
        sumpoint.x = x3
        sumpoint.y = y3
        return sumpoint

    def add_tuple(self, twople):
        sumpoint = Point()
        x3 = self.x + twople[0]
        y3 = self.y + twople[1]
        sumpoint.x = x3
        sumpoint.y = y3
        return sumpoint

def print_point(p):
    """Print a Point object in human-readable format."""
    print('(%g, %g)' % (p.x, p.y))


class Rectangle:
    """Represents a rectangle. 

    attributes: width, height, corner.
    """


def find_center(rect):
    """Returns a Point at the center of a Rectangle.

    rect: Rectangle

    returns: new Point
    """
    p = Point()
    p.x = rect.corner.x + rect.width/2.0
    p.y = rect.corner.y + rect.height/2.0
    return p


def grow_rectangle(rect, dwidth, dheight):
    """Modifies the Rectangle by adding to its width and height.

    rect: Rectangle object.
    dwidth: change in width (can be negative).
    dheight: change in height (can be negative).
    """
    rect.width += dwidth
    rect.height += dheight


def main():
    blank = Point()
    blank.x = 3
    blank.y = 4
    print('blank', end=' ')
    print(blank)

    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0

    center = find_center(box)
    print('center', end=' ')
    print(center)

    print(box.width)
    print(box.height)
    print('grow')
    grow_rectangle(box, 50, 100)
    print(box.width)
    print(box.height)
    three = Point(2, 3)
    four = Point(4,5)
    print(three+four)
    print(three + (1,1))
    print((1,1) + four)


if __name__ == '__main__':
    main()

