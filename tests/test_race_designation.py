from horsetalk import RaceDesignation


def test_race_designation_can_be_created_from_enum():
    assert RaceDesignation.HANDICAP == RaceDesignation(1)


def test_race_designation_can_be_created_from_name():
    assert RaceDesignation.HANDICAP == RaceDesignation["HANDICAP"]


def test_race_designation_can_be_created_from_lowercase_name():
    assert RaceDesignation.HANDICAP == RaceDesignation["handicap"]


def test_race_designation_can_be_created_from_apostrophised_name():
    assert RaceDesignation.HANDICAP == RaceDesignation["H'CAP"]
