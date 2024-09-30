import re

import pytest

from horsetalk import RaceDistance


def test_race_distance_regex_with_mile_furlong_and_yard_string():
    assert re.fullmatch(RaceDistance.REGEX, "1m5f110y")


def test_race_distance_regex_with_mile_furlong_and_yard_spaced_string():
    assert re.fullmatch(RaceDistance.REGEX, "1m 5f 110y")


def test_race_distance_regex_with_mile_furlong_and_yard_full_string():
    assert re.fullmatch(RaceDistance.REGEX, "1 mile 5 furlongs 110 yards")


def test_race_distance_regex_with_yards_only_full_string():
    assert re.fullmatch(RaceDistance.REGEX, "250 yards")


def test_race_distance_regex_with_mile_and_furlong_string():
    assert re.fullmatch(RaceDistance.REGEX, "1m5f")


def test_race_distance_regex_with_mile_string():
    assert re.fullmatch(RaceDistance.REGEX, "1m")


def test_race_distance_regex_with_furlong_string():
    assert re.fullmatch(RaceDistance.REGEX, "5f")


def test_race_distance_regex_with_metres_string():
    assert re.fullmatch(RaceDistance.REGEX, "1609m")


def test_race_distance_can_be_initialised_with_furlong_string():
    assert RaceDistance("5f").yd == pytest.approx(1100)


def test_race_distance_can_be_initialised_with_mile_string():
    assert RaceDistance("1m").yd == pytest.approx(1760)


def test_race_distance_can_be_initialised_with_mile_and_furlong_string():
    assert RaceDistance("1m5f").yd == pytest.approx(2860)


def test_race_distance_can_be_initialised_with_decimal_furlong_string():
    assert RaceDistance("13.0f").yd == pytest.approx(2860)


def test_race_distance_can_be_initialised_with_mile_furlong_and_yard_string():
    assert RaceDistance("1m5f110y").yd == pytest.approx(2970)


def test_race_distance_can_be_initialised_with_mile_furlong_and_yard_full_string():
    assert RaceDistance("1 mile 5 furlongs 110 yards").yd == pytest.approx(2970)


def test_race_distance_can_be_initialised_with_yards_only_full_string():
    assert RaceDistance("250 yards").yd == pytest.approx(250)


def test_race_distance_can_be_initialised_with_mile_furlong_and_yard_spaced_string():
    assert RaceDistance("1m 5f 110y").yd == pytest.approx(2970)


def test_race_distance_can_be_initialised_with_metres_string():
    assert RaceDistance("1609m").km == 1.609


def test_race_distance_can_be_initialised_with_metres_string_with_comma():
    assert RaceDistance("1,609m").km == 1.609


def test_race_distance_can_be_initialised_with_standard_input():
    assert RaceDistance(km=1.609).km == 1.609


def test_race_distance_init_errors_if_invalid_string():
    with pytest.raises(AttributeError):
        RaceDistance("1m 5f Ny")


def test_race_distance_str():
    assert str(RaceDistance("1m5f110y")) == "1m 5f 110y"


def test_race_distance_str_when_zero_value_present():
    assert str(RaceDistance("1m5f0y")) == "1m 5f"
