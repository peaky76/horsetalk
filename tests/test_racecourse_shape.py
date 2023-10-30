from horsetalk import RacecourseShape


def test_racecourse_shape_can_be_created_from_enum():
    assert RacecourseShape(4) == RacecourseShape.OVAL


def test_racecourse_shape_can_be_created_from_name():
    assert RacecourseShape["OVAL"] == RacecourseShape.OVAL


def test_racecourse_shape_can_be_created_from_lowercase_name():
    assert RacecourseShape["oval"] == RacecourseShape.OVAL


def test_racecourse_shape_can_be_created_from_alternative():
    assert RacecourseShape["round"] == RacecourseShape.OVAL
