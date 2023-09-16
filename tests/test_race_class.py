import pytest
from horsetalk import RaceClass


def test_race_class_init_possible_with_valid_int():
    assert RaceClass(1)


def test_race_class_init_possible_with_valid_str():
    assert RaceClass("1")


def test_race_class_init_not_possible_with_invalid_int():
    with pytest.raises(ValueError):
        RaceClass(0)


def test_race_class_repr():
    assert repr(RaceClass(1)) == "<RaceClass: 1>"


def test_race_class_str():
    assert str(RaceClass(1)) == "Class 1"


def test_race_class_eq():
    assert RaceClass(1) == RaceClass(1)


def test_race_class_gt():
    assert RaceClass(1) > RaceClass(2)


def test_race_class_lt():
    assert RaceClass(2) < RaceClass(1)
