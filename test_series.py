"""This is the testing file for fibonacci and lucas mather functions."""


def test1():
    """Test fibonacci for 0 == 0."""
    from series import fibonacci
    # if n == 0:
    assert fibonacci(0) == 0
