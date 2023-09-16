import pytest  # type: ignore
from horsetalk.race_grade import RaceGrade
from horsetalk.racing_code import RacingCode


def test_race_grade_init_possible_with_valid_str_only():
    assert RaceGrade("1")


def test_race_grade_init_possible_with_valid_int_only():
    assert RaceGrade(1)


def test_race_grade_init_possible_with_valid_word_only():
    assert RaceGrade("Listed")


def test_race_grade_init_possible_with_none():
    assert RaceGrade(None)


def test_race_grade_init_possible_with_valid_first_value_and_code():
    assert RaceGrade("1", RacingCode.NATIONAL_HUNT)


def test_race_grade_init_with_flat_default():
    assert RaceGrade("1").racing_code == RacingCode.FLAT


def test_race_grade_init_not_possible_with_invalid_int():
    with pytest.raises(ValueError):
        RaceGrade(4)


def test_race_grade_init_not_possible_with_invalid_str():
    with pytest.raises(ValueError):
        RaceGrade("Quality")


def test_race_grade_repr_():
    assert repr(RaceGrade("1")) == "<RaceGrade: 1>"


def test_race_grade_string_when_flat_listed():
    assert str(RaceGrade("Listed")) == "Listed"


def test_race_grade_string_when_flat_group():
    assert str(RaceGrade("1")) == "Group 1"


def test_race_grade_string_when_flat_none():
    assert str(RaceGrade(None)) == ""


def test_race_grade_string_when_nh_group():
    assert str(RaceGrade("1", RacingCode.NATIONAL_HUNT)) == "Grade 1"


def test_race_grade_eq_when_both_same_group():
    assert RaceGrade("1") == RaceGrade("1")


def test_race_grade_eq_when_both_different_group():
    assert not RaceGrade("1") == RaceGrade("2")


def test_race_grade_eq_when_both_listed():
    assert RaceGrade("Listed") == RaceGrade("Listed")


def test_race_grade_eq_when_self_listed_other_group():
    assert not RaceGrade("Listed") == RaceGrade("1")


def test_race_grade_eq_when_self_group_other_listed():
    assert not RaceGrade("1") == RaceGrade("Listed")


def test_race_grade_eq_when_both_none():
    assert RaceGrade(None) == RaceGrade(None)


def test_race_grade_eq_when_self_none_other_listed():
    assert not RaceGrade(None) == RaceGrade("Listed")


def test_race_grade_eq_when_self_none_other_group():
    assert not RaceGrade(None) == RaceGrade("1")


def test_race_grade_lt_when_both_same_group():
    assert not RaceGrade("1") < RaceGrade("1")


def test_race_grade_lt_when_both_different_group():
    assert RaceGrade("2") < RaceGrade("1")


def test_race_grade_lt_when_self_listed_other_group():
    assert RaceGrade("Listed") < RaceGrade("1")


def test_race_grade_lt_when_self_group_other_listed():
    assert not RaceGrade("1") < RaceGrade("Listed")


def test_race_grade_lt_when_self_group_other_none():
    assert not RaceGrade("1") < RaceGrade("Listed")


def test_race_grade_lt_when_both_none():
    assert not RaceGrade(None) < RaceGrade(None)


def test_race_grade_lt_when_self_none_other_listed():
    assert RaceGrade(None) < RaceGrade("Listed")


def test_race_grade_lt_when_self_none_other_group():
    assert RaceGrade(None) < RaceGrade("1")


def test_race_grade_gt_when_both_same_group():
    assert not RaceGrade("1") > RaceGrade("1")


def test_race_grade_gt_when_both_different_group():
    assert RaceGrade("1") > RaceGrade("2")


def test_race_grade_gt_when_self_listed_other_group():
    assert not RaceGrade("Listed") > RaceGrade("1")


def test_race_grade_gt_when_self_group_other_listed():
    assert RaceGrade("1") > RaceGrade("Listed")


def test_race_grade_gt_when_self_group_other_none():
    assert RaceGrade("1") > RaceGrade(None)


def test_race_grade_gt_when_both_none():
    assert not RaceGrade(None) > RaceGrade(None)


def test_race_grade_gt_when_self_none_other_listed():
    assert not RaceGrade(None) > RaceGrade("Listed")


def test_race_grade_gt_when_self_none_other_group():
    assert not RaceGrade(None) > RaceGrade("1")
