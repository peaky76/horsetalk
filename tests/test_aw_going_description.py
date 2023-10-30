from horsetalk import AWGoingDescription, Surface


def test_aw_going_description_can_be_created_from_enum():
    assert AWGoingDescription(8) == AWGoingDescription.STANDARD


def test_aw_going_description_can_be_created_from_name():
    assert AWGoingDescription["STANDARD"] == AWGoingDescription.STANDARD


def test_aw_going_description_can_be_created_from_lowercase_name():
    assert AWGoingDescription["standard"] == AWGoingDescription.STANDARD


def test_aw_going_description_can_be_created_from_hyphenated_name():
    assert AWGoingDescription["STANDARD-TO-SLOW"] == AWGoingDescription.STANDARD_TO_SLOW


def test_aw_going_description_can_be_created_from_non_hyphenated_name():
    assert AWGoingDescription["STANDARD TO SLOW"] == AWGoingDescription.STANDARD_TO_SLOW


def test_aw_going_description_can_be_created_when_whitespace_needs_trimming():
    assert (
        AWGoingDescription[" standard to slow "] == AWGoingDescription.STANDARD_TO_SLOW
    )


def test_aw_going_description_can_be_created_from_abbreviation():
    assert AWGoingDescription["std"] == AWGoingDescription.STANDARD


def test_aw_going_description_surface():
    assert AWGoingDescription.STANDARD.surface == Surface.ALL_WEATHER
