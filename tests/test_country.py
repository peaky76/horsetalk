from horsetalk import Country, Hemisphere


def test_country_enum_values():
    assert Country.ARG.value == "Argentina"


def test_country_enum_names():
    assert Country["ARG"] == Country.ARG


def test_country_enum_str():
    assert str(Country.ARG) == "Argentina"


def test_country_enum_contains():
    assert "ARG" in Country.__members__


def test_country_hemisphere_for_northern_country():
    assert Country.AUT.hemisphere == Hemisphere.NORTH


def test_country_hemisphere_for_southern_country():
    assert Country.AUS.hemisphere == Hemisphere.SOUTH
