import pytest
from horsetalk import (
    Handedness,
    Racecourse,
    RacecourseContour,
    RacecourseShape,
    RacecourseStyle,
    Surface,
)


def test_racecourse_can_be_initialized_without_characteristics_with_enum_surface():
    assert Racecourse("Portman Park", Surface.TURF)


def test_racecourse_can_be_initialized_without_characteristics_with_text_surface():
    assert Racecourse("Portman Park", "turf")


def test_racecourse_default_handedness():
    assert Racecourse("Portman Park", Surface.TURF).handedness == Handedness.UNKNOWN


def test_racecourse_default_contour():
    assert Racecourse("Portman Park", Surface.TURF).contour == RacecourseContour.UNKNOWN


def test_racecourse_default_shape():
    assert Racecourse("Portman Park", Surface.TURF).shape == RacecourseShape.UNKNOWN


def test_racecourse_default_style():
    assert Racecourse("Portman Park", Surface.TURF).style == RacecourseStyle.UNKNOWN


def test_racecourse_can_be_initialized_with_params():
    assert Racecourse(
        "Aintree",
        Surface.TURF,
        handedness="left",
        contour="flat",
        shape="oval",
        style="galloping",
    )


def test_racecourse_handedness():
    assert (
        Racecourse("Aintree", Surface.TURF, handedness="left").handedness
        == Handedness.LEFT
    )


def test_racecourse_contour():
    assert (
        Racecourse("Aintree", Surface.TURF, contour="flat").contour
        == RacecourseContour.FLAT
    )


def test_racecourse_shape():
    assert (
        Racecourse("Aintree", Surface.TURF, shape="oval").shape == RacecourseShape.OVAL
    )


def test_racecourse_style():
    assert (
        Racecourse("Aintree", Surface.TURF, style="galloping").style
        == RacecourseStyle.GALLOPING
    )


def test_racecourse_init_raises_error_if_characteristic_is_invalid():
    with pytest.raises(KeyError):
        Racecourse("Aintree", Surface.TURF, handedness="invalid")
