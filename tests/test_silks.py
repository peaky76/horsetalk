from horsetalk import (
    Silks,
)


def test_silks_colour_can_be_created_from_name():
    assert Silks.Colour.BEIGE == Silks.Colour["BEIGE"]


def test_silks_colour_can_be_created_from_lowercase_name():
    assert Silks.Colour.BEIGE == Silks.Colour["beige"]


def test_silks_colour_can_be_created_from_spaced_name():
    assert Silks.Colour.DARK_BLUE == Silks.Colour["dark blue"]


def test_silks_shape_can_be_created_from_name():
    assert Silks.Shape.STAR == Silks.Shape["STAR"]


def test_silks_shape_can_be_created_from_lowercase_name():
    assert Silks.Shape.STAR == Silks.Shape["star"]


def test_silks_shape_can_be_created_from_spaced_name():
    assert Silks.Shape.INVERTED_TRIANGLE == Silks.Shape["Inverted triangle"]


def test_silks_parse_returns_dict():
    expected = dict
    actual = type(Silks.parse("orange and blue hoops, white sleeves, orange cap"))
    assert expected == actual
