#!/usr/bin/python
# -*- coding: utf-8 -*-

print

# 1.
# Compute the number of feet corresponding to a number of miles.
# There are 5280 feet in a mile. Write a Python statement that calculates and prints the number of feet in 13 miles.
###################################################
# Miles to feet conversion formula.

mile_length = 5280
number_of_miles = 13
print mile_length * number_of_miles
print

###################################################
# Expected output:
# => 68640


# 2.
# Compute the number of seconds in a given number of hours, minutes, and seconds.
# Write a Python statement that calculates and prints the number of seconds in 7 hours, 21 minutes and 37 seconds.
###################################################
# Hours, minutes, and seconds to seconds conversion formula.

seconds = 1
minutes = seconds * 60
hours = minutes * 60
print (37 * seconds) + (minutes * 21) + (hours * 7)
print

###################################################
# Expected output:
# => 26497


# 3.
# Compute the length of a rectangle's perimeter, given its width and height.
# The perimeter of a rectangle is 2w+2h, where w and h are the lengths of its sides.
# Write a Python statement that calculates and prints the length in inches of the perimeter of a rectangle with
# sides of length 4 and 7 inches.
###################################################
# Rectangle perimeter formula.

height = 4
width = 7
perimeter = 2*width + 2*height
print perimeter
print

###################################################
# Expected output:
# => 22


# 4.
# Compute the area of a rectangle, given its width and height.
# The area of a rectangle is wh, where w and h are the lengths of its sides.
# Note that the multiplication operation is not shown explicitly in this formula.
# This is standard practice in mathematics, but not in programming.
# Write a Python statement that calculates and prints the area in square inches of a rectangle with
# sides of length 4 and 7 inches.
###################################################
# Rectangle area formula.

width = 4
height = 7
area = width * height
print area
print

###################################################
# Expected output:
# => 28


# 5.
# Compute the circumference of a circle, given the length of its radius.
# The circumference of a circle is 2πr where r is the radius of the circle.
# Write a Python statement that calculates and prints the circumference in inches of a circle whose radius is 8 inches.
# Assume that the constant π=3.14.
###################################################
# Circle circumference formula.

radius = 8
pi = 3.14
circumference = 2 * pi * radius
print circumference
print

###################################################
# Expected output:
# => 50.24


# 6.
# Compute the area of a circle, given the length of its radius.
# The area of a circle is πr^2 where r is the radius of the circle.
# (My text editor won't display the raised 2 as an exponent correctly, so I used a hat instead.)
# Write a Python statement that calculates and prints the area in square inches of a circle whose radius is 8 inches.
# Assume that the constant π=3.14.
###################################################
# Circle area formula.

radius = 8
pi = 3.14
area = pi * radius ** 2
print area
print

###################################################
# Expected output:
# => 200.96


# 7.
# Compute the future value of a given present value, annual rate, and number of years.
# Given p dollars, the future value of this money when compounded yearly at a rate of r percent interest
# for y years is p(1+0.01r)y.
# Write a Python statement that calculates and prints the value of 1000 dollars compounded at
# 7 percent interest for 10 years.
###################################################
# Future value formula.

p = 1000
r = 7
y = 10
future_value = p * (1 + 0.01 * r) ** y
print future_value
print

###################################################
# Expected output:
# => 1967.15135729


# 8.
# Compute a name tag, given the first and last name.
# Write a single Python statement that combines the three strings "My name is", "Joe" and "Warren"
# (plus a couple of other small strings) into one larger string "My name is Joe Warren." and prints the result.
###################################################
# Name tag formula.

# print "{0} {1} {2}.".format("My name is", "Joe", "Warren")  ## Works, but rejected by autograder.

greet = "My name is"
first_name = "Joe"
last_name = "Warren"
print greet + " " + first_name + " " + last_name + "."
print

###################################################
# Expected output:
# => My name is Joe Warren.


# 9.
# Compute the statement about a person's name and age, given the person's name and age.
# Write a Python expression that combines the string "Joe Warren is 52 years old." from the string "Joe Warren"
# and the number 52 and then prints the result. (Hint: Use the function str to convert the number into a string.)
###################################################
# Name and age formula.

name = "Joe Warren"
age = str(52)
print name + " is " + age + " years old."
print

###################################################
# Expected output:
# => Joe Warren is 52 years old.


# 10.
# Compute the distance between the points (x_0, y_0) and (x_1, y_1).
# The distance between two points (x_0,y_0) and (x1_,y_1) is sqrt((x_0−x_1)^2+(y_0−y_1)^2).
# Write a Python statement that calculates and prints the distance between the points (2,2) and (5,6).
###################################################
# Distance formula.

x0 = 2
y0 = 2
x1 = 5
y1 = 6
point_distance = ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5
print point_distance
print

###################################################
# Expected output:
# => 5.0
