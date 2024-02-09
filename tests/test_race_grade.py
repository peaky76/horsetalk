import pytest

from horsetalk import RaceClass, RaceGrade, RacingCode


def test_race_grade_init_possible_with_valid_str_only():
    assert RaceGrade("1")


def test_race_grade_init_possible_with_valid_int_only():
    assert RaceGrade(1)


def test_race_grade_init_possible_with_valid_word_only():
    assert RaceGrade("Listed")


def test_race_grade_init_possible_with_valid_grade_str_only():
    assert RaceGrade("Grade 1")


def test_race_grade_init_possible_with_valid_group_str_only():
    assert RaceGrade("Group 1")


def test_race_grade_init_possible_with_valid_g_str_only():
    assert RaceGrade("G1")


def test_race_grade_init_possible_with_none():
    assert isinstance(RaceGrade(None), RaceGrade)


def test_race_grade_init_possible_with_false():
    assert isinstance(RaceGrade(False), RaceGrade)  # noqa: FBT003


def test_race_grade_init_possible_with_zero():
    assert isinstance(RaceGrade(0), RaceGrade)


def test_race_grade_init_possible_with_valid_first_value_and_code():
    assert RaceGrade("1", RacingCode.NATIONAL_HUNT)


def test_race_grade_init_with_flat_default():
    assert RaceGrade("1").racing_code == RacingCode.FLAT


def test_race_grade_init_with_grade_identified_as_nh():
    assert RaceGrade("Grade 1").racing_code == RacingCode.NATIONAL_HUNT


def test_race_grade_init_with_group_identified_as_flat():
    assert RaceGrade("Group 1").racing_code == RacingCode.FLAT


def test_race_grade_init_not_possible_with_invalid_int():
    with pytest.raises(ValueError):
        RaceGrade(4)


def test_race_grade_init_not_possible_with_invalid_str():
    with pytest.raises(ValueError):
        RaceGrade("Quality")


def test_race_grade_init_not_possible_with_grade_conflicting_with_code():
    with pytest.raises(ValueError):
        RaceGrade("Grade 1", RacingCode.FLAT)


def test_race_grade_init_not_possible_with_group_conflicting_with_code():
    with pytest.raises(ValueError):
        RaceGrade("Group 1", RacingCode.NATIONAL_HUNT)


def test_race_grade_init_not_possible_with_point_to_point():
    with pytest.raises(ValueError):
        RaceGrade("Group 1", RacingCode.POINT_TO_POINT)


def test_race_grade_repr_when_graded():
    assert repr(RaceGrade("1")) == "<RaceGrade: 1>"


def test_race_grade_repr_when_listed():
    assert repr(RaceGrade("Listed")) == "<RaceGrade: Listed>"


def test_race_grade_repr_when_ungraded():
    assert repr(RaceGrade(None)) == "<RaceGrade: Ungraded>"


def test_race_grade_str_when_flat_listed():
    assert str(RaceGrade("Listed")) == "Listed"


def test_race_grade_str_when_flat_group():
    assert str(RaceGrade("1")) == "Group 1"


def test_race_grade_str_when_flat_none():
    assert str(RaceGrade(None)) == ""


def test_race_grade_str_when_nh_group():
    assert str(RaceGrade("1", RacingCode.NATIONAL_HUNT)) == "Grade 1"


def test_race_grade_bool_when_none():
    assert not RaceGrade(None)


def test_race_grade_bool_when_listed():
    assert RaceGrade("Listed")


def test_race_grade_hash():
    assert hash(RaceGrade(1)) == hash(RaceGrade(1))


def test_race_grade_eq_when_both_same_group():
    assert (RaceGrade("1") == RaceGrade("1")) is True


def test_race_grade_eq_when_both_listed():
    assert (RaceGrade("Listed") == RaceGrade("Listed")) is True


def test_race_grade_eq_with_int():
    assert (RaceGrade(1) == 1) is True


def test_race_grade_eq_when_both_none():
    assert (RaceGrade(None) == RaceGrade(None)) is True


def test_race_grade_eq_with_other_object():
    assert (RaceGrade(1) == RaceClass(1)) is False


def test_race_grade_ne_when_both_different_group():
    assert (RaceGrade("1") != RaceGrade("2")) is True


def test_race_grade_ne_when_self_listed_other_group():
    assert (RaceGrade("Listed") != RaceGrade("1")) is True


def test_race_grade_ne_when_self_group_other_listed():
    assert (RaceGrade("1") != RaceGrade("Listed")) is True


def test_race_grade_ne_when_self_none_other_listed():
    assert (RaceGrade(None) != RaceGrade("Listed")) is True


def test_race_grade_ne_when_self_none_other_group():
    assert (RaceGrade(None) != RaceGrade("1")) is True


def test_race_grade_ne_with_int_when_listed():
    assert (RaceGrade("Listed") != 1) is True


def test_race_grade_ne_with_other_object():
    assert (RaceGrade(1) != RaceClass(1)) is True


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
