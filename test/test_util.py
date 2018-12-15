from quickstats.util import bytes_to_human
import pytest


@pytest.mark.parametrize("test_int_input, expected", [
    (0, "0.0"),
    (1, "1.0"),
    (100, "100.0"),
    (10000, "9.8 K"),
    (1000000, "976.6 K"),
    (1000000000, "953.7 M")
])
def test_int_input(test_int_input, expected):
    # Test that integer input produces correct output
    result = bytes_to_human(test_int_input)
    assert result == expected


@pytest.mark.parametrize("test_float_input, expected", [
    (1e4, "9.8 K"),
    (1e6, "976.6 K"),
    (1e9, "953.7 M"),
    (1e12, "931.3 G"),
])
def test_float_input(test_float_input, expected):
    # Test that float input produces correct output
    result = bytes_to_human(test_float_input)
    assert result == expected


def test_negative_input():
    # Test that a negative input raises an exception
    with pytest.raises(ValueError):
        result = bytes_to_human(-1)


def test_string_input():
    # Test that a string input raises an exception
    with pytest.raises(ValueError):
        result = bytes_to_human('a')
