### Practice Exercises for Logic and Conditionals ###

# 1.
# Compute whether an integer is even.

###################################################
# Is even formula
# Student should enter function on the next lines.

def is_even(number):
    """
    (int) -> bool

    Write a Python function is_even() that takes as input the parameter number and returns True
    if number is even and False if number is odd.

    >>> is_even(1)
    False
    >>> is_even(2)
    True
    """
    if number % 2 == 0:
        return True
    else:
        return False


###################################################
# Tests
# Student should not change this code.

def test(number):
	"""Tests the is_even function."""
	if is_even(number):
		print number, "is even."
	else:
		print number, "is odd."

print
test(8)
test(3)
test(12)
print

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#8 is even.
#3 is odd.
#12 is even.


# 2.
# Compute whether a person is cool.

###################################################
# Is cool formula
# Student should enter function on the next lines.

def is_cool(name):
    """
    (str) -> bool

    Write a Python function is_cool() that takes as input the string name and returns True if
    name is either "Joe", "John", or "Stephen" and returns False otherwise.

    >>> is_cool("Ben")
    False
    >>> is_cool("Scott")
    False
    >>> is_cool("Joe")
    True
    >>> is_cool("John")
    True
    >>> is_cool("Stephen")
    True
    """
    if name == "Joe" or name == "John" or name == "Stephen":
        return True
    else:
        return False

###################################################
# Tests
# Student should not change this code.

def test(name):
	"""Tests the is_cool function."""

	if is_cool(name):
		print name, "is cool."
	else:
		print name, "is not cool."

test("Joe")
test("John")
test("Stephen")
test("Scott")
print

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#Joe is cool.
#John is cool.
#Stephen is cool.
#Scott is not cool.


# 3.
# Compute whether the given time is lunchtime.

###################################################
# Is lunchtime formula
# Student should enter function on the next lines.

def is_lunchtime(hour, is_am):
    """
    (int, bool) -> bool

    Write a Python function is_lunchtime that takes as input the parameters hour (an integer in the
    range [1,12]) and is_am (a Boolean 'flag' that represents whether the hour is before noon).
    The function should return True when the input corresponds to 11am or 12pm and false otherwise.

    Precondition: hour parameter is an integer in the range[1, 12].

    >>> is_lunchtime(11, True)
    True
    >>> is_lunchtime(12, False)
    True
    >>> is_lunchtime(11, False)
    False
    >>> is_lunchtime(12, True)
    False
    >>> is_lunchtime(1, False)
    False
    """
    return (hour == 11 and is_am == True) or (hour == 12 and is_am == False)

###################################################
# Tests
# Student should not change this code.

def test(hour, is_am):
	"""Tests the is_lunchtime function."""
	print hour,
	if is_am:
		print "AM",
	else:
		print "PM",
	if is_lunchtime(hour, is_am):
		print "is lunchtime."
	else:
		print "is not lunchtime."

test(11, True)
test(12, True)
test(11, False)
test(12, False)
test(10, False)
print

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#11 AM is lunchtime.
#12 AM is not lunchtime.
#11 PM is not lunchtime.
#12 PM is lunchtime.
#10 PM is not lunchtime.



# 4.
# Compute whether the given year is a leap year.

###################################################
# Is leapyear formula
# Student should enter function on the next lines.

def is_leap_year(year):
    """
    (int) -> bool

    Write a Python function that takes as input the parameter year and returns True if year (an integer)
    is a leap year according to the Gregorian calendar and False otherwise.
    https://en.wikipedia.org/wiki/Leap_year contains a simple algorithmic rule for determining whether a
    year is a leap year.
    Your main task will be to translate this rule into Python.

    >>> is_leap_year(2012)
    True
    >>> is_leap_year(2013)
    False
    >>> is_leap_year(1996)
    True
    >>> is_leap_year(1995)
    False
    >>> is_leap_year(2100)
    False
    """
    return (year % 4 == 0 and not year % 100 == 0) or (year % 400 == 0)

###################################################
# Tests
# Student should not change this code.

def test(year):
	"""Tests the is_leapyear function."""
	if is_leap_year(year):
		print year, "is a leap year."
	else:
		print year, "is not a leap year."

test(2000)
test(1996)
test(1800)
test(2013)
print

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#2000 is a leap year.
#1996 is a leap year.
#1800 is not a leap year.
#2013 is not a leap year.







if __name__ == '__main__':
    import doctest
    print doctest.testmod()
