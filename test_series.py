"""This is the testing file for fibonacci and lucas math functions."""
import pytest


FIB_TABLE = [
    [1, 0],
    [2, 1],
    [3, 1],
    [4, 2],
    [5, 3],
    [6, 5],
    [7, 8],
    [8, 13],
]


LUC_TABLE = [
    [1, 2],
    [2, 1],
    [3, 3],
    [4, 4],
    [5, 7],
    [6, 11],
    [7, 18],
    [8, 29],
]

SUM_TABLE = [
    [0, 0, 1, 0],
    [0, 2, 1, 2],
    [1, 4, 5, 5],
    [1, 27, 29, 29],
    [2, 27, 29, 56],
    [3, 27, 29, 85],
    [4, 27, 29, 141],
]


@pytest.mark.parametrize("n, result", FIB_TABLE)
def test_iter_fibonacci(n, result):
    """Test fibonacci function against the results from our fib table."""
    from series import iter_fibonacci
    assert iter_fibonacci(n) == result


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


@pytest.mark.parametrize("x, y, z, result", SUM_TABLE)
def test_sum(x, y, z, result):
    """Test sum_series function."""
    from series import sum_series
    assert sum_series(x, y, z) == result
