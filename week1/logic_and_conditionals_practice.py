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







if __name__ == '__main__':
    import doctest
    print doctest.testmod()
