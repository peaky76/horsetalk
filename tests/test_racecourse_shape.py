from horsetalk import RacecourseShape


def test_racecourse_shape_can_be_created_from_enum():
    assert RacecourseShape.OVAL == RacecourseShape(4)


def test_racecourse_shape_can_be_created_from_name():
    assert RacecourseShape.OVAL == RacecourseShape["OVAL"]


def test_racecourse_shape_can_be_created_from_lowercase_name():
    assert RacecourseShape.OVAL == RacecourseShape["oval"]


def test_racecourse_shape_can_be_created_from_alternative():
    assert RacecourseShape.OVAL == RacecourseShape["round"]
