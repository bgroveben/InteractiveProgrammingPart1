#!/usr/bin/python
# -*- coding: utf-8 -*-

### Practice Exercises for Functions ###

import math
import random

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
    >>> circle_circumference(3.5)
    21.991148575128552
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
# Compute the area of a circle, given the length of its radius.

###################################################
# Circle area formula
# Student should enter function on the next lines.

def circle_area(radius):
    """
    (num) -> float

    Write a Python function circle_area that takes a single parameter radius corresponding to the
    radius of a circle in inches and returns and returns the area of a circle in square inches.
    Do not use π = 3.14, instead use the math module to supply a higher-precision approximation to π.

    >>> circle_area(1)
    3.141592653589793
    >>> circle_area(3.5)
    38.48451000647496
    >>> circle_area(6)
    113.09733552923255
    """
    return math.pi * (radius ** 2)

###################################################
# Tests
# Student should not change this code.

def test(radius):
	print "A circle with a radius of " + str(radius),
	print "inches has an area of",
	print str(circle_area(radius)) + " square inches."

test(8)
test(3)
test(12.9)
print

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#A circle with a radius of 8 inches has an area of 201.06192983 square inches.
#A circle with a radius of 3 inches has an area of 28.2743338823 square inches.
#A circle with a radius of 12.9 inches has an area of 522.792433484 square inches.



# 7.
# Compute the future value of a given present value, annual rate, and number of years.

###################################################
# Future value formula
# Student should enter function on the next lines.

def future_value(present_value, annual_rate, years):
    """
    (num, num, num) -> float

    Write a Python function future_value that takes three parameters present_value, annual_rate,
    and years and returns the future value of present_value dollars invested at annual_rate
    percent interest, compounded annually for the given number of years.

    >>> future_value(1000, 10, 10)
    2593.7424601000025
    >>> future_value(345, 6.7, 8)
    579.6081058448461
    >>> future_value(110000, 7.5, 20.5)
    484469.233697773
    """
    future_value = present_value * (1 + 0.01 * annual_rate) ** years
    return future_value

###################################################
# Tests
# Student should not change this code.

def test(present_value, annual_rate, years):
	"""Tests the future_value function."""

	print "The future value of $" + str(present_value) + " in " + str(years),
	print "years at an annual rate of " + str(annual_rate) + "% is",
	print "$" + str(future_value(present_value, annual_rate, years)) + "."


###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

test(1000, 7, 10)
test(200, 4, 5)
test(1000, 3, 20)
print

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#The future value of $1000 in 10 years at an annual rate of 7% is $1967.15135729.
#The future value of $200 in 5 years at an annual rate of 4% is $243.33058048.
#The future value of $1000 in 20 years at an annual rate of 3% is $1806.11123467.



# 8.
# Compute a name tag, given the first and last name.

###################################################
# Name tag formula
# Student should enter function on the next lines.

def name_tag(first_name, last_name):
    """
    (str, str) -> str

    Write a Python function name_tag that takes as input the parameters first_name and last_name
    as strings and returns a string of the form "My name is % %." where the percents are the strings
    first_name and last_name.
    Reference the test cases in the provided template for an exact description of the format of the
    returned string.

    >>> name_tag("Monty", "Python")
    'My name is Monty Python.'
    >>> name_tag("Guido", "van Rossum")
    'My name is Guido van Rossum.'
    >>> name_tag("Grace", "Hopper")
    'My name is Grace Hopper.'
    """
    return "My name is " + first_name + " " + last_name + "."

###################################################
# Tests
# Student should not change this code.

def test(first_name, last_name):
	print name_tag(first_name, last_name)

test("Joe", "Warren")
test("Scott", "Rixner")
test("John", "Greiner")
print

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#My name is Joe Warren.
#My name is Scott Rixner.
#My name is John Greiner.



# 9.
# Compute the statement about a person's name and age, given the person's name and age.

###################################################
# Name and age formula
# Student should enter function on the next lines.
def name_and_age(name, age):
    """
    (str, num) -> str

    Write a Python function that takes as input the parameters name (a string) and age (a number)
    and returns a string in the form "% is % years old" where the percents are the string forms
    of name and age.
    Reference the test cases in the provided temlate for an exact description of the format of the
    returned string.

    >>> name_and_age("Joe Warren", 52)
    'Joe Warren is 52 years old.'
    >>> name_and_age("Scott Rixner", 40)
    'Scott Rixner is 40 years old.'
    >>> name_and_age("John Greiner", 46)
    'John Greiner is 46 years old.'
    """
    return name + " is " + str(age) + " years old."


###################################################
# Tests
# Student should not change this code.

def test(name, age):
	print name_and_age(name, age)

test("Joe Warren", 52)
test("Scott Rixner", 40)
test("John Greiner", 46)
print

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#Joe Warren is 52 years old.
#Scott Rixner is 40 years old.
#John Greiner is 46 years old.


# 10.
# Compute the distance between the points (x0, y0) and (x1, y1).

###################################################
# Distance formula
# Student should enter function on the next lines.

def point_distance(x0, y0, x1, y1):
    """
    (num, num, num, num) -> num

    Write a Python function that takes the parameters x0, y0, x1 and y1 and returns the
    distance between the points (x0,y0) and (x1,y1).

    >>> point_distance(1, 2, 3, 4)
    2.8284271247461903
    >>> point_distance(2, 4, 6, 8)
    5.656854249492381
    >>> point_distance(1, 3, 5, 7)
    5.656854249492381
    """
    result = ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5
    return result


