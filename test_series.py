"""This is the testing file for fibonacci and lucas math functions."""
import pytest


FIB_TABLE = [
    [0, 0],
    [1, 1],
    [2, 1],
    [3, 2],
    [4, 3],
    [5, 5],
    [6, 8],
    [7, 13],
]

LUC_TABLE = [
    [0, 2],
    [1, 1],
    [2, 3],
    [3, 4],
    [4, 7],
    [5, 11],
    [6, 18],
    [7, 29],
]


@pytest.mark.parametrize("n, result", FIB_TABLE)
def test_fibonacci(n, result):
    """Test fibonacci function against the results from our fib table."""
    from series import fibonacci
    assert fibonacci(n) == result


@pytest.mark.parametrize("n, result", LUC_TABLE)
def test_lucas(n, result):
    """Test lucas function against the results from our luc table."""
    from series import lucas
    assert lucas(n) == result
