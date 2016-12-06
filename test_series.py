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


@pytest.mark.parametrize("n, result", FIB_TABLE)
def test_fibonacci(n, result):
    """Test fibonacci for 0 == 0."""
    from series import fibonacci
    assert fibonacci(n) == result
