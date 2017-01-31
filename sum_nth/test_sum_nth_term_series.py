
"""Tests for series_sum function."""


def test_series_sum1():
    """Test if return the sum of following series upto nth term(parameter)."""
    from sum_nth_term_series import series_sum
    assert series_sum(5) == "1.57"


def test_series_sum2():
    """Test if return the sum of following series upto nth term(parameter)."""
    from sum_nth_term_series import series_sum
    assert series_sum(1) == "1.00"


def test_series_sum3():
    """Test if return the sum of following series upto nth term(parameter)."""
    from sum_nth_term_series import series_sum
    assert series_sum(2) == "1.25"


def test_series_sum4():
    """Test if return the sum of following series upto nth term(parameter)."""
    from sum_nth_term_series import series_sum
    assert series_sum(3) == "1.39"


def test_series_sum0():
    """Test if return the sum of following series upto nth term(parameter)."""
    from sum_nth_term_series import series_sum
    assert series_sum(0) == "0.00"
