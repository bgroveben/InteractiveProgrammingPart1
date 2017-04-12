# http://www.codeskulptor.org/#examples-functions.py

# Computes the area of a triangle:
def triangle_area(base, height):      # header - ends in colon
    area = (1.0 / 2) * base * height  # body - all of the body is indented
    return area                       # body - return outputs value

print
a1 = triangle_area(3, 8)
print a1
a2 = triangle_area(14, 2)
print a2
print


# Convert fahrenheit to celsius:
def fahrenheit2celsius(fahrenheit):
    celsius = (5.0 / 9) * (fahrenheit - 32)
    return celsius

# Now test...
c1 = fahrenheit2celsius(32)
c2 = fahrenheit2celsius(212)
print c1, c2
print


# Convert fahrenheit to kelvin:
def fahrenheit2kelvin(fahrenheit):
    celsius = fahrenheit2celsius(fahrenheit)
    kelvin = celsius + 273.15
    return kelvin

# Now test...
k1 = fahrenheit2kelvin(32)
k2 = fahrenheit2kelvin(212)
print k1, k2
print


# Now let's print us some hello world:
def hello():
    print "Hello World!"

# And some more tests...
hello()      # Call to hello prints "Hello World!".
h = hello()  # Call to hello prints "Hello World!" a second time.
print h      # Prints None because there is no return value in the hello() function.
print
