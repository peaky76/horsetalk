from horsetalk import Hemisphere


def test_hemisphere_can_be_created_from_enum():
    assert Hemisphere(1) == Hemisphere.NORTHERN


def test_hemisphere_can_be_created_from_name():
    assert Hemisphere["NORTHERN"] == Hemisphere.NORTHERN


def test_hemisphere_can_be_created_from_lowercase_name():
    assert Hemisphere["northern"] == Hemisphere.NORTHERN


def test_hemisphere_can_be_created_from_abbreviation():
    assert Hemisphere["N"] == Hemisphere.NORTHERN
