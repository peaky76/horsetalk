from horsetalk import Headgear


def test_headgear_can_be_created_from_enum():
    assert Headgear.HOOD == Headgear(1)


def test_headgear_can_be_created_from_name():
    assert Headgear.HOOD == Headgear["HOOD"]


def test_headgear_can_be_created_from_lowercase_name():
    assert Headgear.HOOD == Headgear["hood"]


def test_headgear_can_be_created_from_spaced_name():
    assert Headgear.TONGUE_TIE == Headgear["Tongue tie"]


def test_headgear_can_be_created_from_hyphenated_name():
    assert Headgear.TONGUE_TIE == Headgear["Tongue-tie"]


def test_headgear_can_be_created_from_abbreviation():
    assert Headgear.HOOD == Headgear["h"]
