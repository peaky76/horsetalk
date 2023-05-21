from horsetalk import (
    Silks,
)


def test_race_title_parse_returns_dict():
    expected = dict
    actual = type(Silks.parse("orange and blue hoops, white sleeves, orange cap"))
    assert expected == actual
