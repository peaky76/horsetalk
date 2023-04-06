from horsetalk import Disaster


def test_disaster_can_be_created_from_enum():
    assert Disaster.FELL == Disaster(1)


def test_disaster_can_be_created_from_name():
    assert Disaster.FELL == Disaster["FELL"]


def test_disaster_can_be_created_from_lowercase_name():
    assert Disaster.FELL == Disaster["fell"]


def test_disaster_can_be_created_from_spaced_name():
    assert Disaster.BROUGHT_DOWN == Disaster["Brought down"]


def test_disaster_can_be_created_from_abbreviation():
    assert Disaster.FELL == Disaster["f"]
