from pytest import raises  # type: ignore
from horsetalk import AWGoingDescription, Going, Surface, TurfGoingDescription


def test_going_can_be_initialized_with_string():
    assert Going("Good")


def test_going_can_be_initialized_with_string_and_float():
    assert Going("Good", 7.0)


def test_going_init_sets_description():
    assert Going("Good").description == "Good"


def test_going_init_sets_reading_on_default():
    assert Going("Good").reading is None


def test_going_init_sets_reading_when_given():
    assert Going("Good", 7.0).reading == 7.0


def test_going_init_throws_error_when_description_is_invalid():
    with raises(ValueError):
        Going("Moist to tricky")


def test_going_init_throws_error_when_description_is_part_valid():
    with raises(ValueError):
        Going("Good, Moist to tricky in places")


def test_going_init_throws_error_when_primary_matches_secondary():
    with raises(ValueError):
        Going("Good, Good in places")


def test_going_init_sets_primary_property_with_enum_for_turf_going():
    assert Going("Good").primary == TurfGoingDescription.GOOD


def test_going_init_sets_primary_property_with_enum_for_all_weather_going():
    assert Going("Standard to slow").primary == AWGoingDescription.STANDARD_TO_SLOW


def test_going_init_sets_primary_property_with_enum_when_secondary_given():
    assert Going("Good, Good to Soft in places").primary == TurfGoingDescription.GOOD


def test_going_init_sets_primary_property_with_enum_when_secondary_given_in_parentheses():
    assert Going("Good (Good to Soft in places)").primary == TurfGoingDescription.GOOD


def test_going_init_sets_secondary_property_with_enum_for_turf_going():
    assert (
        Going("Good, Good to Soft in places").secondary
        == TurfGoingDescription.GOOD_TO_SOFT
    )


def test_going_init_sets_secondary_property_with_enum_for_turf_going_in_parentheses():
    assert (
        Going("Good (Good to Soft in places)").secondary
        == TurfGoingDescription.GOOD_TO_SOFT
    )


def test_going_init_sets_secondary_property_with_enum_for_all_weather_going():
    assert (
        Going("Standard, Standard to slow in places").secondary
        == AWGoingDescription.STANDARD_TO_SLOW
    )


def test_going_init_sets_secondary_property_with_enum_for_all_weather_going_in_parentheses():
    assert (
        Going("Standard (Standard to slow in places)").secondary
        == AWGoingDescription.STANDARD_TO_SLOW
    )


def test_going_init_does_not_set_secondary_property_when_only_primary_given():
    assert Going("Good").secondary is None


def test_going_repr():
    assert (
        Going("Good, Good to Soft in places").__repr__()
        == "<Going(<TurfGoingDescription.GOOD: 8>, <TurfGoingDescription.GOOD_TO_SOFT: 7>)>"
    )


def test_going_str():
    assert (
        Going("GOOD, GOOD TO SOFT IN PLACES").__str__()
        == "Good, Good to Soft in places"
    )


def test_going_surface_returns_turf_for_turf_going_description():
    assert Going("Good").surface == Surface.TURF


def test_going_surface_returns_all_weather_for_all_weather_going_description():
    assert Going("Standard").surface == Surface.ALL_WEATHER


def test_going_value_returns_primary_value_when_only_primary_given():
    assert Going("Good").value == 8


def test_going_value_returns_mean_of_primary_and_secondary_values_when_both_given():
    assert Going("Good, Good to Soft in places").value == 7.5
