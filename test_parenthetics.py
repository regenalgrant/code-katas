"""Test the proper_parenthetics module."""
import pytest


OPEN_TABLE = [
    ["(", 1],
    ["((", 1],
    ["()(", 1],
    ["()", 0],
    ["(())", 0],
    [")(", -1],
    ["(()))(", -1],
]


@pytest.mark.parametrize("test_val, result", OPEN_TABLE)
def test_parenthetics(test_val, result):
    """Test set for proper return."""
    from parenthetics import parenthetics
    assert parenthetics(test_val) == result
