#!/usr/bin/python
# -*- coding: utf-8 -*-

### Practice Exercises for Functions ###

import math

# 1.
# Compute the number of feet corresponding to a number of miles.

###################################################
# Miles to feet conversion formula
# Student should enter function on the next lines.

def miles_to_feet(miles):
    """
    (number) -> number

    Write a Python function miles_to_feet that takes a parameter miles and
    returns the number of feet in miles.

    >>> miles_to_feet(1)
    5280
    >>> miles_to_feet(5)
    26400
    >>> miles_to_feet(10)
    52800
    """
    feet = 5280 * miles
    return feet

###################################################
# Tests
# Student should not change this code.

def test(miles):
	print str(miles) + " miles equals",
	print str(miles_to_feet(miles)) + " feet."

print
test(13)
test(57)
test(82.67)
print

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#13 miles equals 68640 feet.
#57 miles equals 300960 feet.
#82.67 miles equals 436497.6 feet.



# 2.
# Compute the number of seconds in a given number of hours, minutes, and seconds.

###################################################
# Hours, minutes, and seconds to seconds conversion formula
# Student should enter function on the next lines.
def total_seconds(hours, minutes, seconds):
    """
    (int, int, int) -> int

    Write a Python function total_seconds that takes three parameters hours,
    minutes, and seconds, and returns the total number of seconds.

    >>> total_seconds(1, 0, 0)
    3600
    >>> total_seconds(1, 1, 0)
    3660
    >>> total_seconds(1, 1, 1)
    3661
    """
    minutes = minutes * 60
    hours = hours * 3600
    total = seconds + minutes + hours
    return total


###################################################
# Tests
# Student should not change this code.

def test(hours, minutes, seconds):
	print str(hours) + " hours, " + str(minutes) + " minutes, and",
	print str(seconds) + " seconds totals to",
	print str(total_seconds(hours, minutes, seconds)) + " seconds."

test(7, 21, 37)
test(10, 1, 7)
test(1, 0, 1)
print


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#7 hours, 21 minutes, and 37 seconds totals to 26497 seconds.
#10 hours, 1 minutes, and 7 seconds totals to 36067 seconds.
#1 hours, 0 minutes, and 1 seconds totals to 3601 seconds.



# 3.
# Compute the length of a rectangle's perimeter, given its width and height.

###################################################
# Rectangle perimeter formula
# Student should enter function on the next lines.

def rectangle_perimeter(width, height):
    """
    (num, num) -> num

    Write a Python function rectangle_perimeter that takes wo parameters width and height
    corresponding to the lengths of the sides of a rectangle and returns the perimeter
    of the rectangle in inches.

    >>> rectangle_perimeter(1, 2)
    6
    >>> rectangle_perimeter(2, 4)
    12
    >>> rectangle_perimeter(5, 7)
    24
    """
    return 2 * width + 2 * height


###################################################
# Tests
# Student should not change this code.

def test(width, height):
	print "A rectangle " + str(width) + " inches wide and " + str(height),
	print "inches high has a perimeter of",
	print str(rectangle_perimeter(width, height)) + " inches."

test(4, 7)
test(7, 4)
test(10, 10)
print


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#A rectangle 4 inches wide and 7 inches high has a perimeter of 22 inches.
#A rectangle 7 inches wide and 4 inches high has a perimeter of 22 inches.
#A rectangle 10 inches wide and 10 inches high has a perimeter of 40 inches.



# 4.
# Compute the area of a rectangle, given its width and height.

###################################################
# Rectangle area formula
# Student should enter function on the next lines.

def rectangle_area(width, height):
    """
    (num, num) -> num

    Write a Python function rectangle_area that takes two parameters width and height
    corresponding to the lengths of the sides of a rectangle and returns the area of
    the rectangle in square inches.

    >>> rectangle_area(1, 2)
    2
    >>> rectangle_area(2, 4)
    8
    >>> rectangle_area(5, 7)
    35
    """
    return width * height

###################################################
# Tests
# Student should not change this code.

def test(width, height):
	print "A rectangle " + str(width) + " inches wide and " + str(height),
	print "inches high has an area of",
	print str(rectangle_area(width, height)) + " square inches."

test(4, 7)
test(7, 4)
test(10, 10)
print


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#A rectangle 4 inches wide and 7 inches high has an area of 28 square inches.
#A rectangle 7 inches wide and 4 inches high has an area of 28 square inches.
#A rectangle 10 inches wide and 10 inches high has an area of 100 square inches.



# 5.
# Compute the circumference of a circle, given the length of its radius.

###################################################
# Circle circumference formula
# Student should enter function on the next lines.

def circle_circumference(radius):
    """
    (num) -> float

    Write a Python function circle_circumference that takes a single parameter radius corresponding
    to the radius of a circle ininches and returns the circumference of a circle with radius in inches.
    Do not use π = 3.14, instead use the math module to supply a higher precision approximation of π.

    >>> circle_circumference(1)
    6.283185307179586
    >>> circle_circumference(3)
    18.84955592153876
    >>> circle_circumference(6)
    37.69911184307752
    """
    return 2 * (math.pi * radius)

###################################################
# Tests
# Student should not change this code.

def test(radius):
	print "A circle with a radius of " + str(radius),
	print "inches has a circumference of",
	print str(circle_circumference(radius)) + " inches."

test(8)
test(3)
test(12.9)
print

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#A circle with a radius of 8 inches has a circumference of 50.2654824574 inches.
#A circle with a radius of 3 inches has a circumference of 18.8495559215 inches.
#A circle with a radius of 12.9 inches has a circumference of 81.0530904626 inches.



# 6.








if __name__ == '__main__':
    import doctest
    print doctest.testmod()
