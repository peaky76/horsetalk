from horsetalk import RacecourseStyle


def test_racecourse_shape_can_be_created_from_enum():
    assert RacecourseStyle.GALLOPING == RacecourseStyle(1)


def test_racecourse_shape_can_be_created_from_name():
    assert RacecourseStyle.GALLOPING == RacecourseStyle["GALLOPING"]


def test_racecourse_shape_can_be_created_from_lowercase_name():
    assert RacecourseStyle.GALLOPING == RacecourseStyle["galloping"]
