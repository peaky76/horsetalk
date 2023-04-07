from horsetalk import RaceWeightStatus


def test_race_weight_status_can_be_created_from_enum():
    assert RaceWeightStatus.HANDICAP == RaceWeightStatus(1)


def test_race_weight_status_can_be_created_from_name():
    assert RaceWeightStatus.HANDICAP == RaceWeightStatus["HANDICAP"]


def test_race_weight_status_can_be_created_from_lowercase_name():
    assert RaceWeightStatus.HANDICAP == RaceWeightStatus["handicap"]
