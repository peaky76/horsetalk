import pytest
from horsetalk import Draw


def test_draw_can_be_initialized_with_integer():
    assert Draw(1) == 1


def test_draw_can_be_initialized_with_numeric_string():
    assert Draw("1") == 1


def test_draw_cannot_be_initialized_with_non_numeric_string():
    with pytest.raises(ValueError):
        Draw("a")


def test_draw_cannot_be_initialized_with_float():
    with pytest.raises(ValueError):
        Draw(1.0)


def test_draw_can_be_compared_with_gt():
    assert Draw(2) > Draw(1)


def test_draw_can_be_compared_with_lt():
    assert Draw(1) < Draw(2)


def test_draw_cannot_be_added():
    with pytest.raises(TypeError):
        Draw(1) + Draw(2)


def test_draw_cannot_be_subtracted():
    with pytest.raises(TypeError):
        Draw(1) - Draw(2)


def test_draw_cannot_be_multiplied():
    with pytest.raises(TypeError):
        Draw(1) * Draw(2)


def test_draw_cannot_be_divided():
    with pytest.raises(TypeError):
        Draw(1) / Draw(2)
