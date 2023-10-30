import pytest

from horsetalk import Gender, Sex


def test_gender_can_be_created_from_enum():
    assert Gender.COLT == Gender(2)


def test_gender_can_be_created_from_name():
    assert Gender.COLT == Gender["COLT"]


def test_gender_can_be_created_from_lowercase_name():
    assert Gender.COLT == Gender["colt"]


def test_gender_can_be_created_from_abbreviation():
    assert Gender.COLT == Gender["C"]


def test_gender_sex_returns_male_for_male_genders():
    assert Sex.MALE == Gender["COLT"].sex


def test_gender_sex_returns_female_for_female_genders():
    assert Sex.FEMALE == Gender["FILLY"].sex


def test_gender_sex_raises_error_if_yearling():
    with pytest.raises(ValueError):
        Gender["YEARLING"].sex


def test_gender_sex_raises_error_if_foal():
    with pytest.raises(ValueError):
        Gender["FOAL"].sex


def test_gender_determine_returns_correct_value_when_horse_before_first_birthday():
    assert Gender.FOAL == Gender.determine(0)


def test_gender_determine_returns_correct_value_when_horse_one_year_old():
    assert Gender.YEARLING == Gender.determine(1)


def test_gender_determine_returns_correct_value_when_two_and_male():
    assert Gender.COLT == Gender.determine(2, Sex.MALE)


def test_gender_determine_returns_correct_value_when_two_and_female():
    assert Gender.FILLY == Gender.determine(2, Sex.FEMALE)


def test_gender_determine_returns_correct_value_when_older_and_male():
    assert Gender.STALLION == Gender.determine(6, Sex.MALE)


def test_gender_determine_returns_correct_value_when_older_and_female():
    assert Gender.MARE == Gender.determine(6, Sex.FEMALE)


def test_gender_determine_returns_correct_value_when_gelded():
    assert Gender.GELDING == Gender.determine(2, Sex.MALE, is_gelded=True)


def test_gender_determine_returns_correct_value_when_rig():
    assert Gender.RIG == Gender.determine(2, Sex.MALE, is_rig=True)


def test_gender_determine_returns_correct_value_when_sex_implied():
    assert Gender.RIG == Gender.determine(5, is_rig=True)


def test_gender_determine_raises_value_error_for_gelded_female():
    with pytest.raises(ValueError):
        Gender.determine(2, Sex.FEMALE, is_gelded=True)


def test_gender_determine_raises_value_error_for_rigged_female():
    with pytest.raises(ValueError):
        Gender.determine(5, Sex.FEMALE, is_rig=True)


def test_gender_determine_raises_value_error_when_sex_matters_and_not_given():
    with pytest.raises(ValueError):
        Gender.determine(3)
