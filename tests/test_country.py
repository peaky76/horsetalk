from horsetalk.country import Country


def test_country_enum_values():
    assert Country.ARG.value == "Argentina"


def test_country_enum_names():
    assert Country["ARG"] == Country.ARG


def test_country_enum_str():
    assert str(Country.ARG) == "Argentina"


def test_country_enum_contains():
    assert "ARG" in Country.__members__
