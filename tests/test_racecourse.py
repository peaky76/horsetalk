from horsetalk import (
    Handedness,
    Racecourse,
    RacecourseContour,
    RacecourseShape,
    RacecourseStyle,
)


def test_racecourse_can_be_initialized_without_params():
    assert Racecourse()


def test_racecourse_default_handedness():
    assert Racecourse().handedness == Handedness.UNKNOWN


def test_racecourse_default_contour():
    assert Racecourse().contour == RacecourseContour.UNKNOWN


def test_racecourse_default_shape():
    assert Racecourse().shape == RacecourseShape.UNKNOWN


def test_racecourse_default_style():
    assert Racecourse().style == RacecourseStyle.UNKNOWN
