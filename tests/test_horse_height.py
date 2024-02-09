from horsetalk import HorseHeight


def test_horse_height_can_be_initialized_with_hands_string():
    assert HorseHeight("16hh").hh == 16


def test_horse_height_can_be_initialized_with_inches_string():
    assert HorseHeight("64in").hh == 16


def test_horse_height_str_returns_correct_value():
    assert str(HorseHeight("64in")) == "16.0hh"
