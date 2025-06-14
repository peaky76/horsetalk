import pendulum
import pytest

from horsetalk import Breed, Horse


@pytest.fixture
def today():
    return pendulum.date(2023, 1, 1)


def test_horse_created_with_just_name_has_correct_name():
    assert Horse("Dobbin").name == "Dobbin"


def test_horse_created_with_just_name_has_correct_country():
    assert Horse("Dobbin").country is None


def test_horse_created_with_just_name_has_correct_age():
    assert Horse("Dobbin").age is None


def test_horse_created_with_just_name_has_correct_breed_if_beyond_thoroughbred_limit():
    assert Horse("Dobbin De Dobbinville").breed is Breed.AQPS


def test_horse_created_with_just_name_has_no_breed_set_if_within_thoroughbred_limit():
    assert Horse("Dobbin").breed is None


def test_horse_created_with_name_and_country_has_correct_name():
    assert Horse("Dobbin", "GB").name == "Dobbin"


def test_horse_created_with_name_and_country_has_correct_country():
    country = Horse("Dobbin", "GB").country
    assert country
    assert country.name == "GB"


def test_horse_created_with_name_and_country_has_correct_age():
    assert Horse("Dobbin", "GB").age is None


def test_horse_created_with_name_country_and_age_had_correct_name():
    assert Horse("Dobbin", "GB", 3).name == "Dobbin"


def test_horse_created_with_name_country_and_age_had_correct_country():
    country = Horse("Dobbin", "GB", 3).country
    assert country
    assert country.name == "GB"


def test_horse_created_with_name_country_and_age_had_correct_age():
    age = Horse("Dobbin", "GB", 3).age
    assert age
    assert age.official.years == 3


def test_horse_created_with_name_country_age_and_context_date_had_correct_age_for_northern_hemisphere(
    today,
):
    age = Horse("Dobbin", "GB", 3, context_date=pendulum.date(2021, 1, 1)).age
    assert age
    assert age.at(today).official.years == 5


def test_horse_created_with_name_country_age_and_context_date_had_correct_age_for_southern_hemisphere():
    today = pendulum.date(2024, 7, 1)
    age = Horse("Dobbin", "NZ", 3, context_date=pendulum.date(2021, 10, 1)).age
    assert age
    assert age.at(today).official.years == 5


def test_horse_created_from_string_with_country_will_deduce_correct_name():
    assert Horse("Dobbin (GB)").name == "Dobbin"


def test_horse_created_from_string_with_country_will_deduce_correct_country():
    country = Horse("Dobbin (GB)").country
    assert country
    assert country.name == "GB"


def test_horse_created_from_string_with_country_will_deduce_correct_age():
    assert Horse("Dobbin (GB)").age is None


def test_horse_created_from_string_with_name_country_and_age_will_deduce_correct_name():
    assert Horse("Dobbin (GB) 3").name == "Dobbin"


def test_horse_created_from_string_with_name_country_and_age_will_deduce_correct_country():
    country = Horse("Dobbin (GB) 3").country
    assert country
    assert country.name == "GB"


def test_horse_created_from_string_with_name_country_and_age_will_deduce_correct_age():
    age = Horse("Dobbin (GB) 3").age
    assert age
    assert age.official.years == 3


def test_horse_created_from_multi_word_string_with_name_country_and_age_will_deduce_correct_name():
    assert Horse("Dobbin's Delight (GB) 3").name == "Dobbin's Delight"


def test_horse_created_from_multi_word_string_with_name_country_and_age_will_deduce_correct_country():
    country = Horse("Dobbin's Delight (GB) 3").country
    assert country
    assert country.name == "GB"


def test_horse_created_from_multi_word_string_with_name_country_and_age_will_deduce_correct_age():
    age = Horse("Dobbin's Delight (GB) 3").age
    assert age
    assert age.official.years == 3


def test_horse_created_from_string_with_name_country_and_age_with_context_date_will_deduce_correct_age(
    today,
):
    age = Horse("Dobbin (GB) 3", context_date=pendulum.date(2021, 1, 1)).age
    assert age
    assert age.at(today).official.years == 5


def test_horse_created_from_string_with_name_country_and_year_will_deduce_correct_name():
    assert Horse("Dobbin (GB) 2017").name == "Dobbin"


def test_horse_created_from_string_with_name_country_and_year_will_deduce_correct_country():
    country = Horse("Dobbin (GB) 2017").country
    assert country
    assert country.name == "GB"


def test_horse_created_from_string_with_name_country_and_year_will_deduce_correct_age(
    mocker,
):
    mocker.patch("pendulum.today", return_value=pendulum.datetime(2023, 1, 1, 0, 0, 0))
    age = Horse("Dobbin (GB) 2017").age
    assert age
    assert age.official.years == 6


def test_horse_created_from_string_with_country_will_raise_error_if_conflict_with_provided_country():
    with pytest.raises(ValueError):
        Horse("Dobbin (GB)", "USA")


def test_horse_created_from_string_with_age_will_raise_error_if_conflict_with_provided_age():
    with pytest.raises(ValueError):
        Horse("Dobbin (GB) 7", "GB", 3)


def test_horse_created_from_invalid_string_will_raise_error():
    with pytest.raises(ValueError):
        Horse("!")
