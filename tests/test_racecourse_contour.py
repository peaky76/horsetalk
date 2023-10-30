from horsetalk import RacecourseContour


def test_racecourse_contour_can_be_created_from_enum():
    assert RacecourseContour(1) == RacecourseContour.FLAT


def test_racecourse_contour_can_be_created_from_name():
    assert RacecourseContour["FLAT"] == RacecourseContour.FLAT


def test_racecourse_contour_can_be_created_from_lowercase_name():
    assert RacecourseContour["flat"] == RacecourseContour.FLAT


def test_racecourse_contour_can_be_created_from_alternative():
    assert RacecourseContour["down"] == RacecourseContour.DOWNHILL
