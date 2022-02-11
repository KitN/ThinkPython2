
"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import math
import turtle

def spiralLeg(t, turn, length):
    """ For drawing one leg of the spiral. How much to turn to the left and go
    forward
    turn: an angle in degrees
    length: how far to go
    """
    t.lt(turn)
    t.fd(length)

def spiralarc(t, max_angle=360, constant=1):
    """Draws an arc with the given angle and constant proportion.

    t: Turtle
    r: degrees of revolution 
    angle: the ratio of the radius to the angle
    """
    radius = 100
    theta = 100
    while theta < max_angle:
        theta1 = 5
        theta2 = 5
        rad1 = theta
        rad2 = rad1 + theta1
        rad3 = rad2 + theta2
        length1 = abs(cosineLaw(rad1, rad2, theta1))
        length2 = abs(cosineLaw(rad2, rad3, theta2))
        beta1 = abs(sineLaw(rad1, length1, theta1))
        alpha2 = abs(sineLaw(rad3, length2, theta2))
        turn = 180 - beta1 - alpha2
        spiralLeg(t, turn, length1)
        theta += 5

def rad_to_deg(radians):
    degrees = 360 * (radians/(2*math.pi))
    return degrees

def deg_to_rad(degrees):
    radians = 2*math.pi*(degrees/360)
    return radians

def cosineLaw(a, b, theta):
    """ Given two triangle lengths a,b and an angle t, 
    finds the length of the side opposite the angle
    a: first length
    b: second length
    t: angle in degrees
    """
    radians =  deg_to_rad(theta)
    term1 = a**2
    term2 = b**2
    term3 = -(2*a*b*math.cos(radians))
    return term1 + term2 + term3

def sineLaw(a, l, theta):
    """ Find a missing angle when given two sides and an angle"""
    radians = deg_to_rad(theta)
    alpha = a*math.sin(theta)/l
    return alpha

if __name__ == '__main__':
    bob = turtle.Turtle()
    spiralarc(bob)

    # wait for the user to close the window
    turtle.mainloop()
