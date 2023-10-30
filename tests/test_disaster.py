from horsetalk import Disaster


def test_disaster_can_be_created_from_enum():
    assert Disaster(1) == Disaster.FELL


def test_disaster_can_be_created_from_name():
    assert Disaster["FELL"] == Disaster.FELL


def test_disaster_can_be_created_from_lowercase_name():
    assert Disaster["fell"] == Disaster.FELL


def test_disaster_can_be_created_from_spaced_name():
    assert Disaster["Brought down"] == Disaster.BROUGHT_DOWN


def test_disaster_can_be_created_from_abbreviation():
    assert Disaster["f"] == Disaster.FELL


def test_disaster_is_jumping_error():
    assert Disaster.FELL.is_jumping_error


def test_disaster_is_not_jumping_error():
    assert not Disaster.BROUGHT_DOWN.is_jumping_error


def test_disaster_is_behavioural_error():
    assert Disaster.REFUSED.is_behavioural_error


def test_disaster_is_not_behavioural_error():
    assert not Disaster.FELL.is_behavioural_error


def test_disaster_is_third_party_error():
    assert Disaster.BROUGHT_DOWN.is_third_party_error


def test_disaster_is_not_third_party_error():
    assert not Disaster.FELL.is_third_party_error
