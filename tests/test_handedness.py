from horsetalk import Handedness


def test_handedness_can_be_created_from_enum():
    assert Handedness.RIGHT == Handedness(2)


def test_handedness_can_be_created_from_name():
    assert Handedness.RIGHT == Handedness["RIGHT"]


def test_handedness_can_be_created_from_lowercase_name():
    assert Handedness.RIGHT == Handedness["right"]


def test_handedness_can_be_created_from_abbreviation():
    assert Handedness.RIGHT == Handedness["RH"]
