import pytest
from peak_utility.number import RepresentationalInt

from horsetalk import RaceClass, RaceGrade


def test_race_class_init_possible_with_valid_int():
    assert RaceClass(1)


def test_race_class_init_possible_with_valid_str():
    assert RaceClass("1")


def test_race_class_init_possible_with_valid_str_with_class():
    assert RaceClass("Class 1")


def test_race_class_init_not_possible_with_invalid_int():
    with pytest.raises(ValueError):
        RaceClass(0)


def test_race_class_repr():
    assert repr(RaceClass(1)) == "<RaceClass: 1>"


def test_race_class_str():
    assert str(RaceClass(1)) == "Class 1"


def test_race_class_hash():
    assert hash(RaceClass(1)) == hash(RaceClass(1))


def test_race_class_eq():
    assert (RaceClass(1) == RaceClass(1)) is True


def test_race_class_eq_with_int():
    assert (RaceClass(2) == 2) is True


def test_race_class_eq_with_other_object():
    assert (RaceClass(2) == RepresentationalInt(2)) is False


def test_race_class_ne():
    assert (RaceClass(2) != RaceClass(2)) is False


def test_race_class_ne_with_other_object():
    assert (RaceClass(2) != RaceGrade(2)) is True


def test_race_class_gt():
    assert RaceClass(1) > RaceClass(2)


def test_race_class_lt():
    assert RaceClass(2) < RaceClass(1)
