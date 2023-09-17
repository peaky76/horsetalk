import pytest  # type: ignore
from horsetalk import Disaster, RacePerformance


def test_race_performance_init_with_int():
    performance = RacePerformance(1)
    assert performance.finishing_position == "1"
    assert performance.official_position == "1"
    assert performance.disaster is None


def test_race_performance_init_with_digit_str():
    performance = RacePerformance("1")
    assert performance.finishing_position == "1"
    assert performance.official_position == "1"
    assert performance.disaster is None


def test_race_performance_init_with_disaster():
    performance = RacePerformance("F")
    assert performance.finishing_position is None
    assert performance.official_position is None
    assert performance.disaster.name == "FELL"


def test_race_performance_init_with_disaster_enum():
    performance = RacePerformance(Disaster.FELL)
    assert performance.finishing_position is None
    assert performance.official_position is None
    assert performance.disaster.name == "FELL"


def test_race_performance_init_with_official_position():
    performance = RacePerformance("2", official_position=1)
    assert performance.finishing_position == "2"
    assert performance.official_position == "1"
    assert performance.disaster is None


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
