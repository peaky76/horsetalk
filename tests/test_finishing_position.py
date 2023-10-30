import pytest  # type: ignore

from horsetalk import FinishingPosition


def test_finishing_position_can_be_created_from_int_zero_meaning_unplaced():
    assert FinishingPosition(0)


def test_finishing_position_can_be_created_from_positive_int():
    assert FinishingPosition(3)


def test_finishing_position_can_be_created_from_positive_int_as_str():
    assert FinishingPosition("3")


def test_finishing_position_can_be_created_from_positive_int_and_tied_bool():
    assert FinishingPosition(3, tied=True)


def test_finishing_position_cannot_be_created_from_negative_int():
    with pytest.raises(ValueError):
        FinishingPosition(-1)


def test_finishing_position_cannot_be_unplaced_and_tied():
    with pytest.raises(ValueError):
        FinishingPosition(0, tied=True)


def test_finishing_position_parse_correctly_handles_int():
    assert FinishingPosition.parse(3) == FinishingPosition(3)


def test_finishing_position_parse_correctly_handles_str():
    assert FinishingPosition.parse("3") == FinishingPosition(3)


def test_finishing_position_parse_correctly_handles_str_with_equals_prefix():
    assert FinishingPosition.parse("=3") == FinishingPosition(3, tied=True)


def test_finishing_position_parse_correctly_handles_str_with_equals_suffix():
    assert FinishingPosition.parse("3=") == FinishingPosition(3, tied=True)


def test_finishing_position_parse_correctly_handles_unplaced_str():
    assert FinishingPosition.parse("Unplaced") == FinishingPosition(0)


def test_finishing_position_parse_correctly_handles_unplaced_str_abbr():
    assert FinishingPosition.parse("UNPL") == FinishingPosition(0)


def test_finishing_position_tied_is_false_by_default():
    assert FinishingPosition(1).tied is False


def test_finish_position_tied_is_true_when_specified():
    assert FinishingPosition(1, tied=True).tied is True


def test_finishing_position_repr():
    assert repr(FinishingPosition(2)) == "<FinishingPosition: 2nd>"


def test_finishing_position_repr_for_zero():
    assert repr(FinishingPosition(0)) == "<FinishingPosition: Unplaced>"


def test_finishing_position_repr_when_tied():
    assert repr(FinishingPosition(2, tied=True)) == "<FinishingPosition: =2nd>"


def test_finishing_position_str():
    assert str(FinishingPosition(2)) == "2nd"


def test_finishing_position_str_for_zero():
    assert str(FinishingPosition(0)) == "Unplaced"


def test_finishing_position_str_when_tied():
    assert str(FinishingPosition(2, tied=True)) == "=2nd"


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


def test_finishing_position_eq_with_another_instance():
    assert FinishingPosition(1) == FinishingPosition(1)


def test_finishing_position_eq_with_another_instance_when_tied():
    assert FinishingPosition(1, tied=True) == FinishingPosition(1)


def test_finishing_position_eq_with_int():
    assert FinishingPosition(1) == 1


def test_finishing_position_eq_with_int_reverse():
    assert FinishingPosition(1) == 1


def test_finishing_position_less_than():
    assert FinishingPosition(2) < FinishingPosition(1)


def test_finishing_position_less_than_when_tied():
    assert FinishingPosition(2) < FinishingPosition(1, tied=True)


def test_finishing_position_less_than_or_equal():
    assert FinishingPosition(2) <= FinishingPosition(1)


def test_finishing_position_less_than_or_equal_when_tied():
    assert FinishingPosition(2) <= FinishingPosition(1, tied=True)


def test_finishing_position_greater_than():
    assert FinishingPosition(1) > FinishingPosition(2)


def test_finishing_position_greater_than_when_tied():
    assert FinishingPosition(1, tied=True) > FinishingPosition(2)


def test_finishing_position_greater_than_or_equal():
    assert FinishingPosition(1) >= FinishingPosition(2)


def test_finishing_position_greater_than_or_equal_when_tied():
    assert FinishingPosition(1, tied=True) >= FinishingPosition(2)
