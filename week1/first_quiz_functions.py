### Functions from Week 1 Quiz 1 ###
# Continued at #8

def polynomial(x):
    """
    (num) -> num

    Implement the mathematical function f(x) = -5x^5 + 69x^2 - 47 as a Python function.
    Then use Python to compute the function values f(0), f(1), f(2), and f(3).
    Return the maximum of these four values calculated.

    >>> polynomial(0)
    -47
    >>> polynomial(1)
    17
    >>> polynomial(2)
    69
    >>> polynomial(3)
    -641
    """
    result = (-5 * x**5) + (69 * x**2) - 47
    return result


def future_value(present_value, annual_rate, periods_per_year, years):
    """
    (num, float, num, num) -> float

    When investing money, an important concept to know is compound interest.
    The equation:
    FV = PV(1 + rate)^periods
    relates the following four quantities:
    The present value (PV) of your money is how much money you have now.
    The future value (FV) of your money is how much money you will have in the future.
    The nominal interest rate per period (rate) is how much interest you earn during a particular
    length of time, before accounting for compounding. This is typically expressed as a percentage.
    The number of periods (periods) is how many periods in the future this calculation is for.

    Write a Python function that returns the future value based on present_value, annual_rate,
    periods_per_year, and years.

    >>> future_value(500, .04, 10, 10)
    745.3174428239327
    >>> future_value(1000, .02, 365, 3)
    1061.8348011259045
    """
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    future_value = present_value * (1 + rate_per_period) ** periods
    return future_value


print
print "$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3)
print


if __name__=="__main__":
    import doctest
    print doctest.testmod()
