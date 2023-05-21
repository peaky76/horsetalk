from horsetalk import (
    Silks,
)


def test_silks_colour_can_be_created_from_name():
    assert Silks.Colour.BEIGE == Silks.Colour["BEIGE"]


def test_silks_colour_can_be_created_from_lowercase_name():
    assert Silks.Colour.BEIGE == Silks.Colour["beige"]


def test_silks_colour_can_be_created_from_spaced_name():
    assert Silks.Colour.DARK_BLUE == Silks.Colour["dark blue"]


def test_silks_pattern_can_be_created_from_name():
    assert Silks.Pattern.STAR == Silks.Pattern["STAR"]


def test_silks_pattern_can_be_created_from_lowercase_name():
    assert Silks.Pattern.STAR == Silks.Pattern["star"]


def test_silks_pattern_can_be_created_from_spaced_name():
    assert Silks.Pattern.INVERTED_TRIANGLE == Silks.Pattern["Inverted triangle"]


def test_silks_parse_returns_dict():
    expected = dict
    actual = type(Silks.parse("orange and blue hoops, white sleeves, orange cap"))
    assert expected == actual
