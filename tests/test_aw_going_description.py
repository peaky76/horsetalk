from horsetalk import AWGoingDescription


def test_aw_going_description_can_be_created_from_enum():
    assert AWGoingDescription.STANDARD == AWGoingDescription(8)


def test_aw_going_description_can_be_created_from_name():
    assert AWGoingDescription.STANDARD == AWGoingDescription["STANDARD"]


def test_aw_going_description_can_be_created_from_lowercase_name():
    assert AWGoingDescription.STANDARD == AWGoingDescription["standard"]


def test_aw_going_description_can_be_created_from_hyphenated_name():
    assert AWGoingDescription.STANDARD_TO_SLOW == AWGoingDescription["STANDARD-TO-SLOW"]


def test_aw_going_description_can_be_created_from_non_hyphenated_name():
    assert AWGoingDescription.STANDARD_TO_SLOW == AWGoingDescription["STANDARD TO SLOW"]


def test_aw_going_description_can_be_created_when_whitespace_needs_trimming():
    assert (
        AWGoingDescription.STANDARD_TO_SLOW == AWGoingDescription[" standard to slow "]
    )


def test_aw_going_description_can_be_created_from_abbreviation():
    assert AWGoingDescription.STANDARD == AWGoingDescription["std"]
