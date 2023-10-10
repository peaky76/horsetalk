import pendulum  # type: ignore
from horsetalk import Horse


def test_horse_created_with_just_name_has_correct_name():
    assert Horse("Dobbin").name == "Dobbin"


def test_horse_created_with_just_name_has_correct_country():
    assert Horse("Dobbin").country is None


def test_horse_created_with_just_name_has_correct_age():
    assert Horse("Dobbin").age is None


def test_horse_created_with_name_and_country_has_correct_name():
    assert Horse("Dobbin", "GB").name == "Dobbin"


def test_horse_created_with_name_and_country_has_correct_country():
    assert Horse("Dobbin", "GB").country == "GB"


def test_horse_created_with_name_and_country_has_correct_age():
    assert Horse("Dobbin", "GB").age is None


def test_horse_created_with_name_country_and_age_had_correct_name():
    assert Horse("Dobbin", "GB", 3).name == "Dobbin"


def test_horse_created_with_name_country_and_age_had_correct_country():
    assert Horse("Dobbin", "GB", 3).country == "GB"


def test_horse_created_with_name_country_and_age_had_correct_age():
    assert Horse("Dobbin", "GB", 3).age.official.years == 3


def test_horse_created_from_string_with_country_will_deduce_correct_name():
    assert Horse("Dobbin (GB)").name == "Dobbin"


def test_horse_created_from_string_with_country_will_deduce_correct_country():
    assert Horse("Dobbin (GB)").country == "GB"


def test_horse_created_from_string_with_country_will_deduce_correct_age():
    assert Horse("Dobbin (GB)").age is None


def test_horse_created_from_string_with_name_country_and_age_will_deduce_correct_name():
    assert Horse("Dobbin (GB) 3").name == "Dobbin"


def test_horse_created_from_string_with_name_country_and_age_will_deduce_correct_country():
    assert Horse("Dobbin (GB) 3").country == "GB"


def test_horse_created_from_string_with_name_country_and_age_will_deduce_correct_age():
    assert Horse("Dobbin (GB) 3").age.official.years == 3


def test_horse_created_from_string_with_name_country_and_age_will_deduce_correct_name(
    mocker,
):
    mocker.patch("pendulum.now", return_value=pendulum.datetime(2023, 1, 1))
    assert Horse("Dobbin (GB) 2017").name == "Dobbin"


def test_horse_created_from_string_with_name_country_and_age_will_deduce_correct_country(
    mocker,
):
    mocker.patch("pendulum.now", return_value=pendulum.datetime(2023, 1, 1))
    assert Horse("Dobbin (GB) 2017").country == "GB"


def test_horse_created_from_string_with_name_country_and_age_will_deduce_correct_age(
    mocker,
):
    mocker.patch("pendulum.now", return_value=pendulum.datetime(2023, 1, 1))
    assert Horse("Dobbin (GB) 2017").age.official.years == 6
