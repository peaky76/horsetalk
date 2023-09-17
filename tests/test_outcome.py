import pytest
from horsetalk import Disaster, FinishingPosition, Outcome


def test_outcome_can_be_created_with_finishing_position():
    assert Outcome(FinishingPosition(1))


def test_outcome_can_be_created_with_disaster():
    assert Outcome(Disaster.FELL)


def test_outcome_can_be_created_with_disaster_as_str():
    assert Outcome("FELL")


def test_outcome_can_be_created_with_finishing_position_as_str():
    assert Outcome("1")


def test_outcome_cannot_be_created_with_invalid_arg():
    with pytest.raises(ValueError):
        Outcome(1.0)


def test_outcome_value_is_finishing_position_if_init_with_int():
    assert isinstance(Outcome(1)._value, FinishingPosition)


def test_outcome_value_is_disaster_if_init_with_disaster_str():
    assert isinstance(Outcome("FELL")._value, Disaster)


def test_outcome_equal_between_disasters():
    assert Outcome(Disaster.FELL) == Outcome(Disaster.RAN_OUT)


def test_outcome_equal_between_disaster_and_finishing_position():
    assert not Outcome(Disaster.FELL) == Outcome(FinishingPosition(0))


def test_outcome_lt_between_disasters():
    assert not Outcome(Disaster.FELL) < Outcome(Disaster.RAN_OUT)


def test_outcome_lt_between_disaster_and_finishing_position():
    assert Outcome(Disaster.RAN_OUT) < Outcome(FinishingPosition(1))


def test_outcome_lte_between_disasters():
    assert Outcome(Disaster.FELL) <= Outcome(Disaster.RAN_OUT)


def test_outcome_lte_between_disaster_and_finishing_position():
    assert Outcome(Disaster.RAN_OUT) <= Outcome(FinishingPosition(1))


def test_outcome_gt_between_disasters():
    assert not Outcome(Disaster.FELL) > Outcome(Disaster.RAN_OUT)


def test_outcome_gt_between_disaster_and_finishing_position():
    assert Outcome(FinishingPosition(1)) > Outcome(Disaster.RAN_OUT)


def test_outcome_gte_between_disasters():
    assert Outcome(Disaster.FELL) >= Outcome(Disaster.RAN_OUT)


def test_outcome_gte_between_disaster_and_finishing_position():
    assert Outcome(FinishingPosition(1)) >= Outcome(Disaster.RAN_OUT)