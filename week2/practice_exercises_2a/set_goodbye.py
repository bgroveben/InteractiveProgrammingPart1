# 2. set_goodbye()

def set_goodbye():
    """
    () -> NoneType

    Write a Python function set_goodbye() that updates a global variable message with
    the value "Goodbye" and prints the value of this global variable to the console.
    Note that the existing global variable message has its original value "Hello"
    modified to "Goodbye" during the call to set_goodbye().

    About the doctests:
    http://stackoverflow.com/questions/39238675/modifying-global-variables-in-doctests
    https://docs.python.org/2.7/library/doctest.html#what-s-the-execution-context
    and:
    http://stackoverflow.com/questions/13106118/object-reuse-in-python-doctest
    https://docs.python.org/2/library/doctest.html#doctest.testmod

    >>> message = "Hello"
    >>> print message
    Hello
    >>> set_goodbye()
    Goodbye
    >>> print message
    Hello
    """
    global message
    message = "Goodbye"
    print message

# Tests
message = "Hello"
print message
set_goodbye()
print message

message = "Ciao"
print message
set_goodbye()
print message

if __name__ == '__main__':
    import doctest
    print doctest.testmod(extraglobs={'message': 'Hello'})
