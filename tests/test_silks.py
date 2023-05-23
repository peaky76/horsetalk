from horsetalk import (
    Silks,
)
from tests.fixtures.silks import SILKS_INPUT, SILKS_OUTPUT


def test_silks_colour_can_be_created_from_name():
    assert Silks.Colour.BEIGE == Silks.Colour["BEIGE"]


def test_silks_colour_can_be_created_from_lowercase_name():
    assert Silks.Colour.BEIGE == Silks.Colour["beige"]


def test_silks_colour_can_be_created_from_spaced_name():
    assert Silks.Colour.DARK_BLUE == Silks.Colour["dark blue"]


def test_silks_colour_phrases():
    assert "dark blue" in Silks.Colour.phrases()


def test_silks_pattern_can_be_created_from_name():
    assert Silks.Pattern.STAR == Silks.Pattern["STAR"]


def test_silks_pattern_can_be_created_from_lowercase_name():
    assert Silks.Pattern.STAR == Silks.Pattern["star"]


def test_silks_pattern_can_be_created_from_spaced_name():
    assert Silks.Pattern.INVERTED_TRIANGLE == Silks.Pattern["Inverted triangle"]


def test_silks_pattern_phrases():
    assert "inverted triangle" in Silks.Pattern.phrases()


def test_silks_pattern_phrases_contains_aliases():
    assert "hooped" in Silks.Pattern.phrases()


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


def test_silks_conjoin_words_returns_correct_value_when_simple():
    expected = ["orange", "white", "hooped"]
    actual = Silks._conjoin_words(["orange", "white", "hooped"])
    assert expected == actual


def test_silks_conjoin_words_returns_correct_value_when_double_barrelled_colour():
    expected = ["dark blue", "white", "hooped"]
    actual = Silks._conjoin_words(["dark", "blue", "white", "hooped"])
    assert expected == actual


def test_silks_conjoin_words_returns_correct_value_when_triple_barrelled_pattern():
    expected = ["green", "cross of lorraine"]
    actual = Silks._conjoin_words(["green", "cross", "of", "lorraine"])
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
    silks.description = "Orange and dark blue hoops, white sleeves, orange cap"

    assert expected == silks.cap


def test_silks_cap_returns_correct_element_when_joined_with_sleeves():
    expected = Silks.Element(Silks.Colour.ORANGE)

    silks = Silks()
    silks.description = "Orange and dark blue hoops, orange sleeves and cap"

    assert expected == silks.cap


def test_silks_cap_returns_correct_element_when_pattern_specified():
    expected = Silks.Element(
        Silks.Colour.ORANGE, Silks.Colour.WHITE, Silks.Pattern.HOOPS
    )

    silks = Silks()
    silks.description = (
        "Orange and dark blue hoops, orange and white hooped sleeves and cap"
    )

    assert expected == silks.cap


def test_silks_sleeves_returns_correct_element():
    expected = Silks.Element(Silks.Colour.WHITE)

    silks = Silks()
    silks.description = "Orange and dark blue hoops, white sleeves, orange cap"

    assert expected == silks.sleeves


def test_silks_sleeves_returns_correct_element_when_joined_with_cap():
    expected = Silks.Element(Silks.Colour.WHITE)

    silks = Silks()
    silks.description = "Orange and dark blue hoops, white sleeves and cap"

    assert expected == silks.sleeves


def test_silks_sleeves_returns_correct_element_when_pattern_specified():
    expected = Silks.Element(
        Silks.Colour.ORANGE, Silks.Colour.WHITE, Silks.Pattern.HOOPS
    )

    silks = Silks()
    silks.description = (
        "Orange and dark blue hoops, orange and white hooped sleeves and cap"
    )

    assert expected == silks.sleeves


def test_silks_sleeves_returns_correct_element_when_colour_not_specified():
    expected = Silks.Element(
        Silks.Colour.DARK_BLUE, Silks.Colour.RED, Silks.Pattern.HALVED
    )

    silks = Silks()
    silks.description = "Dark blue, red stripe, halved sleeves, red cap"

    assert expected == silks.sleeves


def test_silks_clauses_returns_correct_value_when_and_conjoins_colours():
    expected = [
        ["beige", "black", "hoops"],
        ["white", "sleeves"],
        ["beige", "cap"],
        ["black", "star"],
    ]

    silks = Silks()
    silks.description = "Beige and black hoops, white sleeves, beige cap, black star"

    assert expected == silks._clauses


def test_silks_clauses_returns_correct_value_when_and_conjoins_shape_and_element():
    expected = [
        ["beige"],
        ["dark blue", "cross of lorraine"],
        ["dark blue", "sleeves"],
        ["dark blue", "cap"],
        ["beige", "star"],
    ]

    silks = Silks()
    silks.description = (
        "Beige, dark blue cross of lorraine and sleeves, dark blue cap, beige star"
    )

    assert expected == silks._clauses


def test_silks_clauses_returns_correct_value_when_and_conjoins_element_and_element():
    expected = [
        ["beige"],
        ["dark blue", "cross of lorraine"],
        ["dark blue", "sleeves"],
        ["dark blue", "cap"],
    ]

    silks = Silks()
    silks.description = "Beige, dark blue cross of lorraine, dark blue sleeves and cap"

    assert expected == silks._clauses


def test_silks_clauses_returns_correct_element_when_and_conjoins_element_and_element_and_pattern_specified():
    expected = [
        ["orange", "dark blue", "hoops"],
        ["orange", "white", "hooped", "sleeves"],
        ["orange", "white", "hooped", "cap"],
    ]

    silks = Silks()
    silks.description = (
        "Orange and dark blue hoops, orange and white hooped sleeves and cap"
    )

    assert expected == silks._clauses


# def test_silks_en_masse():
#     for silks_in, silks_out in zip(SILKS_INPUT, SILKS_OUTPUT):
#         silks = Silks.parse(silks_in)
#         body = Silks.Element(*silks_out[0])
#         sleeves = Silks.Element(*silks_out[1])
#         cap = Silks.Element(*silks_out[2])

#         assert body == silks.body
#         assert sleeves == silks.sleeves
#         assert cap == silks.cap
