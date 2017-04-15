### Conditionals Examples ###

# Let's give away (or take away) some money to illustrate coditionals in action:
def greet(friend, money):
    """
    (bool, num) -> num

    Find out if someone you meet is a friend or not.
    If they are a friend and you don't have enough money, greet them.
    If they are a friend and you have enough money, greet them and give them $20.
    If they are a stranger, mug them and take their money, because you are a bad person.

    >>> money = 15
    >>> money = greet(True, money)
    Hello
    >>> money = greet(False, money)
    Gimme Yo Money!
    >>> money = greet(True, money)
    Hi!
    """
    if friend and (money > 20):
        print "Hi!"
        money = money - 20
    elif friend:
        print "Hello"
    else:
        print "Gimme Yo Money!"
        money = money + 10
    return money

money = 15

print
money = greet(True, money)
print "Money:", money
print

money = greet(False, money)
print "Money:", money
print

money = greet(True, money)
print "Money:", money
print


# Is it a leap year?
def is_leap_year(year):
    """
    (int) -> bool

    Return True if year is a leap year, False otherwise.

    >>> is_leap_year(1600)
    True
    >>> is_leap_year(1610)
    False
    >>> is_leap_year(2012)
    True
    >>> is_leap_year(2103)
    False
    """
    if (year % 400) == 0:
        return True
    elif (year % 100) == 0:
        return False
    elif (year % 4) == 0:
        return True
    else:
        return False

year = 2017  # Change this to try different years.
leap_year = is_leap_year(year)

if leap_year:
    print year, "is a leap year."
else:
    print year, "is not a leap year."
print


if __name__ == '__main__':
    import doctest
    doctest.testmod()
