from horsetalk import RacingCode


def test_racing_code_can_be_created_from_enum():
    assert RacingCode(1) == RacingCode.FLAT


def test_racing_code_can_be_created_from_name():
    assert RacingCode["FLAT"] == RacingCode.FLAT


def test_racing_code_can_be_created_from_lowercase_name():
    assert RacingCode["flat"] == RacingCode.FLAT


def test_racing_code_can_be_created_from_spaced_name():
    assert RacingCode["National Hunt"] == RacingCode.NATIONAL_HUNT


def test_racing_code_can_be_created_from_abbreviation():
    assert RacingCode["F"] == RacingCode.FLAT
