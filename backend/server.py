def double_it(x: int) -> int:
    return x * 2  # this looks good, right?

def test_double_it():
    assert double_it(2) == 4
    assert double_it(3) == 6
