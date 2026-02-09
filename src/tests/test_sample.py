# https://docs.pytest.org/en/stable/#a-quick-example


def inc(x: int) -> int:
    """Increment a number by one.

    Args:
        x: The number to increment.

    Returns:
        The input number incremented by one.
    """
    return x + 1


def test_answer() -> None:
    """Test that the inc function correctly increments a number."""
    assert inc(3) == 4
