import pytest
from horsetalk import Draw


def test_draw_can_be_initialized_with_integer():
    assert 1 == Draw(1).value


def test_draw_can_be_initialized_with_numeric_string():
    assert 1 == Draw("1").value


def test_draw_cannot_be_initialized_with_non_numeric_string():
    with pytest.raises(ValueError):
        Draw("a")


def test_draw_cannot_be_initialized_with_float():
    with pytest.raises(ValueError):
        Draw(1.0)
