import pendulum
import pytest

from horsetalk import Hemisphere, HorseAge


@pytest.fixture(autouse=True)
def _now(mocker):
    mocker.patch("pendulum.today", return_value=pendulum.datetime(2023, 6, 1, 0, 0, 0))


def test_horse_age_can_be_initialized_with_age():
    assert HorseAge(2)


def test_horse_age_can_be_initialized_with_context_date():
    assert HorseAge(2, context_date=pendulum.date(2022, 3, 1))


def test_horse_age_cannot_be_initialized_with_context_date_alone():
    with pytest.raises(ValueError):
        HorseAge(context_date=pendulum.date(2022, 3, 1))


def test_horse_age_can_be_initialized_with_foaling_date():
    assert HorseAge(foaling_date=pendulum.date(2019, 1, 1))


def test_horse_age_can_be_initialized_with_year():
    assert HorseAge(birth_year=2019)


def test_horse_age_can_be_initialized_with_hemisphere():
    assert HorseAge(2, hemisphere=Hemisphere.NORTHERN)


def test_horse_age_raises_error_when_initialized_with_both_int_and_foaling_date():
    with pytest.raises(ValueError):
        HorseAge(2, foaling_date=pendulum.date(2019, 1, 1))


def test_horse_age_init_with_age_sets_official_dob():
    assert HorseAge(2)._official_dob == pendulum.date(2021, 1, 1)


def test_horse_age_init_with_age_and_northern_hemisphere_sets_hemisphere_specific_official_dob():
    assert HorseAge(2, hemisphere=Hemisphere.NORTHERN)._official_dob == pendulum.date(
        2021, 1, 1
    )


def test_horse_age_init_with_age_and_southern_hemisphere_sets_hemisphere_specific_official_dob_when_in_early_year(
    mocker,
):
    mocker.patch("pendulum.today", return_value=pendulum.datetime(2023, 6, 1, 0, 0, 0))
    assert HorseAge(2, hemisphere=Hemisphere.SOUTHERN)._official_dob == pendulum.date(
        2020, 8, 1
    )


def test_horse_age_init_with_age_and_southern_hemisphere_sets_hemisphere_specific_official_dob_when_in_late_year(
    mocker,
):
    mocker.patch("pendulum.today", return_value=pendulum.datetime(2023, 9, 1, 0, 0, 0))
    assert HorseAge(2, hemisphere=Hemisphere.SOUTHERN)._official_dob == pendulum.date(
        2021, 8, 1
    )


def test_horse_age_init_with_age_does_not_set_actual_dob():
    assert HorseAge(2)._actual_dob is None


def test_horse_age_init_with_foaling_date_sets_official_dob_for_northern_hemisphere_horses():
    horse_age = HorseAge(foaling_date=pendulum.date(2021, 3, 3))
    assert horse_age._official_dob == pendulum.date(2021, 1, 1)


def test_horse_age_init_with_foaling_date_sets_official_dob_for_southern_hemisphere_horses_born_early_in_year():
    horse_age = HorseAge(
        foaling_date=pendulum.date(2021, 1, 3), hemisphere=Hemisphere.SOUTHERN
    )
    assert horse_age._official_dob == pendulum.date(2020, 8, 1)


def test_horse_age_init_with_foaling_date_sets_official_dob_for_southern_hemisphere_horses_born_late_in_year():
    horse_age = HorseAge(
        foaling_date=pendulum.date(2020, 9, 1), hemisphere=Hemisphere.SOUTHERN
    )
    assert horse_age._official_dob == pendulum.date(2020, 8, 1)


def test_horse_age_init_with_foaling_date_sets_actual_dob():
    horse_age = HorseAge(foaling_date=pendulum.date(2021, 3, 3))
    assert horse_age._actual_dob == pendulum.date(2021, 3, 3)


def test_horse_age_init_with_birth_year_sets_official_years():
    assert HorseAge(birth_year=2017).official.years == 6


def test_horse_age_init_with_birth_year_and_context_date_sets_official_years():
    assert (
        HorseAge(birth_year=2017, context_date=pendulum.date(2024, 1, 1)).official.years
        == 7
    )


