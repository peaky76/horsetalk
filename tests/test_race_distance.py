from measurement.measures import Distance  # type: ignore
from horsetalk import RaceDistance


def test_race_distance_can_be_initialized_with_furlong_string():
    assert Distance(chain=50) == RaceDistance("5f")


def test_race_distance_can_be_initialized_with_mile_string():
    assert Distance(chain=80) == RaceDistance("1m")


def test_race_distance_can_be_initialized_with_mile_and_furlong_string():
    assert Distance(chain=130) == RaceDistance("1m5f")


def test_race_distance_can_be_initalized_with_mile_furlong_and_yard_string():
    assert Distance(chain=135) == RaceDistance("1m5f110y")


def test_race_distance_can_be_initalized_with_mile_furlong_and_yard_spaced_string():
    assert Distance(chain=135) == RaceDistance("1m 5f 110y")


def test_race_distance_can_be_initialize_with_metres_string():
    assert Distance(m=1609) == RaceDistance("1609m")


def test_race_distance_furlong_returns_correct_value():
    assert 13 == RaceDistance("1m5f").furlong
