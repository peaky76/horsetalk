from horsetalk import RacecourseContour


def test_racecourse_contour_can_be_created_from_enum():
    assert RacecourseContour.FLAT == RacecourseContour(1)


def test_racecourse_contour_can_be_created_from_name():
    assert RacecourseContour.FLAT == RacecourseContour["FLAT"]


def test_racecourse_contour_can_be_created_from_lowercase_name():
    assert RacecourseContour.FLAT == RacecourseContour["flat"]


def test_racecourse_contour_can_be_created_from_alternative():
    assert RacecourseContour.DOWNHILL == RacecourseContour["down"]
