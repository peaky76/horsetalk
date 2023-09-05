from horsetalk import StallsPosition


def test_stalls_position_can_be_created_from_enum():
    assert StallsPosition.INSIDE == StallsPosition(1)


def test_stalls_position_can_be_created_from_name():
    assert StallsPosition.INSIDE == StallsPosition["INSIDE"]


def test_stalls_position_can_be_created_from_lowercase_name():
    assert StallsPosition.INSIDE == StallsPosition["inside"]


def test_stalls_position_can_be_created_from_alternative_name():
    assert StallsPosition.INSIDE == StallsPosition["FAR"]
