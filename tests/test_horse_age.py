import pendulum
import pytest
from horsetalk import HorseAge


@pytest.fixture(autouse=True)
def now(mocker):
    mocker.patch("pendulum.now", return_value=pendulum.datetime(2023, 6, 1))


def test_horse_age_can_be_initialized_with_age():
    assert HorseAge(2)


def test_horse_age_can_be_initialized_with_context_date():
    assert HorseAge(2, context_date=pendulum.datetime(2022, 3, 1))


def test_horse_age_cannot_be_initialized_with_context_date_alone():
    with pytest.raises(ValueError):
        HorseAge(context_date=pendulum.datetime(2022, 3, 1))


def test_horse_age_can_be_initialized_with_foaling_date():
    assert HorseAge(foaling_date=pendulum.datetime(2019, 1, 1))


def test_horse_age_can_be_initialized_with_year():
    assert HorseAge(birth_year=2019)


def test_horse_age_raises_error_when_initialized_with_both_int_and_foaling_date():
    with pytest.raises(ValueError):
        HorseAge(2, foaling_date=pendulum.datetime(2019, 1, 1))


def test_horse_age_init_with_age_sets_official_dob():
    assert pendulum.datetime(2021, 1, 1) == HorseAge(2)._official_dob


def test_horse_age_init_with_age_does_not_set_actual_dob():
    assert None is HorseAge(2)._actual_dob


def test_horse_age_init_with_foaling_date_sets_official_dob():
    horse_age = HorseAge(foaling_date=pendulum.datetime(2021, 3, 3))
    assert pendulum.datetime(2021, 1, 1) == horse_age._official_dob


def test_horse_age_init_with_foaling_date_sets_actual_dob():
    horse_age = HorseAge(foaling_date=pendulum.datetime(2021, 3, 3))
    assert pendulum.datetime(2021, 3, 3) == horse_age._actual_dob


def test_horse_age_init_with_year_sets_official_dob():
    assert pendulum.datetime(2019, 1, 1) == HorseAge(birth_year=2019)._official_dob


def test_horse_age_init_with_context_date_uses_context_year_for_official_dob():
    horse_age = HorseAge(2, context_date=pendulum.date(2021, 3, 1))
    assert pendulum.datetime(2019, 1, 1) == horse_age._official_dob


def test_horse_age_init_with_year_sets_actual_dob():
    assert None is HorseAge(birth_year=2019)._actual_dob


def test_horse_age_str():
    assert "2" == str(HorseAge(2))


def test_horse_age_returns_correct_official_age_in_years():
    assert 2 == HorseAge(2).official.years


def test_horse_age_returns_correct_actual_age_in_years_if_actual_dob_known():
    assert 4 == HorseAge(foaling_date=pendulum.datetime(2019, 3, 3)).actual.years


def test_horse_age_raises_error_for_actual_age_in_years_if_actual_dob_not_known():
    with pytest.raises(ValueError):
        HorseAge(2).actual.years


def test_horse_age_returns_correct_official_age_in_days_considering_leap_years():
    assert 1612 == HorseAge(4).official.days


def test_horse_age_returns_correct_actual_age_in_days_considering_leap_years():
    assert 1581 == HorseAge(foaling_date=pendulum.datetime(2019, 2, 1)).actual.days


def test_horse_age_returns_correct_official_age_when_context_date_is_set():
    horse_age = HorseAge(
        2,
        context_date=pendulum.datetime(2022, 6, 1),
    )
    assert 2 == horse_age.official.years


def test_horse_age_returns_correct_actual_age_when_context_date_is_set():
    horse_age = HorseAge(
        foaling_date=pendulum.datetime(2019, 3, 3),
        context_date=pendulum.datetime(2022, 6, 1),
    )
    assert 3 == horse_age.actual.years


def test_horse_age_at_changes_context_date():
    new_date = pendulum.datetime(2022, 6, 1)
    assert new_date == HorseAge(2).at(new_date)._context_date


def test_horse_age_change_of_context_date_changes_official_age():
    horse_age = HorseAge(2, context_date=pendulum.datetime(2020, 6, 1))
    assert 4 == horse_age.at(pendulum.datetime(2022, 3, 1)).official.years


def test_horse_age_returns_correct_official_age_when_context_date_is_before_birth():
    horse_age = HorseAge(foaling_date=pendulum.datetime(2019, 3, 3))
    assert 0 == horse_age.at(pendulum.datetime(1976, 11, 29)).official.years


def test_horse_age_returns_correct_actual_age_when_context_date_is_before_birth():
    horse_age = HorseAge(foaling_date=pendulum.datetime(2019, 3, 3))
    assert 0 == horse_age.at(pendulum.datetime(1976, 11, 29)).actual.years
