from horsetalk import RaceDesignation


def test_race_designation_can_be_created_from_enum():
    assert RaceDesignation(1) == RaceDesignation.HANDICAP


def test_race_designation_can_be_created_from_name():
    assert RaceDesignation["HANDICAP"] == RaceDesignation.HANDICAP


def test_race_designation_can_be_created_from_lowercase_name():
    assert RaceDesignation["handicap"] == RaceDesignation.HANDICAP


def test_race_designation_can_be_created_from_apostrophised_name():
    assert RaceDesignation["H'CAP"] == RaceDesignation.HANDICAP
