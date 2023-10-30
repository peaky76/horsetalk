from measurement.measures import Distance  # type: ignore

from horsetalk import HorseHeight


def test_horse_height_can_be_initialized_with_hands_string():
    assert Distance(inch=64) == HorseHeight("16hh")


def test_horse_height_can_be_initialized_with_inches_string():
    assert Distance(inch=64) == HorseHeight("64in")


def test_horse_height_hands_returns_correct_value():
    assert 16 == HorseHeight("64in").hand


def test_horse_height_repr_returns_correct_value():
    assert "<HorseHeight: 16hh>" == repr(HorseHeight("64in"))


def test_horse_height_str_returns_correct_value():
    assert "16hh" == str(HorseHeight("64in"))
