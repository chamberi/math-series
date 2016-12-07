"""This module defines functions that implement mathematical series."""


def fibonacci(n):
    """Return the nth value in fibonacci series."""
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def iter_fibonacci(n):
    """Return the nth number of the Fibonacci sequence using iteration."""
    a = 0
    b = 1
    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        for num in range(n - 2):
            b = b + a
            a = b - a
        return b


def lucas(n):
    """Return the nth value in the lucas series using recursion."""
    if n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


def iter_lucas(n):
    """Return the nth value in the lucas series using iteration."""
# same model than the iter_fibonacci function


def sum_series(x, y=0, z=1):
    """Return the result of sum_series given x, optional arguments y, z."""
    if x == 0:
        return y
    elif x == 1:
        return z
    else:
        return sum_series((x - 1), y, z) + sum_series((x - 2), y, z)


if __name__ == "__main__":
    output = """
    This module defines functions that implement mathematical series.
    ...

    fibonacci(n):
    Returns the nth value in the fibonacci series

    lucas(n):
    return the nth value in the fibonacci series

    sum_series(x, y=0, z=1):
    return the xth value in this series based on the optional arguments y and z
    the option arguments will act are our base cases.

    """
    print(output)
    print("fibonnaci(2):", fibonacci(2))
    print("lucas(2):", lucas(2))
    print("sum_series(5, 7, 10):", sum_series(5, 7, 10))
