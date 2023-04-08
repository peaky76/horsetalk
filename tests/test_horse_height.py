from horsetalk import HorseHeight
from measurement.measures import Distance  # type: ignore


def test_horse_height_can_be_initialized_with_hands_string():
    assert Distance(inch=64) == HorseHeight("16hh")


def test_horse_height_can_be_initialized_with_inches_string():
    assert Distance(inch=64) == HorseHeight("64in")


def test_horse_height_hands_returns_correct_value():
    assert 16 == HorseHeight("64in").hand
