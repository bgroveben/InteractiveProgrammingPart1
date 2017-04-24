### Examples of Global vs Local Variables ###

print
# num1 is a global variable.
num1 = 1
print num1
print

# num2 is a local variable.
def fun():
    num1 = 2
    num2 = num1 + 1
    print num2
    print

fun()

# The scope of global num1 is the whole program, and num1 retains its definition.
print num1
print

# The scope of the variable num2 is fun(), so num2 is undefined unless the function is called.
# Uncomment the lines below to see the NameError for yourself:
# print num2
# print

# You can use local variables to (among other things):
# - Give a descriptive name toa quantity.
# - Avoid computing something multiple times.

def fahren_to_kelvin(fahren):
    """
    (num) -> num

    Convert degrees fahrenheit to degrees kelvin.

    >>> fahren_to_kelvin(-100)
    199.81666666666663
    >>> fahren_to_kelvin(0)
    255.3722222222222
    >>> fahren_to_kelvin(32)
    273.15
    >>> fahren_to_kelvin(100)
    310.92777777777775
    >>> fahren_to_kelvin(212)
    373.15
    """
    celsius = 5.0 / 9 * (fahren - 32)
    zero_celsius_in_kelvin = 273.15
    return celsius + zero_celsius_in_kelvin

print fahren_to_kelvin(212)
print


# The risk vs. the reward of using global variables.

# Risk -- consider the software system for an airline jet.
#      -- critical piece - flight control system.
#      -- non-critical piece - in-flight entertainment system.
# Both systems might use a variable named "dial", and we DON'T want the possibility
# that changing the volume on your audio might change the plane's flaps.

# Example:
num = 4

def fun1():
    global num
    num = 5

def fun2():
    global num
    num = 6

# Note that num changes after each call with no obvious explanation.
print num
fun1()
print num
fun2()
print num
print


# Global variables are an easy way for event handlers to communicate game information.
# There are safer methods, but they require more sophisticated object-programming techniques.


if __name__=="__main__":
    import doctest
    print doctest.testmod()
