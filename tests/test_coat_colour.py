from horsetalk.coat_colour import CoatColour


def test_coat_colour_can_be_created_from_enum():
    assert CoatColour(1) == CoatColour.BAY


def test_coat_colour_can_be_created_from_name():
    assert CoatColour["BAY"] == CoatColour.BAY


def test_coat_colour_can_be_created_from_lowercase_name():
    assert CoatColour["bay"] == CoatColour.BAY


def test_coat_colour_can_be_created_from_abbreviation():
    assert CoatColour["B"] == CoatColour.BAY
