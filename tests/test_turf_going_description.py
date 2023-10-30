from horsetalk import Surface, TurfGoingDescription


def test_turf_going_description_can_be_created_from_enum():
    assert TurfGoingDescription(8) == TurfGoingDescription.GOOD


def test_turf_going_description_can_be_created_from_name():
    assert TurfGoingDescription["GOOD"] == TurfGoingDescription.GOOD


def test_turf_going_description_can_be_created_from_lowercase_name():
    assert TurfGoingDescription["good"] == TurfGoingDescription.GOOD


def test_turf_going_description_can_be_created_from_hyphenated_name():
    assert TurfGoingDescription["GOOD-TO-SOFT"] == TurfGoingDescription.GOOD_TO_SOFT


def test_turf_going_description_can_be_created_from_non_hyphenated_name():
    assert TurfGoingDescription["GOOD TO SOFT"] == TurfGoingDescription.GOOD_TO_SOFT


def test_turf_going_description_can_be_created_from_abbreviation():
    assert TurfGoingDescription["gd"] == TurfGoingDescription.GOOD


def test_turf_going_description_surface():
    assert TurfGoingDescription.GOOD.surface == Surface.TURF
