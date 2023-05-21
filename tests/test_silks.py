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


def test_silks_element_can_be_initialised_with_single_colour():
    assert Silks.Element(Silks.Colour.ORANGE)


def test_silks_element_initialised_with_single_colour_sets_right_pattern():
    assert Silks.Pattern.PLAIN == Silks.Element(Silks.Colour.ORANGE).pattern


def test_silks_element_initialised_with_single_colour_sets_secondary_colour_to_same():
    assert Silks.Colour.ORANGE == Silks.Element(Silks.Colour.ORANGE).secondary


def test_silks_parse_returns_dict():
    expected = dict
    actual = type(Silks.parse("orange and blue hoops, white sleeves, orange cap"))
    assert expected == actual


def test_silks_parts_returns_correct_split():
    expected = ["orange and blue hoops", "white sleeves", "orange cap"]

    silks = Silks()
    silks.description = "Orange and blue hoops, white sleeves, orange cap"
    actual = silks._parts()
    assert expected == actual
