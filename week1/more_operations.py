# Check out the CodeSkulptor documentation (http://www.codeskulptor.org/docs.html#tabs-Python)
# for operations and modules.


# Remainder -- modular arithmetic.
# Systematically restrict computation to a range.
# Remember long division, where you get a quotient plus a remainder?
# With Python's modular arithmetic, quotient is integer division // and the
# remainder is the modulo, which is represented by the modulus operator %.


# Problem - get the ones digit of a number.
print
num = 49
print num
tens = num // 10
print tens
ones = num % 10
print ones
print 10 * tens + ones, num
print


# Application - 24 hour clock.
# http://en.wikipedia.org/wiki/24-hour_clock
hour = 20
shift = 8
print(hour + shift) % 24  # Don't forget the parens, lest your order of operations be incorrect.
print


# Application - screen wraparound.
# The example used is the spaceship app from week 7, where the ship exits the screen
# and appears on the other side.
width = 800
position = 797
move = 10
position = (position + move) % width
print position
print


# Data conversion operations.
# Convert an integer into a string using str().
# Convert an hour into 24-hour format "03:00", including the leading zero.
hour = 3
ones = hour % 10
tens = hour // 10
print tens, ones, ":00"
print str(tens), str(ones), ":00"
print str(tens) + str(ones) + ":00"
print


# Python modules - extra functions implemented outside of basic Python

# import simplegui    # Access to drawing operations for interactive applications.

# simplegui is a custom module for CodeSkulptor. To run the program locally:
# http://stackoverflow.com/questions/13815722/trouble-importing-simplegui
# https://pypi.python.org/pypi/SimpleGUICS2Pygame
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import math         # Access to standard math functions such as trig.

import random       # Functions to generate random numbers.

print math.pi
print
