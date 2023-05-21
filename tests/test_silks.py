from horsetalk import (
    Silks,
)


def test_silks_shape_can_be_created_from_name():
    assert Silks.Shape.STAR == Silks.Shape["STAR"]


def test_headgear_can_be_created_from_lowercase_name():
    assert Silks.Shape.STAR == Silks.Shape["star"]


def test_headgear_can_be_created_from_spaced_name():
    assert Silks.Shape.INVERTED_TRIANGLE == Silks.Shape["Inverted triangle"]


def test_silks_parse_returns_dict():
    expected = dict
    actual = type(Silks.parse("orange and blue hoops, white sleeves, orange cap"))
    assert expected == actual
