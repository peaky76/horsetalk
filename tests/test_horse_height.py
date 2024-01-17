from horsetalk import HorseHeight


def test_horse_height_can_be_initialized_with_hands_string():
    assert isinstance(HorseHeight("16hh"), HorseHeight)


def test_horse_height_can_be_initialized_with_inches_string():
    assert isinstance(HorseHeight("64in"), HorseHeight)


def test_horse_height_hands_returns_correct_value():
    assert HorseHeight("64in").hand == 16


def test_horse_height_repr_returns_correct_value():
    assert repr(HorseHeight("64in")) == "<HorseHeight: 16.0hh>"


def test_horse_height_str_returns_correct_value():
    assert str(HorseHeight("64in")) == "16.0hh"
