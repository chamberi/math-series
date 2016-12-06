"""This module defines functions that implement mathematical series."""


def fibonacci(n):
    """Return the nth value in fibonacci series."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
