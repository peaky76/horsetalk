from measurement.measures import Distance  # type: ignore

from horsetalk import HorseHeight


def test_horse_height_can_be_initialized_with_hands_string():
    assert Distance(inch=64) == HorseHeight("16hh")


def test_horse_height_can_be_initialized_with_inches_string():
    assert Distance(inch=64) == HorseHeight("64in")


def test_horse_height_hands_returns_correct_value():
    assert HorseHeight("64in").hand == 16


def test_horse_height_repr_returns_correct_value():
    assert repr(HorseHeight("64in")) == "<HorseHeight: 16hh>"


def test_horse_height_str_returns_correct_value():
    assert str(HorseHeight("64in")) == "16hh"
