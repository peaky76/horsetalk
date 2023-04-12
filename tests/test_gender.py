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
