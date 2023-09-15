import pytest
from horsetalk import RaceClass, RaceGrade, RaceLevel


def test_race_level_can_be_initialised_with_race_grade():
    assert RaceLevel(RaceGrade("1"))


def test_race_level_can_be_initialised_with_race_class_below_one():
    assert RaceLevel(RaceClass(2))


def test_race_level_raises_value_error_when_initalised_with_race_class_one():
    with pytest.raises(ValueError):
        RaceLevel(RaceClass(1))


def test_race_level_str_when_grade():
    assert str(RaceLevel(RaceGrade("1"))) == "(1) Group 1"


def test_race_level_str_when_class():
    assert str(RaceLevel(RaceClass(2))) == "(2)"


def test_race_level_initialised_with_race_grade_has_class_one():
    assert RaceLevel(RaceGrade("1")).class_ == RaceClass(1)


def test_race_level_eq_when_same_grade():
    assert RaceLevel(RaceGrade("1")) == RaceLevel(RaceGrade("1"))


def test_race_level_eq_when_same_class_below_one():
    assert RaceLevel(RaceClass(2)) == RaceLevel(RaceClass(2))


def test_race_level_not_eq_when_different_grade_or_class():
    assert not RaceLevel(RaceGrade("1")) == RaceLevel(RaceClass("2"))


def test_race_level_gt_when_different_grade_or_class():
    assert RaceLevel(RaceGrade("1")) > RaceLevel(RaceClass("2"))


def test_race_level_lt_when_different_grade_or_class():
    assert RaceLevel(RaceClass("2")) < RaceLevel(RaceGrade("1"))
