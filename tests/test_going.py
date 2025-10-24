import pytest

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
    with pytest.raises(ValueError):
        Going("Moist to tricky")


def test_going_init_throws_error_when_description_is_part_valid():
    with pytest.raises(ValueError):
        Going("Good, Moist to tricky in places")


def test_going_init_throws_error_when_primary_matches_secondary():
    with pytest.raises(ValueError):
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


def test_going_str_when_single_going():
    assert Going("GOOD TO SOFT").__str__() == "Good to Soft"


def test_going_str_when_primary_is_multi_word():
    assert (
        Going("GOOD TO SOFT, SOFT IN PLACES").__str__()
        == "Good to Soft, Soft in places"
    )


def test_going_str_when_secondary_is_multi_word():
    assert (
        Going("GOOD, GOOD TO SOFT IN PLACES").__str__()
        == "Good, Good to Soft in places"
    )


def test_going_str_when_secondary_is_on_bends():
    assert (
        Going("GOOD, GOOD TO SOFT ON BENDS").__str__() == "Good, Good to Soft on bends"
    )


def test_going_hash():
    assert hash(Going("Good, Good to Soft in places")) == hash(
        Going("Good, Good to Soft in places")
    )


def test_going_equality_when_primary_different():
    assert Going("Good") != Going("Soft")


def test_going_equality_when_secondary_different():
    assert Going("Good, Good to Soft in places") != Going(
        "Good, Good to Firm in places"
    )


def test_going_equality_when_reading_different():
    assert Going("Good", 7.0) != Going("Good", 7.5)


def test_going_equality_when_all_different():
    assert Going("Good", 7.0) != Going("Soft", 7.5)


def test_going_equality_when_all_same():
    assert Going("Good", 7.0) == Going("Good", 7.0)


def test_going_equality_when_going_same_and_reading_unspecified():
    assert Going("Good") == Going("Good")


def test_going_surface_returns_turf_for_turf_going_description():
    assert Going("Good").surface == Surface.TURF


def test_going_surface_returns_all_weather_for_all_weather_going_description():
    assert Going("Standard").surface == Surface.ALL_WEATHER


def test_going_value_returns_primary_value_when_only_primary_given():
    assert Going("Good").value == 8


def test_going_value_returns_mean_of_primary_and_secondary_values_when_both_given():
    assert Going("Good, Good to Soft in places").value == 7.5


def test_going_multiparse_with_single_going():
    assert Going.multiparse("Good") == {"default": Going("Good")}


def test_going_multiparse_with_colon_identified_goings():
    assert Going.multiparse("Chase: Good, Hurdle: Good to soft") == {
        "chase": Going("Good"),
        "hurdle": Going("Good to soft"),
    }


def test_going_multiparse_with_parenthesis_identified_goings():
    assert Going.multiparse("Good (Good to soft on hurdle)") == {
        "chase": Going("Good"),
        "hurdle": Going("Good to soft"),
    }


def test_going_multiparse_with_parenthesis_identified_secondary_goings():
    assert Going.multiparse(
        "Good (Good to soft in places on hurdle, Good to firm in places on chase)"
    ) == {
        "chase": Going("Good, Good to firm in places"),
        "hurdle": Going("Good, Good to soft in places"),
    }


def test_going_multiparse_with_single_parenthesis_identified_secondary_goings():
    assert Going.multiparse("Good (Good to soft in places on round course)") == {
        "straight": Going("Good"),
        "round": Going("Good, Good to soft in places"),
    }


def test_going_multiparse_with_initial_identifier():
    assert Going.multiparse(
        "Chase course Soft (Good to Soft in places), Hurdles course Soft (Heavy in places)"
    ) == {
        "chase": Going("Soft, Good to Soft in places"),
        "hurdle": Going("Soft, Heavy in places"),
    }


def test_going_multiparse_when_split_is_turf_vs_all_weather():
    assert Going.multiparse("Turf course Good to Firm, AW course Standard to Slow") == {
        "turf": Going("Good to Firm"),
        "aw": Going("Standard to Slow"),
    }


def test_going_multiparse_when_split_is_national_vs_mildmay():
    assert Going.multiparse("Good to Firm, National course Good to Soft") == {
        "mildmay": Going("Good to Firm"),
        "national": Going("Good to Soft"),
    }


def test_going_multiparse_when_split_is_cross_country_with_hyphen():
    assert Going.multiparse("Soft (Heavy in places Cross-Country course)") == {
        "chase": Going("Soft"),
        "hurdle": Going("Soft"),
        "cross country": Going("Soft, Heavy in places"),
    }


def test_going_multiparse_when_triple_courses_specified():
    assert Going.multiparse(
        "Chase course Heavy, Hurdles and Cross-Country course Soft to Heavy"
    ) == {
        "chase": Going("Heavy"),
        "hurdle": Going("Soft to Heavy"),
        "cross country": Going("Soft to Heavy"),
    }
