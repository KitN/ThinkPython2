"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division
import math



class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """


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

def move_rectangle(rect, dx, dy):
    """Modifies the Rectangle by moving its corner.

    rect: Rectangle object.
    dx: How many units to shift the corner (right is positive)
    dy: How many units to shift the corner (up is positive)
    """
    rect.corner.x += dx
    rect.corner.y += dy

def deep_move_rectangle(rect, dx, dy):
    """Modifies the Rectangle by moving its corner.
    Returns a new, deep copy of the rect.

    rect: Rectangle object.
    dx: How many units to shift the corner (right is positive)
    dy: How many units to shift the corner (up is positive)
    """
    import copy
    rect2 = copy.deepcopy(rect)
    rect2.corner.x += dx
    rect2.corner.y += dy
    return rect2
    
def distance_bw_points(alpha, beta):
    """Takes two points, alpha and beta, and returns a float according to their
    Euclidean distance.

    alpha, beta: Point objects
    """
    x1, y1 = alpha.x, alpha.y
    x2, y2 = beta.x, beta.y
    distance = math.sqrt((x2-x1) ** 2 + (y2-y1)**2)
    return distance

class Circle:
    """ Represents a circle in 2D space

    centrepoint: a Point
    radius: the radius
    """

def point_in_circle(pnt, crc):
    """ Returns true if and only if the point is in the circle

    pnt: a Point
    crc: a Circle
    returns: True or False, when the point is in or out.
    """
    dist_from_cent = distance_bw_points(pnt, crc.centre)
    if dist_from_cent <= crc.radius:
        return True
    else:
        return False

def rect_in_circle(rect, crc):
    """Returns true iff all corners of a rectangle are in a circle.

    crc: a Circle
    rect: a Rectangle

    returns: True or False
    """

def main():
    plato = Circle()
    plato.centre = Point()
    plato.centre.x = 150
    plato.centre.y = 100
    plato.radius = 75

    hole = Point()
    hole.x = 160
    hole.y = 94

    hole = Point()
    hole.x = 500
    hole.y = 0

    print(f"The point is in the circle: ", point_in_circle(hole, plato))

if __name__ == '__main__':
    main()

