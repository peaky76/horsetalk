from horsetalk import DirtGoingDescription, Surface


def test_dirt_going_description_can_be_created_from_enum():
    assert DirtGoingDescription(6) == DirtGoingDescription.MUDDY


def test_dirt_going_description_can_be_created_from_name():
    assert DirtGoingDescription["MUDDY"] == DirtGoingDescription.MUDDY


def test_dirt_going_description_can_be_created_from_lowercase_name():
    assert DirtGoingDescription["muddy"] == DirtGoingDescription.MUDDY


def test_dirt_going_description_can_be_created_from_hyphenated_name():
    assert DirtGoingDescription["WET-FAST"] == DirtGoingDescription.WET_FAST


def test_dirt_going_description_can_be_created_from_non_hyphenated_name():
    assert DirtGoingDescription["WET FAST"] == DirtGoingDescription.WET_FAST


def test_dirt_going_description_surface():
    assert DirtGoingDescription.MUDDY.surface == Surface.DIRT
