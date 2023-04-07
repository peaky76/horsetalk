from horsetalk import RacingCode


def test_racing_code_can_be_created_from_enum():
    assert RacingCode.FLAT == RacingCode(1)


def test_racing_code_can_be_created_from_name():
    assert RacingCode.FLAT == RacingCode["FLAT"]


def test_racing_code_can_be_created_from_lowercase_name():
    assert RacingCode.FLAT == RacingCode["flat"]


def test_racing_code_can_be_created_from_spaced_name():
    assert RacingCode.NATIONAL_HUNT == RacingCode["National Hunt"]


def test_racing_code_can_be_created_from_abbreviation():
    assert RacingCode.FLAT == RacingCode["F"]
