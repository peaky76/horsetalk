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


def test_silks_element_equal_to_itself():
    element = Silks.Element(Silks.Colour.ORANGE)
    assert element == element


def test_silks_element_equal_to_other_element_with_same_primary_colour():
    element1 = Silks.Element(Silks.Colour.ORANGE)
    element2 = Silks.Element(Silks.Colour.ORANGE)
    assert element1 == element2


def test_silks_element_repr():
    expected = (
        "Element(primary=Colour.ORANGE, secondary=Colour.ORANGE, pattern=Pattern.PLAIN)"
    )
    actual = repr(Silks.Element(Silks.Colour.ORANGE))
    assert expected == actual


def test_silks_parse_returns_instance_of_silks():
    expected = Silks
    actual = type(Silks.parse("orange and blue hoops, white sleeves, orange cap"))
    assert expected == actual


def test_silks_parts_returns_correct_split():
    expected = ["orange and blue hoops", "white sleeves", "orange cap"]

    silks = Silks()
    silks.description = "Orange and blue hoops, white sleeves, orange cap"
    actual = silks._parts()
    assert expected == actual


def test_silks_words_returns_correct_split_when_separate_words():
    expected = ["orange", "white", "hooped"]

    silks = Silks()
    actual = silks._words("orange and white hooped cap")
    assert expected == actual


def test_silks_words_returns_correct_split_when_double_barrelled_colour():
    expected = ["dark blue", "white", "hooped"]

    silks = Silks()
    actual = silks._words("dark blue and white hooped cap")
    assert expected == actual


def test_silks_words_returns_correct_split_when_triple_barrelled_pattern():
    expected = ["green", "cross of lorraine"]

    silks = Silks()
    actual = silks._words("green cross of lorraine")
    assert expected == actual


def test_silks_words_returns_correct_split_when_location_specified():
    expected = ["green", "white", "hoops"]

    silks = Silks()
    actual = silks._words("green and white hoops on sleeves")
    assert expected == actual


def test_silks_body_returns_correct_element():
    expected = Silks.Element(Silks.Colour.ORANGE)

    silks = Silks()
    silks.description = "Orange, white sleeves, orange cap"

    assert expected == silks.body


def test_silks_body_returns_correct_element_when_pattern_specified():
    expected = Silks.Element(
        Silks.Colour.DARK_BLUE, Silks.Colour.RED, Silks.Pattern.STRIPE
    )

    silks = Silks()
    silks.description = "Dark blue, red stripe, pink sleeves and cap"

    assert expected == silks.body


def test_silks_cap_returns_correct_element():
    expected = Silks.Element(Silks.Colour.ORANGE)

    silks = Silks()
    silks.description = "Orange and blue hoops, white sleeves, orange cap"

    assert expected == silks.cap


def test_silks_cap_returns_correct_element_when_joined_with_sleeves():
    expected = Silks.Element(Silks.Colour.ORANGE)

    silks = Silks()
    silks.description = "Orange and blue hoops, orange sleeves and cap"

    assert expected == silks.cap


def test_silks_cap_returns_correct_element_when_pattern_specified():
    expected = Silks.Element(
        Silks.Colour.ORANGE, Silks.Colour.WHITE, Silks.Pattern.HOOPS
    )

    silks = Silks()
    silks.description = "Orange and blue hoops, orange and white hooped sleeves and cap"

    assert expected == silks.cap


def test_silks_sleeves_returns_correct_element():
    expected = Silks.Element(Silks.Colour.WHITE)

    silks = Silks()
    silks.description = "Orange and blue hoops, white sleeves, orange cap"

    assert expected == silks.sleeves


def test_silks_sleeves_returns_correct_element_when_joined_with_cap():
    expected = Silks.Element(Silks.Colour.WHITE)

    silks = Silks()
    silks.description = "Orange and blue hoops, white sleeves and cap"

    assert expected == silks.sleeves


def test_silks_sleeves_returns_correct_element_when_pattern_specified():
    expected = Silks.Element(
        Silks.Colour.ORANGE, Silks.Colour.WHITE, Silks.Pattern.HOOPS
    )

    silks = Silks()
    silks.description = "Orange and blue hoops, orange and white hooped sleeves and cap"

    assert expected == silks.sleeves


def test_silks_sleeves_returns_correct_element_when_colour_not_specified():
    expected = Silks.Element(
        Silks.Colour.DARK_BLUE, Silks.Colour.RED, Silks.Pattern.HALVED
    )

    silks = Silks()
    silks.description = "Dark blue, red stripe, halved sleeves, red cap"

    assert expected == silks.sleeves
