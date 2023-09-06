import pytest
from horsetalk import (
    Handedness,
    Racecourse,
    RacecourseContour,
    RacecourseShape,
    RacecourseStyle,
)


def test_racecourse_can_be_initialized_without_characteristics():
    assert Racecourse("Portman Park")


def test_racecourse_default_handedness():
    assert Racecourse("Portman Park").handedness == Handedness.UNKNOWN


def test_racecourse_default_contour():
    assert Racecourse("Portman Park").contour == RacecourseContour.UNKNOWN


def test_racecourse_default_shape():
    assert Racecourse("Portman Park").shape == RacecourseShape.UNKNOWN


def test_racecourse_default_style():
    assert Racecourse("Portman Park").style == RacecourseStyle.UNKNOWN


def test_racecourse_can_be_initialized_with_params():
    assert Racecourse(
        "Aintree", handedness="left", contour="flat", shape="oval", style="galloping"
    )


def test_racecourse_handedness():
    assert Racecourse("Aintree", handedness="left").handedness == Handedness.LEFT


def test_racecourse_contour():
    assert Racecourse("Aintree", contour="flat").contour == RacecourseContour.FLAT


def test_racecourse_shape():
    assert Racecourse("Aintree", shape="oval").shape == RacecourseShape.OVAL


def test_racecourse_style():
    assert Racecourse("Aintree", style="galloping").style == RacecourseStyle.GALLOPING


def test_racecourse_init_raises_error_if_characteristic_is_invalid():
    with pytest.raises(KeyError):
        Racecourse("Aintree", handedness="invalid")
