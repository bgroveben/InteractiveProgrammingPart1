# 1. print_goodbye()


def print_goodbye():
    """
    () -> NoneType

    Define a local variable whose value is "Goodbye" and prints the value of this local
    variable to the console.
    Note that the existing global variable message retains its original value of "Hello"
    after the call to print_goodbye().

    >>> message = "Hello"
    >>> print_goodbye()
    Goodbye
    >>> print message
    Hello
    """
    message = "Goodbye"
    print message

# Tests
message = "Hello"
print message
print_goodbye()
print message

message = "Ciao"
print message
print_goodbye()
print message


if __name__ == '__main__':
    import doctest
    print doctest.testmod()
