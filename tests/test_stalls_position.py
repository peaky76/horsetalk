from horsetalk import StallsPosition


def test_stalls_position_can_be_created_from_enum():
    assert StallsPosition(1) == StallsPosition.INSIDE


def test_stalls_position_can_be_created_from_name():
    assert StallsPosition["INSIDE"] == StallsPosition.INSIDE


def test_stalls_position_can_be_created_from_lowercase_name():
    assert StallsPosition["inside"] == StallsPosition.INSIDE


def test_stalls_position_can_be_created_from_alternative_name():
    assert StallsPosition["FAR"] == StallsPosition.INSIDE
