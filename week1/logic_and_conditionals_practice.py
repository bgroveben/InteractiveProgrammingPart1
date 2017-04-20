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

    Write a Python function is_lunchtime() that takes as input the parameters hour (an integer in the
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

    Write a Python function is_leap_year() that takes as input the parameter year and returns True if year (an integer)
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



# 5.
# Compute whether two intervals intersect.

###################################################
# Interval intersection formula
# Student should enter function on the next lines.

def interval_intersect(a, b, c, d):
    """
    (int, int, int, int) -> bool

    Write a Python function interval_intersect() that takes parameters a, b, c, and d and returns
    True if the intervals [a,b] and [c,d] intersect and False otherwise.
    In other words, if there are any numbers that are in both [a,b] and [c,d], return True,
    False otherwise.

    Precondition: (a <= b) and (c <= d)

    >>> interval_intersect(0, 1, 1, 2)
    True
    >>> interval_intersect(1, 2, 0, 1)
    True
    >>> interval_intersect(0, 1, 2, 3)
    False
    >>> interval_intersect(2, 3, 0, 1)
    False
    >>> interval_intersect(0, 3, 1, 2)
    True
    """
    return (b >= c) and (a <= d)

###################################################
# Tests
# Student should not change this code.

def test(a, b, c, d):
    """Tests the interval_intersect function."""
    print "Intervals [" + str(a) + ", " + str(b) + "] and [" + str(c) + ", " + str(d) + "]",
    if interval_intersect(a, b, c, d):
        print "intersect."
    else:
        print "do not intersect."

test(0, 1, 1, 2)
test(1, 2, 0, 1)
test(0, 1, 2, 3)
test(2, 3, 0, 1)
test(0, 3, 1, 2)
print


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#Intervals [0, 1] and [1, 2] intersect.
#Intervals [1, 2] and [0, 1] intersect.
#Intervals [0, 1] and [2, 3] do not intersect.
#Intervals [2, 3] and [0, 1] do not intersect.
#Intervals [0, 3] and [1, 2] intersect.



# 6.
# Compute the statement about a person's name and age, given the person's name and age.

###################################################
# Name and age formula
# Student should enter function on the next lines.

def name_and_age(name, age):
    """
    (str, num) -> str

    Write a Python function name_and_age() that takse as input the parameters name (a string)
    and age (a number) and returns a string of the form "% is % years old." where the percents
    are the string forms of name and age.
    The function should include an error check for the case when age is less than zero.
    If age is less than zero, the function should return the string "Error: Invalid Age"

    >>> name_and_age('Ben', 27)
    'Ben is 27 years old.'
    >>> name_and_age('Dave', -1)
    'Error: Invalid age'
    >>> name_and_age('Tavo', 22)
    'Tavo is 22 years old.'
    """
    if age < 0:
        return "Error: Invalid age"
    else:
        return name + " is " + str(age) + " years old."

###################################################
# Tests
# Student should not change this code.

def test(name, age):
	"""Tests the name_and_age function."""

	print name_and_age(name, age)

test("Joe Warren", 52)
test("Scott Rixner", 40)
test("John Greiner", -46)
print

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#Joe Warren is 52 years old.
#Scott Rixner is 40 years old.
#Error: Invalid age



# 7.
# Compute and print tens and ones digit of an integer in [0,100).

###################################################
# Digits function
# Student should enter function on the next lines.

def print_digits(number):
    """
    (int) -> str

    Write a Python function print_digits() that takes an integer number in the range [0,100]
    and prints the message "The tens digit is %, and the ones digit is %." where the percents
    should be replaced with the appropriate values.
    The function should include an error check for the case when number is negative or greater
    than or equal to 100.
    In those cases, the function should instead print "Error: Input is not a two-digit number."

    Preconditions: number is an integer and -1 < number < 100.

    >>> print_digits(-1)
    Error: Input is not a two-digit number.
    >>> print_digits(100)
    Error: Input is not a two-digit number.
    >>> print_digits(1)
    The tens digit is 0, and the ones digit is 1.
    >>> print_digits(12)
    The tens digit is 1, and the ones digit is 2.
    >>> print_digits(50)
    The tens digit is 5, and the ones digit is 0.
    >>> print_digits(99)
    The tens digit is 9, and the ones digit is 9.
    """
    ones = number % 10
    tens = number // 10
    if number < 0 or number > 99:
        print "Error: Input is not a two-digit number."
    else:
        print "The tens digit is %d, and the ones digit is %d."%(tens, ones)

###################################################
# Tests
# Student should not change this code.

print_digits(42)
print_digits(99)
print_digits(5)
print_digits(459)
print


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#The tens digit is 4, and the ones digit is 2.
#The tens digit is 9, and the ones digit is 9.
#The tens digit is 0, and the ones digit is 5.
#Error: Input is not a two-digit number.



# 8.
# Compute instructor's last name, given the first name.

###################################################
# Name lookup formula
# Student should enter function on the next lines.

def name_lookup(first_name):
    """
    (str) -> str

    Write a Python function name_lookup() that takes a string first_name that corresponds to one
    of ("Joe", "Scott", "John", or "Stephen") and then returns their corresponding last name
    ("Warren", "Rixner", "Greiner", or "Wong").
    If the string first_name doesn't match any of the corresponding last names, return the string
    "Error: Not an instructor".

    >>> name_lookup("Joe")
    'Warren'
    >>> name_lookup("Scott")
    'Rixner'
    >>> name_lookup("John")
    'Greiner'
    >>> name_lookup("Stephen")
    'Wong'
    >>> name_lookup("Mary")
    'Error: Not an instructor'
    """
    if first_name == "Joe":
        return "Warren"
    elif first_name == "Scott":
        return "Rixner"
    elif first_name == "John":
        return "Greiner"
    elif first_name == "Stephen":
        return "Wong"
    else:
        return "Error: Not an instructor"

###################################################
# Tests
# Student should not change this code.

def test(first_name):
	"""Tests the name_lookup function."""

	print name_lookup(first_name)

test("Joe")
test("Scott")
test("John")
test("Stephen")
test("Mary")
print


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#Warren
#Rixner
#Greiner
#Wong
#Error: Not an instructor



# 9.
# Compute a (simplified) Pig Latin version of a word.

###################################################
# Pig Latin formula
def pig_latin(word):
    """
    (str) -> str

    Returns the (simplified) Pig Latin version of the word.
    Write a Python function pig_latin() that takes a string word and applies the following rules to
    generate a new word in Pig Latin.
    If the first letter in word is a consonant, append the consonant plus "ay" to the end of the remainder of the word.
    If the first letter in word is a vowel, append "way" to the end of the word.

    Preconditions: word is lowercase.

    >>> pig_latin("pig")
    'igpay'
    >>> pig_latin("owl")
    'owlway'
    """

    first_letter = word[0]
    rest_of_word = word[1 : ]
	# Student should complete function on the next lines.
    vowels = ['a', 'e', 'i', 'o', 'u']
    if first_letter in vowels:
        result = first_letter + rest_of_word + "way"
    else:
        result = rest_of_word + first_letter + "ay"

    return result

###################################################
# Tests
# Student should not change this code.

def test(word):
	"""Tests the pig_latin function."""

	print pig_latin(word)

test("pig")
test("owl")
test("python")
print


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#igpay
#owlway
#ythonpay



# 10.
# Compute the smaller root of a quadratic equation.

###################################################
# Smaller quadratic root formula
# Student should enter function on the next lines.

def smaller_root(a, b, c):
    """
    (num, num, num) -> num or NoneType

    https://en.wikipedia.org/wiki/Quadratic_equation
    Given numbers a, b, and c, the quadratic equation can have zero, one, or two real solutions.
    The quadratic formula (found in the wikipedia entry above) can be used to compute these solutions.
    The expression b**2 - 4*a*c is called the discriminant associated with the equation.
    If the discriminant is zero, the equation has one solution.
    If the discriminant is positive, the equation has two solutions.
    If the discriminant is negative, the equation has no solutions.
    Write a Python function smaller_root() that takes as input the numbers a, b, and c and returns
    the smaller solution to this equation if one exists.
    If the equation has no real solution, print the message "Error: No real solutions" and simply return.
    If there is no real solution, the function will print the message and return the Python value None.

    >>> smaller_root(2, 0, -10)
    -2.23606797749979
    >>> smaller_root(1, 2, 3)
    Error: No real solutions
    """
    discriminant = (b**2) - (4 * a * c)
    # quadratic_formula = (-b - (discriminant ** 0.5)) / 2 * a
    if discriminant < 0:
        print "Error: No real solutions"
        return
    elif discriminant == 0:
        # x = (-b + math.sqrt(d)) / (2 * a)
        x = (-b + (discriminant ** 0.5)) / (2 * a)
        return x
    else:
        x1 = (-b + (discriminant ** 0.5)) / (2 * a)
        x2 = (-b - (discriminant ** 0.5)) / (2 * a)
        if x1 < x2:
            return x1
        else:
            return x2

###################################################
# Tests
# Student should not change this code.

def test(a, b, c):
    """Tests the smaller_root function."""

    print "The smaller root of " + str(a) + "x^2 + " + str(b) + "x + " + str(c) + " is:"
    print str(smaller_root(a, b, c))


test(1, 2, 3)
test(2, 0, -10)
test(6, -3, 5)
print

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#The smaller root of 1x^2 + 2x + 3 is:
#Error: No real solutions
#None
#The smaller root of 2x^2 + 0x + -10 is:
#-2.2360679775
#The smaller root of 6x^2 + -3x + 5 is:
#Error: No real solutions
#None



if __name__ == '__main__':
    import doctest
    print doctest.testmod()