###################################################
# Tests
# Student should not change this code.

def test(x0, y0, x1, y1):
	print "The distance from (" + str(x0) + ", " + str(y0) + ") to",
	print "(" + str(x1) + ", " + str(y1) + ") is",
	print str(point_distance(x0, y0, x1, y1)) + "."

test(2, 2, 5, 6)
test(1, 1, 2, 2)
test(0, 0, 3, 4)
print

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#The distance from (2, 2) to (5, 6) is 5.0.
#The distance from (1, 1) to (2, 2) is 1.41421356237.
#The distance from (0, 0) to (3, 4) is 5.0.


# 11.
# Compute the area of a triangle (using Heron's formula),
# given its side lengths.

###################################################
# Triangle area (Heron's) formula
# Student should enter function on the next lines.
# Hint:  Also define point_distance as use it as a helper function.

def triangle_area(x0, y0, x1, y1, x2, y2):
    """
    Write a Python function triangle_area that takes the parameters x0, y0, x1, y1, x2 and y2,
    and returns the area of the triangle with vertices (x0,y0), (x1,y1), and (x2,y2).

    >>> triangle_area(0, 0, 3, 4, 1, 1)
    0.5
    >>> triangle_area(-2, 4, 1, 6, 2, 1)
    8.5
    >>> triangle_area(10, 0, 0, 0, 0, 10)
    50.0
    """
    side_a = point_distance(x0, y0, x1, y1)
    side_b = point_distance(x1, y1, x2, y2)
    side_c = point_distance(x2, y2, x0, y0)
    semiperimeter = (side_a + side_b + side_c) / 2.0
    area = (semiperimeter * (semiperimeter - side_a) * (semiperimeter - side_b) *\
           (semiperimeter - side_c)) ** 0.5
    result = round(area, 2)
    return result

###################################################
# Tests
# Student should not change this code.

def test(x0, y0, x1, y1, x2, y2):
	print "A triangle with vertices (" + str(x0) + "," + str(y0) + "),",
	print "(" + str(x1) + "," + str(y1) + "), and",
	print "(" + str(x2) + "," + str(y2) + ") has an area of",
	print str(triangle_area(x0, y0, x1, y1, x2, y2)) + "."

test(0, 0, 3, 4, 1, 1)
test(-2, 4, 1, 6, 2, 1)
test(10, 0, 0, 0, 0, 10)
print

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#A triangle with vertices (0,0), (3,4), and (1,1) has an area of 0.5.
#A triangle with vertices (-2,4), (1,6), and (2,1) has an area of 8.5.
#A triangle with vertices (10,0), (0,0), and (0,10) has an area of 50.


# 12.
# Compute and print tens and ones digit of an integer in [0,100).

###################################################
# Digits function
# Student should enter function on the next lines.

def print_digits(number):
    """
    (num) -> NoneType

    Write a Python function print_digits that takes an integer number in the range 0 < number < 100
    and prints a message in the format "The tens digit is %, and the ones digit is %.", where the
    percent signs are replaced with the appropriate values.
    Note that this function should print the desired message, rather than returning it as a string.

    >>> print_digits(42)
    The tens digit is 4, and the ones digit is 2.
    >>> print_digits(99)
    The tens digit is 9, and the ones digit is 9.
    >>> print_digits(5)
    The tens digit is 0, and the ones digit is 5.
    """
    tens = number // 10
    ones = number % 10
    print "The tens digit is " + str(tens) + ", and the ones digit is " + str(ones) + "."

###################################################
# Tests
# Student should not change this code.

print_digits(42)
print_digits(99)
print_digits(5)
print


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#The tens digit is 4, and the ones digit is 2.
#The tens digit is 9, and the ones digit is 9.
#The tens digit is 0, and the ones digit is 5.



# 13.
# Compute and print powerball numbers.

###################################################
# Powerball function
# Student should enter function on the next lines.

def powerball():
    """
    (None) -> NoneType

    Powerball is a lottery game in which 6 numbers are drawn at random.
    Players can purchase a lottery ticket with a specific number combination and, if the number
    on the ticket matches the numbers generated in a random drawing, the player wins the jackpot.
    Write a Python function powerball that takes no arguments an prints the message:

    "Today's numbers are %, %, %, %, and %. The Powerball number is %."

    The first five numbers should be random integers in the range 1 <= number < 60.
    In reality, these five numbers must all be distinct, but this problem will allow duplicates.
    The Powerball number is a random integer in the range 1 <= number < 36.
    Use the random module and the function random.randrange() to generate the appropriate numbers.
    Note that this function should print the desired message, rather than returning it as a string.
    >>> random.seed(1)
    >>> powerball()
    Today's numbers are 8, 50, 46, 16, and 30. The Powerball number is 16.
    >>> powerball()
    Today's numbers are 39, 47, 6, 2, and 50. The Powerball number is 16.
    >>> powerball()
    Today's numbers are 45, 1, 27, 43, and 14. The Powerball number is 34.
    """
    # https://docs.python.org/2.7/library/stdtypes.html#string-formatting
    print "Today's numbers are %i, %i, %i, %i, and %i. The Powerball number is %i."%(\
           random.randrange(1,60), random.randrange(1,60), random.randrange(1,60),\
           random.randrange(1,60), random.randrange(1,60), random.randrange(1,36))

###################################################
# Tests
# Student should not change this code.

powerball()
powerball()
powerball()
print



if __name__ == '__main__':
    import doctest
    print doctest.testmod()
