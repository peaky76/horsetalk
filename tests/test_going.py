import pytest
from horsetalk import AWGoingDescription, Going, TurfGoingDescription


def test_going_can_be_initialized_with_string():
    assert Going("Good")


def test_going_can_be_initialized_with_string_and_float():
    assert Going("Good", 7.0)


def test_going_init_sets_description():
    assert "Good" == Going("Good").description


def test_going_init_sets_reading_on_default():
    assert None is Going("Good").reading


def test_going_init_sets_reading_when_given():
    assert 7.0 == Going("Good", 7.0).reading


def test_going_init_throws_error_when_description_is_invalid():
    with pytest.raises(ValueError):
        Going("Moist to tricky")


def test_going_init_throws_error_when_description_is_part_valid():
    with pytest.raises(ValueError):
        Going("Good, Moist to tricky in places")


def test_going_init_sets_primary_property_with_enum_for_turf_going():
    assert TurfGoingDescription.GOOD == Going("Good").primary


def test_going_init_sets_primary_property_with_enum_for_all_weather_going():
    assert AWGoingDescription.STANDARD_TO_SLOW == Going("Standard to slow").primary


def test_going_init_sets_primary_property_with_enum_when_secondary_given():
    assert TurfGoingDescription.GOOD == Going("Good, Good to Soft in places").primary


def test_going_init_sets_secondary_property_with_enum_for_turf_going():
    assert (
        TurfGoingDescription.GOOD_TO_SOFT
        == Going("Good, Good to Soft in places").secondary
    )


def test_going_init_sets_secondary_property_with_enum_for_all_weather_going():
    assert (
        AWGoingDescription.STANDARD_TO_SLOW
        == Going("Standard, Standard to slow in places").secondary
    )


def test_going_init_does_not_set_secondary_property_when_only_primary_given():
    assert None is Going("Good").secondary


def test_going_str():
    assert (
        Going("GOOD, GOOD TO SOFT IN PLACES").__str__()
        == "Good, Good to Soft in places"
    )


def test_going_value_returns_primary_value_when_only_primary_given():
    assert 8 == Going("Good").value


def test_going_value_returns_mean_of_primary_and_secondary_values_when_both_given():
    assert 7.5 == Going("Good, Good to Soft in places").value
