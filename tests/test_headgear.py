from horsetalk import Headgear


def test_headgear_can_be_created_from_enum():
    assert Headgear(1) == Headgear.HOOD


def test_headgear_can_be_created_from_name():
    assert Headgear["HOOD"] == Headgear.HOOD


def test_headgear_can_be_created_from_lowercase_name():
    assert Headgear["hood"] == Headgear.HOOD


def test_headgear_can_be_created_from_spaced_name():
    assert Headgear["Tongue tie"] == Headgear.TONGUE_TIE


def test_headgear_can_be_created_from_hyphenated_name():
    assert Headgear["Tongue-tie"] == Headgear.TONGUE_TIE


def test_headgear_can_be_created_from_abbreviation():
    assert Headgear["h"] == Headgear.HOOD
