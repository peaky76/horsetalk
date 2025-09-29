import pytest

from horsetalk import Gender, Sex


def test_gender_can_be_created_from_enum():
    assert Gender(2) == Gender.COLT


def test_gender_can_be_created_from_name():
    assert Gender["COLT"] == Gender.COLT


def test_gender_can_be_created_from_lowercase_name():
    assert Gender["colt"] == Gender.COLT


def test_gender_can_be_created_from_abbreviation():
    assert Gender["C"] == Gender.COLT


def test_gender_sex_returns_male_for_male_genders():
    assert Gender["COLT"].sex == Sex.MALE


def test_gender_sex_returns_female_for_female_genders():
    assert Gender["FILLY"].sex == Sex.FEMALE


def test_gender_sex_returns_male_for_horse():
    assert Gender["HORSE"].sex == Sex.MALE


def test_gender_sex_raises_error_if_yearling():
    with pytest.raises(ValueError):
        Gender["YEARLING"].sex


def test_gender_sex_raises_error_if_foal():
    with pytest.raises(ValueError):
        Gender["FOAL"].sex


def test_gender_has_tests_returns_true_for_entire():
    assert Gender["ENTIRE"].has_testes


def test_gender_has_testes_returns_false_for_female():
    assert not Gender["MARE"].has_testes


def test_gender_has_testes_returns_false_for_gelding():
    assert not Gender["GELDING"].has_testes


def test_gender_determine_returns_correct_value_when_horse_before_first_birthday():
    assert Gender.determine(0) == Gender.FOAL


def test_gender_determine_returns_correct_value_when_horse_one_year_old():
    assert Gender.determine(1) == Gender.YEARLING


def test_gender_determine_returns_correct_value_when_two_and_male():
    assert Gender.determine(2, Sex.MALE) == Gender.COLT


def test_gender_determine_returns_correct_value_when_two_and_female():
    assert Gender.determine(2, Sex.FEMALE) == Gender.FILLY


def test_gender_determine_returns_correct_value_when_older_and_male():
    assert Gender.determine(6, Sex.MALE) == Gender.STALLION


def test_gender_determine_returns_correct_value_when_older_and_female():
    assert Gender.determine(6, Sex.FEMALE) == Gender.MARE


def test_gender_determine_returns_correct_value_when_gelded():
    assert Gender.determine(2, Sex.MALE, is_gelded=True) == Gender.GELDING


def test_gender_determine_returns_correct_value_when_rig():
    assert Gender.determine(2, Sex.MALE, is_rig=True) == Gender.RIG


def test_gender_determine_returns_correct_value_when_sex_implied():
    assert Gender.determine(5, is_rig=True) == Gender.RIG


def test_gender_determine_raises_value_error_for_gelded_female():
    with pytest.raises(ValueError):
        Gender.determine(2, Sex.FEMALE, is_gelded=True)


def test_gender_determine_raises_value_error_for_rigged_female():
    with pytest.raises(ValueError):
        Gender.determine(5, Sex.FEMALE, is_rig=True)


def test_gender_determine_raises_value_error_when_sex_matters_and_not_given():
    with pytest.raises(ValueError):
        Gender.determine(3)
