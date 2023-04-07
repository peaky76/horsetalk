from horsetalk import DirtGoingDescription


def test_dirt_going_description_can_be_created_from_enum():
    assert DirtGoingDescription.MUDDY == DirtGoingDescription(3)


def test_dirt_going_description_can_be_created_from_name():
    assert DirtGoingDescription.MUDDY == DirtGoingDescription["MUDDY"]


def test_dirt_going_description_can_be_created_from_lowercase_name():
    assert DirtGoingDescription.MUDDY == DirtGoingDescription["muddy"]


def test_dirt_going_description_can_be_created_from_hyphenated_name():
    assert DirtGoingDescription.WET_FAST == DirtGoingDescription["WET-FAST"]


def test_dirt_going_description_can_be_created_from_non_hyphenated_name():
    assert DirtGoingDescription.WET_FAST == DirtGoingDescription["WET FAST"]
