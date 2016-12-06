"""This module defines functions that implement mathematical series."""


def fibonacci(n):
    """Return the nth value in fibonacci series."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """Return the nth value in the lucas series."""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(x, y=0, z=1):
    """Return the result of sum_series given x, optional arguments y, z."""
    if x == 0:
        return y
    elif x == 1:
        return z
    else:
        return sum_series(x - 1) + sum_series(x - 2)
