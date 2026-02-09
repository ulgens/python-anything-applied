# https://docs.pytest.org/en/stable/#a-quick-example
from python_anything_applied import increment


def test_answer():
    assert increment(3) == 4
