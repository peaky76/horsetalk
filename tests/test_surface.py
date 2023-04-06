from horsetalk import Surface


def test_surface_can_be_created_from_enum():
    assert Surface.TURF == Surface(1)


def test_surface_can_be_created_from_name():
    assert Surface.TURF == Surface["TURF"]


def test_surface_can_be_created_from_hyphenated_name():
    assert Surface.ALL_WEATHER == Surface["ALL-WEATHER"]


def test_surface_can_be_created_from_non_hyphenated_name():
    assert Surface.ALL_WEATHER == Surface["ALL WEATHER"]


def test_surface_can_be_created_from_abbreviation():
    assert Surface.TURF == Surface["t"]
