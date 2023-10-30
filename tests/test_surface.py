from horsetalk import Surface


def test_surface_can_be_created_from_enum():
    assert Surface(1) == Surface.TURF


def test_surface_can_be_created_from_name():
    assert Surface["TURF"] == Surface.TURF


def test_surface_can_be_created_from_hyphenated_name():
    assert Surface["ALL-WEATHER"] == Surface.ALL_WEATHER


def test_surface_can_be_created_from_non_hyphenated_name():
    assert Surface["ALL WEATHER"] == Surface.ALL_WEATHER


def test_surface_can_be_created_from_abbreviation():
    assert Surface["t"] == Surface.TURF
