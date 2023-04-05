from horsetalk.coat_colour import CoatColour


def test_coat_colour_can_be_created_from_enum():
    assert CoatColour.BAY == CoatColour(1)


def test_coat_colour_can_be_created_from_name():
    assert CoatColour.BAY == CoatColour["BAY"]


def test_coat_colour_can_be_created_from_abbreviation():
    assert CoatColour.BAY == CoatColour["B"]
