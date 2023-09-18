import pytest  # type: ignore
from horsetalk import Disaster, FinishingPosition, Outcome, RacePerformance


def test_race_performance_init_with_int_sets_outcome():
    performance = RacePerformance(1)
    assert performance.outcome == FinishingPosition(1)


def test_race_performance_init_with_int_sets_official_position():
    performance = RacePerformance(1)
    assert performance.official_position == FinishingPosition(1)


def test_race_performance_init_with_digit_str_sets_outcome():
    performance = RacePerformance("1")
    assert performance.outcome == FinishingPosition(1)


def test_race_performance_init_with_digit_str_sets_official_position():
    performance = RacePerformance("1")
    assert performance.official_position == FinishingPosition(1)


def test_race_performance_init_with_disaster_sets_outcome():
    performance = RacePerformance("F")
    assert performance.outcome == Disaster.FELL


def test_race_performance_init_with_disaster_sets_official_position():
    performance = RacePerformance("F")
    assert performance.official_position is None


def test_race_performance_init_with_disaster_enum_sets_outcome():
    performance = RacePerformance(Disaster.FELL)
    assert performance.outcome == Disaster.FELL


def test_race_performance_init_with_disaster_enum_sets_official_position():
    performance = RacePerformance(Disaster.FELL)
    assert performance.official_position is None


def test_race_performance_init_with_official_position_sets_outcome():
    performance = RacePerformance("2", official_position=1)
    assert performance.outcome == FinishingPosition(2)


def test_race_performance_init_with_official_position_sets_official_position():
    performance = RacePerformance("2", official_position=1)
    assert performance.official_position == FinishingPosition(1)


def test_race_performance_raises_error_if_str_not_valid():
    with pytest.raises(ValueError):
        RacePerformance("X")


def test_race_performace_raises_error_if_position_and_disaster_given():
    with pytest.raises(ValueError):
        RacePerformance("F", official_position="6")


def test_race_performance_repr_with_disaster():
    performance = RacePerformance("F")
    assert repr(performance) == "<RacePerformance: Disaster.FELL>"


def test_race_performance_repr_with_position():
    performance = RacePerformance("2")
    assert repr(performance) == "<RacePerformance: 2>"


def test_race_performance_repr_with_different_official_position():
    performance = RacePerformance("2", official_position="1")
    assert repr(performance) == "<RacePerformance: 2, placed 1>"


def test_race_performance_str_with_disaster():
    performance = RacePerformance("F")
    assert str(performance) == "Fell"


def test_race_performance_str_with_position():
    performance = RacePerformance("2")
    assert str(performance) == "2nd"


def test_race_performance_str_with_different_official_position():
    performance = RacePerformance("2", official_position="1")
    assert str(performance) == "2nd, placed 1st"
