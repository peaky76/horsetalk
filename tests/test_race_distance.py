from measurement.measures import Distance  # type: ignore
from horsetalk import RaceDistance


def test_race_distance_can_be_initialized_with_furlong_string():
    assert Distance(chain=50) == RaceDistance("5f")


def test_race_distance_can_be_initialized_with_mile_string():
    assert Distance(chain=80) == RaceDistance("1m")


def test_race_distance_can_be_initialized_with_mile_and_furlong_string():
    assert Distance(chain=130) == RaceDistance("1m5f")


def test_race_distance_furlong_returns_correct_value():
    assert 13 == RaceDistance("1m5f").furlong