def test_horse_age_init_with_year_sets_official_dob():
    assert HorseAge(birth_year=2019)._official_dob == pendulum.date(2019, 1, 1)


def test_horse_age_init_with_context_date_uses_context_year_for_official_dob():
    horse_age = HorseAge(2, context_date=pendulum.date(2021, 3, 1))
    assert horse_age._official_dob == pendulum.date(2019, 1, 1)


def test_horse_age_init_with_year_sets_actual_dob():
    assert HorseAge(birth_year=2019)._actual_dob is None


def test_horse_age_repr_when_dob_not_known():
    assert repr(HorseAge(2)) == "<HorseAge: 2 (unknown dob)>"


def test_horse_age_repr_when_dob_known():
    assert (
        repr(
            HorseAge(
                foaling_date=pendulum.date(2019, 3, 3),
                context_date=pendulum.date(2021, 6, 1),
            )
        )
        == "<HorseAge: 2 (3/3/2019)>"
    )


def test_horse_age_str():
    assert str(HorseAge(2)) == "2"


@pytest.mark.benchmark
def test_horse_age_returns_correct_official_age_in_years():
    assert HorseAge(2).official.years == 2


@pytest.mark.benchmark
def test_horse_age_returns_correct_actual_age_in_years_if_actual_dob_known():
    assert HorseAge(foaling_date=pendulum.date(2019, 3, 3)).actual.years == 4


@pytest.mark.benchmark
def test_horse_age_returns_correct_date_of_birth_when_known():
    assert HorseAge(
        foaling_date=pendulum.date(2019, 3, 3)
    ).date_of_birth == pendulum.date(2019, 3, 3)


@pytest.mark.benchmark
def test_horse_age_returns_correct_date_of_birth_when_not_known():
    with pytest.raises(ValueError):
        HorseAge(2).date_of_birth


@pytest.mark.benchmark
def test_horse_age_returns_correct_year_of_birth():
    assert HorseAge(foaling_date=pendulum.date(2019, 3, 3)).year_of_birth == 2019


@pytest.mark.benchmark
def test_horse_age_raises_error_for_actual_age_in_years_if_actual_dob_not_known():
    with pytest.raises(ValueError):
        HorseAge(2).actual.years


@pytest.mark.benchmark
def test_horse_age_returns_correct_official_age_in_days_considering_leap_years():
    assert HorseAge(4).official.days == 1612


@pytest.mark.benchmark
def test_horse_age_returns_correct_actual_age_in_days_considering_leap_years():
    assert HorseAge(foaling_date=pendulum.date(2019, 2, 1)).actual.days == 1581


@pytest.mark.benchmark
def test_horse_age_returns_correct_official_age_when_context_date_is_set():
    horse_age = HorseAge(
        2,
        context_date=pendulum.date(2022, 6, 1),
    )
    assert horse_age.official.years == 2


@pytest.mark.benchmark
def test_horse_age_returns_correct_actual_age_when_context_date_is_set():
    horse_age = HorseAge(
        foaling_date=pendulum.date(2019, 3, 3),
        context_date=pendulum.date(2022, 6, 1),
    )
    assert horse_age.actual.years == 3


@pytest.mark.benchmark
def test_horse_age_at_changes_context_date():
    new_date = pendulum.date(2022, 6, 1)
    assert new_date == HorseAge(2).at(new_date)._context_date


@pytest.mark.benchmark
def test_horse_age_change_of_context_date_changes_official_age():
    horse_age = HorseAge(2, context_date=pendulum.date(2020, 6, 1))
    assert horse_age.at(pendulum.date(2022, 3, 1)).official.years == 4


@pytest.mark.benchmark
def test_horse_age_returns_correct_official_age_when_context_date_is_before_birth():
    horse_age = HorseAge(foaling_date=pendulum.date(2019, 3, 3))
    assert horse_age.at(pendulum.date(1976, 11, 29)).official.years == 0


@pytest.mark.benchmark
def test_horse_age_returns_correct_actual_age_when_context_date_is_before_birth():
    horse_age = HorseAge(foaling_date=pendulum.date(2019, 3, 3))
    assert horse_age.at(pendulum.date(1976, 11, 29)).actual.years == 0
