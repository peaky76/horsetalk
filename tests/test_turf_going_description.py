from horsetalk import Surface, TurfGoingDescription


def test_turf_going_description_can_be_created_from_enum():
    assert TurfGoingDescription.GOOD == TurfGoingDescription(8)


def test_turf_going_description_can_be_created_from_name():
    assert TurfGoingDescription.GOOD == TurfGoingDescription["GOOD"]


def test_turf_going_description_can_be_created_from_lowercase_name():
    assert TurfGoingDescription.GOOD == TurfGoingDescription["good"]


def test_turf_going_description_can_be_created_from_hyphenated_name():
    assert TurfGoingDescription.GOOD_TO_SOFT == TurfGoingDescription["GOOD-TO-SOFT"]


def test_turf_going_description_can_be_created_from_non_hyphenated_name():
    assert TurfGoingDescription.GOOD_TO_SOFT == TurfGoingDescription["GOOD TO SOFT"]


def test_turf_going_description_can_be_created_from_abbreviation():
    assert TurfGoingDescription.GOOD == TurfGoingDescription["gd"]


def test_turf_going_description_surface():
    assert TurfGoingDescription.GOOD.surface == Surface.TURF
