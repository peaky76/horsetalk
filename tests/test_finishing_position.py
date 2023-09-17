import pytest  # type: ignore
from horsetalk import FinishingPosition


def test_finishing_position_can_be_created_from_int_zero_meaning_unplaced():
    assert FinishingPosition(0)


def test_finishing_position_can_be_created_from_positive_int():
    assert FinishingPosition(3)


def test_finishing_position_can_be_created_from_positive_int_as_str():
    assert FinishingPosition("3")


def test_finishing_position_cannot_be_created_from_negative_int():
    with pytest.raises(ValueError):
        FinishingPosition(-1)


def test_finishing_position_repr():
    assert repr(FinishingPosition(2)) == "<FinishingPosition: 2nd>"


def test_finishing_position_repr_for_zero():
    assert repr(FinishingPosition(0)) == "<FinishingPosition: Unplaced>"


def test_finishing_position_str():
    assert str(FinishingPosition(2)) == "2nd"


def test_finishing_position_str_for_zero():
    assert str(FinishingPosition(0)) == "Unplaced"


def test_finishing_position_cannot_be_added():
    with pytest.raises(TypeError):
        FinishingPosition(1) + FinishingPosition(2)


def test_finishing_position_cannot_be_subtracted():
    with pytest.raises(TypeError):
        FinishingPosition(1) - FinishingPosition(2)


def test_finishing_position_cannot_be_multiplied():
    with pytest.raises(TypeError):
        FinishingPosition(1) * FinishingPosition(2)


def test_finishing_position_cannot_be_divided():
    with pytest.raises(TypeError):
        FinishingPosition(1) / FinishingPosition(2)


def test_finishing_position_equal_to():
    assert FinishingPosition(1) == FinishingPosition(1)


def test_finishing_position_less_than():
    assert FinishingPosition(2) < FinishingPosition(1)


def test_finishing_position_less_than_or_equal():
    assert FinishingPosition(2) <= FinishingPosition(1)


def test_finishing_position_greater_than():
    assert FinishingPosition(1) > FinishingPosition(2)


def test_finishing_position_greater_than_or_equal():
    assert FinishingPosition(1) >= FinishingPosition(2)
