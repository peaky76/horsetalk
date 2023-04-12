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


def test_gender_sex_raises_error_if_not_enough_info():
    with pytest.raises(ValueError):
        Gender["YEARLING"].sex


def test_gender_determine_returns_correct_value_when_sex_does_not_matter():
    assert Gender.FOAL == Gender.determine(0)


def test_gender_determine_returns_correct_value_when_sex_matters():
    assert Gender.COLT == Gender.determine(2, Sex.MALE)


def test_gender_determine_raises_value_error_when_sex_matters_and_not_given():
    with pytest.raises(ValueError):
        Gender.determine(3)


def test_gender_determine_returns_correct_value_when_gelded():
    assert Gender.GELDING == Gender.determine(2, Sex.MALE, is_gelded=True)


def test_gender_determine_returns_correct_value_when_rig():
    assert Gender.RIG == Gender.determine(2, Sex.MALE, is_rig=True)


def test_gender_determine_returns_correct_value_when_sex_implied():
    assert Gender.RIG == Gender.determine(5, is_rig=True)


def test_gender_determine_raises_error_for_gelded_female():
    with pytest.raises(ValueError):
        Gender.determine(2, Sex.FEMALE, is_gelded=True)
